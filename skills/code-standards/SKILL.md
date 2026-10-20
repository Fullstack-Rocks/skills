---
name: code-standards
description: Reviews code against the project's own linters, its taught ast-grep rules and a learned standards.md, and learns new rules from rejected code. Use for code review requests, "is this clean?", when the developer rejects a pattern ("don't do this", "we never X", "flag this"), or to set up coding standards for a repo.
---

# Code standards

Three layers review code, and every finding cites the rule that raised it:

1. **Project linters** (ruff, eslint, oxlint, biome, …), run as the project configures them. Their configs belong to the project; leave them as they are.
2. **ast-grep rules** in `.code-standards/rules/`: structural patterns the developers taught, ids `cs-*`.
3. **Your judgment** against `.code-standards/standards.md`: prose entries, ids `std-*`, for what a pattern can't express.

lizard (complexity, function length, parameters) and jscpd (duplication) run beside them with the thresholds in `config.toml`.

The skill is **language-blind**. `config.toml` lists the file `extensions` to review, and each tool picks its own parser by extension. Any language that ast-grep, lizard or jscpd can parse works, and supporting a new one means adding its extension.

Everything in `.code-standards/` is **project-owned and meant to be committed**: rules, fixtures, standards and the negations log are the team's memory, reviewed in PRs like code. Say so when you create or change them.

Scripts are in this skill's `scripts/` folder. Run them with `python3`; they find the project root by walking up to `.code-standards/`. Rule syntax is in [`references/ast-grep-rules.md`](references/ast-grep-rules.md), and you need it only when writing or refining a rule.

## Pick the mode

- The project has no `.code-standards/config.toml`: run **init**, then continue with what was asked.
- The developer rejects code ("don't do this", "we never…", "flag this pattern", "stop writing X"), pointing at a snippet or location: run **negate**.
- Anything else (review this, is this clean, check my changes): run **review**.

## init

1. `python3 scripts/init.py`. It scaffolds `.code-standards/` and reports the detected linters and an extension `census`: each extension in the repo, its file count, and the ast-grep language that parses it. Code extensions that ast-grep parses go in `extensions`; the rest go in `not_reviewed`.
   - If a linter is configured but not installed, or ast-grep, lizard or jscpd is missing, list the install commands from the README and ask before installing anything. Without ast-grep, `extensions` starts empty; fill it from the census together with the developer.
   - The project may use a linter that `init` doesn't recognise (golangci-lint, rubocop, clippy, …). Add a `[[linters]]` block for it, with a command that prints SARIF (`format = "sarif"`) or `path:line:col: message` lines (`format = "unix"`), and the extensions it lints.
2. **Interview** in one message, with at most these five questions:
   - What does clean code mean in this project?
   - What are the layering or architecture boundaries (what may import or call what)?
   - What are the naming conventions?
   - How should errors be handled (raise, return, wrap, log)?
   - What do you keep correcting in reviews?

   In the same message, ask for 2–3 files they consider exemplary, and show both extension lists in one line so the developer can move any (for example, review `.vue` too).
3. Read the exemplary files. Draft `standards.md` entries in the template's format: `## std-<slug>: <title>`, then a `scope:` line, the rule, the rationale, and a good and a bad example. Draw the examples from their files where you can. Each entry traces to an answer or to a pattern visible in the exemplary files. An answer that is structural ("we never call requests directly") becomes a candidate rule. List those separately and offer to run negate on each one.
4. Show the draft. Write `standards.md` only after the developer approves it, with their edits applied, replacing the template's commented example.

Done when `config.toml` lists the right linters and the approved entries are written.

## review

1. Run `python3 scripts/review.py --out /tmp/cs-review.json`. Scope defaults to the files changed since the merge-base with `base`, plus staged and untracked files. Pass `--base REF`, `--all`, or `--files ...` when the developer names a scope. The command prints a summary line with timing, and lists tool errors and missing-tool warnings. A `NOTE` line means changed files have an extension in neither `extensions` nor `not_reviewed`. Report that those files weren't reviewed, and ask which list each extension belongs in. Read findings from the JSON (`findings[]`, sorted by severity then file) with `python3 -c` or `jq`, not by dumping the whole file.
2. **Standards pass.** `standards[]` lists each entry whose `scope` matches, and the files it matches. For each entry, read `.code-standards/standards.md` and the changed code in its files: `git diff <diff_from> -- <file>`, or the whole file when it's new. Check the entry against that code. Apply only the listed entries, and only to their listed files.
3. **Report**, grouped by severity, then by file:

   ```
   Code standards: <scope>, <n> files, <total>s (ruff 0.4s, ast-grep 0.1s, lizard 0.3s, jscpd 0.5s)
   Errors
     src/api/orders.py
       12  cs-env-outside-config  os.getenv("DB_URL"): read settings.DB_URL instead   [fix]
   Warnings
     src/services/billing.py
       40  lizard/complexity      apply_discounts: 14 (limit 10)
       88  std-thin-routers       handler queries the DB directly; move it to orders.place()
   Info …
   Tool problems: jscpd not installed (npm i -g jscpd@5.4.1)
   ```

   Every line cites a linter rule, a `cs-*` rule, `lizard/<check>`, `jscpd/duplicate` or a `std-*` entry. Report only what one of those backs. Mark findings that have a mechanical fix with `[fix]`.
