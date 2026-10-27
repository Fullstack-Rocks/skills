"""Fixture routes: two the OpenAPI document describes, one it leaves out."""
from app.reports import order_total, orders_for_customer


def route(method: str, path: str):
    return lambda handler: handler


@route("GET", "/orders/{order_id}/total")
def get_total(request: dict) -> dict:
    return {"order_id": request["order_id"], "total_cents": order_total(int(request["order_id"]))}


@route("GET", "/customers/{ref}/orders")
def customer_orders(request: dict) -> list[dict]:
    return orders_for_customer(request["ref"])


@route("POST", "/imports")
def start_import(request: dict) -> dict:
    return {"started": True}
