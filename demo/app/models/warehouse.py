from dataclasses import dataclass


@dataclass
class Warehouse:
    id: int
    city: str
    capacity: int
    open: bool

    def label(self) -> str:
        return f"Warehouse #{self.id} ({self.city})"