4. **Offer fixes; apply them only when asked.** Use ast-grep's `fix` with `ast-grep scan -c .code-standards/sgconfig.yml --filter '^<id>$' -U <files>`, or the linter's own fix command. Edit by hand for the rest.

Suppressions belong to the developers: `ast-grep-ignore: <id>`, `noqa`, `eslint-disable`, `#lizard forgives`, `jscpd:ignore-start`. Suppressed code doesn't appear in the report. When a finding looks wrong, offer to refine the rule (negate) instead of adding a suppression.

Done when every finding and every in-scope standards entry has been reported or checked.

## negate

The developer rejected some code. Turn it into a rule or standard that catches it next time.

1. **Restate** the pattern in one sentence. Name the developer's **intent** (what they want to stop happening), not just the snippet they pointed at.
2. **Bypasses.** Until the proposal below is sent, make at most two tool calls:
   - read the flagged lines, if the developer didn't paste them
   - `grep -n -i '<construct>' .code-standards/negations.log.md`, to find bypasses already declined

   No exploring the repo, its config or its package files. The question is what the developer meant, not what this repo happens to contain. Think through the other ways code could produce the same rejected outcome while dodging a rule written only from this snippet:
   - other spellings of the same call: aliased or `from` imports, wrapper helpers, method vs. function forms, subscript vs. `.get`
   - sibling APIs with the same effect
   - the same thing in the project's other language
   - the same thing one scope over (a neighbouring folder or layer)

   Keep only bypasses that defeat the same intent. Leave out anything that is merely related, and anything the developer already declined for this id in `negations.log.md`. Then send **one** message with:
   - the restatement
   - the bypasses as a numbered list, each with a one-line example and whether a rule can catch it or it needs a standards entry
   - the question "Extend the negation to cover these? (all / some numbers / none)"
   - if the scope is unclear, the one scope question as well, for example "everywhere, or only in routers?"

   Wait for the answer. Accepted bypasses become part of this negation. Declined ones go in the log.
3. **Classify** the pattern and each accepted bypass.
   - **Structural**: recognizable from syntax in a single file (a call, import, construct or name shape). It becomes an ast-grep rule.
   - **Semantic**: needs intent, meaning, or knowledge across files (responsibility, naming meaning, layering by role). It becomes a `standards.md` entry.
   - **Both**: a rule catches the shape, and a standard covers the intent the pattern can't see.
4. **Look for an existing rule or standard first.** Search by the construct and by intent: `grep -rH '^id:\|^message:\|^note:' .code-standards/rules/`, `grep -n '^## std-' .code-standards/standards.md`, then `grep -rn '<api or construct>' .code-standards/`. If one bans the same thing (another spelling, a wider or narrower scope, a missed variant), **refine it** and keep its id:
   - add an `any` branch
   - adjust `files`/`ignores` or a `not`
   - add fixtures for the new case

   Only a different intent gets a new id.
5. **Rule** (details in the reference):
   1. Write `rules/<id>.yml`. Generalize the snippet with metavariables, and add an `any` branch for each accepted bypass a rule can catch. The `message` says what to do instead, the `note` holds the developer's reason, and severity follows their words: "never" means `error`, "avoid" means `warning`, "prefer" means `info`.
   2. Write `rule-tests/<id>-test.yml`. `invalid` holds the flagged code, at least one variant, and one case per accepted bypass. `valid` holds at least two near-misses: same names in a different shape, or the allowed context.
   3. Run `python3 scripts/check_rule.py <id> --expected <sites the developer pointed at>`:
      - **FIX (exit 1):** the fixtures fail or are thin. Fix the rule or the fixtures and rerun.
      - **ASK (exit 2):** the rule hits more of the repo than expected. Show the sample and ask: "real violations, or should I tighten the rule?" For real violations, rerun with `--expected` set to the confirmed count. Otherwise tighten the rule and rerun.
      - **SAVE (exit 0):** keep the rule.

   The rule is saved only on SAVE. If you can't reach it, delete the new files, or restore the previous version of a refined rule (`git checkout`, or your copy). Then tell the developer, and offer a standards entry instead.
6. **Standard:** add or refine a `## std-<slug>` entry, with a scope, the rule, the rationale, and good and bad examples built from the flagged code. Name every accepted bypass a rule can't catch, so reviews check for it.
7. **Log.** Append an entry to `.code-standards/negations.log.md` in its format (date, id, new/refined/merged, file:line, snippet, the developer's words quoted, bypasses accepted and declined, result). Then summarize in two lines: what was added or changed, and the repo hit count.

Done when every accepted bypass has a fixture or a standards line, the rule reached SAVE (or the standard is written), the log has the entry, and the next `review.py` run reports the flagged code.
