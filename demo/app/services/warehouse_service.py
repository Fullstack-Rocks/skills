from app.db import Database
from app.models.warehouse import Warehouse


def get_warehouse(db: Database, warehouse_id: int) -> Warehouse:
    row = db.fetch_one("warehouses", warehouse_id)
    if row is None:
        raise LookupError(f"warehouse {warehouse_id} not found")
    return Warehouse(**row)


def create_warehouse(db: Database, data: dict) -> Warehouse:
    if "city" not in data:
        raise ValueError("warehouse.city is required")
    if "capacity" not in data:
        raise ValueError("warehouse.capacity is required")
    if "open" not in data:
        raise ValueError("warehouse.open is required")
    new_id = db.insert("warehouses", data)
    return Warehouse(id=new_id, city=data["city"], capacity=data["capacity"], open=data["open"])


def list_warehouses(db: Database, limit: int = 50) -> list[Warehouse]:
    return [Warehouse(**row) for row in db.fetch_many("warehouses", limit=limit)]
