# Choosing the agent, model and effort for a unit

What two full demos (Maison Lumen, 31 runs; Kaelvorn, 43 runs) showed about each agent. Fill a unit's `agent`, `model`, `effort` and `why` from this; `delegate.py models <harness>` lists what each one offers today.

## Model and effort

Start each unit on the cheapest model and effort that fit its risk, and step up one model or one effort level on a re-do, never more:

| Unit | Model | Effort |
|---|---|---|
| A mechanical edit: a number, a rename, pasting given copy | the harness's light tier | low |
| Images, copy, a review of a few files | the main model | medium |
| Research with sources, a spec, a design system, a page builder | the main model | high |
| Architecture, a shell other units build on, a bug two runs could not fix | the strongest model | xhigh |

## The agents

| Agent | Strengths | Limits and gotchas |
|---|---|---|
| **Codex** (`codex`, GPT-6.1 Sol) | Code, tests, builds, Lighthouse, link crawls; research with live web search; **images** with its built-in tool: painterly concept art, UI and website mock-ups, layouts; turning prose into typed data with a validator | Images come at fixed sizes (1672×941, 1024×1536, 1536×1024, 1254×1254) with no size control, and read as renders, so steer them to the style bible; a write turn of a large build can pass 30 minutes, so give it `--timeout 5400` |
| **Antigravity** (`antigravity`, Gemini 4 Argon) | Research with sources; its **browser** (Playwright): pages at several widths, screenshots, keyboard and accessibility checks; driving `gemini-api image` batches through its shell | A turn ends at 30 minutes: one deliverable per run; its own image tool has a small quota, so it should run `gemini-api image` instead; a server started in the foreground hangs the turn |
| **Cursor** (`cursor`) | **Grok 4.7**: sharp, concrete reviews of copy, UX, marketing and consistency, with the fix written out; **GPT-5.6 Sol**: a second builder in parallel | Never its Claude models when the lead is Claude; it loads Claude Code's plugins, the delegate skill among them, so its role must be explicit (the delegate's rules say so) |
| **Gemini API** (`gemini-api`, Gemini 4 Argon) | Long-form writing (10,000 to 35,000 words a turn): lore, copy decks, page copy; second opinions on files sent with `--attach` | No tools and no files: its reply is the deliverable, saved by the lead; images need an agent with a shell to run `gemini-api image` |
| **Nano Banana 2.1** (through `gemini-api image`, run by Antigravity or Codex) | Images that must match references (`-i` anchors): icon sheets, re-makes, masks, frames, ornaments, logos; 2K output | Billed per image (about $0.05 at 2K): count the calls; flat backgrounds need asking for, and a sheet needs cutting by script |

## The skills each agent loads

Agents with a shell load skills of their own, so a brief can name one ("use your `webapp-testing` skill"):

| Agent | Skills from | Seen in use |
|---|---|---|
| Codex | `~/.agents/skills` | `under-engineering`, `call-depth`, `frontend-design`, `webapp-testing`, `diagnosing-bugs`, `research` |
| Antigravity | `~/.gemini/config/skills` (often a link to `~/.agents/skills`) and its built-in skills | `research` |
| Cursor | Claude Code's plugins in `~/.claude/plugins` | `delegate` |
| Gemini API | none | |
