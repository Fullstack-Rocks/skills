from app.db import Database
from app.services.ledger import Ledger


def _refund_damaged(db: Database, order: dict) -> dict:
    return Ledger(db).record("refund", order["id"], order["total_cents"])


def _refund_late(db: Database, order: dict) -> dict:
    return Ledger(db).record("credit", order["id"], order["total_cents"] // 2)


REFUND_HANDLERS = {"damaged": _refund_damaged, "late": _refund_late}


def refund(db: Database, order_id: int, reason: str) -> dict:
    order = db.fetch_one("orders", order_id)
    if order is None:
        raise LookupError(f"order {order_id} not found")
    return REFUND_HANDLERS[reason](db, order)
