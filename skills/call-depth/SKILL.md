---
name: call-depth
description: Measures call-chain depth, memory hops, cyclomatic complexity and code layout in any language. Use when tracing a call chain from its root (route, tool, job, CLI, handler), checking how nested or complex a function is, or checking file, function and folder sizes.
---

# Call depth

**Measure with programs, not by reading.** Reading costs context and guesses wrong; a parser is exact and cheap. For every measurement, use the first of these that works:

1. a tool the project already uses (its linter, its language server)
2. a parser for the language: a bundled adapter, or a short script you write against the language's own parser ([`references/languages.md`](references/languages.md))
3. grep patterns from `references/languages.md`, with each result labelled as approximate

Read code only to confirm a finding or to follow a chain.

## Tools

Look for tools without side effects: the project's environment folders (`.venv/bin`, `node_modules/.bin`, `vendor/bin`, `target`), `command -v`, and binaries bundled with the editor. Skip commands that can create an environment or download something (`poetry run`, `uv run`, `npx` without `--no-install`).

- **Found in the project's own environment:** use it; its version matches the project.
- **Anything else:** ask the developer once per session. List what you found (global, editor-bundled) and one-off download options, and say whether each changes the project's dependencies. Use the answer for the rest of the session.

When the project has no config for a check, run the tool isolated (ruff `--isolated`, ESLint `--no-config-lookup`) so unrelated rules don't mix in.

## Scripts

Scripts emit TAB-separated findings as `KIND<TAB>location<TAB>detail` and end with `SCANNED<TAB>summary`. A clean scan emits `OK<TAB>summary` first. Run them on whole scopes.

| Script | Language | Reports |
|---|---|---|
| `scripts/layout.py <paths>` | any | `FILE_LENGTH` (> 1000), `FOLDER_SIZE` (> 6 code files, tests excluded), `FOLDER_NAME` (> 3 words) |
| `scripts/adapters/python_scan.py [--check-types] <paths>` | Python | `FUNCTION_LENGTH` (> 80), `DYNAMIC_CALL`, `DYNAMIC_ATTR`, `LOOKUP_CALL`, `IMPLICIT_PROTOCOL`; `--check-types` adds `UNTYPED_PARAM`, `ANY_PARAM` |
| `scripts/adapters/ts_scan.mjs --project <root> <paths>` | JS / TS | `FUNCTION_LENGTH`, `DYNAMIC_CALL`, `LOOKUP_CALL`; exits 3 if the project has no `typescript` |

**Finding kinds:**

- `FUNCTION_LENGTH`: a function exceeds the configured line limit (default 80).
- `DYNAMIC_CALL`: a call resolved at runtime: `getattr(...)(...)`, `eval`, reflection, dynamic import. Always a memory hop.
- `DYNAMIC_ATTR`: an attribute looked up by a non-constant name. It is a hop only if the result gets called; check where it goes.
- `LOOKUP_CALL`: a call through a subscript (`handlers[kind](...)`), meaning a registry. Usually a memory hop.
- `IMPLICIT_PROTOCOL`: a structural interface that no scanned class inherits. Calls through it are memory hops.
- `UNTYPED_PARAM`: with `--check-types`, a missing parameter annotation in a sync/async function, including nested functions, constructors, positional-only and keyword-only parameters, `*args` and `**kwargs`. The scanner skips the first positional parameter of non-static class methods.
- `ANY_PARAM`: with `--check-types`, a parameter annotation syntactically containing `Any` or qualified `typing.Any`, including inside generics. Aliases and string annotations are not resolved; use a type checker for those.

**Status and error kinds:**

- `OK`: no findings; a two-field status line, not a finding.
- `SCANNED`: final file count; Python includes files with parse errors, but not missing paths.
- `PARSE_ERROR`: Python syntax or UTF-8 decoding failure; that file was not analyzed.
- `MISSING_PATH`: a requested path does not exist.

Treat `PARSE_ERROR` and `MISSING_PATH` as incomplete coverage. The Python scanner does not return a nonzero exit code for findings or these errors.

Output is TAB-separated, so filter it with `cut -f1 | sort | uniq -c` before reading lines.

Every limit is a flag, so pass the project's own limits when it has them. The Python scripts use only the standard library. For other languages, write an adapter with the same output kinds from `references/languages.md`.

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

**Tracing:** run the adapter on the files along the path first, so the memory hops are known before you trace. Then follow the calls with the language server, and fall back to grep.

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

**Measure** with the tool for the language in `references/languages.md`. For each function over the threshold, read only that function: report its score and maximum nesting (blocks inside blocks, calls inside calls). Flatten in this order, re-measuring after each change:

1. guard clauses and early returns
2. a named function per branch
3. separate functions instead of flag parameters

Done when every function and chain in scope has a measured result, or is listed as blocked with the reason.
