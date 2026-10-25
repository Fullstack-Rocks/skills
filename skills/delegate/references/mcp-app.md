# The Delegate MCP App

For hosts without Claude Code's plugin pane. `scripts/mcp_server.py` is a stdlib MCP server (stdio). Its tools wrap `delegate.py`, and every one carries the MCP App `ui://delegate/panel`: an iframe that streams the transcript with the provider logos, and has a box where the person writes to the delegate. When a reply to the person's message arrives, the panel hands it to the lead model with `ui/update-model-context`.

| Tool | Does |
|---|---|
| `delegate_start` | starts a delegation, returns its id at once (the turn runs detached) |
| `delegate_send` | the next message, returns at once; queued behind a running turn |
| `delegate_status` | lists delegations, or one delegation's state and latest reply |
| `delegate_stop` | ends a running turn |
| `delegate_model` | changes a delegation's model from its next turn |
| `delegate_poll` | for the panel alone (`visibility: ["app"]`); hidden from hosts without MCP Apps |

## Register it

Use the skill's installed path for `<skill>`, for example `~/.agents/skills/delegate`.

```bash
codex mcp add delegate -- python3 <skill>/scripts/mcp_server.py
agy mcp add delegate python3 <skill>/scripts/mcp_server.py
gemini mcp add delegate python3 <skill>/scripts/mcp_server.py
```

Cursor, Claude Desktop and VS Code read JSON: `~/.cursor/mcp.json`, `claude_desktop_config.json` and `.vscode/mcp.json` respectively.

```json
{ "mcpServers": { "delegate": { "command": "python3", "args": ["<skill>/scripts/mcp_server.py"] } } }
```

The project the server works in is the host's first MCP root, else `DELEGATE_ROOT`, else the directory the host starts it in. Set `DELEGATE_ROOT` when the host starts servers elsewhere and sends no roots.

## Where the panel renders

The iframe draws in hosts that implement MCP Apps (SEP-1865), such as Claude's desktop and web apps and VS Code's chat. Terminal hosts get the tools' text: the lead calls `delegate_status` for the reply, and the person watches with `python3 <skill>/scripts/delegate.py --color show <id> --follow`.

## Testing without a host

`python3 scripts/mcp_server.py --http 3011` serves the same tools as Streamable HTTP (JSON responses) on `127.0.0.1:3011/mcp`. Point the ext-apps reference host at it (`examples/basic-host` in github.com/modelcontextprotocol/ext-apps, run with `SERVERS='["http://localhost:3011/mcp"]'`) and call `delegate_status`.
