"""Fixture data access."""


def run(sql: str, *params: object) -> list[dict]:
    return []


def fetch_one(table: str, row_id: int) -> dict:
    return run(f"SELECT * FROM {table} WHERE id = %s", row_id)[0]
