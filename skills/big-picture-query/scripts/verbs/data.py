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
