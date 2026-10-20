---
name: call-depth
description: Measures call-chain depth, memory hops, cyclomatic complexity and code layout in any language. Use when tracing a call chain from its root (route, tool, job, CLI, handler), checking how nested or complex a function is, or checking file, function and folder sizes.
---

# Call depth

**Measure with programs, not by reading.** Reading costs context and guesses wrong; a parser is exact and cheap. For every measurement, use the first of these that works:

1. a tool the project already uses (its linter, its language server)
2. the bundled `scripts/scan.py`: real parsers (lizard and ast-grep) for any language, with no runtime from the target project
3. grep patterns from [`references/languages.md`](references/languages.md), only for a language `scan.py` reports as `NO_RULES`, with each result labelled as approximate

Read code only to confirm a finding or to follow a chain.

## Tools

The scripts need Python 3.10+ and use only the standard library. If `python3` is older, use `python3.13`/`python3.12` when one exists, otherwise `uv run --no-project --python 3.12 -- python scripts/<script>.py`. `scan.py` also needs **ast-grep** and **lizard**. **Install what's missing yourself**: when a script prints `MISSING_TOOL`, run `python3 scripts/install_tools.py ast-grep lizard`, rerun, and tell the developer in one line what was installed.
- It installs pinned versions at user level (npm -g, uv tool, pipx, cargo or pip --user, whichever exists) and leaves the project's manifests, lockfiles and environments alone.
- If it exits 1, give the developer the manual command it printed, and use the grep fallback meanwhile.

The project's own tools are found in its environment folders (`.venv/bin`, `node_modules/.bin`, `vendor/bin`, `target`). Use them as configured. When the project has no config for a check, run the tool isolated (ruff `--isolated`, ESLint `--no-config-lookup`) so unrelated rules don't mix in. Commands that create an environment or download into the project are out of bounds: `poetry run`, `npx` without `--no-install`, and plain `uv run`, which syncs and rewrites a Python project's `.venv` (`uv run --no-project` is safe).

## Scripts

Scripts emit TAB-separated findings as `KIND<TAB>location<TAB>detail` and end with `SCANNED<TAB>summary`. A clean scan emits `OK<TAB>summary` first. Run them on whole scopes.

| Script | Language | Reports |
|---|---|---|
| `scripts/layout.py <paths>` | any | `FILE_LENGTH` (> 1000), `FOLDER_SIZE` (> 6 code files, tests excluded), `FOLDER_NAME` (> 3 words) |
| `scripts/scan.py [--max-function-lines 80] [--max-complexity 10] <paths>` | any | `FUNCTION_LENGTH`, `COMPLEXITY` (lizard); `DYNAMIC_CALL`, `DYNAMIC_ATTR`, `LOOKUP_CALL` (ast-grep rule packs in `scripts/rules/`) |
| `scripts/python_scan.py [--check-types] <paths>` | Python | `IMPLICIT_PROTOCOL`; `--check-types` adds `UNTYPED_PARAM`, `ANY_PARAM` |
| `scripts/install_tools.py [TOOL ...]` | — | Installs ast-grep and lizard at pinned versions; exit 1 means a manual install is needed |

**Finding kinds:**

- `FUNCTION_LENGTH`: a function exceeds the configured line limit (default 80).
- `COMPLEXITY`: a function's cyclomatic complexity exceeds the threshold (default 10; pass the project's own).
- `DYNAMIC_CALL`: a call resolved at runtime: `getattr(...)(...)`, `eval`, reflection, dynamic import, `send`, `call_user_func`. Always a memory hop.
- `DYNAMIC_ATTR`: an attribute or constant looked up by a non-constant name. It is a hop only if the result gets called; check where it goes.
- `LOOKUP_CALL`: a call through a subscript or a fetched callable (`handlers[kind](...)`, `HANDLERS[kind].call`), meaning a registry. Usually a memory hop.
- `IMPLICIT_PROTOCOL`: a structural interface that no scanned class inherits. Calls through it are memory hops.
- `UNTYPED_PARAM`: with `--check-types`, a missing parameter annotation in a sync/async function, including nested functions, constructors, positional-only and keyword-only parameters, `*args` and `**kwargs`. The scanner skips the first positional parameter of non-static class methods.
- `ANY_PARAM`: with `--check-types`, a parameter annotation syntactically containing `Any` or qualified `typing.Any`, including inside generics. Aliases and string annotations are not resolved; use a type checker for those.

