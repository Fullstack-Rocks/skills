from dataclasses import dataclass


@dataclass
class Order:
    id: int
    customer_id: int
    total_cents: int
    status: str

    def label(self) -> str:
        return f"Order #{self.id} ({self.customer_id})"
