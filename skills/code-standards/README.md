# code-standards

Reviews code in three layers:
1. the project's own linters
2. ast-grep rules the developers taught it
3. agent judgment against a learned `standards.md`

lizard and jscpd run alongside for complexity, function length, parameter count and duplication. jscpd compares the changed files with the whole repo, so a change that copies existing code is flagged.

When you reject a pattern, the skill turns it into a tested rule or a standards entry. Then every later review catches it.

Everything runs locally, and a review makes no network calls. On a 55-file Python + TS demo, all tools finish in about 0.6s wall time, running in parallel.

**Any language.** The scripts carry no language tables. `config.toml` lists the file `extensions` to review, and each tool picks its own parser by extension, skipping files it can't read:
- ast-grep: about 25 languages
- lizard: about 25 languages
- jscpd: about 150 formats

At init, the skill counts the repo's extensions and asks ast-grep which language parses each one, so a Go, Ruby, Rust or Java repo works the same as a Python one. When a change adds a file type that's in neither `extensions` nor `not_reviewed`, the review says so instead of skipping it silently.

**Duplication across the repo.** By default (`[duplication] scope = "repo"`), jscpd scans every file with a reviewed extension and keeps only the clones that touch a reviewed file, so a new file that copies old code is flagged. jscpd reads about 20–50 MB of source a second. If the reviewed source is over `repo_max_mb` (30 by default), the review compares the changed files only with each other and prints a warning saying so. Measured on an M4 MacBook with jscpd 5.4.1, wall time for the whole review (`--files`, 3 runs, median):

| Repo | Reviewed source | 10 files: `changed` → default | 100 files: `changed` → default |
|---|---|---|---|
| demo + benchmark fixture | 58 files, 0.03 MB | 0.04s → 0.05s | |
| django | 2,621 `.py`, 18 MB | 0.05s → 0.61s | 0.26s → 0.67s |
| TypeScript | 13,153 `.ts`, 23 MB | 0.06s → 1.48s | 0.25s → 1.35s |
| vscode | 14,004 `.ts`, 209 MB: over the limit, falls back | 0.07s → 0.33s | 0.36s → 0.60s |

A full repo scan of vscode took 7–8.5s, which is why the limit exists. Checking the size costs 0.1–0.3s on these repos, and it runs in parallel with the other tools. Set `scope = "changed"` to skip the repo scan, or raise `repo_max_mb` if a few more seconds are fine. jscpd's own `--changed` flag isn't used, because it writes `.jscpd-baseline.json` into the repo.

## Install the tools

**The agent installs them itself.** When a tool is missing, it runs `scripts/install_tools.py`. The script installs pinned versions at user level with whichever installer exists (npm -g, uv tool, pipx, cargo, or pip --user) and leaves the project's manifests, lockfiles and environments alone. A linter the project configures but hasn't installed comes from the project's own lockfile command (`npm ci`, `uv sync --frozen`, …).

To install them by hand instead:

| Tool | Pinned version | Install |
|---|---|---|
| ast-grep | 0.50.0 | `npm i -g @ast-grep/cli@0.50.0`, or `uv tool install ast-grep-cli==0.50.0`, `pipx install ast-grep-cli==0.50.0`, `cargo install ast-grep --locked --version 0.50.0` |
| lizard | 1.24.1 | `uv tool install lizard==1.24.1`, or `pipx install lizard==1.24.1`, `pip install --user lizard==1.24.1` |
| jscpd | 5.4.1 | `npm i -g jscpd@5.4.1` (needs Node.js) |

Python 3.11+ runs the scripts, which use only the standard library. The scripts look for tools in the project's `.venv/bin` and `node_modules/.bin` first, then `PATH`, then `~/.local/bin` and `~/.cargo/bin`. A review never downloads anything.

If a tool is still missing, the review continues without it and reports a warning saying how to install it.

## What it adds to a repo

```
.code-standards/            # project-owned: commit it
  config.toml               # extensions to review, base ref, thresholds, linters and their commands
  standards.md              # prose standards: std-<slug>, scope globs, rule, rationale, good/bad example
  sgconfig.yml              # ast-grep config
  rules/cs-*.yml            # one ast-grep rule per rejected pattern
  rule-tests/cs-*-test.yml  # invalid (must match) / valid (near-misses) fixtures
  negations.log.md          # append-only: what was rejected, by whom, what it became
```

`config.toml` replaces the `config.yml` from the original spec. Python's standard library parses TOML but not YAML, and TOML keeps comments.

## Modes

### init: first use in a repo

> Set up code standards for this repo.

1. Scaffolds `.code-standards/`, detects linters, and counts the repo's extensions. It proposes which to review, and you confirm them.
2. Asks up to five questions: what clean code means here, architecture boundaries, naming, error handling, and what you keep correcting in reviews.
3. Asks for 2–3 exemplary files.
4. Drafts `standards.md` entries and writes them only after you approve them.

### review: the default mode

> Review my changes.
> Is `app/services/billing.py` clean?
> Review everything against our standards (`--all`).

Runs `scripts/review.py`, which reviews the files changed since the merge-base with `base`, plus staged and untracked files. The agent then checks only the `standards.md` entries whose `scope` matches those files. Findings are reported by severity, then by file, and each one cites a rule id: a linter code, `cs-*`, `lizard/*`, `jscpd/duplicate` or `std-*`. Fixes are offered and applied only when you ask.

### negate: teach it

> Don't do this. We never read env vars outside `app/config.py`. *(pointing at `os.getenv(...)`)*
> Flag this pattern in routers.
> `os.environ[...]` is the same thing, and so is `.get`. Catch those too.

1. The agent restates the pattern. Without using any tools, it lists other ways code could get the same rejected outcome past a narrow rule: aliases, sibling APIs, the other language, the next folder over. It asks in one message whether to extend the negation to cover them, adding a scope question only if one is needed. Accepted bypasses go into the rule. Declined ones are logged and not proposed again.
2. It classifies the pattern and each accepted bypass as structural (an ast-grep rule), semantic (a standards entry) or both.
3. It refines an existing rule if one covers the same intent.
4. It writes the rule and its fixtures, then runs `scripts/check_rule.py`, which runs `ast-grep test` and counts hits across the repo. If the rule flags more than expected, it shows you a sample before saving.
5. It appends to `negations.log.md`.

To suppress a single finding, add `# ast-grep-ignore: <rule-id>` (or `// …`) on the line above. Only developers add suppressions.

## Scripts

| Script | Does |
|---|---|
| `scripts/init.py` | Scaffolds `.code-standards/` from `templates/` and writes `config.toml` with the detected linters |
| `scripts/detect_linters.py [--sgconfig FILE]` | Prints the extension census (count and ast-grep language per extension) and the detected linters as JSON |
| `scripts/review.py [--base REF \| --all \| --files …] [--out FILE]` | Runs linters, ast-grep, lizard and jscpd in parallel and writes one JSON report: `findings[]` (`source`, `rule_id`, `severity`, `file`, `line`, `end_line`, `message`, `snippet`, optional `fix`), `standards[]` in scope, `timing`, `files_scanned`, per-tool `errors` and missing-tool `warnings` |
| `scripts/install_tools.py [--dry-run]` | Installs any missing tool at its pinned version, at user level. Exit codes: 0 everything available, 1 something needs a manual install |
| `scripts/check_rule.py <id> [--expected N]` | `ast-grep test` for one rule plus a repo-wide hit count. Exit codes: 0 save, 1 fix the rule or fixtures, 2 ask the developer |

See [`../../demo/WALKTHROUGH.md`](../../demo/WALKTHROUGH.md) for a full run.
