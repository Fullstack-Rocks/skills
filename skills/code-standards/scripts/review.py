"""Run the deterministic review layers in parallel and print one JSON report.

Layers: the project's linters, ast-grep rules in .code-standards/rules, lizard (complexity,
function length, parameter count) and jscpd (duplication). Also lists which standards.md
entries apply to which files.

Language-blind: config.toml lists the file extensions to review. Every tool gets those files and
picks its own parser by extension, skipping files it can't read.

Usage: python3 review.py [--base REF | --all | --files F ...] [--out FILE]
"""
import sys

if sys.version_info < (3, 11):
    sys.exit(f"code-standards needs Python 3.11+ (this is {sys.version.split()[0]}). "
             "Rerun with python3.11+ or: uv run --no-project --python 3.12 -- python " + " ".join(sys.argv))

import argparse
import csv
import json
import re
import subprocess
import tempfile
import time
import tomllib
from concurrent.futures import ThreadPoolExecutor
from fnmatch import fnmatch
from pathlib import Path
from urllib.parse import unquote

from install_tools import find_tool, install_hint

STANDARDS_DIR = ".code-standards"
SEVERITY = {
    "error": "error", "fatal": "error", "blocker": "error", "critical": "error",
    "warning": "warning", "warn": "warning", "major": "warning", "minor": "warning",
    "info": "info", "hint": "info", "advice": "info", "note": "info", "none": "info",
}
SEVERITY_ORDER = {"error": 0, "warning": 1, "info": 2}


class ToolMissing(Exception):
    pass


class ToolError(Exception):
    pass


# ---------- project, config, files ----------

def find_root(start: Path) -> Path:
    for folder in [start, *start.parents]:
        if (folder / STANDARDS_DIR / "config.toml").is_file():
            return folder
    sys.exit(f"No {STANDARDS_DIR}/config.toml in {start} or its parents. Run init.py first.")


def load_config(root: Path) -> dict:
    return tomllib.loads((root / STANDARDS_DIR / "config.toml").read_text())


def git_lines(root: Path, *args: str) -> list[str] | None:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return [line for line in result.stdout.splitlines() if line] if result.returncode == 0 else None


def changed_files(root: Path, base: str) -> tuple[list[str], dict]:
    """Committed, staged and unstaged changes since the merge-base with `base`, plus untracked files."""
    merge_base = git_lines(root, "merge-base", base, "HEAD")
    ref = merge_base[0] if merge_base else "HEAD"
    tracked = git_lines(root, "diff", "--name-only", "--relative", "--diff-filter=ACMR", ref)
    if tracked is None:  # no commits yet: everything tracked counts as changed
        tracked = git_lines(root, "ls-files", "--cached") or []
    untracked = git_lines(root, "ls-files", "--others", "--exclude-standard") or []
    return tracked + untracked, {"mode": "changed", "base": base, "diff_from": ref}


def all_files(root: Path) -> tuple[list[str], dict]:
    files = git_lines(root, "ls-files", "--cached", "--others", "--exclude-standard") or []
    return files, {"mode": "all"}


def glob_match(path: str, patterns: list[str]) -> bool:
    """fnmatch globs where * also crosses /; a leading **/ also matches top-level files."""
    return any(fnmatch(path, p) or (p.startswith("**/") and fnmatch(path, p[3:])) for p in patterns)


def has_extension(path: str, extensions: list[str]) -> bool:
    return Path(path).suffix.lower() in {e.lower() for e in extensions}


def candidate_files(root: Path, files: list[str], config: dict) -> list[str]:
    excludes = config.get("exclude", [])
    return [f for f in files
            if not f.startswith(STANDARDS_DIR + "/") and not glob_match(f, excludes) and (root / f).is_file()]


def review_files(root: Path, files: list[str], config: dict) -> list[str]:
    if "extensions" not in config:
        sys.exit(f"{STANDARDS_DIR}/config.toml has no `extensions` list (e.g. extensions = [\".py\", \".ts\"]).")
    return sorted({f for f in candidate_files(root, files, config) if has_extension(f, config["extensions"])})


def new_extensions(root: Path, files: list[str], config: dict) -> dict[str, int]:
    """Changed files whose extension is neither reviewed nor deliberately skipped: a decision to ask for."""
    known = {e.lower() for e in config.get("extensions", []) + config.get("not_reviewed", [])}
    counts: dict[str, int] = {}
    for f in candidate_files(root, files, config):
        suffix = Path(f).suffix.lower()
        if suffix and suffix not in known:
            counts[suffix] = counts.get(suffix, 0) + 1
    return counts


def relative(root: Path, path: str) -> str:
    candidate = Path(path)
    if candidate.is_absolute():
        try:
            return str(candidate.resolve().relative_to(root.resolve()))
        except ValueError:
            return path
    return path.removeprefix("./")


