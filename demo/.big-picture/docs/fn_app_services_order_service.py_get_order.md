---
node: fn:app/services/order_service.py#get_order
source_hash: 41886cf6fb4e
---
Loads one order by id and returns it as an `Order`.

- Reads the `orders` table through `Database.fetch_one`.
- Raises `LookupError` when no row has that id, so callers map it to a 404.

```python
order = order_service.get_order(get_db(), order_id)
```

Used by both order endpoints; keep it free of HTTP concerns.
