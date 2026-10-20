from app.db import Database
from app.models.product import Product


def get_product(db: Database, product_id: int) -> Product:
    row = db.fetch_one("products", product_id)
    if row is None:
        raise LookupError(f"product {product_id} not found")
    return Product(**row)


def create_product(db: Database, data: dict) -> Product:
    if "sku" not in data:
        raise ValueError("product.sku is required")
    if "price_cents" not in data:
        raise ValueError("product.price_cents is required")
    if "stock" not in data:
        raise ValueError("product.stock is required")
    new_id = db.insert("products", data)
    return Product(id=new_id, sku=data["sku"], price_cents=data["price_cents"], stock=data["stock"])


def list_products(db: Database, limit: int = 50) -> list[Product]:
    return [Product(**row) for row in db.fetch_many("products", limit=limit)]
