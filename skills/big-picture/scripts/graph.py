"""The graph the build stages fill in and build.py writes to .big-picture/out/graph.json.

Format: references/graph-schema.md. Bump SCHEMA_VERSION when a field changes meaning or goes away;
big-picture-query refuses a version it doesn't know.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1


class Graph:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.nodes: dict[str, dict] = {}
        self.edges: dict[tuple[str, str, str], dict] = {}
        self.findings: dict[str, dict] = {}
        self.coverage: dict[str, str] = {}
        self.repeats: list[dict] = []  # operations and shapes found in several places (stages/health/repeats.py)
        self.views: list[dict] = []  # extra viewer tabs defined in .big-picture/views (stages/views.py)
        self.code_by_file: dict[str, list[dict]] = {}
        self.file_node: dict[str, str] = {}  # a file's own node (module, infra, config, ...), set by the inventory

    def add_node(self, node_id: str, node_type: str, name: str, **fields: object) -> str:
        node = self.nodes.setdefault(node_id, {"id": node_id, "type": node_type, "name": name})
        node.update({k: v for k, v in fields.items() if v is not None})
        if "start" in node and node_type != "module" and node not in self.code_by_file.setdefault(node["file"], []):
            self.code_by_file[node["file"]].append(node)
        return node_id

    def add_edge(self, source: str, target: str, kind: str, via: str, resolved: str = "exact",
                 site: tuple[str, int] | None = None) -> None:
        edge = self.edges.setdefault((source, target, kind), {
            "from": source, "to": target, "kind": kind, "via": via, "resolved": resolved, "sites": []})
        if site and list(site) not in edge["sites"]:
            edge["sites"].append(list(site))

    def add_finding(self, rule: str, node: str, file: str, line: int | None, detail: str, source: str) -> None:
        """One finding per rule and node; a second hit in the same node adds a site."""
        finding = self.findings.setdefault(f"{rule}:{node}", {
            "id": f"{rule}:{node}", "rule": rule, "node": node, "detail": detail, "source": source, "sites": []})
        finding["sites"].append([file, line])

    def enclosing(self, file: str, line: int) -> str:
        """The innermost node with a line range (function, endpoint, model, ...) holding this line, else the module."""
        holders = [n for n in self.code_by_file.get(file, []) if n["start"] <= line <= n["end"]]
        if not holders:
            return f"module:{file}"
        return min(holders, key=lambda n: n["end"] - n["start"])["id"]

    def write(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "schemaVersion": SCHEMA_VERSION,
            "builtAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "root": str(self.root),
            "coverage": self.coverage,
            "nodes": sorted(self.nodes.values(), key=lambda n: n["id"]),
            "edges": sorted(self.edges.values(), key=lambda e: (e["from"], e["kind"], e["to"])),
            "findings": sorted(self.findings.values(), key=lambda f: f["id"]),
            "repeats": self.repeats,
            "views": self.views,
        }
        path.write_text(json.dumps(data, indent=1) + "\n")
