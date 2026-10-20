# Negations log

Append-only record of code the developers rejected and what it became. Newest last.

<!-- Entry format:

## YYYY-MM-DD · <rule-or-standard-id> · new | refined | merged
- where: path/to/file.py:42
- snippet: `the flagged code`
- developer: "their words, quoted"
- result: one line on what changed (patterns, scope, fixtures, repo hits)
-->

## 2026-10-20 · cs-env-outside-config · new
- where: app/api/order_routes.py:21
- snippet: `api_key = os.getenv("PAYMENTS_API_KEY")`
- developer: "We never call os.getenv outside app/config.py — use settings."
- result: Python rule on `os.getenv($$$ARGS)`, ignores app/config.py, severity error; 2 invalid / 3 valid fixtures; 1 repo hit

## 2026-10-20 · cs-env-outside-config · refined
- where: app/services/invoice_service.py:30
- snippet: `smtp_host = os.environ["SMTP_HOST"]`
- developer: "os.environ[...] is the same thing, and so is os.environ.get. Flag those too."
- result: added `any` branches `os.environ[$KEY]` and `os.environ.get($$$ARGS)`; fixtures 4 invalid / 5 valid (near-misses: `request.environ[...]`, local `environ` dict); 3 repo hits (new: app/jobs/cleanup.py:8)

## 2026-10-20 · cs-env-outside-config · refined
- where: (bypass proposal accepted by the developer, no new flagged site)
- snippet: `from os import getenv` … `getenv("DEFAULT_CARRIER", "ups")`
- developer: "yes, extend the demo rule to catch getenv"
- bypasses: accepted `from os import getenv` + bare `getenv(...)`; not yet proposed: `from os import environ`, `import os as <alias>`
- result: added `all: [getenv($$$ARGS), inside module that imports getenv from os]` branch; fixtures 6 invalid / 6 valid (near-miss: `getenv` imported from app.flags); 4 repo hits (new: app/services/shipment_service.py:30)
