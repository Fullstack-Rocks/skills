from app.api import (  # noqa: F401  (importing registers the routes)
    coupon_routes, customer_routes, invoice_routes, order_routes,
    product_routes, review_routes, shipment_routes, warehouse_routes,
)
from app.http import ROUTES


def describe_routes() -> list[str]:
    return [f"{method} {path}" for method, path, _ in ROUTES]
