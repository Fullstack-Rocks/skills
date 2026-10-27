"""bp node and bp neighbors: one node with everything connected to it, or a walk N steps out."""
from graph.load import Graph
from graph.walk import edges, neighbors
from verbs.find import location

INVERSE = {"calls": "called by", "handled-by": "handles", "contains": "in", "reads": "read by",
           "writes": "written by", "maps-to": "mapped by", "references": "referenced by", "selects-from": "selected by",
           "looks-up": "looked up by", "through": "looked through by", "finds": "found by", "defines": "defined in",
           "groups": "in capsule", "implemented-by": "implements", "calls-api": "called by (API)", "publishes": "published by",
           "consumes": "consumed by", "sends": "sent by", "receives": "received by"}
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


def column_flags(column: dict) -> str:
    flags = ["PK" if column.get("pk") else "", "" if column.get("nullable", True) else "NOT NULL",
             "UNIQUE" if column.get("unique") and not column.get("pk") else "",
             f"-> {column['references']}" if column.get("references") else "",
             f"DEFAULT {column['default']}" if column.get("default") else "", f"CHECK ({column['check']})" if column.get("check") else ""]
    return " ".join(f for f in flags if f)


def print_fields(node: dict) -> None:
    """A table's kind, columns, constraints and indexes, or a model's fields."""
    if node.get("columns"):
        origin = "declared in SQL" if node.get("declared") else "inferred from its model; keys by naming convention"
        print(f"{node.get('kind', 'table')}, {origin}")
        print(f"columns ({len(node['columns'])})")
        for column in node["columns"]:
            print(f"  {column['name']:<20} {column['type']:<16} {column_flags(column)}")
    for constraint in node.get("constraints", []):
        print(f"  constraint {constraint}")
    for index in node.get("indexes", []):
        print(f"  {'unique ' if index['unique'] else ''}index {index['name']} ({', '.join(index['columns'])})")
    if node.get("fields"):
        print(f"fields ({len(node['fields'])}): " + ", ".join(f"{f['name']}: {f['type']}" for f in node["fields"]))
    if node.get("expression"):
        print(f"lookup: {node['table']}.{node['column']} path {node['path']} = {node['to_table']}.{node['to_column']}")
        print(f"  e.g. {node['expression']}")


def print_health(graph: Graph, node_id: str) -> None:
    findings = graph.findings.get(node_id, [])
    if findings:
        print(f"health ({len(findings)})")
    for finding in findings:
        file, line = finding["sites"][0]
        print(f"  {finding['rule']:<24} {finding['detail'][:90]}  {file}:{line or ''}")


def print_doc(node: dict) -> None:
    """The note an agent wrote about this node (.big-picture/docs), flagged when the code changed since."""
    if node.get("docText"):
        print(f"note ({node['doc']}{', STALE: the code changed since it was written' if node.get('docStale') else ''})")
        print("  " + node["docText"].replace("\n", "\n  "))


def show_node(graph: Graph, node: dict, entries: list[str]) -> None:
    """entries: the node's entry points, from walk.entry_points."""
    details = [node["type"], f"system {node['system']}" if node.get("system") else "", location(node), node.get("signature", ""),
               f"hash {node['hash']}" if node.get("hash") else ""]
    print(node["id"])
    print("  " + " · ".join(d for d in details if d))
    if entries:
        print("entry points: " + ", ".join(entries))
    print_doc(node)
    print_fields(node)
    print_groups(graph, node["id"], "out")
    print_groups(graph, node["id"], "in")
    print_health(graph, node["id"])


def show_neighbors(graph: Graph, node: dict, depth: int, direction: str, kinds: set[str] | None) -> None:
    found = neighbors(graph, node["id"], depth, direction, kinds)
    print(f"{node['id']}: {len(found)} nodes within {depth} steps ({direction})")
    for step, edge, other in found:
        arrow = "->" if edge["from"] != other else "<-"
        print(f"  {step} {mark(edge)}{arrow} {edge['kind']:<11} {other:<64} {site(edge)}")
