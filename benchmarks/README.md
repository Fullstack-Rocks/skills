# Benchmarks

Each skill answers one question, compared with Claude Code doing the same job without it:

| Skill | Question | Answer |
|---|---|---|
| [code-standards](#code-standards-how-long-does-a-review-take-and-what-does-it-cost) | How long does a review take, and what does it cost? | Scripts: **0.14 s, $0**. Claude + skill: 30–57 s, $0.28–0.43. Claude alone, reading: 31–99 s, $0.38–0.76 |
| [code-standards](#code-standards-what-does-a-review-find) | What does a review find? | 8 of 8 planted smells. Claude alone found 8 with a shell and 7 reading only |
| [under-engineering](#under-engineering-how-much-code-does-a-feature-take) | How much code does a feature take? | **130 → 60 lines (−54%)**, no new smells, at higher cost |
| [call-depth](#call-depth-does-the-trace-come-out-right) | Does the trace come out right? | Yes, the same as Claude alone given the rules; `scan.py` finds the hidden calls in 0.11 s |

## How the runs work

Every run starts from a fresh git copy of the [demo shop](../demo/), a Python API plus a React/TS client with 55 files. There are up to three conditions:

- **without** (Claude Code alone): the `Skill` tool is blocked (`--disallowedTools Skill`). In the code-standards speed suite it also gets no shell (only Read, Glob and Grep), so it reviews by reading.
- **with** (Claude Code + skill): the agent is told to load the skill, which is how a project's `CLAUDE.md` or `AGENTS.md` line works.
- **scripts** (code-standards only): `review.py` runs with no model at all. The median of 3 runs is reported.

Both agent conditions get the same fixed reply ("go with your recommendation") if they stop to ask a question. Results are measured with this repo's own scanners: `call-depth`'s `scan.py` and `code-standards`' `review.py`. For implementation tasks, each finding is compared with the same file before the change, so only what the run introduced counts.

Run on 2026-10-21 on an Apple M-series MacBook, with Claude Code 2.1.280 and `claude-opus-5-5`, **one run per cell**. That's enough to see the size of an effect, but these aren't statistics. Rerun them:

```bash
python3 benchmarks/run.py                                  # every suite and condition
python3 benchmarks/run.py --suite code-standards-speed     # just one suite
python3 benchmarks/run.py --rescore                        # recompute metrics from saved sandboxes; no agent runs
```

Each result is in `results/<suite>/<task>.<condition>.json`: metrics, cost, tokens, turns, the skills the agent actually loaded, and its final answers. Implementation tasks also save the `.diff`.

## code-standards: how long does a review take, and what does it cost?

Two reviews of the demo: the whole repository, and the 3-file loyalty change from the [planted-smell fixture](fixtures/code-standards/).

- **Claude Code alone** gets only Read, Glob and Grep: no shell, so no linter, analyzer or install can do the work for it, and `.code-standards/` is removed from its copy.
- **Claude Code + code-standards** and the **scripts** get the project's dev tools pre-installed in the sandbox (ruff, oxlint, lizard), so neither pays for setup.

| Review | Condition | Time to result | Cost | Tokens | Shell commands |
|---|---|---|---|---|---|
| Whole repo (55 files) | code-standards scripts | **0.14 s** | **$0** | 0 | — |
| | Claude Code + code-standards | 57 s | $0.43 | 338k | 5 |
| | Claude Code alone (reads the code) | 99 s | $0.76 | 447k | 0 (64 turns) |
| 3-file change | code-standards scripts | **0.14 s** | **$0** | 0 | — |
| | Claude Code + code-standards | 30 s | $0.28 | 258k | 4 |
| | Claude Code alone (reads the code) | 31 s | $0.38 | 181k | 0 |

**What each review found**
- **Whole repo:** the scripts report 17 issues. Claude + code-standards covered all 17 and added two from `standards.md`. Claude alone covered 15: it found the copied `summarize` but missed a 6-line table block shared by `ShipmentList.tsx` and `InvoiceList.tsx`. It added its own observations from reading, such as near-identical route handlers.
- **The change:** Claude + code-standards found 8 of 8 planted smells. Claude alone, reading, found 7 of 8: it noted that `points_for` "has many branches that need [tests]" but didn't flag it as too complex ([grading](results/code-standards/grading.md#speed-suite-read-only-baseline)).

**Reading it**
- **Scripts:** the deterministic layers return in well under a second, at no cost, with the same findings every run, so they can gate every commit.
- **Agents:** an agent review costs 30–99 s and $0.28–0.76 on this small repo. Reading a whole repo costs the most, and more code means more to read. With the skill, the agent starts from the scripts' results and spends its time on `standards.md` and the report.
- **Getting the baseline right took three tries.** With `.code-standards/` left in the repo, Claude alone found the config and rebuilt the tool pipeline by hand. With analyzers removed from `PATH`, it ran `npm ci` and `uv sync` to install the demo's dev dependencies, then ran them. Only taking away the shell made it review by reading.

## under-engineering: how much code does a feature take?

| Task | Lines added (Claude alone → + under-engineering) | Code files touched | New modules | New smells* | Cost |
|---|---|---|---|---|---|
| `coupon`: POST /orders/{id}/apply-coupon | 38 → **23** | 4 → **2** | 0 → 0 | 0 → 0 | $0.95 → $1.37 |
| `rate-limit`: 100 requests/min per customer | 59 → **24** | 3 → **2** | 1 → **0** | 0 → 0 | $0.58 → $1.25 |
| `csv-export`: download InvoiceList as CSV | 33 (+11 rewritten) → **13** | 1 → 1 | 0 → 0 | 0 → 0 | $0.43 → $0.76 |
| **Total** | **130 → 60 (−54%)** | **8 → 5** | **1 → 0** | **0 → 0** | **$1.96 → $3.38** |

\* Memory hops, complexity over 10, functions over 80 lines, and new lint, rule or duplication findings in the changed files. Neither condition introduced any. The difference is how much code it took.

The `with` runs loaded `under-engineering`, and it pulled in `um-maybe` for the hallway check by itself. The checkpoint and the hallway rounds account for the extra cost.

**What the numbers don't show**

- **rate-limit:** without the skill, the agent built a `RateLimiter` class with a thread lock, a deque-based sliding window and a decorator factory, and added a new `X-Customer-Id` request-header contract. With it, the agent wrote one 7-line function and a module-level counter, called from the three routes. ([diff without](results/under-engineering/rate-limit.without.diff) · [diff with](results/under-engineering/rate-limit.with.diff))
- **coupon:** the prompt said to recompute the total "with `order_total_cents`". Without the skill, the agent reimplemented the discount instead, adding two `Database` methods and a coupon service. With it, the agent reused `order_total_cents` as asked. The trade-off is that it wrote two raw SQL statements in the service instead of adding `Database` methods.
- **csv-export:** with the skill, the agent skipped CSV quoting, because every exported field is a number or a boolean.

**Found and fixed by the benchmark.** In `rate-limit/with`, the agent checked its own code with `uv run --group dev ruff …`. That synced the project's virtualenv and wrote a `uv.lock`. `under-engineering` now says to measure with `call-depth`'s `scan.py`, which installs its own tools and leaves the project alone.

## code-standards: what does a review find?

The [fixture](fixtures/code-standards/) adds a loyalty feature as uncommitted changes. Prompt: *"Review my uncommitted changes for code quality. List every problem you find, each with file:line."* Both runs could read the project's `.code-standards/standards.md`.

Graded by hand from the saved answers; see [`results/code-standards/grading.md`](results/code-standards/grading.md) for the evidence behind each cell:

| Planted smell | Kind | Claude alone | Claude + code-standards |
|---|---|---|---|
| `os.environ.get` in a route | `cs-env-outside-config` rule | ✅ | ✅ |
| Route calls `get_db().fetch_one` | `std-routes-delegate` | ✅ | ✅ |
| Service returns `None` for a missing record | `std-service-errors` | ✅ | ✅ |
| `points_for`, complexity 11 | lizard | ✅ | ✅ |
| Unused `import json` | ruff F401 | ✅ | ✅ |
| Component calls `fetch` directly | `std-components-use-api-modules` | ✅ | ✅ |
| Leftover `debugger;` | oxlint | ✅ | ✅ |
| `summarize` copied from `OrderList.tsx` | jscpd duplication | ✅ | ✅ |
| **Found** | | **8 / 8** | **8 / 8** |
| Cost / time | | $0.23 / 0.8 min | $0.34 / 1.1 min |

**Honest reading.** A strong model that reads the project's `standards.md` does as well on a one-off review. The baseline also found two real problems outside the planted set: the route is never registered, and a birthday-bonus logic bug.

What `code-standards` adds:
- every finding cites a rule
- the deterministic layers run in seconds, so the same check runs in CI or on every change
- `negate` turns "we never do X" into a tested rule, so the next review doesn't depend on the model noticing

The previous run (kept in `results/code-standards/v2/`) missed the copy, 7 of 8. Back then, duplication compared changed files only with each other (`[duplication] scope = "changed"`). The default is now `scope = "repo"`: jscpd compares the changed files with the whole repo. Above `repo_max_mb` (30 MB of reviewed source), it falls back to comparing changed files only with each other. On the demo jscpd takes 0.05s; on django (18 MB) a review takes 0.6s, on TypeScript (23 MB) 1.4s, and on vscode (209 MB, over the limit) 0.3–0.6s. The full timings are in [`skills/code-standards/README.md`](../skills/code-standards/README.md) under "Duplication across the repo".

An earlier run on a version of the fixture where `points_for` sat exactly at complexity 10 is kept in `results/code-standards/v1/`. There, both found 7 of 8: the baseline caught the copy, and the skill caught the complexity.

## call-depth: does the trace come out right?

The [fixture](fixtures/call-depth/) adds `POST /orders/{id}/refund`. It has a weighted depth of 7 and two memory hops: a dict registry `REFUND_HANDLERS[reason](...)`, and a `getattr(self, f"_write_{kind}")(...)` dispatch. The prompt spelled out the counting rules: project-owned calls count 1, calls go-to-definition can't follow count 2.

| | Claude alone | Claude + call-depth |
|---|---|---|
| Weighted depth 7 | ✅ | ✅ |
| Both memory hops, with file:line | ✅ | ✅ |
| Cost | $0.11 | $0.24 |

With the rules in the prompt, the plain agent traced it correctly too. The skill's value is that nobody has to write those rules into the prompt, and that `scan.py` finds both hops by parsing, in any language, before the agent reads the code: 0.11 s across the 58 files (median of 3). The recording in the main README shows it at work.
