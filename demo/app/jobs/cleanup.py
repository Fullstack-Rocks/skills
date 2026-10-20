import os
from datetime import datetime, timedelta

from app.db import get_db


def delete_old_reviews() -> int:
    days = int(os.environ.get("RETENTION_DAYS", "30"))
    cutoff = datetime.now() - timedelta(days=days)
    cursor = get_db().conn.execute("DELETE FROM reviews WHERE created_at < ?", (cutoff.isoformat(),))
    return cursor.rowcount
