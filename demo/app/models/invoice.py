from dataclasses import dataclass


@dataclass
class Invoice:
    id: int
    order_id: int
    due_days: int
    paid: bool

    def label(self) -> str:
        return f"Invoice #{self.id} ({self.order_id})"
