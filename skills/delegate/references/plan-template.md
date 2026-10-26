# Delegation plan template

Copy this to `delegation-plan.md` at the repository root (or `docs/delegation-plan.md`). `delegate.py plan check` reads it, and `delegate.py start --unit <name>` runs one unit from it. Lines before the first `##` describe the plan; each `## <unit>` heading opens a unit, and its `- key: value` lines describe it, one key per line. Paths are from the repository root and may be globs; separate several with commas and put a note on how to use each in parentheses.

```markdown
# Delegation plan: <what we are making>

project: <project tag, as for --project>
goal: <one sentence: what done means for the whole plan>

## research-ui
- role: UI researcher
- agent: antigravity
- model: gemini-4-argon
- effort: high
- why: research with sources and a browser to look at live sites
- mode: write
- uses: docs/PLAN.md (the brief for the whole site)
- makes: research/game-ui.md
- handed to: build-ui (the component list and accessibility rules)
- done when: every component the spec needs has a construction note and its accessibility rules

## concepts
- role: Concept artist, website UI
- agent: codex
- model: gpt-6.1-sol
- effort: medium
- why: Codex paints UI mock-ups and layouts in the style bible
- mode: write
- uses: docs/STYLE.md (the prompt prefix), art/style/anchor-*.png (style references)
- makes: art/concepts/*.png
- handed to: build-ui (the look the components must match)
- done when: one mock-up per key screen, each readable as a layout with blank text bars

## build-ui
- role: Builder A, design system
- agent: codex
- model: gpt-6.1-sol
- effort: high
- why: React, CSS and tests, and the hardest code of the build
- mode: write
- uses: docs/SPEC.md, research/game-ui.md, art/concepts/*.png (match these mock-ups)
- makes: src/components/ui/**
- handed to: build-pages (components every page is built from)
- done when: every page in the spec can be built from these components, and they match the mock-ups

## build-pages
- role: Builder C, content pages
- agent: cursor
- model: gpt-5.6-sol
- effort: high
- why: a second builder on a different model, working in parallel
- mode: write
- uses: src/components/ui/** (build only from these), docs/SPEC.md (routes and copy)
- makes: src/pages/**
- handed to: final
- done when: every route renders its copy with one h1, and the checks pass
```

## The keys

| Key | What it holds |
|---|---|
| `role` | The agent's name for the job, said back to it: "You are Builder A, design system". |
| `agent` | The harness: `codex`, `cursor`, `antigravity`, `gemini`, `gemini-api`, `claude`. |
| `model`, `effort` | What the unit runs on; `default` leaves it to the harness. Pick the cheapest that fits the unit's risk (see [agents.md](agents.md)). |
| `why` | Why this agent and model: the strength the unit uses. |
| `mode` | `write` for a worktree of its own; read-only otherwise. |
| `uses` | Inputs, with a note on how to use each. `start --unit` attaches them and names the unit that makes each one. |
| `makes` | Outputs. |
| `handed to` | The units that use the outputs (with a note on how), or `final` for a deliverable. |
| `done when` | Acceptance, written from the next unit's side: what it needs from this output. |

`plan check` reports an output that no unit uses, a unit handed work whose `uses` names none of it, an input that no unit makes and that does not exist, and a unit missing a key. It also lists each unit's delegations and their status.