def finding(source, rule_id, severity, file, line, end_line=None, message="", snippet=None, **extra):
    return {"source": source, "rule_id": rule_id or "unknown",
            "severity": SEVERITY.get(str(severity).lower(), "warning"), "file": file,
            "line": line, "end_line": end_line or line, "message": message, "snippet": snippet, **extra}


def run(command: list[str], root: Path, ok_codes=(0, 1)) -> str:
    result = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=300)
    if result.returncode not in ok_codes:
        raise ToolError(f"exit {result.returncode}: {(result.stderr or result.stdout).strip()[-800:]}")
    return result.stdout


def tool(root: Path, name: str) -> str:
    binary = find_tool(root, name)
    if not binary:
        raise ToolMissing(f"{name} not found. To install it, {install_hint(name)}")
    return binary


# ---------- project linters ----------

def parse_ruff(out: str, root: Path) -> list[dict]:
    return [finding("ruff", d.get("code") or "syntax-error", d.get("severity") or "warning",
                    relative(root, d["filename"]), d["location"]["row"], d["end_location"]["row"], d["message"])
            for d in json.loads(out or "[]")]


def parse_eslint(out: str, root: Path) -> list[dict]:
    results = []
    for file_result in json.loads(out or "[]"):
        for m in file_result["messages"]:
            if not m.get("ruleId") and "ignored" in m.get("message", ""):
                continue
            severity = "error" if m.get("severity") == 2 else "warning"
            results.append(finding("eslint", m.get("ruleId") or "parse-error", severity,
                                   relative(root, file_result["filePath"]), m.get("line", 1),
                                   m.get("endLine"), m["message"]))
    return results


def parse_oxlint(out: str, root: Path) -> list[dict]:
    results = []
    for d in json.loads(out or "{}").get("diagnostics", []):
        line = d["labels"][0]["span"]["line"] if d.get("labels") else 1
        message = d["message"] + (f" ({d['help']})" if d.get("help") else "")
        results.append(finding("oxlint", d.get("code") or "parse-error", d.get("severity"),
                               relative(root, d["filename"]), line, message=message))
    return results


def parse_biome(out: str, root: Path) -> list[dict]:
    start = out.find("[")
    issues = json.loads(out[start:]) if start >= 0 else []
    return [finding("biome", d.get("check_name"), d.get("severity"), relative(root, d["location"]["path"]),
                    d["location"]["lines"]["begin"], d["location"]["lines"].get("end"), d["description"])
            for d in issues]


UNIX_LINE = re.compile(r"^(?P<file>[^:\s][^:]*):(?P<line>\d+):(?:\d+:)?\s*(?P<message>.+)$")
UNIX_RULE = re.compile(r"^([A-Z]+\d+)\b|\[([\w/@.-]+)\]$|\(([\w/@.-]+)\)$")


def parse_unix(out: str, root: Path, name: str = "linter") -> list[dict]:
    """`path:line[:col]: message` lines, as flake8, oxlint -f unix and many others print."""
    results = []
    for raw in out.splitlines():
        match = UNIX_LINE.match(raw.strip())
        if not match:
            continue
        message = match["message"]
        rule = UNIX_RULE.search(message)
        rule_id = next((g for g in rule.groups() if g), None) if rule else None
        results.append(finding(name, rule_id, "warning", relative(root, match["file"]),
                               int(match["line"]), message=message))
    return results


def parse_sarif(out: str, root: Path, name: str = "linter") -> list[dict]:
    """SARIF 2.1 (`runs[].results[]`), which most linters in most languages can emit."""
    results = []
    for run_ in json.loads(out or "{}").get("runs", []):
        for r in run_.get("results", []):
            location = (r.get("locations") or [{}])[0].get("physicalLocation", {})
            uri = unquote(location.get("artifactLocation", {}).get("uri", "").removeprefix("file://"))
            region = location.get("region", {})
            results.append(finding(name, r.get("ruleId"), r.get("level", "warning"), relative(root, uri),
                                   region.get("startLine", 1), region.get("endLine"),
                                   r.get("message", {}).get("text", "")))
    return results


PARSERS = {"ruff": parse_ruff, "eslint": parse_eslint, "oxlint": parse_oxlint, "biome": parse_biome}
GENERIC_PARSERS = {"sarif": parse_sarif, "unix": parse_unix}


def run_linter(spec: dict, files: list[str], root: Path) -> list[dict]:
    binary = find_tool(root, spec["command"][0])
    if not binary:
        raise ToolMissing(f"{spec['name']} is configured but not installed. Install the project's dev dependencies "
                          "with its lockfile command (npm ci, uv sync --frozen, ...)")
    out = run([binary, *spec["command"][1:], *files], root, ok_codes=tuple(spec.get("ok_codes", (0, 1))))
    if spec["format"] in PARSERS:
        return PARSERS[spec["format"]](out, root)
    return GENERIC_PARSERS.get(spec["format"], parse_unix)(out, root, spec["name"])


