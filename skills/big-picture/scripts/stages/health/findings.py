"""Stage 5: health findings from the call-depth and code-standards skills, attached to the node whose
lines they fall in. Both skills are found next to this one; a missing one is reported and skipped."""
import json
import subprocess
import sys
from pathlib import Path

from graph import Graph

SKILLS = Path(__file__).resolve().parents[4]
CALL_DEPTH = SKILLS / "call-depth" / "scripts"
CODE_STANDARDS = SKILLS / "code-standards" / "scripts"
INSTALL = "npx skills add Fullstack-Rocks/skills --skill {}"
# How to address each kind of finding, from the under-engineering and call-depth skills. Findings from a
# linter or a code-standards rule carry their advice in their message.
FIXES = {
    "complexity": "Flatten it, re-measuring after each step: guard clauses and early returns, then a named "
                  "function per branch, then separate functions instead of flag parameters.",
    "function-length": "Split it so each function does one thing; the entrypoint keeps a short sequence of "
                       "well-named calls and the work moves into the functions it calls.",
    "file-length": "Split the file by responsibility, or extract the shared helper other files repeat.",
    "folder-size": "Group the files into subfolders named after what they hold, 5-6 code files each, "
                   "continuing the parent's name (payments/ -> payments/refunds/).",
    "folder-name": "Rename the folder to 1-3 words naming what it holds.",
    "dynamic-call": "Replace the runtime lookup with a direct call, or a match/switch on a typed value whose "
                    "branches call directly, so go-to-definition reaches the code that runs.",
    "dynamic-attr": "If the looked-up attribute gets called, make it a direct call or a typed match/switch.",
    "lookup-call": "Replace the registry call (handlers[kind](...)) with a match/switch whose branches call "
                   "each handler directly.",
    "duplicate": "Extract the duplicated code into one function both places call.",
}
LINTER_FIX = "Follow the rule's message above; `code-standards` review marks the ones with a mechanical fix."


def call_depth_lines(graph: Graph, code_paths: list[str]) -> list[str]:
    lines = []
    for script in ("scan.py", "layout.py"):
        result = subprocess.run([sys.executable, str(CALL_DEPTH / script), *code_paths], cwd=graph.root,
                                capture_output=True, text=True, check=False)
        lines += result.stdout.splitlines()
    return lines


def add_call_depth(graph: Graph, code_paths: list[str]) -> None:
    """scan.py and layout.py print KIND<TAB>path[:line]<TAB>detail; folders have no line."""
    for row in call_depth_lines(graph, code_paths):
        kind, location, detail = (row.split("\t") + ["", ""])[:3]
        if kind in ("OK", "SCANNED", "COVERED", "NO_RULES", "MISSING_TOOL", "MISSING_PATH", ""):
            continue
        path, _, line = location.rpartition(":") if location[-1:].isdigit() else (location, "", "")
        relative = str((graph.root / path).resolve().relative_to(graph.root))
        node = f"folder:{relative}" if kind.startswith("FOLDER") else graph.enclosing(relative, int(line or 0))
        if node not in graph.nodes:  # ignored or minified: call-depth walks whole folders, the inventory doesn't
            continue
        graph.add_finding(kind.lower().replace("_", "-"), node, relative, int(line) if line else None,
                          detail, "call-depth")


def add_code_standards(graph: Graph, out: Path) -> None:
    """review.py --all; lizard findings are skipped since call-depth already reports them."""
    report = out / "code-standards.json"
    subprocess.run([sys.executable, str(CODE_STANDARDS / "review.py"), "--all", "--out", str(report)],
                   cwd=graph.root, capture_output=True, text=True, check=False)
    if not report.exists():
        print("health: code-standards review produced no report")
        return
    for finding in json.loads(report.read_text())["findings"]:
        if finding["source"] == "lizard":
            continue
        node = graph.enclosing(finding["file"], finding["line"] or 0)
        graph.add_finding(finding["rule_id"], node, finding["file"], finding["line"], finding["message"],
                          finding["source"])


def add_fixes(graph: Graph) -> None:
    """Give every finding a `fix`: what to do about it."""
    for finding in graph.findings.values():
        finding.setdefault("fix", FIXES.get(finding["rule"], LINTER_FIX))


def add_health(graph: Graph, code_paths: list[str], out: Path) -> None:
    if (CALL_DEPTH / "scan.py").exists():
        add_call_depth(graph, code_paths)
    else:
        print(f"health: call-depth skill not found next to big-picture ({INSTALL.format('call-depth')})")
    if not (graph.root / ".code-standards" / "config.toml").exists():
        print("health: no .code-standards/ in this project, code-standards findings skipped")
    elif (CODE_STANDARDS / "review.py").exists():
        add_code_standards(graph, out)
    else:
        print(f"health: code-standards skill not found next to big-picture ({INSTALL.format('code-standards')})")
