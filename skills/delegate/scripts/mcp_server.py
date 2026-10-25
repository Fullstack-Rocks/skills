#!/usr/bin/env python3
"""MCP server for the delegate skill, for hosts without Claude Code plugins.

    python3 mcp_server.py               stdio, the way hosts launch servers
    python3 mcp_server.py --http 3001   Streamable HTTP on 127.0.0.1:3001/mcp (JSON responses), for testing

Tools wrap scripts/delegate.py: delegate_start and delegate_send return at once (the turn runs
detached), delegate_status reads the reply, delegate_stop ends a turn. Each carries the MCP App
`ui://delegate/panel`, an iframe that streams the transcript, draws the provider logos and lets the
person write to the delegate. Hosts that don't render MCP Apps get the same tools as text.

The project is the client's first root (roots/list), else $DELEGATE_ROOT, else the working directory.
Python 3.9+, stdlib only.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

HERE = Path(__file__).resolve().parent
DELEGATE = HERE / "delegate.py"
PANEL_URI = "ui://delegate/panel"
APP_MIME = "text/html;profile=mcp-app"
PROTOCOLS = ("2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05")
HARNESSES = ["codex", "cursor", "antigravity", "gemini", "gemini-api", "claude"]
UI = {"ui": {"resourceUri": PANEL_URI}}

TOOLS = [
    {
        "name": "delegate_start",
        "description": "Hand a task to another coding agent (Codex, Cursor, Antigravity, Gemini, the Gemini API or Claude). Returns its "
                       "id at once; the agent works in the background, streaming into the Delegate panel. Write the "
                       "message as a brief for a colleague with no access to this conversation. Read-only unless "
                       "write is true, which gives it a git worktree of its own. Check delegate_status for the reply.",
        "inputSchema": {"type": "object", "required": ["harness", "message"], "properties": {
            "harness": {"type": "string", "enum": HARNESSES},
            "message": {"type": "string", "description": "the brief: goal, files, constraints, what done looks like"},
            "write": {"type": "boolean", "description": "let it edit files, in its own worktree"},
            "model": {"type": "string"},
            "title": {"type": "string", "description": "a short label for the panel"},
        }},
        "_meta": UI,
    },
    {
        "name": "delegate_send",
        "description": "Send the next message to a delegation (an answer to its question, or a follow-up). Returns at "
                       "once; the reply arrives through delegate_status. Sent mid-turn, it waits its turn.",
        "inputSchema": {"type": "object", "required": ["id", "message"], "properties": {
            "id": {"type": "string"}, "message": {"type": "string"},
            "as_user": {"type": "boolean", "description": "the message is the person's, not the lead agent's"},
        }},
        "_meta": UI,
    },
    {
        "name": "delegate_status",
        "description": "List delegations, or with an id, its state and its latest reply, which ends in "
                       "STATUS: done | question | blocked. A running delegation has no new reply yet.",
        "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}}},
        "_meta": UI,
    },
    {
        "name": "delegate_stop",
        "description": "Stop a delegation's running turn.",
        "inputSchema": {"type": "object", "required": ["id"], "properties": {"id": {"type": "string"}}},
        "_meta": UI,
    },
    {
        "name": "delegate_model",
        "description": "Change the model a delegation uses from its next turn; 'default' returns to the harness's own.",
        "inputSchema": {"type": "object", "required": ["id", "model"], "properties": {
            "id": {"type": "string"}, "model": {"type": "string"}}},
        "_meta": UI,
    },
    {
        "name": "delegate_poll",
        "description": "Panel only: delegations and the selected transcript's events after line `after`.",
        "inputSchema": {"type": "object", "properties": {
            "id": {"type": "string"}, "after": {"type": "integer", "minimum": 0}}},
        "_meta": {"ui": {"resourceUri": PANEL_URI, "visibility": ["app"]}},
    },
]


class Server:
    def __init__(self):
        self.root = Path(os.environ.get("DELEGATE_ROOT") or os.getcwd())
        self.lead = "lead"
        self.client_caps = {}
        self.models = {}  # harness -> its model list, asked of delegate.py once

    # ------------------------------------------------------------ project state

    def base(self):
        return self.root / ".delegate"

    def states(self):
        rows = [json.loads(p.read_text()) for p in self.base().glob("*/state.json")]
        return sorted(rows, key=lambda s: s.get("created", 0))

    def summary(self, s):
        return {"id": s["id"], "harness": s["harness"], "status": s["status"], "agentStatus": s.get("agent_status", ""),
                "mode": s["mode"], "turns": s.get("turns", 0), "title": s.get("title", ""), "model": s.get("model") or "",
                "created": s.get("created", 0)}

    def delegate(self, *args, message=None):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(message or "")
        try:
            argv = [sys.executable, str(DELEGATE), "--no-color", *args] + (["--file", f.name] if message else [])
            return subprocess.run(argv, cwd=self.root, capture_output=True, text=True, timeout=120)
        finally:
            os.unlink(f.name)

    # ------------------------------------------------------------ tools

    def call(self, name, a):
        if name == "delegate_start":
            args = ["start", a["harness"], "--detach", "--lead", self.lead]
            args += ["--write"] if a.get("write") else []
            args += (["--model", a["model"]] if a.get("model") else []) + (["--title", a["title"]] if a.get("title") else [])
            done = self.delegate(*args, message=a["message"])
            if done.returncode:
                return error(done.stderr or done.stdout)
            ident = done.stdout.strip().splitlines()[-1]
            return result(f"Started {ident}. It is working in the background; call delegate_status with id {ident} "
                          "for its reply.", {"id": ident})
        if name == "delegate_send":
            args = ["send", a["id"], "--detach"] + (["--as-user"] if a.get("as_user") else ["--lead", self.lead])
            done = self.delegate(*args, message=a["message"])
            if done.returncode:
                return error(done.stderr or done.stdout)
            return result(f"Sent to {a['id']}; it is working. Call delegate_status for the reply.", {"id": a["id"]})
        if name == "delegate_status":
            if not a.get("id"):
                rows = [self.summary(s) for s in self.states()]
                text = "\n".join(f"{r['id']}: {r['status']}, last STATUS {r['agentStatus'] or '-'}, {r['title']}" for r in rows)
                return result(text or "No delegations in this project.", {"delegations": rows})
            folder = self.base() / a["id"]
            if not (folder / "state.json").exists():
                return error(f"no delegation {a['id']}")
            s = self.summary(json.loads((folder / "state.json").read_text()))
            reply = (folder / "final.md").read_text() if (folder / "final.md").exists() else ""
            head = f"{s['id']} ({s['harness']}) is {s['status']} after {s['turns']} turn(s)."
            body = "Still working; there is no new reply yet." if s["status"] == "running" else reply or "No reply."
            return result(f"{head}\n\n{body}", {"id": s["id"], "delegation": s, "reply": reply})
        if name == "delegate_model":
            done = self.delegate("set", a["id"], "--model", a["model"])
            return error(done.stderr or done.stdout) if done.returncode else result(done.stdout.strip(), {"id": a["id"]})
        if name == "delegate_stop":
            done = self.delegate("stop", a["id"])
            return error(done.stderr) if done.returncode else result(f"Stopped {a['id']}.", {"id": a["id"]})
        if name == "delegate_poll":
            rows = [self.summary(s) for s in self.states()]
            ident = a.get("id") or (rows[-1]["id"] if rows else "")
            after, events = int(a.get("after") or 0), []
            path = self.base() / ident / "events.jsonl"
            if ident and path.exists():
                lines = path.read_text().splitlines()
                events = [json.loads(x) for x in lines[after:] if x.strip()]
                after = len(lines)
            harness = next((r["harness"] for r in rows if r["id"] == ident), None)
            if harness and harness not in self.models:
                done = self.delegate("models", harness, "--json")
                self.models[harness] = json.loads(done.stdout) if done.returncode == 0 else []
            data = {"delegations": rows, "id": ident, "events": events, "next": after,
                    "models": self.models.get(harness, [])}
            return {"content": [{"type": "text", "text": json.dumps(data)}], "structuredContent": data}
        return error(f"unknown tool {name}")

    # ------------------------------------------------------------ JSON-RPC

    def handle(self, msg):
        """One message in; the response to send, or None."""
        method, ident, params = msg.get("method"), msg.get("id"), msg.get("params") or {}
        if method is None:  # a response to our roots/list
            roots = (msg.get("result") or {}).get("roots") or []
            if roots and roots[0].get("uri", "").startswith("file://"):
                self.root = Path(unquote(urlparse(roots[0]["uri"]).path))
            return None
        if method == "initialize":
            self.client_caps = params.get("capabilities") or {}
            self.lead = lead_of((params.get("clientInfo") or {}).get("name", ""))
            asked = params.get("protocolVersion")
            res = {"protocolVersion": asked if asked in PROTOCOLS else PROTOCOLS[0],
                   "capabilities": {"tools": {}, "resources": {}},
                   "serverInfo": {"name": "delegate", "version": "0.1.0"},
                   "instructions": "Delegate tasks to other coding agents and follow them in the Delegate panel."}
        elif method == "ping":
            res = {}
        elif method == "tools/list":
            # A host that doesn't render MCP Apps gets the text tools alone.
            shows_ui = "io.modelcontextprotocol/ui" in (self.client_caps.get("extensions") or {})
            res = {"tools": TOOLS if shows_ui else [t for t in TOOLS if t["name"] != "delegate_poll"]}
        elif method == "tools/call":
            try:
                res = self.call(params.get("name"), params.get("arguments") or {})
            except (KeyError, OSError, subprocess.SubprocessError, ValueError) as e:
                res = error(f"{type(e).__name__}: {e}")
        elif method == "resources/list":
            res = {"resources": [{"uri": PANEL_URI, "name": "Delegate panel", "mimeType": APP_MIME}]}
        elif method == "resources/read" and params.get("uri") == PANEL_URI:
            html = (HERE.parent / "app" / "panel.html").read_text()
            html = html.replace("/*BRANDS*/{}", (HERE.parent / "assets" / "brands.json").read_text().strip())
            res = {"contents": [{"uri": PANEL_URI, "mimeType": APP_MIME, "text": html,
                                 "_meta": {"ui": {"prefersBorder": True, "permissions": {"clipboardWrite": {}}}}}]}
        elif method in ("resources/templates/list", "prompts/list"):
            res = {"resourceTemplates": []} if method.startswith("resources") else {"prompts": []}
        elif ident is None:  # notifications: nothing to answer
            return None
        else:
            return {"jsonrpc": "2.0", "id": ident, "error": {"code": -32601, "message": f"method not found: {method}"}}
        return {"jsonrpc": "2.0", "id": ident, "result": res}


def result(text, structured):
    return {"content": [{"type": "text", "text": text}], "structuredContent": structured}


def error(text):
    return {"content": [{"type": "text", "text": text.strip() or "failed"}], "isError": True}


def lead_of(client):
    """Name the lead agent after the host, so transcripts show who delegated."""
    client = client.lower()
    for key, name in (("claude", "claude"), ("codex", "codex"), ("cursor", "cursor"), ("antigravity", "antigravity"),
                      ("agy", "antigravity"), ("gemini", "gemini")):
        if key in client:
            return name
    return "lead"


def serve_stdio(server):
    out = sys.stdout
    for raw in sys.stdin:
        if not raw.strip():
            continue
        try:
            msg = json.loads(raw)
        except ValueError:
            continue
        reply = server.handle(msg)
        if reply:
            out.write(json.dumps(reply) + "\n")
            out.flush()
        if msg.get("method") == "notifications/initialized" and "roots" in server.client_caps:
            out.write(json.dumps({"jsonrpc": "2.0", "id": "roots", "method": "roots/list"}) + "\n")
            out.flush()


def serve_http(server, port):
    class Handler(BaseHTTPRequestHandler):
        def cors(self):
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Headers", "content-type, mcp-session-id, mcp-protocol-version")
            self.send_header("Access-Control-Expose-Headers", "mcp-session-id")
            self.send_header("Access-Control-Allow-Methods", "POST, GET, DELETE, OPTIONS")

        def do_OPTIONS(self):
            self.send_response(204)
            self.cors()
            self.end_headers()

        def do_GET(self):  # no server-initiated stream
            self.send_response(405)
            self.cors()
            self.end_headers()

        do_DELETE = do_GET

        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers.get("content-length", 0))) or b"null")
            replies = [r for r in map(server.handle, body if isinstance(body, list) else [body]) if r]
            if not replies:
                self.send_response(202)
                self.cors()
                self.end_headers()
                return
            data = json.dumps(replies if isinstance(body, list) else replies[0]).encode()
            self.send_response(200)
            self.cors()
            self.send_header("Content-Type", "application/json")
            self.send_header("Mcp-Session-Id", "delegate")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, *args):
            pass

    print(f"delegate MCP server on http://127.0.0.1:{port}/mcp (root {server.root})", file=sys.stderr, flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--http", type=int, metavar="PORT", help="serve Streamable HTTP instead of stdio")
    args = p.parse_args()
    server = Server()
    serve_http(server, args.http) if args.http else serve_stdio(server)


if __name__ == "__main__":
    main()
