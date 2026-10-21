<p align="center">
  <img src="assets/banner.jpg" alt="under-engineering skills: a tangled heap of gears, pipes and scaffolding on the left resolves into a single straight walkway across calm water on the right" width="100%">
</p>

<p align="center">
  <b>Agent skills that push coding agents toward the least code that works,<br>
  written so a developer can read it with nothing in memory.</b>
</p>

<p align="center">
  <a href="#install"><img alt="npx skills add Fullstack-Rocks/skills" src="https://img.shields.io/badge/npx%20skills%20add-Fullstack--Rocks%2Fskills-0b3d36?style=flat-square"></a>
  <a href="#the-skills"><img alt="5 skills" src="https://img.shields.io/badge/skills-5-0b3d36?style=flat-square"></a>
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-0b3d36?style=flat-square"></a>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#the-skills">Skills</a> ·
  <a href="#how-they-fit-together">How it works</a> ·
  <a href="#skill-details">Details</a> ·
  <a href="demo/WALKTHROUGH.md">Demo walkthrough</a>
</p>

---

Coding agents over-build. They add validation nobody asked for, retries, config, abstraction layers, registries and "future-proof" modules. Each piece looks reasonable alone, but together they leave code that is deep, hard to trace and expensive to maintain.

These skills add a **checkpoint before implementation** and **hard limits during it**, review what's already there against the same limits, and turn your "we never do that" into rules that run on every review. Anything the agent can't justify goes back to you as a decision.

<table>
<tr>
<th width="50%">❌ Without</th>
<th width="50%">✅ With</th>
</tr>
<tr>
<td valign="top">

- A one-line fix arrives with a config layer, a retry wrapper and a registry
- Call chains run five deep, through string-keyed handler dicts
- Reviews hand out generic advice you can't trace to a rule
- You correct the same pattern in every PR

</td>
<td valign="top">

- One checkpoint message before any code: what's cut, what's kept, and why
- Limits on depth, complexity and size, measured by parsers instead of by reading
- Every review finding cites a linter rule, a `cs-*` rule or a `std-*` standard
- "We never do X" becomes a tested ast-grep rule, and the agent asks about the bypasses up front

</td>
</tr>
</table>

## Install

