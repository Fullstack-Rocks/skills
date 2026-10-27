"""bp node and bp neighbors: one node with everything connected to it, or a walk N steps out."""
from graph.load import Graph
from graph.walk import edges, neighbors
from verbs.find import location

INVERSE = {"calls": "called by", "handled-by": "handles", "contains": "in", "reads": "read by",
           "writes": "written by", "maps-to": "mapped by"}
GROUP_MAX = 40


def site(edge: dict) -> str:
    sites = edge["sites"]
    if not sites:
        return ""
    more = f" (+{len(sites) - 1})" if len(sites) > 1 else ""
    return f"{sites[0][0]}:{sites[0][1]}{more}"


def mark(edge: dict) -> str:
    """~ before an edge whose target was matched by name, not by a type-aware index."""
    return "~" if edge["resolved"] == "approx" else " "


def print_groups(graph: Graph, node_id: str, direction: str) -> None:
    groups: dict[str, list[tuple[dict, str]]] = {}
    for edge, other in edges(graph, node_id, direction):
        label = edge["kind"] if direction == "out" else INVERSE.get(edge["kind"], f"{edge['kind']} (in)")
        groups.setdefault(label, []).append((edge, other))
    for label, members in sorted(groups.items()):
        print(f"{label} ({len(members)})")
        for edge, other in sorted(members, key=lambda m: m[1])[:GROUP_MAX]:
            print(f" {mark(edge)}{other:<64} {site(edge)}")
        if len(members) > GROUP_MAX:
            print(f"   ... {len(members) - GROUP_MAX} more: bp neighbors {node_id!r} --dir {direction}")


def print_fields(graph: Graph, node: dict) -> None:
    """A model's fields, or a table's columns from the model that maps to it."""
    source = node
    if "fields" not in node:
        models = [e["from"] for e in graph.incoming.get(node["id"], []) if e["kind"] == "maps-to"]
        source = graph.nodes.get(models[0], {}) if models else {}
    fields = source.get("fields", [])
    if fields:
        origin = "" if source is node else f" (from {source['id']})"
        print(f"{'fields' if source is node else 'columns'} ({len(fields)}){origin}")
        print("  " + ", ".join(f"{f['name']}: {f['type']}" for f in fields))


def print_health(graph: Graph, node_id: str) -> None:
    findings = graph.findings.get(node_id, [])
    if findings:
        print(f"health ({len(findings)})")
    for finding in findings:
        file, line = finding["sites"][0]
        print(f"  {finding['rule']:<24} {finding['detail'][:90]}  {file}:{line or ''}")


def show_node(graph: Graph, node: dict, entries: list[str]) -> None:
    """entries: the node's entry points, from walk.entry_points."""
    details = [node["type"], location(node), node.get("signature", "")]
    print(node["id"])
    print("  " + " · ".join(d for d in details if d))
    if entries:
        print("entry points: " + ", ".join(entries))
    print_fields(graph, node)
    print_groups(graph, node["id"], "out")
    print_groups(graph, node["id"], "in")
    print_health(graph, node["id"])


def show_neighbors(graph: Graph, node: dict, depth: int, direction: str, kinds: set[str] | None) -> None:
    found = neighbors(graph, node["id"], depth, direction, kinds)
    print(f"{node['id']}: {len(found)} nodes within {depth} steps ({direction})")
    for step, edge, other in found:
        arrow = "->" if edge["from"] != other else "<-"
        print(f"  {step} {mark(edge)}{arrow} {edge['kind']:<11} {other:<64} {site(edge)}")
