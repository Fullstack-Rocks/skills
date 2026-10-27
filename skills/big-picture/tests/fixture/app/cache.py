"""Fixture cache: order totals kept in Redis, configured from the environment."""
import os

import redis

from app.reports import order_total

client = redis.from_url(os.getenv("REDIS_URL"))
TTL = int(os.environ["CACHE_TTL_SECONDS"])


def cached_total(order_id: int) -> int:
    hit = client.get(f"order-total:{order_id}")
    if hit is not None:
        return int(hit)
    total = order_total(order_id)
    client.setex(f"order-total:{order_id}", TTL, total)
    return total
