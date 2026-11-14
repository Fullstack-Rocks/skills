"""bp health and bp similar: what is wrong in a part of the code and how to fix it, and what it repeats."""
from graph.load import Graph

BRIEF_MAX = 60


def inside(graph: Graph, node_id: str) -> list[str]:
    """The node and everything it contains."""
    found, frontier = [node_id], [node_id]
    while frontier:
        frontier = [child for parent in frontier for child in graph.children.get(parent, [])]
        found += frontier
    return found


def show_health(graph: Graph, node: dict) -> None:
    """Every finding on the node and inside it, grouped by rule, with where it is and how to fix it."""
    findings = [f for n in inside(graph, node["id"]) for f in graph.findings.get(n, [])]
    print(f"{node['id']}: {len(findings)} health findings" + (" (none)" if not findings else ""))
    by_rule: dict[str, list[dict]] = {}
    for finding in findings:
        by_rule.setdefault(finding["rule"], []).append(finding)
    for rule, group in sorted(by_rule.items(), key=lambda g: -len(g[1])):
        print(f"\n{rule} ({len(group)}, {group[0]['source']})")
        print(f"  fix: {group[0].get('fix', '')}")
        for finding in group[:BRIEF_MAX]:
            file, line = finding["sites"][0]
            print(f"  - {finding['node']}  {file}:{line or ''}  {finding['detail'][:120]}")


def show_similar(graph: Graph, node: dict) -> None:
    """Repeated operations and shapes that run in the node or inside it, with every other place they run."""
    mine = set(inside(graph, node["id"]))
    groups = [r for r in graph.repeats if any(site[2] in mine for site in r["sites"])]
    print(f"{node['id']}: {len(groups)} repeated operations or shapes" + (" (none)" if not groups else ""))
    for group in groups:
        label = "repeated operation (health finding)" if group["kind"] == "operation" else "repeated shape (information)"
        print(f"\n{group['key']}  [{label}]")
        for file, line, owner in group["sites"]:
            print(f"  {'*' if owner in mine else ' '} {owner:<60} {file}:{line}")
