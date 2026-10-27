"""Fixture code: JSON lookups in SQL strings, and one query run from two places."""
from app.db import fetch_one, run


def orders_for_customer(ref: str) -> list[dict]:
    return run("""
        SELECT o.id, o.total_cents
        FROM orders AS o
        JOIN customers c ON (o.meta->>'customer_ref')::text = c.ref
        WHERE c.ref = %s
    """, ref)


def customer_of_order(order_id: int) -> dict:
    return run("SELECT c.* FROM customers c JOIN orders o ON c.ref = o.meta->>'customer_ref' WHERE o.id = %s", order_id)


def sqlite_lookup(order_id: int) -> dict:
    return run("SELECT * FROM orders JOIN customers ON json_extract(orders.meta, '$.customer.ref') = customers.ref", order_id)


def order_total(order_id: int) -> int:
    return fetch_one("orders", order_id)["total_cents"]


def order_status(order_id: int) -> str:
    return fetch_one("orders", order_id)["status"]
