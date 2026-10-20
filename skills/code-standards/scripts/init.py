"""Scaffold .code-standards/ in a project from the templates. Prints what it created and detected.

Usage: python3 init.py [--root DIR]
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

from detect_linters import detect
from review import STANDARDS_DIR, git_lines

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"
COPIED = ["sgconfig.yml", "standards.md", "negations.log.md"]
# ast-grep parses these, but they are data or markup, not code to review by default.
DATA_LANGUAGES = {"Json", "Yaml", "Html", "Css"}


def default_base(root: Path) -> str:
    origin = git_lines(root, "symbolic-ref", "--short", "refs/remotes/origin/HEAD")
    if origin:
        return origin[0]
    for branch in ("main", "master"):
        if git_lines(root, "rev-parse", "--verify", "--quiet", branch):
            return branch
    return "HEAD"


def linter_blocks(linters: list[dict]) -> str:
    blocks = []
    for linter in linters:
        blocks.append("\n".join([
            "[[linters]]",
            f"name = {json.dumps(linter['name'])}  # found via {linter['evidence']}",
            f"format = {json.dumps(linter['format'])}",
            f"command = {json.dumps(linter['command'])}",
            f"extensions = {json.dumps(linter['extensions'])}",
        ]))
    return "\n\n".join(blocks) or "# No project linters detected. Add [[linters]] blocks here."


def scaffold(target: Path) -> None:
    for folder in ("rules", "rule-tests"):
        (target / folder).mkdir(parents=True, exist_ok=True)
        (target / folder / ".gitkeep").touch()
    for name in COPIED:
        if not (target / name).exists():
            shutil.copy(TEMPLATES / name, target / name)


def write_config(root: Path, target: Path) -> dict:
    # Probe with the project's sgconfig so its languageGlobs (e.g. .ts parsed as Tsx) are reflected.
    detected = detect(root, target / "sgconfig.yml")
    census = detected["extensions"]
    reviewed = [e["extension"] for e in census if e["ast_grep"] and e["ast_grep"] not in DATA_LANGUAGES]
    not_reviewed = [e["extension"] for e in census if e["extension"] not in reviewed]
    config = (TEMPLATES / "config.toml").read_text()
    config = (config.replace("{{extensions}}", json.dumps(reviewed))
                    .replace("{{not_reviewed}}", json.dumps(not_reviewed))
                    .replace("{{base}}", json.dumps(default_base(root)))
                    .replace("{{linters}}", linter_blocks(detected["linters"])))
    (target / "config.toml").write_text(config)
    return {
        "extensions": reviewed,
        "not_reviewed": not_reviewed,
        "census": census,
        "ast_grep_installed": detected["ast_grep_installed"],
        "linters": [{"name": linter["name"], "evidence": linter["evidence"], "installed": bool(linter["binary"])}
                    for linter in detected["linters"]],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    target = root / STANDARDS_DIR
    if (target / "config.toml").exists():
        sys.exit(f"{target} already has config.toml; edit it instead of re-running init.")
    scaffold(target)
    summary = write_config(root, target)
    created = sorted(str(p.relative_to(root)) for p in target.rglob("*") if p.is_file())
    print(json.dumps({"created": created, **summary}, indent=2))


if __name__ == "__main__":
    main()
