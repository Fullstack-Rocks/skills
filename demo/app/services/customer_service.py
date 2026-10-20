from app.db import Database
from app.models.customer import Customer


def get_customer(db: Database, customer_id: int) -> Customer:
    row = db.fetch_one("customers", customer_id)
    if row is None:
        raise LookupError(f"customer {customer_id} not found")
    return Customer(**row)


def create_customer(db: Database, data: dict) -> Customer:
    if "email" not in data:
        raise ValueError("customer.email is required")
    if "name" not in data:
        raise ValueError("customer.name is required")
    if "tier" not in data:
        raise ValueError("customer.tier is required")
    new_id = db.insert("customers", data)
    return Customer(id=new_id, email=data["email"], name=data["name"], tier=data["tier"])


def list_customers(db: Database, limit: int = 50) -> list[Customer]:
    return [Customer(**row) for row in db.fetch_many("customers", limit=limit)]
