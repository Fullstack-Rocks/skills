from os import getenv

from app.db import Database
from app.models.shipment import Shipment


def get_shipment(db: Database, shipment_id: int) -> Shipment:
    row = db.fetch_one("shipments", shipment_id)
    if row is None:
        raise LookupError(f"shipment {shipment_id} not found")
    return Shipment(**row)


def create_shipment(db: Database, data: dict) -> Shipment:
    if "order_id" not in data:
        raise ValueError("shipment.order_id is required")
    if "carrier" not in data:
        raise ValueError("shipment.carrier is required")
    if "tracking" not in data:
        raise ValueError("shipment.tracking is required")
    new_id = db.insert("shipments", data)
    return Shipment(id=new_id, order_id=data["order_id"], carrier=data["carrier"], tracking=data["tracking"])


def list_shipments(db: Database, limit: int = 50) -> list[Shipment]:
    return [Shipment(**row) for row in db.fetch_many("shipments", limit=limit)]


def default_carrier() -> str:
    return getenv("DEFAULT_CARRIER", "ups")
