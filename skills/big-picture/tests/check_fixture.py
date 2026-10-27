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


def check_api(edges: set, findings: set) -> dict[str, bool]:
    return {
        "operation matched across parameter names": ("operation:GET /orders/{id}/total", "implemented-by", "endpoint:GET /orders/{order_id}/total") in edges,
        "operation models": ("operation:PUT /customers/{ref}", "accepts", "api-model:CustomerUpdate") in edges
        and ("api-model:Order", "has", "api-model:CustomerUpdate") in edges,
        "operation without handler": "operation-without-handler:operation:PUT /customers/{ref}" in findings,
        "endpoint not in spec": "endpoint-not-in-spec:endpoint:POST /imports" in findings,
    }


def check_lenses(nodes: dict, edges: set, views: list[dict]) -> dict[str, bool]:
    """Pattern rules over .env and compose files, and views defined by files."""
    return {
        "env keys from a pattern rule": {"env-key:REDIS_URL", "env-key:CACHE_TTL_SECONDS", "env-key:DATABASE_URL"} <= set(nodes),
        "compose services by image": "redis:redis" in nodes and "valkey:valkey" in nodes and "redis:postgres" not in nodes,
        "code reads env and cache": {("module:app/cache.py", "reads-env", "env-key:REDIS_URL"),
                                     ("fn:app/cache.py#cached_total", "writes-cache", "redis:redis")} <= edges,
        "views from files": [v["id"] for v in views] == ["cache", "config"] and views[0]["colors"]["redis"] == "#DC382D",
    }


def check_systems(nodes: dict, edges: set) -> dict[str, bool]:
    """Systems from top-level code folders, and the contracts between them (topics, socket messages)."""
    in_system = {n["id"]: n.get("system") for n in nodes.values()}
    return {
        "systems from code folders": {n for n in nodes if n.startswith("system:")} == {"system:app", "system:web", "system:worker"},
        "event across systems": {("fn:app/events.py#announce_order", "publishes", "topic:order.created"),
                                 ("fn:worker/handlers.py#send_receipt", "consumes", "topic:order.created")} <= edges,
        "socket both ways": {("fn:web/live.ts#watchPrices", "sends", "message:subscribe"),
                             ("fn:app/events.py#on_subscribe", "receives", "message:subscribe"),
                             ("fn:app/events.py#push_price", "sends", "message:price.update")} <= edges,
        "no call across languages": not any(k == "calls" and in_system.get(a) == "web" and in_system.get(b) == "app" for a, k, b in edges),
    }


def check(graph: dict) -> list[str]:
    nodes = {n["id"]: n for n in graph["nodes"]}
    edges = {(e["from"], e["kind"], e["to"]) for e in graph["edges"]}
    findings = {f["id"] for f in graph["findings"]}
    expected = (check_schema(nodes, edges) | check_lookups(nodes, edges, findings) | check_api(edges, findings)
                | check_lenses(nodes, edges, graph.get("views", [])) | check_systems(nodes, edges))
    return [name for name, ok in expected.items() if not ok]


def main() -> None:
    subprocess.run([sys.executable, str(BUILD), str(FIXTURE)], check=True, capture_output=True)
    misses = check(json.loads((FIXTURE / ".big-picture" / "out" / "graph.json").read_text()))
    print("fixture: all checks pass" if not misses else "fixture misses: " + ", ".join(misses))
    sys.exit(1 if misses else 0)


if __name__ == "__main__":
    main()
