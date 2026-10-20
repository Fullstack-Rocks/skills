from dataclasses import dataclass


@dataclass
class Product:
    id: int
    sku: str
    price_cents: int
    stock: int

    def label(self) -> str:
        return f"Product #{self.id} ({self.sku})"
