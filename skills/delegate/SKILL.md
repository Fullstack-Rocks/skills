---
name: delegate
description: Delegates a task to another coding agent's CLI (Codex, Cursor, Antigravity, Gemini, the Gemini API, Claude) and keeps a back-and-forth with it while you keep working. Use when asked to hand work to, consult, or get a second opinion from another agent or model, or to run a side task in parallel.
---

# Delegate

`scripts/delegate.py` runs the other agent headless, one **turn** at a time, and resumes the same session on every turn, so the delegate keeps its context. It streams each event as a line branded with the provider's mark (⌬ OpenAI, ⬢ Cursor, ∧ Antigravity, ✦ Gemini, ✻ Anthropic, from `assets/brands.json`) and records both directions in `.delegate/<id>/events.jsonl`. The `.delegate/` folder is kept out of git through `.git/info/exclude`.

| Harness | For | Signs in with |
|---|---|---|
| `codex` | OpenAI Codex | `codex login` |
| `cursor` | Cursor's agent | `cursor-agent login` |
| `antigravity` (`agy`) | Google Antigravity | `agy`, once |
| `gemini` | Gemini CLI | `gemini`, then Login with Google |
| `gemini-api` | The Gemini API's CLI: a model with no tools, for second opinions and files it reads (`--attach`) | an AI Studio key the user stores with `gemini-api configure` |
| `claude` | Claude Code, when another agent leads | `claude auth login` |

Each turn is a full agent run in that product, billed to the user's account there. Install for every project with `npx skills add Fullstack-Rocks/skills --skill delegate -g`.

## Run a delegation

1. **Brief.** Write the brief as if to a colleague with no access to this conversation: the goal, the files and context it needs, the constraints, and what done looks like. The script appends the reply protocol: a self-contained final message ending in `STATUS: done | question … | blocked …`.
2. **Start, in the background.** Run `python3 scripts/delegate.py start <harness> --title "<2-5 word name of the task>" --file <brief.md>` (or the message inline) with `run_in_background`, then carry on with other work. The title is the chat's name in the panes; add `--project <name>` to group related delegations. You're notified when the turn ends, and the end of the task's output holds the reply block: id, turn, seconds, STATUS and the full reply.
   - Read-only is the default, through each harness's own read-only mode. Add `--write` when the delegate must edit files: it then works in its own git worktree on branch `delegate/<id>`, never in the checkout.
   - Where you can't run a command in the background, add `--detach`: it prints the id and returns, the turn runs on, and `list` shows when it is `idle` again, with the reply in `.delegate/<id>/final.md`.
   - `--model M`, `--effort E` and `--speed fast` pick the delegate's model, reasoning effort and speed; `python3 scripts/delegate.py models <harness>` lists them. `set <id> --model/--effort/--speed` changes them from the next turn.
   - `--attach PATH` (repeatable), or `@path` in the message, sends files, folders or images with it.
3. **Act on the STATUS.**
   - `question`: answer it from what you know, or ask the user, then `python3 scripts/delegate.py send <id> "<answer>"`, again in the background.
   - `blocked`: tell the user what blocks it.
   - `done`: check the work before you rely on it. Read the files it names. For a `--write` delegation, `python3 scripts/delegate.py diff <id>` prints its changes against the commit it started from, its own commits included. Apply them with `python3 scripts/delegate.py diff <id> | git apply`, then `python3 scripts/delegate.py close <id>`, which removes the worktree and branch and keeps the transcript.
4. **Follow-ups** go to the same id with `send`, so the delegate keeps its context. Start a new delegation only for a separate task.

Exit code `1` means the delegate failed. The last line names the cause, and for a sign-in problem, the command the user runs. Relay that command to the user; the sign-in is theirs. A `send` to a delegate that is mid-turn is queued and returns at once: the reply arrives in the output of the command that is running the turn.

`python3 scripts/delegate.py list` shows every delegation with its status, and `usage` the tokens, time and cost of each, totalled per harness. `stop <id>` ends a running turn.

## Where the user watches

- **Claude Code** loads this skill folder as a plugin with two panes: **Delegations**, the chats by project, and the chat itself. The chat opens when a turn starts, and `/delegations` reopens both. The chat draws each provider's logo beside its lines, shows your messages to the delegate and its replies, and has a box where the user can write to the delegate directly. When they do, a `[delegate]` note with their message and the reply lands in your conversation. Those are the user's own words to the delegate: take them into account as you continue.
- **Other hosts** use the same panel as an MCP App, an iframe served by `scripts/mcp_server.py`, with `delegate_start`, `delegate_send` and `delegate_status` tools for a host that has no shell. A `[delegate]` note from the panel means the same as above. To register it, or when the user asks about the panel outside Claude Code, read [`references/mcp-app.md`](references/mcp-app.md).
- **Any terminal**: `python3 scripts/delegate.py --color show <id> --follow` prints the transcript live.

Done when every delegation you started has reached `done`, `blocked`, or been stopped, its reply has been reported or acted on, and each `--write` delegation's changes are applied or discarded and closed.
