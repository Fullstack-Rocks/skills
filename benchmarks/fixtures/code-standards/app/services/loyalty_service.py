import json

from app.db import Database


def find_customer(db: Database, customer_id: int) -> dict | None:
    row = db.fetch_one("customers", customer_id)
    if row is None:
        return None
    return row


def points_for(customer: dict, rate: float) -> int:
    spent = customer.get("spent_cents", 0)
    points = int(spent * rate / 100)
    if customer.get("tier") == "gold":
        points += 50
    elif customer.get("tier") == "silver":
        points += 20
    elif customer.get("tier") == "bronze":
        points += 5
    if customer.get("birthday_month"):
        points += 10
    if customer.get("referrals", 0) > 3:
        points += 25
    elif customer.get("referrals", 0) > 0:
        points += 5
    if customer.get("newsletter"):
        points += 3
    if customer.get("blocked"):
        points = 0
    if points > 1000 and customer.get("tier") != "gold":
        points = 1000
    return points
