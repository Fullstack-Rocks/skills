import sqlite3
from functools import cache

from app.config import settings


class Database:
    def __init__(self, url: str) -> None:
        self.conn = sqlite3.connect(url.removeprefix("sqlite:///"))
        self.conn.row_factory = sqlite3.Row

    def fetch_one(self, table: str, row_id: int) -> dict | None:
        row = self.conn.execute(f"SELECT * FROM {table} WHERE id = ?", (row_id,)).fetchone()
        return dict(row) if row else None

    def fetch_many(self, table: str, limit: int) -> list[dict]:
        return [dict(r) for r in self.conn.execute(f"SELECT * FROM {table} LIMIT ?", (limit,))]

    def insert(self, table: str, data: dict) -> int:
        columns = ", ".join(data)
        marks = ", ".join("?" for _ in data)
        cursor = self.conn.execute(f"INSERT INTO {table} ({columns}) VALUES ({marks})", tuple(data.values()))
        return cursor.lastrowid


@cache
def get_db() -> Database:
    return Database(settings.database_url)