# ---------- ast-grep ----------

def run_ast_grep(files: list[str], root: Path) -> list[dict]:
    config = f"{STANDARDS_DIR}/sgconfig.yml"
    out = run([tool(root, "ast-grep"), "scan", "-c", config, "--json=stream", *files], root)
    results = []
    for raw in out.splitlines():
        d = json.loads(raw)
        start, end = d["range"]["start"]["line"] + 1, d["range"]["end"]["line"] + 1
        message = d["message"] + (f" ({d['note']})" if d.get("note") else "")
        extra = {"fix": d["replacement"]} if d.get("replacement") else {}
        results.append(finding("ast-grep", d["ruleId"], d["severity"], d["file"], start, end, message,
                               d["lines"], **extra))
    return results


# ---------- lizard ----------

def run_lizard(files: list[str], root: Path, config: dict) -> list[dict]:
    limits = config["thresholds"]
    threads = ["-t", "4"] if len(files) > 500 else []  # process start-up outweighs the gain below that
    out = run([tool(root, "lizard"), "--csv", *threads, *files], root)  # skips files it has no parser for
    results = []
    for row in csv.reader(out.splitlines()):
        if len(row) < 11 or not row[0].isdigit():
            continue
        ccn, params, length = int(row[1]), int(row[3]), int(row[4])
        file, name, start, end = relative(root, row[6]), row[7], int(row[9]), int(row[10])
        checks = [("complexity", ccn, limits["complexity"], "cyclomatic complexity"),
                  ("function-length", length, limits["function_lines"], "lines"),
                  ("param-count", params, limits["params"], "parameters")]
        for rule_id, value, limit, label in checks:
            if value > limit:
                results.append(finding("lizard", rule_id, "warning", file, start, end,
                                       f"{name}: {value} {label} (limit {limit})"))
    return results


# ---------- jscpd ----------

def run_jscpd(files: list[str], root: Path, config: dict) -> list[dict]:
    repo_scope = config.get("duplication", {}).get("scope") == "repo"
    if repo_scope:  # the whole repo, limited to the reviewed extensions
        names = [e.lstrip(".") for e in config["extensions"]]
        pattern = f"**/*.{names[0]}" if len(names) == 1 else "**/*.{" + ",".join(names) + "}"
        ignore = ",".join(["**/.git/**", *config.get("exclude", [])])
        targets = ["--pattern", pattern, "--ignore", ignore, "."]
    else:
        targets = files
    with tempfile.TemporaryDirectory() as out_dir:
        run([tool(root, "jscpd"), "--reporters", "json", "--output", out_dir, "--silent", "--no-tips", "--absolute",
             "--min-tokens", str(config["thresholds"]["duplicate_tokens"]), *targets],
            root, ok_codes=(0,))
        report = Path(out_dir) / "jscpd-report.json"
        if not report.is_file():
            raise ToolError("jscpd wrote no report")
        duplicates = json.loads(report.read_text())["duplicates"]
    reviewed = set(files)
    results = []
    for dup in duplicates:
        sides = [(dup["firstFile"], dup["secondFile"]), (dup["secondFile"], dup["firstFile"])]
        for this, other in sides:
            file = relative(root, this["name"])
            if file not in reviewed:
                continue
            message = (f"duplicates {relative(root, other['name'])}:{other['start']}-{other['end']} "
                       f"({dup['lines']} lines, {dup['tokens']} tokens)")
            snippet = "\n".join(dup.get("fragment", "").splitlines()[:5])
            results.append(finding("jscpd", "duplicate", "warning", file, this["start"], this["end"], message, snippet))
    return results


# ---------- standards.md scope ----------

STANDARD_HEADING = re.compile(r"^## (std-[\w-]+):?\s*(.*)$", re.MULTILINE)
SCOPE_LINE = re.compile(r"^-?\s*\**scope:?\**:?\s*(.+)$", re.IGNORECASE | re.MULTILINE)


def standards_in_scope(root: Path, files: list[str]) -> list[dict]:
    path = root / STANDARDS_DIR / "standards.md"
    text = re.sub(r"<!--.*?-->", "", path.read_text(), flags=re.DOTALL) if path.is_file() else ""
    headings = list(STANDARD_HEADING.finditer(text))
    entries = []
    for i, heading in enumerate(headings):
        body = text[heading.end(): headings[i + 1].start() if i + 1 < len(headings) else len(text)]
        scope = SCOPE_LINE.search(body)
        patterns = [p.strip().strip("`") for p in scope.group(1).split(",")] if scope else ["**"]
        matched = [f for f in files if glob_match(f, patterns)]
        if matched:
            entries.append({"id": heading.group(1), "title": heading.group(2).strip(), "files": matched})
    return entries


