# Code standards

Requirements this project's developers have set for code that no linter or ast-grep rule can check.
Reviews apply an entry only to files matching its `scope`. Committed with the project; edit freely.

Entry format: a `## std-<slug>: <title>` heading, then a `scope:` line (comma-separated globs, `*` crosses folders),
the rule, the rationale, and a good and a bad example.

<!-- Example (delete once real entries exist):

## std-thin-routers: Routers only translate HTTP
scope: src/api/**/*.py
Rule: A route handler parses the request, calls one service function and shapes the response. Queries, branching
business rules and retries live in the service layer.
Rationale: business rules in handlers get duplicated across endpoints and can't be reused from jobs.
Good:
```python
@router.post("/orders")
def create_order(body: OrderIn) -> OrderOut:
    return OrderOut.from_model(orders.place(body.to_command()))
```
Bad:
```python
@router.post("/orders")
def create_order(body: OrderIn, db: Session):
    if db.query(Customer).get(body.customer_id).blocked:
        raise HTTPException(403)
    ...
```
-->
