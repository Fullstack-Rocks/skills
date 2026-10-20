"""Detect a project's file extensions and linters. Prints JSON.

Each extension in the repo is listed with its file count and the ast-grep language that parses it
(asked from ast-grep itself, honouring --sgconfig languageGlobs), so no language table lives here.

Usage: python3 detect_linters.py [--root DIR] [--sgconfig FILE]
"""
import argparse
import json
import shutil
import subprocess
import tempfile
import tomllib
from collections import Counter
from pathlib import Path

PYTHON = [".py", ".pyi"]
JS_TS = [".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".mts", ".cts"]

# Linters this script recognises: the command (files are appended), the output parser review.py uses,
# and the extensions whose files it receives. Any other linter goes in config.toml by hand with
# format "sarif" or "unix".
KNOWN_LINTERS = {
    "ruff": {"command": ["ruff", "check", "--output-format", "json", "--force-exclude", "--no-cache"],
             "format": "ruff", "extensions": PYTHON},
    "flake8": {"command": ["flake8"], "format": "unix", "extensions": PYTHON},
    "eslint": {"command": ["eslint", "--format", "json"], "format": "eslint", "extensions": JS_TS},
    "oxlint": {"command": ["oxlint", "--format", "json"], "format": "oxlint", "extensions": JS_TS},
    "biome": {"command": ["biome", "lint", "--reporter=gitlab", "--no-errors-on-unmatched",
                          "--files-ignore-unknown=true"], "format": "biome", "extensions": JS_TS},
}
CENSUS_LIMIT = 30

ENV_BIN_DIRS = [".venv/bin", "venv/bin", "node_modules/.bin"]


def find_tool(root: Path, name: str) -> str | None:
    """The project's own environment first, then PATH. Never a downloader such as npx."""
    for folder in ENV_BIN_DIRS:
        candidate = root / folder / name
        if candidate.is_file():
            return str(candidate)
    return shutil.which(name)


def project_files(root: Path) -> list[str]:
    result = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                            cwd=root, capture_output=True, text=True)
    if result.returncode == 0:
        return [line for line in result.stdout.splitlines() if line]
    skipped = {".git", "node_modules", ".venv", "venv", "dist", "build"}
    return [str(p.relative_to(root)) for p in root.rglob("*")
            if p.is_file() and not skipped.intersection(p.relative_to(root).parts)]


def ast_grep_languages(root: Path, extensions: list[str], sgconfig: Path | None) -> dict[str, str]:
    """Extension -> ast-grep language, by running ast-grep on a one-line probe file per extension."""
    binary = find_tool(root, "ast-grep")
    if not binary or not extensions:
        return {}
    with tempfile.TemporaryDirectory() as probe_dir:
        for ext in extensions:
            (Path(probe_dir) / f"probe{ext}").write_text("x\n")
        config = ["-c", str(sgconfig)] if sgconfig and sgconfig.is_file() else []
        out = subprocess.run([binary, "run", "-p", "$X", "--json=stream", *config, probe_dir],
                             capture_output=True, text=True).stdout
    languages = {}
    for line in out.splitlines():
        match = json.loads(line)
        languages.setdefault(Path(match["file"]).suffix, match["language"])
    return languages


def extension_census(root: Path, files: list[str], sgconfig: Path | None) -> list[dict]:
    counts = Counter(Path(f).suffix.lower() for f in files
                     if Path(f).suffix and not f.startswith(".code-standards/"))
    top = [ext for ext, _ in counts.most_common(CENSUS_LIMIT)]
    languages = ast_grep_languages(root, top, sgconfig)
    return [{"extension": ext, "files": counts[ext], "ast_grep": languages.get(ext)} for ext in top]


def read_text(path: Path) -> str:
    return path.read_text(errors="ignore") if path.is_file() else ""


def python_linters(root: Path) -> dict[str, str]:
    found = {}
    pyproject = tomllib.loads(read_text(root / "pyproject.toml"))
    if "ruff" in pyproject.get("tool", {}):
        found["ruff"] = "pyproject.toml [tool.ruff]"
    for name in ("ruff.toml", ".ruff.toml"):
        if (root / name).is_file():
            found["ruff"] = name
    if (root / ".flake8").is_file() or "[flake8]" in read_text(root / "setup.cfg") + read_text(root / "tox.ini"):
        found["flake8"] = ".flake8 / setup.cfg / tox.ini"
    return found


# Node linter -> (config file globs, package name). A config file or a dependency counts as evidence.
NODE_LINTERS = {
    "eslint": (["eslint.config.*", ".eslintrc*"], "eslint"),
    "oxlint": ([".oxlintrc*", "oxlint.config.*"], "oxlint"),
    "biome": (["biome.json*"], "@biomejs/biome"),
}


def node_linters(root: Path) -> dict[str, str]:
    package = json.loads(read_text(root / "package.json") or "{}")
    deps = {**package.get("dependencies", {}), **package.get("devDependencies", {})}
    found = {}
    for name, (globs, dependency) in NODE_LINTERS.items():
        configs = [p.name for pattern in globs for p in root.glob(pattern)]
        if configs:
            found[name] = configs[0]
        elif dependency in deps:
            found[name] = "package.json dependency"
    if "eslintConfig" in package:
        found.setdefault("eslint", "package.json eslintConfig")
    return found


def configured_linters(root: Path) -> dict[str, str]:
    """Linter name -> the evidence that the project uses it."""
    return {**python_linters(root), **node_linters(root)}


def detect(root: Path, sgconfig: Path | None = None) -> dict:
    census = extension_census(root, project_files(root), sgconfig)
    linters = []
    for name, evidence in configured_linters(root).items():
        spec = KNOWN_LINTERS[name]
        linters.append({"name": name, "evidence": evidence, **spec,
                        "binary": find_tool(root, spec["command"][0])})
    return {"root": str(root), "ast_grep_installed": bool(find_tool(root, "ast-grep")),
            "extensions": census, "linters": linters}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--sgconfig", type=Path, help="ast-grep config whose languageGlobs apply to the probe")
    args = parser.parse_args()
    print(json.dumps(detect(args.root.resolve(), args.sgconfig), indent=2))


if __name__ == "__main__":
    main()
