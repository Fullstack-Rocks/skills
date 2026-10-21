# code-standards review: graded by hand

Graded from the final answers in `loyalty-review.without.json` and `loyalty-review.with.json`. The `auto_found` keyword score in those files is approximate: it credits the duplicate to the `with` run because the word `summarize` appears in a complexity finding, but that answer explicitly says "No duplication was found."

| Planted smell | without | with | Evidence |
|---|---|---|---|
| env-read: `os.environ.get` in a route | ✅ | ✅ | both cite `cs-env-outside-config` at `loyalty_routes.py:10` |
| route-db: route calls `get_db().fetch_one` | ✅ | ✅ | both cite `std-routes-delegate` |
| service-none: `find_customer` returns None | ✅ | ✅ | both cite `std-service-errors` |
| complexity: `points_for` 11 | ✅ | ✅ | both report 11 against a limit of 10 |
| unused-import: `import json` | ✅ | ✅ (predicted) | `with`: ruff wasn't installed (no lockfile), so the answer names F401 as the likely finding |
| direct-fetch: component calls `fetch` | ✅ | ✅ | both cite `std-components-use-api-modules` |
| debugger | ✅ | ✅ | `with` cites oxlint `no-debugger` |
| duplicate: `summarize` copied from OrderList | ✅ | ❌ | `without`: "summarize is copy-pasted … already exists in OrderList.tsx:24 and InvoiceList.tsx:24"; `with`: "No duplication was found" (jscpd compares changed files only by default) |
| **Total** | **8 / 8** | **7 / 8** | |

The `without` answer also reported two real problems outside the planted set: the route module is never imported, so the route isn't registered, and the birthday bonus applies all year.

`v1/` holds an earlier run where `points_for` sat at exactly 10. By hand: without 7/8 (didn't flag complexity), with 7/8 (missed the duplicate).
