"""bp db: every table, view and lookup with its columns' keys and how the tables connect."""
from graph.load import Graph

RELATIONS = ("references", "selects-from")


def table_line(graph: Graph, table: dict) -> str:
    """One table: name, kind, column count, primary key, where its structure comes from, its relations."""
    columns = table.get("columns", [])
    keys = ",".join(c["name"] for c in columns if c.get("pk")) or "-"
    links = [f"{e['kind']} {e['to'].removeprefix('table:')}{' ~' if e['resolved'] == 'approx' else ''}"
             for e in graph.outgoing.get(table["id"], []) if e["kind"] in RELATIONS]
    source = "sql" if table.get("declared") else ("model" if columns else "code only")
    return f"  {table['name']:<24} {table.get('kind', 'table'):<18} {len(columns):>3} cols  pk {keys:<14} [{source}]  {'; '.join(links)}"


def show_db(graph: Graph) -> None:
    tables = sorted((n for n in graph.nodes.values() if n["type"] == "table"), key=lambda n: n["id"])
    print(f"{len(tables)} tables and views")
    for table in tables:
        print(table_line(graph, table))
    lookups = [n for n in graph.nodes.values() if n["type"] == "lookup"]
    print(f"\n{len(lookups)} JSON lookups")
    for lookup in lookups:
        sites = [e["from"] for e in graph.incoming.get(lookup["id"], []) if e["kind"] == "looks-up"]
        print(f"  {lookup['name']}  ({len(sites)} places: {', '.join(sites)})")
    print("\n~ marks a relation inferred by naming convention; bp node table:<name> shows a table in full.")


def show_view(graph: Graph, view_id: str | None) -> None:
    """A view the project defined in .big-picture/views: its nodes by type and the connections it follows."""
    view = next((v for v in graph.views if v["id"] == view_id), None)
    if view is None:
        print("views: " + (", ".join(f"{v['id']} ({v['title']})" for v in graph.views) or "none; the big-picture skill adds them"))
        return
    print(f"{view['title']}: types {', '.join(view['types'])}; connections {', '.join(view['edges'] or ['all'])}")
    for node in sorted((n for n in graph.nodes.values() if n["type"] in view["types"]), key=lambda n: n["id"]):
        print(view_line(graph, node, view["edges"]))


def view_line(graph: Graph, node: dict, kinds: list[str] | None) -> str:
    """A view's node with the connections into it that the view follows (none: nothing uses it)."""
    links = [f"{e['kind']} <- {e['from']}" for e in graph.incoming.get(node["id"], []) if not kinds or e["kind"] in kinds]
    return f"  {node['id']:<40} {'; '.join(links) or '(nothing uses it)'}"


def show_capsules(graph: Graph) -> None:
    """Groups of modules (and tables) that work together, as the build found them."""
    capsules = sorted((n for n in graph.nodes.values() if n["type"] == "capsule"), key=lambda n: -n.get("members", 0))
    print(f"{len(capsules)} capsules (name them in .big-picture/capsules.yml)")
    for capsule in capsules:
        members = [e["to"].split(":", 1)[1] for e in graph.outgoing.get(capsule["id"], []) if e["kind"] == "groups"]
        print(f"  {capsule['name']:<24} {capsule['id']:<52} {', '.join(sorted(members))}")


def direct_links(graph: Graph) -> dict[tuple[str, str, str], int]:
    """(system, system, kind) -> how many edges run straight from one system's code to another's."""
    links: dict[tuple[str, str, str], int] = {}
    for edge in [e for edges in graph.outgoing.values() for e in edges if e["kind"] != "contains"]:
        a, b = graph.nodes.get(edge["from"], {}).get("system"), graph.nodes.get(edge["to"], {}).get("system")
        if a and b and a != b:
            links[(a, b, edge["kind"])] = links.get((a, b, edge["kind"]), 0) + 1
    return links


def shared_contracts(graph: Graph) -> dict[str, list[str]]:
    """contract -> ["app publishes", "worker consumes"], for nodes in no system that two or more systems use."""
    uses: dict[str, set[str]] = {}
    for edge in [e for edges in graph.outgoing.values() for e in edges if e["kind"] != "contains"]:
        system = graph.nodes.get(edge["from"], {}).get("system")
        if system and not graph.nodes.get(edge["to"], {}).get("system"):
            uses.setdefault(edge["to"], set()).add(f"{system} {edge['kind']}")
    return {node: sorted(u) for node, u in uses.items() if len({x.split()[0] for x in u}) > 1}


def show_systems(graph: Graph) -> None:
    """The project's systems, how they call each other directly, and the contracts they share."""
    systems = sorted(n["name"] for n in graph.nodes.values() if n["type"] == "system")
    print(f"{len(systems)} systems: {', '.join(systems) or 'none (one system, or set them in .big-picture/systems.yml)'}")
    direct, shared = direct_links(graph), shared_contracts(graph)
    print("\ndirect links between systems")
    for (a, b, kind), count in sorted(direct.items()):
        print(f"  {a} -> {b}  {kind} x{count}")
    print("\ncontracts several systems use (topics, messages, ...)")
    for node, uses in sorted(shared.items()):
        print(f"  {node:<36} {' · '.join(uses)}")
    print("\nbp node <contract or endpoint> shows both sides with file:line.")
