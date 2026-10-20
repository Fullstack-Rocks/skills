from app.db import Database
from app.models.review import Review


def get_review(db: Database, review_id: int) -> Review:
    row = db.fetch_one("reviews", review_id)
    if row is None:
        raise LookupError(f"review {review_id} not found")
    return Review(**row)


def create_review(db: Database, data: dict) -> Review:
    if "product_id" not in data:
        raise ValueError("review.product_id is required")
    if "stars" not in data:
        raise ValueError("review.stars is required")
    if "body" not in data:
        raise ValueError("review.body is required")
    new_id = db.insert("reviews", data)
    return Review(id=new_id, product_id=data["product_id"], stars=data["stars"], body=data["body"])


def list_reviews(db: Database, limit: int = 50) -> list[Review]:
    return [Review(**row) for row in db.fetch_many("reviews", limit=limit)]
