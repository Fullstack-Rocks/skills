from app.db import Database


class Ledger:
    def __init__(self, db: Database) -> None:
        self.db = db

    def record(self, kind: str, order_id: int, cents: int) -> dict:
        entry = {"kind": kind, "order_id": order_id, "cents": cents}
        return getattr(self, f"_write_{kind}")(entry)

    def _write_refund(self, entry: dict) -> dict:
        entry_id = self.db.insert("ledger", entry)
        return {"entry": entry_id, **entry}

    def _write_credit(self, entry: dict) -> dict:
        entry_id = self.db.insert("credits", entry)
        return {"entry": entry_id, **entry}
