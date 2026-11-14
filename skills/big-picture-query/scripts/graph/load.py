"""Load .big-picture/out/graph.json, building it first with the big-picture skill when it is missing."""
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

SCHEMA_VERSION = 1  # the graph.json version this skill reads; big-picture's scripts/graph.py writes it
BUILD = Path(__file__).resolve().parents[3] / "big-picture" / "scripts" / "build.py"
INSTALL = "npx skills add Fullstack-Rocks/skills --skill big-picture"


@dataclass
class Graph:
    nodes: dict[str, dict]
    outgoing: dict[str, list[dict]] = field(default_factory=dict)
    incoming: dict[str, list[dict]] = field(default_factory=dict)
    findings: dict[str, list[dict]] = field(default_factory=dict)
    children: dict[str, list[str]] = field(default_factory=dict)
    repeats: list[dict] = field(default_factory=list)
    views: list[dict] = field(default_factory=list)
    built_at: str = ""
    root: Path = Path(".")


def find_project(start: Path) -> Path | None:
    """The nearest folder at or above start that has a .big-picture/ folder."""
    return next((p for p in (start, *start.parents) if (p / ".big-picture").is_dir()), None)


def build(root: Path) -> None:
    if not BUILD.exists():
        sys.exit(f"no graph at {root}/.big-picture/out/graph.json and big-picture isn't installed: {INSTALL}")
    print(f"bp: no graph yet, building it with {BUILD}", file=sys.stderr)
    subprocess.run([sys.executable, str(BUILD), str(root)], check=True, stdout=sys.stderr)


def index(data: dict) -> Graph:
    graph = Graph({n["id"]: n for n in data["nodes"]}, built_at=data["builtAt"], repeats=data.get("repeats", []),
                  views=data.get("views", []), root=Path(data["root"]))
    for edge in data["edges"]:
        graph.outgoing.setdefault(edge["from"], []).append(edge)
        graph.incoming.setdefault(edge["to"], []).append(edge)
        if edge["kind"] == "contains":
            graph.children.setdefault(edge["from"], []).append(edge["to"])
    for finding in data["findings"]:
        graph.findings.setdefault(finding["node"], []).append(finding)
    return graph


def load(start: Path) -> Graph:
    root = find_project(start)
    if root is None:
        sys.exit(f"no .big-picture/ at or above {start}: build the map first with the big-picture skill ({INSTALL})")
    path = root / ".big-picture" / "out" / "graph.json"
    if not path.exists():
        build(root)
    data = json.loads(path.read_text())
    if data.get("schemaVersion") != SCHEMA_VERSION:
        sys.exit(f"graph.json is schema {data.get('schemaVersion')}, this skill reads {SCHEMA_VERSION}: "
                 "update big-picture and big-picture-query to the same release, then rebuild")
    return index(data)
