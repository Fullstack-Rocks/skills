from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    email: str
    name: str
    tier: str

    def label(self) -> str:
        return f"Customer #{self.id} ({self.email})"