**Status and error kinds:**

- `OK`: no findings; a two-field status line, not a finding.
- `SCANNED`: final file count, with a count per extension.
- `NO_RULES`: an extension whose language has no rule pack, so its memory hops weren't scanned. Use the grep fallback for those files, or add a pack (`references/languages.md`). `COVERED` means every scanned language has one.
- `MISSING_TOOL`: ast-grep or lizard isn't installed; install it (see **Tools**) and rerun.
- `PARSE_ERROR`: `python_scan.py` couldn't parse a file (syntax or UTF-8 error); that file was not analyzed.
- `MISSING_PATH`: a requested path does not exist.

Treat `NO_RULES`, `MISSING_TOOL`, `PARSE_ERROR` and `MISSING_PATH` as incomplete coverage. The scripts don't return a nonzero exit code for findings or these statuses.

Output is TAB-separated, so filter it with `cut -f1 | sort | uniq -c` before reading lines.

Every limit is a flag, so pass the project's own limits when it has them.

Flags are candidates: confirm each one before reporting it.

## Chain depth

**Starting points:**

- **root:** where the work starts: route handler, tool, job, CLI command, event consumer or public library function
- **sub-root:** code the framework runs around the root: injected dependencies, middleware, decorators, interceptors, guards and context managers. Trace each one as its own chain; dependencies that depend on others add depth.
- **ctx:** startup, route loading and app mounting. Show these above the root when they matter, and don't count them.

**Counting:**

- Each project-owned call adds **1**. Project-owned includes first-party packages in the same workspace or monorepo. Framework, library and driver calls don't count.
- A **memory hop** adds **2**: a call that go-to-definition can't follow to the code that actually runs. The developer has to remember where it goes.
- **Interfaces:** if the implementation declares the interface (`implements`, explicit inheritance), count a normal hop to the implementation. If it matches only structurally (Python `Protocol`, Go interfaces, TS structural types), you find the implementation by search; that is a memory hop. Never count the stub itself as a frame.
- **Constructors** count when they run logic beyond assigning fields.
- **Recursion:** count one level, label it, and note the bound.
- **Conditional branches** count when the code can reach them; note the condition.
- **A function that runs twice** (for example, an app-wide guard that is also a route dependency) is traced once; note the duplicate.
- **Module-alias calls** (`_module.Name(...)`) are normal hops when the language server resolves them.

Weighted depth over **3** is a hit.

**Tracing:** run `scan.py` (and `python_scan.py` for Python) on the files along the path first, so the memory hops are known before you trace. Then follow the calls with the language server, and fall back to grep.

**Labels:**

| Label | Meaning | Weight |
|---|---|---|
| `[ctx]` | above the root, shown for context | 0 |
| `[dep]` / `[mw]` | sub-root run by the framework | starts at 0 |
| `[NOT LSP: <how>]` | dynamic call: `getattr`, reflection, string or enum registry, dynamic import | 2 |
| `[interface → Impl]` | structural interface; implementation found by search | 2 |
| `[callback]` | function passed as a value and called elsewhere | 2 |
| `[recursive]` | calls itself | 1, bound noted |

**Report:**

```
ctx   create_app()                       app/main.py:12                        [ctx]
root  create_order(...)                  routes/orders.py:26
  1   OrderService.place                 orders/service.py:27
  3   PaymentStep.run                    orders/steps.py:179                   [NOT LSP: getattr "run"]  <- over 3
  4   LedgerService.record               ledger/service.py:72                  <- over 3
depth 4 (calls 3, memory hops 1) · limit 3
```

The left column is the running weighted depth. When planning, trace to the function you plan to write or call. When reviewing, report the deepest path from each root, plus each branch that goes over the limit.

## Complexity

**Threshold:** take it from project config (ruff `max-complexity`, ESLint `complexity`, or the linter's equivalent). If none is set, use **10** and tell the developer you used the default.

**Measure** with the project's configured linter when it has one, otherwise `scan.py --max-complexity N`. For each function over the threshold, read only that function: report its score and maximum nesting (blocks inside blocks, calls inside calls). Flatten in this order, re-measuring after each change:

1. guard clauses and early returns
2. a named function per branch
3. separate functions instead of flag parameters

Done when every function and chain in scope has a measured result, or is listed as blocked with the reason.
