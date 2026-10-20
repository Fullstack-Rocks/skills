from app.db import Database
from app.models.coupon import Coupon


def get_coupon(db: Database, coupon_id: int) -> Coupon:
    row = db.fetch_one("coupons", coupon_id)
    if row is None:
        raise LookupError(f"coupon {coupon_id} not found")
    return Coupon(**row)


def create_coupon(db: Database, data: dict) -> Coupon:
    if "code" not in data:
        raise ValueError("coupon.code is required")
    if "percent_off" not in data:
        raise ValueError("coupon.percent_off is required")
    if "active" not in data:
        raise ValueError("coupon.active is required")
    new_id = db.insert("coupons", data)
    return Coupon(id=new_id, code=data["code"], percent_off=data["percent_off"], active=data["active"])


def list_coupons(db: Database, limit: int = 50) -> list[Coupon]:
    return [Coupon(**row) for row in db.fetch_many("coupons", limit=limit)]
