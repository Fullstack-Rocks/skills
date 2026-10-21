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

## Speed suite: Claude Code alone

From `../code-standards-speed/*.without.json`. Claude Code had a normal shell, the project's linters (ruff, oxlint, tsc) and no code-standards.

**The change, 8 planted smells: 7 of 8**

| Planted smell | Found | Evidence |
|---|---|---|
| env-read | ✅ | #2 "`loyalty_routes.py:10`: It reads `os.environ` directly" |
| route-db | ✅ | #3 "The route queries the database itself instead of going through a service" |
| service-none | ✅ | #7 `find_customer`'s "`if row is None: return None; return row`", and #4 says to raise `LookupError` |
| complexity | ❌ | #15 only "no tests for `points_for`, even though it has many branches"; not flagged as too complex |
| unused-import | ✅ | #6 "`import json` is never used" |
| direct-fetch | ✅ | #16 "It uses raw `fetch` … instead of `apiClient`" |
| debugger | ✅ | #20 "A `debugger;` statement is left in" |
| duplicate | ✅ | #21 "It's also the third copy of the same function" |

**The whole repo: 15 of the 17 issues code-standards' tools report.** It covered all 4 env reads, the unused import, the long line, both unused `summarize` copies, `debugger`, `==`, `order_total_cents` (through ruff C901), the `summarize` copy, and the table block shared by the `*List.tsx` components. It missed the complexity of the two `summarize` copies (12 each).
