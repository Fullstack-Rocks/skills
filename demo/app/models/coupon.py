from dataclasses import dataclass


@dataclass
class Coupon:
    id: int
    code: str
    percent_off: int
    active: bool

    def label(self) -> str:
        return f"Coupon #{self.id} ({self.code})"