# ---------- assembly ----------

def add_snippets(root: Path, findings: list[dict]) -> None:
    cache: dict[str, list[str]] = {}
    for f in findings:
        if f["snippet"] is not None:
            continue
        if f["file"] not in cache:
            path = root / f["file"]
            cache[f["file"]] = path.read_text(errors="ignore").splitlines() if path.is_file() else []
        lines = cache[f["file"]]
        last = min(f["end_line"], f["line"] + 2)
        f["snippet"] = "\n".join(lines[f["line"] - 1: last])


def timed(name: str, job) -> tuple[str, list[dict], float, Exception | None]:
    started = time.perf_counter()
    try:
        return name, job(), time.perf_counter() - started, None
    except (ToolMissing, ToolError, subprocess.TimeoutExpired, json.JSONDecodeError, KeyError) as exc:
        return name, [], time.perf_counter() - started, exc


def build_jobs(root: Path, files: list[str], config: dict) -> list[tuple]:
    jobs = [("ast-grep", lambda: run_ast_grep(files, root)),
            ("lizard", lambda: run_lizard(files, root, config)),
            ("jscpd", lambda: run_jscpd(files, root, config))]
    for spec in config.get("linters", []):
        own = [f for f in files if has_extension(f, spec.get("extensions", config["extensions"]))]
        if own:
            jobs.append((spec["name"], lambda spec=spec, own=own: run_linter(spec, own, root)))
    return jobs


def review(root: Path, candidates: list[str], scope: dict, config: dict) -> dict:
    started = time.perf_counter()
    files = review_files(root, candidates, config)
    report = {"root": str(root), "scope": scope, "files_scanned": len(files), "files": files,
              "new_extensions": new_extensions(root, candidates, config),
              "summary": {}, "findings": [], "standards": standards_in_scope(root, files),
              "timing": {}, "errors": {}, "warnings": []}
    if files:
        jobs = build_jobs(root, files, config)
        with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
            for name, findings, seconds, exc in pool.map(lambda job: timed(*job), jobs):
                report["timing"][name] = round(seconds, 3)
                report["findings"].extend(findings)
                if isinstance(exc, ToolMissing):
                    report["warnings"].append({"tool": name, "message": str(exc)})
                elif exc:
                    report["errors"][name] = f"{type(exc).__name__}: {exc}"
    add_snippets(root, report["findings"])
    report["findings"].sort(key=lambda f: (SEVERITY_ORDER[f["severity"]], f["file"], f["line"]))
    for f in report["findings"]:
        report["summary"][f["severity"]] = report["summary"].get(f["severity"], 0) + 1
    report["timing"]["total"] = round(time.perf_counter() - started, 3)
    return report


def summary_line(report: dict) -> str:
    counts = ", ".join(f"{n} {sev}" for sev, n in report["summary"].items()) or "no findings"
    timing = ", ".join(f"{k} {v}s" for k, v in report["timing"].items())
    lines = [f"{report['files_scanned']} files, {counts}, {len(report['standards'])} standards in scope. {timing}"]
    lines += [f"ERROR {tool_name}: {msg}" for tool_name, msg in report["errors"].items()]
    lines += [f"WARNING {w['tool']}: {w['message']}" for w in report["warnings"]]
    if report["new_extensions"]:
        found = ", ".join(f"{ext} ({n})" for ext, n in report["new_extensions"].items())
        lines.append(f"NOTE changed files with extensions in neither `extensions` nor `not_reviewed`: {found}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--base", help="diff against the merge-base with this ref (default: config base)")
    scope.add_argument("--all", action="store_true", help="review every project file")
    scope.add_argument("--files", nargs="+", help="review exactly these files (relative to the project root)")
    parser.add_argument("--root", type=Path, help="project root (default: nearest folder with .code-standards/)")
    parser.add_argument("--out", type=Path, help="write the JSON report here and print a summary instead")
    args = parser.parse_args()

    root = (args.root or find_root(Path.cwd())).resolve()
    config = load_config(root)
    if args.files:
        candidates, scope_info = [relative(root, str(Path(f).resolve())) for f in args.files], {"mode": "files"}
    elif args.all:
        candidates, scope_info = all_files(root)
    else:
        candidates, scope_info = changed_files(root, args.base or config.get("base", "main"))
    report = review(root, candidates, scope_info, config)

    if args.out:
        args.out.write_text(json.dumps(report, indent=1))
        print(summary_line(report))
    else:
        print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
