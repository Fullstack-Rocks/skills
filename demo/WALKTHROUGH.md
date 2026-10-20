# code-standards demo walkthrough

This is a throwaway shop project with 55 source files: a Python API (`app/`, about 35 files) and a React/TS client (`web/src/`, about 20 files).

It contains planted problems:
- env reads scattered across modules
- an over-complex pricing function
- a copy-pasted TS helper
- an unused import
- a `debugger` statement

`.code-standards/` holds the **end state** of this walkthrough. To replay it from the start, delete that folder first.

Everything below was run on 2026-10-20 (macOS, Apple Silicon). The interview answers and the developer's words are **simulated**.

## Setup

The tools are pinned and installed locally (both folders are gitignored):

```bash
npm install                        # @ast-grep/cli 0.50.0, jscpd 5.4.1, oxlint 1.89.0, typescript
uv venv && uv pip install ruff==0.17.1 lizard==1.24.1
```

## 1. init

```bash
python3 ../skills/code-standards/scripts/init.py
```

Output (trimmed):

```
"created": [".code-standards/config.toml", ".code-standards/negations.log.md",
            ".code-standards/rule-tests/.gitkeep", ".code-standards/rules/.gitkeep",
            ".code-standards/sgconfig.yml", ".code-standards/standards.md"],
"extensions": [".py", ".ts", ".tsx"],
"not_reviewed": [".json", ".md", ".yml", ".toml"],
"census": [{"extension": ".py", "files": 34, "ast_grep": "Python"}, {"extension": ".ts", "files": 11, "ast_grep": "Tsx"}, ...],
"linters": [{"name": "ruff",   "evidence": "pyproject.toml [tool.ruff]", "installed": true},
            {"name": "oxlint", "evidence": ".oxlintrc.json",             "installed": true}]
```

### Interview (simulated)

| Question | Answer |
|---|---|
| Clean code here | Small functions, typed signatures, one responsibility per module |
| Boundaries | `api` → `services` → `db`; web components → `web/src/api/*` → `apiClient` |
| Naming | services `verb_noun`, components `<Entity>List`, hooks `useX` |
| Errors | services raise `ValueError` / `LookupError`; routes don't catch |
| Keep correcting | env vars read all over the place; components calling `fetch` |

Exemplary files: `app/services/customer_service.py`, `web/src/api/order.ts`, `app/config.py`.

These answers produced three approved entries in `standards.md`:
- `std-routes-delegate` (`app/api/**`)
- `std-service-errors` (`app/services/**`)
- `std-components-use-api-modules` (`web/src/components/**`, `web/src/hooks/**`)

The answer "env vars read all over the place" is structural, so it became a candidate rule for negate, below.

## 2. review

```bash
python3 ../skills/code-standards/scripts/review.py --out /tmp/cs-review.json
```

```
55 files, 5 error, 8 warning, 3 standards in scope. ast-grep 0.136s, lizard 0.569s, jscpd 0.502s, ruff 0.146s, oxlint 0.229s, total 0.572s
```

- **0.57s for the tools and 0.66s for the whole command (`time`)**, against a budget of 3s for about 50 files.
- The tools run in parallel. lizard and jscpd are the slowest, each around 0.5s.
- The scope is the files changed since the merge-base with `origin/main`. The demo is untracked, so all 55 files count as changed.

Findings, ordered by severity then file:

```
error   ruff    F401                 app/services/invoice_service.py:29   `json` imported but unused
error   ruff    E501                 app/services/order_service.py:20     Line too long (116 > 110)
error   oxlint  eslint(no-unused-vars) web/src/components/InvoiceList.tsx:24  Function 'summarize' is declared but never used
error   oxlint  eslint(no-unused-vars) web/src/components/OrderList.tsx:24    (same)
error   oxlint  eslint(no-debugger)  web/src/hooks/useOrderTotals.ts:12   `debugger` statement is not allowed
warning lizard  complexity           app/services/order_service.py:27     order_total_cents: 14 cyclomatic complexity (limit 10)
warning jscpd   duplicate            web/src/components/InvoiceList.tsx:16 duplicates web/src/components/OrderList.tsx:16-35 (20 lines, 176 tokens)
warning lizard  complexity           web/src/components/InvoiceList.tsx:24 summarize: 12 cyclomatic complexity (limit 10)
warning oxlint  eslint(eqeqeq)       web/src/hooks/useOrderTotals.ts:9    Expected === and instead saw ==
...  (8 warnings total)
```

`standards[]` lists each in-scope entry with the files it matches (9 files each here). The agent then checks those entries against the changed code.

## 3. negate #1: new rule

The developer points at `app/api/order_routes.py:21`, `api_key = os.getenv("PAYMENTS_API_KEY")`, and says: *"We never call os.getenv outside app/config.py — use settings."*

1. **Restate:** reading environment variables with `os.getenv` outside `app/config.py`; read `settings` instead. The developer named the scope, so there's no clarifying question.
2. **Classify:** structural, so it becomes an ast-grep rule.
3. **Existing rule or standard?** `grep -rn 'getenv\|environ' .code-standards/` found nothing, so this is a new id.
4. **Rule and fixtures.** The rule was `pattern: os.getenv($$$ARGS)`, `ignores: [app/config.py]`, severity `error` because the developer said "never". The fixtures were the flagged line plus a variant inside a function as invalid cases, and three near-miss valid cases: `settings.payments_api_key`, `os.path.join(...)` and `config.getenv(...)`.

```bash
python3 ../skills/code-standards/scripts/check_rule.py cs-env-outside-config --expected 1
```

