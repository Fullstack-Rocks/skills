from dataclasses import dataclass


@dataclass
class Review:
    id: int
    product_id: int
    stars: int
    body: str

    def label(self) -> str:
        return f"Review #{self.id} ({self.product_id})"