With the [`skills`](https://github.com/vercel-labs/skills) CLI, for Claude Code, Codex, Cursor and other agents:

```bash
npx skills add Fullstack-Rocks/skills                          # all five skills
npx skills add Fullstack-Rocks/skills --skill code-standards   # just one
npx skills add Fullstack-Rocks/skills -g                       # for every project
```

Install the four under-engineering skills together: `under-engineering` calls `um-maybe` and `call-depth`, and `under-engineering-review` calls `call-depth`. `code-standards` stands alone.

<details>
<summary><b>Manual install</b></summary>

Copy the folders from [`skills/`](skills/) into your agent's skills directory, for example `~/.claude/skills/` for Claude Code, or `.claude/skills/` inside a project.

</details>

<details>
<summary><b>Tools for <code>code-standards</code></b></summary>

You don't need to do anything: the agent installs ast-grep, lizard and jscpd itself the first time it needs them, at pinned versions and user level, without touching your project's dependencies. To install them yourself:

```bash
npm i -g @ast-grep/cli@0.50.0 jscpd@5.4.1
uv tool install lizard==1.24.1          # or: pipx install lizard==1.24.1
```

Details and alternatives are in [`skills/code-standards/README.md`](skills/code-standards/README.md).

</details>

> [!TIP]
> To make the checkpoint run every time, add one line to your `AGENTS.md` or `CLAUDE.md`:
>
> ```markdown
> Before writing or changing code, load the `under-engineering` skill and follow it.
> ```

## The skills

| Skill | What it does | Try saying |
|---|---|---|
| [**under-engineering**](skills/under-engineering/SKILL.md) | Minimum-code checkpoint before implementation, plus limits while writing | *"Add rate limiting to the orders API"* |
| [**um-maybe**](skills/um-maybe/SKILL.md) | Hallway check: a weaker colleague agent with no context challenges your plan and offers simpler options | *"Hallway-check this plan before you start"* |
| [**under-engineering-review**](skills/under-engineering-review/SKILL.md) | Reviews existing code against the same limits, reports findings with IDs and proposes fixes | *"Review POST /orders for depth and complexity"* |
| [**call-depth**](skills/call-depth/SKILL.md) | Measures call-chain depth, memory hops, complexity and layout with parsers, not by reading | *"How deep is the call chain from the checkout route?"* |
| [**code-standards**](skills/code-standards/SKILL.md) | Reviews changes with your linters, taught ast-grep rules and a learned `standards.md`, and turns rejected code into tested rules | *"Is my change clean?"* · *"We never call os.getenv outside config.py"* |

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

The agent sends **one** checkpoint message: the `um-maybe` result, then every Depth, Module or Governance hit. It then waits for your answers before writing code.

`code-standards` runs a learning loop beside it:

```
"we never do X"  ──>  bypasses proposed  ──>  rule + fixtures  ──>  ast-grep test + repo-wide scan  ──>  caught on every later review
```

## Skill details

<details>
<summary><b>under-engineering</b>: the minimum-code checkpoint</summary>

<br>

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

</details>

<details>
<summary><b>um-maybe</b>: the hallway check</summary>

<br>

You pitch your plan in the hallway to a colleague who knows nothing about it. Their counter is usually "um, maybe you could just …".

1. **Pitch.** The agent writes the plan in under 15 plain-language lines, quotes what the human asked for and names every *extra*.
2. **Hallway rounds.** A subagent on a **weaker model**, given only [`agents/colleague.md`](skills/um-maybe/agents/colleague.md) and the pitch, asks why and offers simpler options. The agent concedes, defends with **proof** or admits it can't. It runs at most three rounds.
3. **Weigh.** Every piece lands in exactly one group: *Simplified*, *Kept with proof*, *Unproven* or *Belongs elsewhere* (infrastructure, legal, product or another team).
4. **Ask the human.** One message lists each unproven piece with its options and ends with "Does the simpler plan make sense to you?"

**Proof** means the human asked for it (quoted), or something they asked for can't work without it (a short chain ending at a quote). "Best practice", "future-proofing" and "it's cleaner" are not proof.

</details>

<details>
<summary><b>under-engineering-review</b>: audit existing code</summary>

<br>

Reviews **existing** code against the same limits without changing it. The agent proposes fixes and edits nothing unless the developer asks.

1. **Scope.** Turns the request into a file list (paths, a package, or `git diff --name-only <ref>`) and a list of roots.
2. **Trace.** Uses `call-depth` to trace each root. Every file the trace reaches joins the scope, and the files on traced paths are *on-path*.
3. **Measure.** Runs `layout.py` and `call-depth`'s `scan.py` (length, complexity, memory hops) over the file list. Raw output goes to a file in `/tmp`, so it never fills the agent's context.
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

</details>

<details>
<summary><b>call-depth</b>: measure with programs, not by reading</summary>

<br>

For every measurement, `call-depth` prefers the project's own tools, then a parser, then grep, with grep results labelled approximate.

- **Chain depth.** Traces from a root (route, tool, job, CLI, handler), including framework-run sub-roots such as dependencies and middleware. Each project-owned call adds 1. A **memory hop**, a call go-to-definition can't follow (dynamic dispatch, registries, structural interfaces, callbacks), adds 2.
- **Complexity.** Uses the project's configured threshold, or 10 by default. It flattens with guard clauses, then a named function per branch, then separate functions instead of flag parameters.
- **Bundled scripts.** They need no runtime from the project being measured. They print TAB-separated `KIND<TAB>location<TAB>detail` findings:

| Script | Language | Reports |
|---|---|---|
| `scripts/layout.py <paths>` | any | `FILE_LENGTH`, `FOLDER_SIZE`, `FOLDER_NAME` |
| `scripts/scan.py <paths>` | any | `FUNCTION_LENGTH`, `COMPLEXITY` (lizard); `DYNAMIC_CALL`, `DYNAMIC_ATTR`, `LOOKUP_CALL` (ast-grep rule packs for Python, JS/TS, Go, Ruby, Java, C#, PHP) |
| `scripts/python_scan.py [--check-types] <paths>` | Python | `IMPLICIT_PROTOCOL`, plus `UNTYPED_PARAM`/`ANY_PARAM` with `--check-types` |

A language without a rule pack is reported as `NO_RULES` rather than skipped silently. [`references/languages.md`](skills/call-depth/references/languages.md) shows how to add a pack (one YAML file plus test fixtures), and lists the grep fallback for those languages. The agent installs ast-grep and lizard itself, at pinned versions, when they're missing.

</details>

<details>
<summary><b>code-standards</b>: a code review that learns</summary>

<br>

Each review runs three layers on the changed files:

1. the project's own linters
2. project-owned ast-grep rules (`cs-*`)
3. agent judgment against a prose `standards.md` (`std-*`)

lizard (complexity, length, parameters) and jscpd (duplication) run alongside. The deterministic layers run in parallel and finish in well under a second on about 50 files. It works with any language the tools parse: config lists file extensions, not languages.

- **init** scaffolds `.code-standards/`, detects the project's linters, asks five questions at most, and drafts `standards.md` from 2–3 exemplary files.
- **review** reports findings by severity and file. Each finding cites a rule id.
- **negate** runs when you say "we never do X" about some code. It first proposes the bypasses a narrow rule would miss, so you don't have to ask twice. Then it refines an existing rule, or writes a new one, plus `valid`/`invalid` fixtures, and saves it only after `ast-grep test` passes and a repo-wide false-positive check. It also logs the change in `negations.log.md`.

The pinned tool versions and the config format are in [`skills/code-standards/README.md`](skills/code-standards/README.md). A full run on a demo project is in [`demo/WALKTHROUGH.md`](demo/WALKTHROUGH.md).

</details>

## Requirements

- **Subagents with model selection** for `um-maybe` and the module-plan scorer. Without subagents, the agent plays the colleague or scorer itself from the text alone and says so.
- **Python 3.10+** for the `call-depth` scripts, and **3.11+** for the `code-standards` scripts. Both use only the standard library.
- **ast-grep and lizard** (`call-depth`, `code-standards`) and **jscpd** (`code-standards`). The agent installs them itself, at pinned versions and user level, with whichever of npm, uv, pipx, cargo or pip the machine has. Only jscpd needs Node.js.
- Nothing from the project being measured: no Node.js, `typescript` or language toolchain is required. The project's own linters are used when it configures them.

## Customizing

Every limit is a flag or a stated default, and the project's own config wins:

- the complexity threshold comes from ruff `max-complexity`, ESLint `complexity` and similar settings
- the scripts take `--max-function-lines`, `--max-complexity`, `--max-file-lines`, `--max-folder-files` and `--max-folder-words`
- the depth limit (3) and the size limits live in plain Markdown in each `SKILL.md`; edit them to suit your team
- `code-standards` keeps its thresholds, extensions and linters in the project's `.code-standards/config.toml`

## License

[MIT](LICENSE)
