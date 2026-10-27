"""Stage 5: health findings from the call-depth and code-standards skills, attached to the node whose
lines they fall in. Both skills are found next to this one; a missing one is reported and skipped."""
import json
import subprocess
import sys
from pathlib import Path

from graph import Graph

SKILLS = Path(__file__).resolve().parents[3]
CALL_DEPTH = SKILLS / "call-depth" / "scripts"
CODE_STANDARDS = SKILLS / "code-standards" / "scripts"
INSTALL = "npx skills add Fullstack-Rocks/skills --skill {}"


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
        relative = str(Path(path).resolve().relative_to(graph.root))
        node = f"folder:{relative}" if kind.startswith("FOLDER") else graph.enclosing(relative, int(line or 0))
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
