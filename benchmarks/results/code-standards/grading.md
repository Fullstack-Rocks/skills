# code-standards review: graded by hand

Graded from the final answers in `loyalty-review.without.json` and `loyalty-review.with.json`. This run uses the default `[duplication] scope = "repo"`: jscpd compares the changed files with the whole repo.

| Planted smell | without | with | Evidence |
|---|---|---|---|
| env-read: `os.environ.get` in a route | ✅ | ✅ | both cite `cs-env-outside-config` at `loyalty_routes.py:10` |
| route-db: route calls `get_db().fetch_one` | ✅ | ✅ | both cite `std-routes-delegate` at `loyalty_routes.py:11` |
| service-none: `find_customer` returns None | ✅ | ✅ | both cite `std-service-errors` |
| complexity: `points_for` 11 | ✅ | ✅ | both report 11 against a limit of 10 |
| unused-import: `import json` | ✅ | ✅ | both report ruff F401; `with` ran ruff through `uvx ruff@0.17.1` |
| direct-fetch: component calls `fetch` | ✅ | ✅ | both cite `std-components-use-api-modules` |
| debugger | ✅ | ✅ | `with` cites oxlint `no-debugger` after `npm ci`; `without` found it by reading, since oxlint wasn't installed |
| duplicate: `summarize` copied from OrderList | ✅ | ✅ | `with`: "`jscpd/duplicate` summarize copies web/src/components/InvoiceList.tsx:24-35"; that's the same function as in `OrderList.tsx`. `without`: "the third copy of the same function (also in `OrderList.tsx:24` and `InvoiceList.tsx:24`)" |
| **Total** | **8 / 8** | **8 / 8** | |

The `without` answer again reported real problems outside the planted set: the route module is never imported, and the birthday bonus applies all year.

The `with` run loaded the user-level installed copy of the skill, whose `review.py` predates the `repo_max_mb` check but scans the repo the same way when `scope = "repo"`. The demo's config sets that. The demo is 0.03 MB of source, far under the limit, so the result is the same with the current script. The `with` answer reports jscpd at 2.1s. That was a cold first run right after `npm ci`, with oxlint at 1.3s in the same run. The current script on the same sandbox takes 0.08s for jscpd and 0.09s in total.

Earlier runs:
- `v2/`: before this default, with `scope = "changed"`. Without 8/8, with 7/8: the review said "No duplication was found", because jscpd compared the changed files only with each other.
- `v1/`: `points_for` sat at exactly 10. Without 7/8 (didn't flag complexity), with 7/8 (missed the duplicate).

## Speed suite: read-only baseline

The same 8 planted smells, graded from `../code-standards-speed/change.without.json`. Claude Code had only Read, Glob and Grep: no shell, so it reviewed by reading.

| Planted smell | Found | Evidence |
|---|---|---|
| env-read | ✅ | "`loyalty_routes.py:10`: `LOYALTY_RATE` is read from `os.environ` on every request" |
| route-db | ✅ | the route "queries the database directly instead of calling `loyalty_service.find_customer`" |
| service-none | ✅ | `find_customer`'s "`if row is None: return None; return row`" |
| complexity | ❌ | only "`points_for` has many branches that need [tests]"; not flagged as too complex |
| unused-import | ✅ | "`loyalty_service.py:1`: `import json` is never used" |
| direct-fetch | ✅ | "`LoyaltyBadge.tsx:6`: It calls `fetch` directly" |
| debugger | ✅ | "`LoyaltyBadge.tsx:10`: A `debugger;` statement was left in" |
| duplicate | ✅ | "a `summarize` function that now exists in three places" |
| **Total** | **7 / 8** | |
