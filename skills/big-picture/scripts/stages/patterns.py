"""Pattern rules (.big-picture/patterns/*.yml): regexes over files ast-grep can't parse (.env, nginx
config, INI, Dockerfiles). Each match comes out shaped like an ast-grep match, named groups as
captures, so the type, edge and property metadata of rules.py applies unchanged.

  id: env-file-key
  files: [".env.example", "**/.env.*"]       # globs against the path or the file name
  regex: '^(?P<KEY>[A-Z][A-Z0-9_]*)='         # capture names, never secret values
  metadata: { node: env-key, id: "{KEY}" }
"""
import re
from fnmatch import fnmatch
from pathlib import Path, PurePosixPath

from stages.files import definitions


def matching(files: list[str], globs: list[str]) -> list[str]:
    return [f for f in files if any(fnmatch(f, g) or fnmatch(PurePosixPath(f).name, g) for g in globs)]


def as_match(rule: dict, file: str, text: str, found: re.Match) -> dict:
    """One regex match in the shape of an ast-grep JSON match (0-based lines)."""
    line = text.count("\n", 0, found.start())
    end = line + found[0].count("\n")
    captures = {name: {"text": value, "range": {"start": {"line": line}}} for name, value in found.groupdict().items() if value is not None}
    return {"ruleId": rule["id"], "file": file, "text": found[0], "metadata": rule.get("metadata", {}),
            "range": {"start": {"line": line}, "end": {"line": end}}, "metaVariables": {"single": captures}}


def scan_patterns(root: Path, files: list[str]) -> list[dict]:
    """Every pattern rule's matches across the files its globs select."""
    matches = []
    for _, rule in definitions(root / ".big-picture" / "patterns"):
        regex = re.compile(rule["regex"], re.MULTILINE)
        for file in matching(files, rule.get("files", [])):
            text = (root / file).read_text(errors="replace")
            matches += [as_match(rule, file, text, found) for found in regex.finditer(text)]
    return matches
