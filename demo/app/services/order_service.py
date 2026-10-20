from app.db import Database
from app.models.order import Order


def get_order(db: Database, order_id: int) -> Order:
    row = db.fetch_one("orders", order_id)
    if row is None:
        raise LookupError(f"order {order_id} not found")
    return Order(**row)


def create_order(db: Database, data: dict) -> Order:
    if "customer_id" not in data:
        raise ValueError("order.customer_id is required")
    if "total_cents" not in data:
        raise ValueError("order.total_cents is required")
    if "status" not in data:
        raise ValueError("order.status is required")
    new_id = db.insert("orders", data)
    return Order(id=new_id, customer_id=data["customer_id"], total_cents=data["total_cents"], status=data["status"])


def list_orders(db: Database, limit: int = 50) -> list[Order]:
    return [Order(**row) for row in db.fetch_many("orders", limit=limit)]


def order_total_cents(order: Order, items: list[dict], coupon: dict | None, customer_tier: str) -> int:
    total = 0
    for item in items:
        if item["qty"] <= 0:
            continue
        price = item["price_cents"] * item["qty"]
        if item.get("bulk") and item["qty"] >= 10:
            price = int(price * 0.9)
        total += price
    if coupon and coupon.get("active"):
        if coupon["percent_off"] > 50:
            raise ValueError("coupon too generous")
        total -= total * coupon["percent_off"] // 100
    if customer_tier == "gold":
        total -= 500
    elif customer_tier == "silver":
        total -= 200
    elif customer_tier == "staff" and total > 10_000:
        total = total // 2
    if order.status == "draft" or total < 0:
        total = max(total, 0)
    return total
