"""Walks over the loaded graph. The viewer's walks (big-picture, phase 2) must give the same answers."""
from pathlib import PurePosixPath

from graph.load import Graph

ENTRY_TYPES = {"endpoint", "job", "cli"}


def edges(graph: Graph, node_id: str, direction: str) -> list[tuple[dict, str]]:
    """(edge, the node on its other end) leaving node_id in one direction: out, in or both."""
    found = []
    if direction in ("out", "both"):
        found += [(e, e["to"]) for e in graph.outgoing.get(node_id, [])]
    if direction in ("in", "both"):
        found += [(e, e["from"]) for e in graph.incoming.get(node_id, [])]
    return found


def neighbors(graph: Graph, node_id: str, depth: int, direction: str, kinds: set[str] | None = None) -> list[tuple[int, dict, str]]:
    """Breadth-first (step, edge, node) up to depth steps away; each node once, at its nearest step."""
    seen, frontier, found = {node_id}, [node_id], []
    for step in range(1, depth + 1):
        following = []
        for current in frontier:
            for edge, other in edges(graph, current, direction):
                if other in seen or (kinds and edge["kind"] not in kinds):
                    continue
                seen.add(other)
                following.append(other)
                found.append((step, edge, other))
        frontier = following
    return found


def entry_points(graph: Graph, node_id: str, max_depth: int = 12) -> list[str]:
    """Endpoints, jobs and CLIs that reach node_id through handled-by, calls, reads and writes edges."""
    reached = neighbors(graph, node_id, max_depth, "in", {"calls", "handled-by", "reads", "writes"})
    return sorted(other for _, _, other in reached if graph.nodes.get(other, {}).get("type") in ENTRY_TYPES)


def search_key(node: dict) -> str:
    """The id plus file-stem.name, so order_service.get_order finds fn:app/services/order_service.py#get_order."""
    stem = PurePosixPath(node["file"]).stem if node.get("file") else ""
    return f"{node['id']} {stem}.{node['name']}".lower()


def find(graph: Graph, text: str, node_type: str | None = None) -> list[dict]:
    """Nodes whose id or file-stem.name contains text (case-insensitive), optionally of one type;
    exact ids and names first."""
    needle = text.lower()
    hits = [n for n in graph.nodes.values()
            if needle in search_key(n) and (node_type is None or n["type"] == node_type)]
    return sorted(hits, key=lambda n: (n["id"].lower() != needle, n["name"].lower() != needle, len(n["id"])))
