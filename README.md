# Under-engineering skills

Agent skills that push coding agents toward **the least code that works**, written so a developer can read it with **nothing in memory**.

Coding agents tend to over-build. They add validation nobody asked for, retries, config, abstraction layers, registries and "future-proof" modules. Each piece looks reasonable alone, but together they leave code that is deep, hard to trace and expensive to maintain. These skills add a checkpoint before implementation and hard limits during it. Anything the agent can't justify goes back to the human as a decision.

| Skill | What it does | When it runs |
|---|---|---|
| [`under-engineering`](skills/under-engineering/SKILL.md) | Minimum-code checkpoint, plus limits while writing | Before writing or changing code for a feature, fix, module or refactor |
| [`um-maybe`](skills/um-maybe/SKILL.md) | "Hallway check": a weaker colleague agent with no context challenges the plan | On any plan before implementing, and from inside `under-engineering` |
| [`under-engineering-review`](skills/under-engineering-review/SKILL.md) | Reviews existing code against the same limits and reports findings with IDs and proposed fixes | When asked to review or audit a route, module, folder, package or diff |
| [`call-depth`](skills/call-depth/SKILL.md) | Measures call-chain depth, memory hops, cyclomatic complexity and layout, using parsers instead of reading | Whenever depth, complexity or size has to be measured |
| [`code-standards`](skills/code-standards/SKILL.md) | Reviews changes with the project's linters, taught ast-grep rules and a learned `standards.md`, and turns rejected code into tested rules | On review requests, "is this clean?", when the developer rejects a pattern, or to set up standards |

## How they fit together

```
under-engineering
├── Step 1  Size the task ── small? ───────────────┐
├── Step 2  Find the minimum                       │
│             └── um-maybe (hallway rounds)        │
├── Step 3  Checkpoint: Depth / Module / Governance│
│             └── call-depth (chain trace)         │
├── Step 4  Module plan (if a module is confirmed) │
├── Step 5  Limits while writing  <────────────────┘
│             └── call-depth (scripts, complexity)
└── Step 6  Report exceeded limits and violations left alone
```

The agent sends **one** checkpoint message: the `um-maybe` result, then every Depth, Module or Governance hit. It then waits for the developer's answers before writing code.

## The skills

### under-engineering

Two goals drive every step: the least code that works, and code a reader can follow without remembering where they came from.

1. **Size the task.** A small task, such as a rename, typo, new field or one-line fix, skips straight to the limits.
2. **Find the minimum.** The agent states the minimum requirement in one or two sentences, cuts every planned piece that doesn't map to it, and runs `um-maybe` on what remains.
3. **Checkpoint.** Three checks, each of which can "hit":
   - **Depth.** The planned step's weighted call depth is over 3, and calls that go-to-definition can't follow count double. The agent reports the chain and 2–3 alternatives, each with its trade-off.
   - **Module.** Other features could reuse this. The agent names them and asks whether to build it as a module.
   - **Governance.** The change enforces policy rather than product behaviour, such as compliance, retention, audit, IP or region restrictions, or policy rate limits. The agent offers an infrastructure option (firewall, WAF, gateway, IAM, lifecycle rules) next to the code option, and writes governance code only with explicit approval.
4. **Module plan.** For a confirmed module, the agent writes a plan in pseudocode in the implementation language. It covers purpose, usage examples, boilerplate, public surface, 2–3 implementation styles and layout. A weaker-model **readability scorer** then tries to use the module from the plan alone. The agent grades what the scorer actually understood, revises and re-scores until no key behaviour is misread.
5. **Limits while writing:**
   - functions fit on one screen (about 80 lines) and do one thing
   - cyclomatic complexity stays under the project's threshold (10 by default)
   - files stay under 900–1000 lines
   - folders hold at most 5–6 code files, with 1–3 word names
   - every call resolves with go-to-definition: no string-to-function lookups, `getattr`/`eval`, or handler dicts keyed by strings
6. **Report.** Every limit exceeded, with its reason, and every violation found in existing code but left for the developer to decide.

Code the agent wrote in the current session is fixed right away. Violations in existing code are reported first, and fixed only with the developer's approval.

### um-maybe

You pitch your plan in the hallway to a colleague who knows nothing about it. Their counter is usually "um, maybe you could just …".

1. **Pitch.** The agent writes the plan in under 15 plain-language lines, quotes what the human asked for and names every *extra*.
2. **Hallway rounds.** A subagent on a **weaker model**, given only [`agents/colleague.md`](skills/um-maybe/agents/colleague.md) and the pitch, asks why and offers simpler options. The agent concedes, defends with **proof** or admits it can't. It runs at most three rounds.
3. **Weigh.** Every piece lands in exactly one group: *Simplified*, *Kept with proof*, *Unproven* or *Belongs elsewhere* (infrastructure, legal, product or another team).
4. **Ask the human.** One message lists each unproven piece with its options and ends with "Does the simpler plan make sense to you?"

**Proof** means the human asked for it (quoted), or something they asked for can't work without it (a short chain ending at a quote). "Best practice", "future-proofing" and "it's cleaner" are not proof.

### under-engineering-review

Reviews **existing** code against the same limits without changing it. The agent proposes fixes and edits nothing unless the developer asks.