```
TEST PASS  cs-env-outside-config  invalid=2 valid=3
HITS 1  (expected 1, ask above 3)
  app/api/order_routes.py:21  api_key = os.getenv("PAYMENTS_API_KEY")
SAVE
```

`app/config.py` also calls `os.getenv`, but `ignores` excludes it. An entry went into `negations.log.md`.

**The next review catches it:**

```
55 files, 6 error, 8 warning, 3 standards in scope. ... total 0.675s
error cs-env-outside-config app/api/order_routes.py:21 Read configuration from app.config.settings, not os.getenv (...) |     api_key = os.getenv("PAYMENTS_API_KEY")
```

The guard paths were also checked:
- An `invalid` fixture the rule can't match gives `TEST FAIL ... [Missing]` and exit 1.
- `--expected 0 --slack 0` gives `ASK more hits than expected` and exit 2.

## 4. negate #2: refine the same rule

This run predates the **bypass** step. With that step, negate #1 would have proposed `os.environ[...]`, `os.environ.get(...)` and `from os import getenv` before writing the rule, so the developer wouldn't have needed this second request. It still shows how a refinement works, and refinements go through the same bypass step.

The developer points at `app/services/invoice_service.py:30`, `smtp_host = os.environ["SMTP_HOST"]`, and says: *"os.environ[...] is the same thing, and so is os.environ.get. Flag those too."*

1. **Existing rule:** `grep -rn 'getenv\|environ' .code-standards/rules` finds `cs-env-outside-config`. It has the same intent and misses these spellings, so the agent **refines** it and keeps the id.
2. **Rule:** `pattern` became `any: [os.getenv($$$ARGS), os.environ[$KEY], os.environ.get($$$ARGS)]`, and the message now names both spellings.
3. **Fixtures:** two new invalid cases (`os.environ["SMTP_HOST"]` and `os.environ.get("RETENTION_DAYS", "30")`) and two new near-misses (`request.environ["PATH_INFO"]` and a local dict named `environ`).

The first run failed:

```
TEST FAIL  cs-env-outside-config  invalid=4 valid=5
[Noisy] Expect cs-env-outside-config to report no issue, but some issues found in:
  os.environ["TZ"] == "UTC" or settings.tz
```

That "valid" fixture really is an env read, so the fixture was wrong, not the rule. After replacing it with the local-dict near-miss:

```
TEST PASS  cs-env-outside-config  invalid=4 valid=5
HITS 3  (expected 2, ask above 4)
  app/jobs/cleanup.py:8  days = int(os.environ.get("RETENTION_DAYS", "30"))
  app/services/invoice_service.py:30  smtp_host = os.environ["SMTP_HOST"]
  app/api/order_routes.py:21  api_key = os.getenv("PAYMENTS_API_KEY")
SAVE
```

There is still exactly one rule file and one test file:

```
.code-standards/rules/cs-env-outside-config.yml
.code-standards/rule-tests/cs-env-outside-config-test.yml
```

The log entry is marked `refined`. The next review:

```
55 files, 8 error, 8 warning, 3 standards in scope. ast-grep 0.047s, lizard 0.568s, jscpd 0.448s, ruff 0.178s, oxlint 0.233s, total 0.585s
error cs-env-outside-config app/api/order_routes.py:21 | api_key = os.getenv("PAYMENTS_API_KEY")
error cs-env-outside-config app/jobs/cleanup.py:8 | days = int(os.environ.get("RETENTION_DAYS", "30"))
error cs-env-outside-config app/services/invoice_service.py:30 | smtp_host = os.environ["SMTP_HOST"]
```

## 4b. Accepted bypass: bare `getenv`

The bypass step proposed `from os import getenv` followed by a bare `getenv(...)` call, and the developer accepted it. The rule gained a fourth `any` branch: `getenv($$$ARGS)`, but only `inside` a module whose `import_from_statement` imports `getenv` from `os`. A `getenv` imported from somewhere else stays a valid near-miss. For the demo, I added `from os import getenv` and a `default_carrier()` function to `app/services/shipment_service.py`.

```
TEST PASS  cs-env-outside-config  invalid=6 valid=6
HITS 4  (expected 4, ask above 6)
  app/jobs/cleanup.py:8  days = int(os.environ.get("RETENTION_DAYS", "30"))
  app/api/order_routes.py:21  api_key = os.getenv("PAYMENTS_API_KEY")
  app/services/shipment_service.py:30  return getenv("DEFAULT_CARRIER", "ups")
  app/services/invoice_service.py:30  smtp_host = os.environ["SMTP_HOST"]
SAVE
```

## 5. Missing tools

With no tools installed and no git repo (a copy of one file, run with a bare `PATH`), the run still succeeds. Each warning says how to fix it:

```
1 files, no findings, 1 standards in scope. ...
WARNING ast-grep: ast-grep not found. To install it, run python3 <skill>/scripts/install_tools.py
WARNING lizard: lizard not found. To install it, run python3 <skill>/scripts/install_tools.py
WARNING jscpd: jscpd not found. To install it, run python3 <skill>/scripts/install_tools.py
WARNING ruff: ruff is configured but not installed. Install the project's dev dependencies with its lockfile command (npm ci, uv sync --frozen, ...)
```

The agent doesn't stop at the warning. It runs `install_tools.py`, which installs the pinned versions at user level with whichever installer exists (npm -g, uv tool, pipx, cargo or pip --user), then reruns the review. In a fresh headless session with ast-grep and jscpd missing and the system Python at 3.9:
- the agent ran the scripts through `uv run --no-project --python 3.12`
- it installed ast-grep 0.50.0 and jscpd 5.4.1 with npm
- it told the developer in one line
- ruff was configured but the project has no lockfile, so it asked before installing ruff
- the project folder was left untouched
