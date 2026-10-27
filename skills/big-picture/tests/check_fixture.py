"""Build tests/fixture and check what the schema, lookup and repeat stages must find there.

Usage: python3 check_fixture.py      (exit 1 and a list of misses when anything is wrong)
"""
import json
import subprocess
import sys
from pathlib import Path

FIXTURE = Path(__file__).resolve().parent / "fixture"
BUILD = FIXTURE.parent.parent / "scripts" / "build.py"
LOOKUP = "lookup:orders.meta.customer_ref→customers.ref"


def check_schema(nodes: dict, edges: set) -> dict[str, bool]:
    orders = {c["name"]: c for c in nodes["table:orders"]["columns"]}
    items = {c["name"]: c for c in nodes["table:order_items"]["columns"]}
    kinds = [nodes[f"table:{t}"]["kind"] for t in ("orders", "import_rows", "paid_orders", "customer_totals")]
    return {
        "table kinds": kinds == ["table", "temporary table", "view", "materialized view"],
        "inline primary key": orders["id"]["pk"] and not orders["id"]["nullable"],
        "composite primary key": items["order_id"]["pk"] and items["sku"]["pk"],
        "inline foreign key": orders["customer_id"].get("references") == "customers.id",
        "table foreign key": items["order_id"].get("references") == "orders.id",
        "default": orders["status"].get("default") == "'new'",
        "check": orders["total_cents"].get("check") == "total_cents >= 0",
        "named constraint": any("orders_status_check" in c for c in nodes["table:orders"]["constraints"]),
        "indexes": [i["name"] for i in nodes["table:customers"].get("indexes", [])] == ["customers_email_idx"],
        "view sources": ("table:paid_orders", "selects-from", "table:orders") in edges,
    }


def check_lookups(nodes: dict, edges: set, findings: set) -> dict[str, bool]:
    in_code = {("fn:app/reports.py#orders_for_customer", "looks-up", LOOKUP), ("fn:app/reports.py#customer_of_order", "looks-up", LOOKUP)}
    return {
        "lookup in code, both orders": in_code <= edges,
        "lookup in a view": ("table:customer_totals", "looks-up", LOOKUP) in edges,
        "sqlite json_extract": "lookup:orders.meta.customer.ref→customers.ref" in nodes,
        "repeated operation": "repeated-operation:fn:app/reports.py#order_total" in findings,
    }


def check(graph: dict) -> list[str]:
    nodes = {n["id"]: n for n in graph["nodes"]}
    edges = {(e["from"], e["kind"], e["to"]) for e in graph["edges"]}
    expected = check_schema(nodes, edges) | check_lookups(nodes, edges, {f["id"] for f in graph["findings"]})
    return [name for name, ok in expected.items() if not ok]


def main() -> None:
    subprocess.run([sys.executable, str(BUILD), str(FIXTURE)], check=True, capture_output=True)
    misses = check(json.loads((FIXTURE / ".big-picture" / "out" / "graph.json").read_text()))
    print("fixture: all checks pass" if not misses else "fixture misses: " + ", ".join(misses))
    sys.exit(1 if misses else 0)


if __name__ == "__main__":
    main()