1. **Scope.** Turns the request into a file list (paths, a package, or `git diff --name-only <ref>`) and a list of roots.
2. **Trace.** Uses `call-depth` to trace each root. Every file the trace reaches joins the scope, and the files on traced paths are *on-path*.
3. **Measure.** Runs `layout.py`, the language adapter and the complexity tool over the file list. Raw output goes to a file in `/tmp`, so it never fills the agent's context.
4. **Spot governance.** Notes policy enforcement in code (allow-lists, retention, compliance gates, policy rate limits) as infrastructure candidates, without judging it.
5. **Report.** A table of checks against limits for on-path code, the 10 worst findings, governance items, and "fix first" (at most 3). Each finding has an ID such as `D1` or `C2`, so the developer can reply "do M1 and C2".

```
| Check           | Limit   | On-path | Worst              |
|-----------------|---------|---------|--------------------|
| Call depth      | 3       | 2/5     | 5 POST /orders     |
| Memory hops     | 0       | 3       | LOOKUP_CALL ...    |
| Complexity      | 10      | 1       | 14 place_order (nesting 4) |
...
```

### call-depth

**Measure with programs, not by reading.** For every measurement, `call-depth` prefers the project's own tools, then a parser, then grep, with grep results labelled approximate.

- **Chain depth.** Traces from a root (route, tool, job, CLI, handler), including framework-run sub-roots such as dependencies and middleware. Each project-owned call adds 1. A **memory hop**, a call go-to-definition can't follow (dynamic dispatch, registries, structural interfaces, callbacks), adds 2.
- **Complexity.** Uses the project's configured threshold, or 10 by default. It flattens with guard clauses, then a named function per branch, then separate functions instead of flag parameters.
- **Bundled scripts.** They print TAB-separated `KIND<TAB>location<TAB>detail` findings:

| Script | Language | Reports |
|---|---|---|
| `scripts/layout.py <paths>` | any | `FILE_LENGTH`, `FOLDER_SIZE`, `FOLDER_NAME` |
| `scripts/adapters/python_scan.py [--check-types] <paths>` | Python | `FUNCTION_LENGTH`, `DYNAMIC_CALL`, `DYNAMIC_ATTR`, `LOOKUP_CALL`, `IMPLICIT_PROTOCOL`, plus `UNTYPED_PARAM`/`ANY_PARAM` with `--check-types` |
| `scripts/adapters/ts_scan.mjs --project <root> <paths>` | JS / TS | `FUNCTION_LENGTH`, `DYNAMIC_CALL`, `LOOKUP_CALL` |

[`references/languages.md`](skills/call-depth/references/languages.md) lists parsers, complexity tools and grep fallbacks for Go, Rust, Java, Kotlin, C#, Ruby, PHP, Swift and more, so the agent can write an adapter for any language.

### code-standards

Style review that learns. Each review runs three layers on the changed files:
1. the project's own linters
2. project-owned ast-grep rules (`cs-*`)
3. agent judgment against a prose `standards.md` (`std-*`)

lizard (complexity, length, parameters) and jscpd (duplication) run alongside. The deterministic layers run in parallel and finish in well under a second on about 50 files. It works with any language the tools parse: config lists file extensions, not languages.

- **init** scaffolds `.code-standards/`, detects the project's linters, asks five questions at most, and drafts `standards.md` from 2–3 exemplary files.
- **review** reports findings by severity and file. Each finding cites a rule id.
- **negate** runs when you say "we never do X" about some code. It first proposes the bypasses a narrow rule would miss, so you don't have to ask twice. Then it refines an existing rule, or writes a new one, plus `valid`/`invalid` fixtures, and saves it only after `ast-grep test` passes and a repo-wide false-positive check. It also logs the change in `negations.log.md`.

Install commands for the pinned tools are in [`skills/code-standards/README.md`](skills/code-standards/README.md), and a full run on a demo project is in [`demo/WALKTHROUGH.md`](demo/WALKTHROUGH.md).

## Install

With the [`skills`](https://github.com/vercel-labs/skills) CLI:

```bash
npx skills add theclocker/under-engineering-skills
```

Or copy the folders from `skills/` into your agent's skills directory, for example `~/.claude/skills/` for Claude Code or `.claude/skills/` in a project. Install all four of the under-engineering skills together: `under-engineering` calls `um-maybe` and `call-depth`, and `under-engineering-review` calls `call-depth`. `code-standards` stands alone, but needs ast-grep, lizard and jscpd (see its README).

To make the checkpoint run every time, add a line to your `AGENTS.md` or `CLAUDE.md`:

```markdown
Before writing or changing code, load the `under-engineering` skill and follow it.
```

## Requirements

- **Subagents with model selection** for `um-maybe` and the module-plan scorer. Without subagents, the agent plays the colleague or scorer itself from the text alone and says so.
- **Python 3.10+** for `layout.py` and `python_scan.py`. They use only the standard library.
- **Node.js**, plus `typescript` installed in the target project, for `ts_scan.mjs`.
- A complexity tool for your language, such as ruff, ESLint or lizard (see `languages.md`). `call-depth` asks before using anything outside the project's own environment.

## Customizing

Every limit is a flag or a stated default, and the project's own config wins:

- the complexity threshold comes from ruff `max-complexity`, ESLint `complexity` and similar settings
- the scripts take `--max-function-lines`, `--max-file-lines`, `--max-folder-files` and `--max-folder-words`
- the depth limit (3) and the size limits live in plain Markdown in each `SKILL.md`; edit them to suit your team

## License

[MIT](LICENSE)
