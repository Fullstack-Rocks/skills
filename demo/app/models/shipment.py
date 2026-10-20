from dataclasses import dataclass


@dataclass
class Shipment:
    id: int
    order_id: int
    carrier: str
    tracking: str

    def label(self) -> str:
        return f"Shipment #{self.id} ({self.order_id})"
