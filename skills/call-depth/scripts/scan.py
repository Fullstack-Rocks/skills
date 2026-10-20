"""Language-agnostic scan: memory hops, function length and complexity, in any language.

lizard measures function length and cyclomatic complexity (about 25 languages). ast-grep runs the
rule packs in rules/, one file per language, for dynamic calls, dynamic attribute lookups and
registry calls. A language that no pack covers is reported as NO_RULES, so the gap is visible:
add a pack (references/languages.md) or use the grep fallback there.

Usage: python3 scan.py <paths> [--max-function-lines 80] [--max-complexity 10]
"""
import argparse
import csv
import json
import re
import subprocess
import tempfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from install_tools import find_tool, install_hint
from layout import code_files

HERE = Path(__file__).resolve().parent
SGCONFIG = HERE / "sgconfig.yml"
KINDS = {"dynamic-call": "DYNAMIC_CALL", "dynamic-attr": "DYNAMIC_ATTR", "lookup-call": "LOOKUP_CALL"}
# ast-grep parses these, but they hold no calls to trace.
DATA_LANGUAGES = {"Json", "Yaml", "Html", "Css"}


class ToolMissing(Exception):
    pass


def tool(name: str) -> str:
    binary = find_tool(Path.cwd(), name)
    if not binary:
        raise ToolMissing(f"MISSING_TOOL\t{name}\tto install it, {install_hint(name)}")
    return binary


def shown(path: str) -> str:
    try:
        return str(Path(path).resolve().relative_to(Path.cwd()))
    except ValueError:
        return path


def rule_languages() -> set[str]:
    return {lang for pack in (HERE / "rules").glob("*.yml")
            for lang in re.findall(r"^language:\s*(\S+)", pack.read_text(), re.MULTILINE)}


def languages_by_extension(extensions: list[str]) -> dict[str, str]:
    """Extension -> ast-grep language, by asking ast-grep about a one-line probe file per extension."""
    with tempfile.TemporaryDirectory() as probe_dir:
        for ext in extensions:
            (Path(probe_dir) / f"probe{ext}").write_text("x\n")
        out = subprocess.run([tool("ast-grep"), "run", "-p", "$X", "--json=stream", "-c", str(SGCONFIG), probe_dir],
                             capture_output=True, text=True).stdout
    languages: dict[str, str] = {}
    for line in out.splitlines():
        match = json.loads(line)
        languages.setdefault(Path(match["file"]).suffix, match["language"])
    return languages


def run_ast_grep(files: list[str], languages: dict[str, str]) -> list[str]:
    covered = rule_languages()
    targets = [f for f in files if languages.get(Path(f).suffix.lower()) in covered]
    if not targets:
        return []
    result = subprocess.run([tool("ast-grep"), "scan", "-c", str(SGCONFIG), "--json=stream", *targets],
                            capture_output=True, text=True)
    if result.returncode not in (0, 1):
        return [f"SCAN_ERROR\tast-grep\t{result.stderr.strip()[-300:]}"]
    return outermost_findings(result.stdout)


def outermost_findings(stream: str) -> list[str]:
    """One finding per kind and line: a chain like a.getMethod(m).invoke(o) matches once per link."""
    outermost: dict[tuple[str, str], dict] = {}
    for line in stream.splitlines():
        match = json.loads(line)
        kind = next((k for key, k in KINDS.items() if key in match["ruleId"]), None)
        where = f"{shown(match['file'])}:{match['range']['start']['line'] + 1}"
        if kind and len(match["text"]) > len(outermost.get((kind, where), {}).get("text", "")):
            outermost[(kind, where)] = match
    return [f"{kind}\t{where}\t{' '.join(m['text'].split())[:80]}  ({m['message']})"
            for (kind, where), m in outermost.items()]


def run_lizard(files: list[str], max_lines: int, max_complexity: int) -> list[str]:
    threads = ["-t", "4"] if len(files) > 500 else []  # process start-up outweighs the gain below that
    result = subprocess.run([tool("lizard"), "--csv", *threads, *files], capture_output=True, text=True)
    findings = []
    for row in csv.reader(result.stdout.splitlines()):
        if len(row) < 11 or not row[0].isdigit():
            continue
        complexity, length, where, name = int(row[1]), int(row[4]), f"{shown(row[6])}:{row[9]}", row[7]
        if length > max_lines:
            findings.append(f"FUNCTION_LENGTH\t{where}\t{name} {length} lines > {max_lines}")
        if complexity > max_complexity:
            findings.append(f"COMPLEXITY\t{where}\t{name} {complexity} > {max_complexity}")
    return findings


def coverage_gaps(counts: Counter, languages: dict[str, str]) -> list[str]:
    covered = rule_languages()
    gaps = []
    for ext, count in counts.most_common():
        language = languages.get(ext)
        if language in covered or language in DATA_LANGUAGES:
            continue
        reason = f"{language} has no rule pack" if language else "ast-grep can't parse it"
        gaps.append(f"NO_RULES\t{ext}\t{count} files: {reason}; find memory hops with the grep fallback in "
                    "references/languages.md")
    return gaps


def location(line: str) -> tuple[str, int]:
    path, _, number = line.split("\t")[1].rpartition(":")
    return (path, int(number)) if number.isdigit() else (line, 0)


def safely(job) -> list[str]:
    try:
        return job()
    except ToolMissing as missing:
        return [str(missing)]


def measure(files: list[str], languages: dict[str, str], args: argparse.Namespace) -> list[str]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        hops = pool.submit(safely, lambda: run_ast_grep(files, languages) if languages else [])
        sizes = pool.submit(safely, lambda: run_lizard(files, args.max_function_lines, args.max_complexity))
        return hops.result() + sizes.result()


def collect(paths: list[Path]) -> tuple[list[str], list[str]]:
    missing = [f"MISSING_PATH\t{path}\tdoes not exist" for path in paths if not path.exists()]
    files = sorted({str(f) for path in paths if path.exists() for f in code_files(path.resolve())})
    return files, missing


def report(status: list[str], results: list[str], counts: Counter, languages: dict[str, str]) -> None:
    status = status + [line for line in results if line.startswith(("MISSING_TOOL", "SCAN_ERROR"))]
    findings = sorted((line for line in results if line not in status), key=location)
    print("\n".join(dict.fromkeys(status + findings)) or "OK\tno findings")
    if languages:
        print("\n".join(coverage_gaps(counts, languages)) or "COVERED\tevery scanned language has a rule pack")
    print(f"SCANNED\t{sum(counts.values())} code files ({', '.join(f'{e} {n}' for e, n in counts.most_common())})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--max-function-lines", type=int, default=80)
    parser.add_argument("--max-complexity", type=int, default=10)
    args = parser.parse_args()
    files, status = collect(args.paths)
    counts = Counter(Path(f).suffix.lower() for f in files)
    languages = safely(lambda: languages_by_extension(list(counts)))
    if isinstance(languages, list):  # ast-grep is missing: its MISSING_TOOL line comes back instead
        status, languages = [*status, *languages], {}
    report(status, measure(files, languages, args), counts, languages)


if __name__ == "__main__":
    main()
