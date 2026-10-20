# Code standards

Requirements this project's developers have set for code that no linter or ast-grep rule can check.
Reviews apply an entry only to files matching its `scope`. Committed with the project; edit freely.

Entry format: a `## std-<slug>: <title>` heading, then a `scope:` line (comma-separated globs, `*` crosses folders),
the rule, the rationale, and a good and a bad example.


## std-routes-delegate: Route handlers only translate HTTP
scope: app/api/**
Rule: A handler reads params/body from the `Request`, makes one service call, and returns a `Response`. No SQL, no
business branching, no direct `Database` methods; pass `get_db()` through to the service.
Rationale: business rules in handlers get duplicated across endpoints and can't be reused from jobs.
Good:
```python
@route("GET", "/customers/{id}")
def show_customer(request: Request) -> Response:
    customer = customer_service.get_customer(get_db(), int(request.params["id"]))
    return Response.json(customer.__dict__)
```
Bad:
```python
@route("GET", "/customers/{id}")
def show_customer(request: Request) -> Response:
    row = get_db().fetch_one("customers", int(request.params["id"]))
    if row and row["tier"] == "gold": ...
```

## std-service-errors: Services raise, they don't return sentinels
scope: app/services/**
Rule: Invalid input raises `ValueError`, a missing record raises `LookupError`, with a message naming the entity and
field. Never return `None`/`False` to signal failure; never catch broad exceptions inside a service.
Rationale: routes map these two exceptions to 400/404 in one place; sentinels leak `if result is None` checks everywhere.
Good:
```python
if row is None:
    raise LookupError(f"order {order_id} not found")
```
Bad:
```python
if row is None:
    return None
```

## std-components-use-api-modules: Components fetch through api/ modules
scope: web/src/components/**, web/src/hooks/**
Rule: Components and hooks call the typed functions in `web/src/api/<entity>.ts` (`getOrder`, `createOrder`). They do
not import `apiClient` or call `fetch` themselves.
Rationale: the api modules own URLs and response types; one place to change when an endpoint moves.
Good:
```tsx
import { getOrder } from "../api/order";
```
Bad:
```tsx
const res = await fetch(`/api/orders/${id}`);
```
