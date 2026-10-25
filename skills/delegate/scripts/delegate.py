#!/usr/bin/env python3
"""Delegate a task to another coding-agent CLI and talk to it turn by turn.

    delegate.py start <harness> [--write] [--model M] [--title T] [--attach PATH]... [--detach] (MESSAGE | --file F)
    delegate.py send <id> [--as-user] [--attach PATH]... [--detach] (MESSAGE | --file F)
    delegate.py list | show <id> [--follow] | stop <id> | diff <id> | close <id>
    delegate.py models <harness> | set <id> [--model M] [--effort E] [--speed S]   (default clears one)
    delegate.py meta <id> [--archive | --unarchive] [--name NAME] [--project NAME | --no-project] [--seen]
    delegate.py rename-project OLD NEW | delete <id> | pick [--folders] | usage [--json]

How a delegation is filed (archived, its project tag, the turn the person last saw) lives in
.delegate/<id>/meta.json, which only the UIs and `meta` write, never a running turn.

Harnesses: codex, cursor, antigravity (agy), gemini, gemini-api, claude. Every delegation lives in
<repo>/.delegate/<id>/: state.json, events.jsonl (the stream in both directions, one JSON event
per line) and final.md (the agent's last reply). `start` and `send` each run one turn and exit when
the agent ends it, printing a branded line per stream event and then the reply. With --detach they
print the id and return at once, and the turn runs on in its own process.

A message sent while the delegate is mid-turn is queued (.delegate/<id>/queue.jsonl) and runs as the
next turn; `send` then returns at once, and the process running the current turn runs it and prints
its reply. Attachments (--attach, or @path in the message) are files, folders or images: each harness
gets them through its own flags (images, extra directories) and the prompt lists them.

Exit codes: 0 the turn ended (or the message was queued), 1 the agent failed, 2 bad usage.
Python 3.9+, stdlib only.
"""
from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
import uuid
from pathlib import Path

SCRIPT = Path(__file__).resolve()
# Name, colour, terminal glyph and SVG logo of every sender, shared with the pane and the MCP App.
BRANDS = json.loads((SCRIPT.parent.parent / "assets" / "brands.json").read_text())
ALIASES = {"agy": "antigravity", "google": "gemini", "openai": "codex", "cursor-agent": "cursor", "gemapi": "gemini-api"}
BINARIES = {"codex": "codex", "cursor": "cursor-agent", "antigravity": "agy", "gemini": "gemini", "gemini-api": "gemini-api",
            "claude": "claude"}
GRACE = 10  # seconds between SIGTERM and SIGKILL when a turn times out or is stopped

STATUS_RE = re.compile(r"^\s*\**STATUS:?\**\s*(done|question|blocked)\b[:\s]*(.*)$", re.I | re.M)
PROTOCOL = """

---
You are working for {lead}, another coding agent, who delegated this task and reads only your final \
message. Make that message self-contained: what you did or found, and every file you changed.{mode_note}
End it with exactly one line: `STATUS: done`, `STATUS: question <your question>` or `STATUS: blocked <why>`."""
READ_NOTE = "\nThis is a read-only task: do not modify files."
REMINDER = "\n\n(End your reply with a STATUS line, as before.)"


# ---------------------------------------------------------------- stream parsers, one per harness

def clip(text, n=240):
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[: n - 1] + "…"


def tool_summary(name, args):
    if not isinstance(args, dict):
        return name
    for key in ("command", "CommandLine", "file_path", "path", "Path", "pattern", "globPattern", "query", "url"):
        if args.get(key):
            return f"{name} {args[key]}"
    return name


class Parser:
    """Turns a harness's JSON lines into events: message, thinking, tool, tool_result, error.

    `failed` records a terminal failure the harness reported, whatever text came before it."""

    def __init__(self):
        self.session_id = None
        self.final = None
        self.last_message = None
        self.usage = None
        self.failed = None

    def message(self, text):
        text = (text or "").strip()
        if not text:
            return []
        self.last_message = text
        return [{"kind": "message", "text": text}]

    def fail(self, text):
        self.failed = text or "the harness reported an error"
        return [{"kind": "error", "text": self.failed}]

    def flush(self):
        return []


class CodexParser(Parser):
    def feed(self, o):
        t, item = o.get("type"), o.get("item") or {}
        it = item.get("type")
        if t == "thread.started":
            self.session_id = o.get("thread_id")
        elif t == "item.started" and it == "command_execution":
            cmd = re.sub(r"^/bin/(ba|z)?sh -l?c ", "", item.get("command", ""))
            return [{"kind": "tool", "text": f"$ {cmd}"}]
        elif t == "item.completed":
            if it == "agent_message":
                return self.message(item.get("text"))
            if it == "reasoning":
                return [{"kind": "thinking", "text": item.get("text", "")}]
            if it == "command_execution":
                out = (item.get("aggregated_output") or "").strip()
                return [{"kind": "tool_result", "text": f"exit {item.get('exit_code')}  {out}"}]
            if it == "file_change":
                paths = ", ".join(c.get("path", "") for c in item.get("changes", []))
                return [{"kind": "tool", "text": f"edit {paths}"}]
            if it == "mcp_tool_call":
                return [{"kind": "tool", "text": f"{item.get('server')}.{item.get('tool')}"}]
            if it == "web_search":
                return [{"kind": "tool", "text": f"search {item.get('query', '')}"}]
            if it == "error":
                return [{"kind": "error", "text": item.get("message", "")}]
        elif t == "turn.completed":
            self.usage = o.get("usage")
        elif t == "turn.failed":
            return self.fail((o.get("error") or {}).get("message"))
        elif t == "error":
            return self.fail(o.get("message"))
        return []


class CursorParser(Parser):
    """cursor-agent: thinking arrives as deltas, and `result` glues every message together,
    so the reply is the last assistant message."""

    def __init__(self):
        super().__init__()
        self.thinking = ""

    def feed(self, o):
        t = o.get("type")
        self.session_id = o.get("session_id") or self.session_id
        if t == "thinking":
            if o.get("subtype") == "delta":
                self.thinking += o.get("text", "")
                return []
            text, self.thinking = self.thinking, ""
            return [{"kind": "thinking", "text": text}]
        if t == "assistant":
            parts = (o.get("message") or {}).get("content") or []
            return self.message("".join(p.get("text", "") for p in parts if p.get("type") == "text"))
        if t == "tool_call":
            call = o.get("tool_call") or {}
            key = next(iter(call), "tool")
            name = key.removesuffix("ToolCall")
            body = call.get(key) or {}
            if o.get("subtype") == "started":
                return [{"kind": "tool", "text": tool_summary(name, body.get("args"))}]
            result = body.get("result") or {}
            ok = result.get("success")
            detail = (ok or {}).get("stdout") or (ok or {}).get("content") or "" if ok else "failed"
            return [{"kind": "tool_result", "text": f"{name}  {detail}"}]
        if t == "result":
            self.usage = o.get("usage")
            if o.get("is_error"):
                return self.fail(o.get("result"))
        return []


class AntigravityParser(Parser):
    """agy: everything is a step_update; a reply streams as text_delta and ends on DONE."""

    def __init__(self):
        super().__init__()
        self.buffer = ""

    def flush(self):
        text, self.buffer = self.buffer, ""
        return self.message(text)

    def feed(self, o):
        event = o.get("event")
        if event == "init":
            self.session_id = o.get("conversation_id")
        elif event == "step_update":
            step = o.get("step_update") or {}
            self.session_id = step.get("conversation_id") or self.session_id
            kind, state = step.get("step_type"), step.get("state")
            if kind == "agent_response":
                self.buffer += step.get("text_delta", "")
                return self.flush() if state == "DONE" else []
            if kind == "tool":
                info = step.get("tool_info") or {}
                name = info.get("name") or step.get("tool_name", "tool")
                if state == "ACTIVE":
                    return [{"kind": "tool", "text": tool_summary(name, info.get("parameters"))}]
                if state == "DONE":
                    return [{"kind": "tool_result", "text": f"{name}  {info.get('output', '')}"}]
                if state in ("ERROR", "FAILED", "CANCELED"):
                    return [{"kind": "tool_result", "text": f"{name} {state.lower()}"}]
        elif event == "result":
            result = o.get("result") or {}
            self.final, self.usage = result.get("response"), result.get("usage")
            if result.get("status") not in (None, "SUCCESS"):
                return self.flush() + self.fail(result.get("error") or result.get("status"))
        elif event == "error":
            return self.fail(o.get("message") or json.dumps(o.get("error")))
        return []


class GeminiParser(Parser):
    def __init__(self):
        super().__init__()
        self.buffer = ""

    def flush(self):
        text, self.buffer = self.buffer, ""
        return self.message(text)

    def feed(self, o):
        t = o.get("type")
        self.session_id = o.get("session_id") or self.session_id
        if t == "message":
            if o.get("role") != "assistant":
                return []
            if o.get("delta"):
                self.buffer += o.get("content", "")
                return []
            return self.flush() + self.message(o.get("content"))
        out = self.flush()
        if t == "tool_use":
            out.append({"kind": "tool", "text": tool_summary(o.get("tool_name", "tool"), o.get("parameters"))})
        elif t == "tool_result":
            body = o.get("output") or (o.get("error") or {}).get("message", "")
            out.append({"kind": "tool_result", "text": f"{o.get('status', '')}  {body}"})
        elif t == "error":
            out += self.fail(o.get("message"))
        elif t == "result":
            self.usage = o.get("stats")
            if o.get("status") not in (None, "success"):
                out += self.fail((o.get("error") or {}).get("message") or o.get("status"))
        return out


class GeminiApiParser(Parser):
    """gemini-api generate --output-format json: one interaction per turn, its steps (thought, model output)
    streamed as deltas. The interaction's id is what the next turn continues from."""

    def __init__(self):
        super().__init__()
        self.step, self.buffer = None, ""

    def flush(self):
        text, self.buffer = self.buffer, ""
        if self.step == "thought":
            return [{"kind": "thinking", "text": text}] if text.strip() else []
        return self.message(text)

    def feed(self, o):
        o = o.get("data", o)
        t = o.get("event_type")
        if t in ("interaction.created", "interaction.completed"):
            interaction = o.get("interaction") or {}
            self.session_id = interaction.get("id") or self.session_id
            if t == "interaction.completed":
                self.usage = interaction.get("usage")
                if interaction.get("status") not in (None, "completed"):
                    return self.fail(f"interaction {interaction.get('status')}")
        elif t == "step.start":
            self.step, self.buffer = (o.get("step") or {}).get("type"), ""
        elif t == "step.delta":
            delta = o.get("delta") or {}
            self.buffer += delta.get("text") or delta.get("thought") or ""
        elif t == "step.stop":
            return self.flush()
        elif t == "error" or o.get("error"):
            error = o.get("error") or {}
            return self.fail(error.get("message") if isinstance(error, dict) else str(error))
        return []


class ClaudeParser(Parser):
    def feed(self, o):
        t = o.get("type")
        self.session_id = o.get("session_id") or self.session_id
        out = []
        if t == "assistant":
            for block in (o.get("message") or {}).get("content") or []:
                if block.get("type") == "text":
                    out += self.message(block.get("text"))
                elif block.get("type") == "thinking":
                    out.append({"kind": "thinking", "text": block.get("thinking", "")})
                elif block.get("type") == "tool_use":
                    out.append({"kind": "tool", "text": tool_summary(block.get("name"), block.get("input"))})
        elif t == "user":
            for block in (o.get("message") or {}).get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_result":
                    out.append({"kind": "tool_result", "text": "error" if block.get("is_error") else "ok"})
        elif t == "result":
            self.final = o.get("result")
            self.usage = {**(o.get("usage") or {}), "cost_usd": o.get("total_cost_usd")}
            if o.get("is_error"):
                out += self.fail(o.get("result") or o.get("subtype"))
        return out


PARSERS = {"codex": CodexParser, "cursor": CursorParser, "antigravity": AntigravityParser,
           "gemini": GeminiParser, "gemini-api": GeminiApiParser, "claude": ClaudeParser}


IMAGES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}


def attachment_flags(harness, attachments, workdir):
    """Codex takes images with -i; the others reach a file or folder outside the workspace by adding its folder."""
    images = [a for a in attachments if Path(a).suffix.lower() in IMAGES]
    if harness == "codex":
        return [x for a in images for x in ("-i", a)]
    if harness == "gemini-api":  # files go in as input, folders it can't take
        return [x for a in attachments if Path(a).is_file() for x in ("-i", a)]
    folders = sorted({a if Path(a).is_dir() else str(Path(a).parent) for a in attachments})
    outside = [d for d in folders if not Path(d).resolve().is_relative_to(Path(workdir).resolve())]
    flag = "--include-directories" if harness == "gemini" else "--add-dir"
    return [x for d in outside for x in (flag, d)]


def command(state, prompt, attachments=()):
    """The argv and environment for one turn: read-only, or allowed to edit (in its worktree)."""
    h, sid, write = state["harness"], state.get("session_id"), state["mode"] == "write"
    model, effort, speed = state.get("model_id") or state.get("model"), state.get("effort"), state.get("speed")
    effort_in_id = state.get("effort_in_id", False)
    env = dict(os.environ)
    extra = attachment_flags(h, attachments, state["workdir"])
    if h == "codex":
        sandbox = f'sandbox_mode="{"workspace-write" if write else "read-only"}"'
        # Live web search as the other harnesses have it; `--search` is missing from `exec resume`, the config key is not.
        argv = ["codex", "exec"] + (["resume", sid] if sid else []) + ["--json", "--skip-git-repo-check", "-c", sandbox]
        argv += ["-c", 'web_search="live"']
        argv += (["-m", model] if model else []) + (["-c", f'model_reasoning_effort="{effort}"'] if effort else [])
        argv += (["-c", 'service_tier="priority"'] if speed == "fast" else []) + extra + ["--"]
    elif h == "cursor":
        argv = ["cursor-agent", "-p", "--output-format", "stream-json", "--trust"]
        argv += ["-f"] if write else ["--mode", "ask"]
        argv += (["--resume", sid] if sid else []) + (["--model", model] if model else []) + extra
    elif h == "antigravity":
        argv = ["agy", "--output-format", "stream-json"]
        # Headless agy can't answer a permission prompt, so it is denied and the turn ends empty; plan
        # mode is what keeps a read-only run from editing, so its tools are approved too.
        argv += ["--dangerously-skip-permissions"] + ([] if write else ["--mode", "plan"])
        argv += (["--conversation", sid] if sid else []) + (["--model", model] if model else [])
        argv += (["--effort", effort] if effort and not effort_in_id else []) + extra + ["-p"]
    elif h == "gemini-api":
        # A plain API: no tools, so read and write are the same; a turn continues the last interaction.
        argv = ["gemini-api", "generate", "--output-format", "json", "--no-interactive"]
        argv += (["--previous-interaction-id", sid] if sid else []) + (["-m", model] if model else []) + extra + ["--"]
    elif h == "gemini":
        argv = ["gemini", "-o", "stream-json", "--skip-trust", "--approval-mode", "yolo" if write else "plan"]
        argv += ["--resume", sid] if sid else ["--session-id", state["new_session_id"]]
        argv += (["-m", model] if model else []) + extra + ["-p"]
    else:
        env.pop("CLAUDECODE", None)  # a nested `claude` refuses to start inside a Claude Code session otherwise
        argv = ["claude", "-p", "--output-format", "stream-json", "--verbose"]
        argv += ["--permission-mode", "acceptEdits"] if write else ["--disallowedTools", "Edit", "Write", "NotebookEdit"]
        argv += (["--resume", sid] if sid else []) + (["--model", model] if model else [])
        argv += (["--effort", effort] if effort else []) + extra + ["--"]
    return argv + [prompt], env


def resolve_attachments(root, paths, text):
    """Absolute paths of --attach arguments and of @path mentions in the message that exist."""
    mentioned = re.findall(r"(?:^|\s)@((?:~|\.{0,2}/|[\w.-]+/)[^\s]*|[\w.-]+\.\w+)", text)
    found = []
    for raw in [*paths, *mentioned]:
        path = Path(os.path.expanduser(raw.rstrip(".,;:)")))
        path = path if path.is_absolute() else Path(root) / path
        if path.exists() and str(path) not in found:
            found.append(str(path))
        elif raw in paths:
            sys.exit(f"attachment not found: {raw}")
    return found


CLAUDE_ALIASES = ["fable", "opus", "sonnet", "haiku"]


EFFORT_LEVELS = ["none", "minimal", "low", "medium", "high", "xhigh", "extra-high", "max", "ultra"]
# Cursor and Antigravity fold effort and speed into the id: `gpt-5.3-codex-high-fast`.
VARIANT_RE = re.compile(r"^(?P<base>.+?)(?:-(?P<effort>" + "|".join(EFFORT_LEVELS) + r"))?(?P<fast>-fast)?$")
LABEL_TAIL_RE = re.compile(r"(\s+\(?(None|Minimal|Low|Medium|High|Extra High|XHigh|Max|Ultra|Fast)\)?)+$", re.I)
FLAG_EFFORTS = {"claude": ["low", "medium", "high", "xhigh", "max"], "antigravity": ["low", "medium", "high", "xhigh", "max"]}


def list_models(harness):
    """Models as [{"id", "label", "efforts", "speeds"}], "default" (the harness's own choice) first.

    Effort and speed are split out of ids that encode them, so each is picked on its own; `set` puts
    the chosen three back together as the harness wants them (one id, or flags)."""
    raw = raw_models(harness)
    general = FLAG_EFFORTS.get(harness, [])
    if harness == "codex":
        try:
            cache = json.loads((Path.home() / ".codex" / "models_cache.json").read_text()).get("models", [])
        except (OSError, ValueError):
            cache = []
        models = [{"id": m["slug"], "label": m.get("display_name", m["slug"]),
                   "efforts": [lvl["effort"] for lvl in m.get("supported_reasoning_levels", [])],
                   "speeds": ["fast"] if m.get("additional_speed_tiers") else []} for m in cache]
        general = sorted({e for m in models for e in m["efforts"]}, key=EFFORT_LEVELS.index)
    elif harness in ("cursor", "antigravity"):
        grouped = {}
        for row in raw:
            match = VARIANT_RE.match(row["id"])
            base = match["base"] if match else row["id"]
            entry = grouped.setdefault(base, {"id": base, "label": LABEL_TAIL_RE.sub("", row["label"]),
                                              "efforts": [], "speeds": []})
            if match and match["effort"] and match["effort"] not in entry["efforts"]:
                entry["efforts"].append(match["effort"])
            if match and match["fast"] and "fast" not in entry["speeds"]:
                entry["speeds"].append("fast")
        models = list(grouped.values())
        for m in models:
            m["efforts"] = sorted(m["efforts"], key=EFFORT_LEVELS.index) or list(general)
    else:
        models = [{**row, "efforts": list(general), "speeds": []} for row in raw]
    default = {"id": "default", "label": f"Default ({harness}'s own)", "efforts": general, "speeds": []}
    return [default] + models


def resolve_model(harness, model, effort, speed):
    """The model id to pass, and whether effort and speed are already in it (Cursor, Antigravity)."""
    if not model or harness not in ("cursor", "antigravity"):
        return model, False
    ids = {row["id"] for row in raw_models(harness)}
    fast = "-fast" if speed == "fast" else ""
    for candidate in (f"{model}-{effort}{fast}" if effort else None, f"{model}-{effort}" if effort else None,
                      f"{model}{fast}", model):
        if candidate and candidate in ids:
            return candidate, bool(effort and f"-{effort}" in candidate)
    return model, False


def raw_models(harness):
    """The models a harness lists, as [{"id", "label"}], exactly as it names them."""
    rows = []
    try:
        if harness == "cursor":  # "id - Label"
            out = subprocess.run(["cursor-agent", "models"], capture_output=True, text=True, timeout=60).stdout
            rows = [dict(zip(("id", "label"), x.split(" - ", 1))) for x in out.splitlines() if " - " in x]
        elif harness == "antigravity":  # "id<TAB>Label"
            out = subprocess.run(["agy", "models"], capture_output=True, text=True, timeout=60).stdout
            rows = [dict(zip(("id", "label"), x.split("\t", 1))) for x in out.splitlines() if "\t" in x]
        elif harness == "codex":  # Codex keeps the account's models in a cache
            cache = json.loads((Path.home() / ".codex" / "models_cache.json").read_text())
            rows = [{"id": m["slug"], "label": m.get("display_name", m["slug"])} for m in cache.get("models", [])]
        elif harness == "claude":
            rows = [{"id": a, "label": a.capitalize()} for a in CLAUDE_ALIASES]
        elif harness == "gemini-api":  # "  id   Description", under Gemma:/Gemini:/Image: headings
            out = subprocess.run(["gemini-api", "models", "--no-interactive"], capture_output=True, text=True, timeout=60).stdout
            rows = [{"id": x.split()[0], "label": x.split()[0]} for x in out.splitlines()
                    if x.startswith("  ") and x.split() and "image" not in x.split()[0]]
    except (OSError, ValueError, subprocess.SubprocessError, KeyError):
        rows = []
    return [{"id": r["id"].strip(), "label": r.get("label", r["id"]).strip().removesuffix(" (current, default)")}
            for r in rows if r.get("id", "").strip() and r["id"].strip() != "auto"]


def auth_hint(harness, text):
    text = text.lower()
    if harness == "gemini" and ("gemini_api_key" in text or "auth" in text):
        return "Gemini isn't signed in for headless use: run `gemini`, pick Login with Google (/auth), or set GEMINI_API_KEY."
    if harness == "gemini-api" and ("api key" in text or "unauthenticated" in text or "permission_denied" in text):
        return "gemini-api has no API key: create one in Google AI Studio and run `gemini-api configure` yourself."
    if harness == "cursor" and ("sign in" in text or "login" in text or "authenticat" in text):
        return "Cursor isn't signed in: run `cursor-agent login`."
    if harness == "antigravity" and ("sign in" in text or "login" in text or "auth" in text):
        return "Antigravity isn't signed in: run `agy` once and sign in."
    if harness == "codex" and ("login" in text or "401" in text or "unauthorized" in text):
        return "Codex isn't signed in: run `codex login`."
    if harness == "claude" and ("login" in text or "auth" in text):
        return "Claude isn't signed in: run `claude auth login`."
    return None


# ---------------------------------------------------------------- state on disk

def git(cwd, *args, check=True):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, check=check).stdout.strip()


def repo_root():
    try:
        return Path(git(Path.cwd(), "rev-parse", "--show-toplevel"))
    except (subprocess.CalledProcessError, FileNotFoundError):
        return Path.cwd()


def home():
    root = repo_root()
    base = root / ".delegate"
    if not base.exists():
        base.mkdir()
        try:  # keep transcripts and worktrees out of git without touching the project's .gitignore
            exclude = Path(git(root, "rev-parse", "--git-common-dir"))
            exclude = (exclude if exclude.is_absolute() else root / exclude) / "info" / "exclude"
            exclude.parent.mkdir(exist_ok=True)
            lines = exclude.read_text().splitlines() if exclude.exists() else []
            if ".delegate/" not in lines:
                exclude.write_text("\n".join(lines + [".delegate/"]) + "\n")
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
    return root, base


def load(base, ident):
    path = base / ident / "state.json"
    if not path.exists():
        sys.exit(f"no delegation {ident!r} (python3 {SCRIPT} list)")
    return json.loads(path.read_text())


def save(base, state):
    state["updated"] = time.time()
    path = base / state["id"] / "state.json"
    tmp = path.with_name(f"state.{os.getpid()}.tmp")
    tmp.write_text(json.dumps(state, indent=1))
    tmp.replace(path)


def read_meta(base, ident):
    path = base / ident / "meta.json"
    return json.loads(path.read_text()) if path.exists() else {}


def write_meta(base, ident, **changes):
    meta = {**read_meta(base, ident), **changes}
    tmp = base / ident / f"meta.{os.getpid()}.tmp"
    tmp.write_text(json.dumps(meta, indent=1))
    tmp.replace(base / ident / "meta.json")
    return meta


def enqueue(base, ident, entry):
    """Adds a message to the delegation's queue; returns how many are waiting."""
    with open(base / ident / "queue.lock", "w") as guard:
        fcntl.flock(guard, fcntl.LOCK_EX)
        with (base / ident / "queue.jsonl").open("a") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        return len((base / ident / "queue.jsonl").read_text().splitlines())


def dequeue(base, ident, clear=False):
    """Takes the oldest queued message (or, with clear, drops them all). None when the queue is empty."""
    path = base / ident / "queue.jsonl"
    with open(base / ident / "queue.lock", "w") as guard:
        fcntl.flock(guard, fcntl.LOCK_EX)
        lines = path.read_text().splitlines() if path.exists() else []
        path.write_text("" if clear else "".join(x + "\n" for x in lines[1:]))
        return json.loads(lines[0]) if lines and not clear else None


def lock(base, ident, wait=False):
    """The delegation's turn lock: held for a whole turn, so two sends never overlap. None when busy."""
    fd = os.open(base / ident / "lock", os.O_RDWR | os.O_CREAT)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | (0 if wait else fcntl.LOCK_NB))
        return fd
    except BlockingIOError:
        os.close(fd)
        return None


def signal_group(pid, sig):
    try:
        os.killpg(pid, sig)
    except (ProcessLookupError, PermissionError):
        pass


def terminate(pid):
    """SIGTERM the turn's process group, then SIGKILL it if anything is left after GRACE seconds."""
    signal_group(pid, signal.SIGTERM)
    deadline = time.time() + GRACE
    while time.time() < deadline:
        try:
            os.killpg(pid, 0)
        except (ProcessLookupError, PermissionError):
            return
        time.sleep(0.2)
    signal_group(pid, signal.SIGKILL)


def alive(pid):
    if not pid:
        return False
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError):
        return False


# ---------------------------------------------------------------- output

def paint(name, text, kind, color):
    brand = BRANDS.get(name, BRANDS["lead"])
    badge = f"{brand['glyph']} {name:<6}"
    if not color:
        return f"{badge} {text}"
    r, g, b = (int(brand["color"][i:i + 2], 16) for i in (1, 3, 5))
    tint = {"thinking": "\x1b[2;3m", "tool": "\x1b[2m", "tool_result": "\x1b[2m", "error": "\x1b[31m"}.get(kind, "")
    return f"\x1b[1;38;2;{r};{g};{b}m{badge}\x1b[0m {tint}{text}\x1b[0m"


ARROWS = {"message": "", "thinking": "∴ ", "tool": "› ", "tool_result": "  ↳ ", "error": "✗ ", "status": "· "}


def line(ev, color, full=False):
    # In full, the reply and the lead's messages print whole; the agent's own messages are clipped,
    # since its last one repeats as the reply.
    whole = full and (ev["kind"] == "final" or (ev["kind"] == "message" and ev["from"] not in PARSERS))
    text = ev["text"] if whole else clip(ev["text"])
    if ev["kind"] == "final":
        return paint(ev["from"], f"── reply ──\n{text}", "message", color)
    return paint(ev["from"], ARROWS.get(ev["kind"], "") + text, ev["kind"], color)


class Log:
    def __init__(self, folder, turn, color):
        self.path, self.turn, self.color = folder / "events.jsonl", turn, color

    def emit(self, sender, kind, text, echo=True, **extra):
        ev = {"ts": round(time.time(), 3), "turn": self.turn, "from": sender, "kind": kind, "text": text, **extra}
        with self.path.open("a") as f:
            f.write(json.dumps(ev, ensure_ascii=False) + "\n")
        if echo and kind != "final":
            print(line(ev, self.color), flush=True)


# ---------------------------------------------------------------- one turn

def run_turn(base, state, text, sender, timeout, color, attachments=()):
    """One turn, under the delegation's lock (held by the caller). Returns the exit code."""
    folder = base / state["id"]
    state["turns"] = state.get("turns", 0) + 1
    log = Log(folder, state["turns"], color)
    log.emit(sender, "message", text, **({"attachments": list(attachments)} if attachments else {}))
    if sender == "user":
        text = f"Message from the human user, not from {state['lead']}:\n{text}"
    if attachments:
        text += "\n\nAttached (read them as part of this message):\n" + "\n".join(
            f"- {a} ({'folder' if Path(a).is_dir() else 'image' if Path(a).suffix.lower() in IMAGES else 'file'})"
            for a in attachments)
    prompt = text + (PROTOCOL.format(lead=state["lead"], mode_note=READ_NOTE if state["mode"] == "read" else "")
                     if state["turns"] == 1 else REMINDER)
    argv, env = command(state, prompt, attachments)
    parser = PARSERS[state["harness"]]()
    started = time.time()
    stderr = (folder / "stderr.log").open("w")
    try:
        proc = subprocess.Popen(argv, cwd=state["workdir"], env=env, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                stderr=stderr, text=True, bufsize=1, start_new_session=True)
    except FileNotFoundError:
        log.emit(state["harness"], "error", f"{argv[0]} is not installed or not on PATH")
        return 1
    state.update(status="running", pid=proc.pid)
    save(base, state)
    timed_out = threading.Event()

    def expire():
        timed_out.set()
        terminate(proc.pid)

    killer = threading.Timer(timeout, expire)
    killer.daemon = True
    killer.start()
    noise = []
    try:
        for raw in proc.stdout:
            try:
                obj = json.loads(raw)
            except ValueError:
                if raw.strip():
                    noise.append(raw.strip())
                continue
            if isinstance(obj, dict):
                for ev in parser.feed(obj):
                    if str(ev["text"]).strip():
                        log.emit(state["harness"], ev["kind"], ev["text"])
        for ev in parser.flush():
            log.emit(state["harness"], ev["kind"], ev["text"])
    finally:
        killer.cancel()
        if proc.poll() is None:
            terminate(proc.pid)
        code = proc.wait()
        stderr.close()

    # A stop or close changed the state on disk while this turn ran: keep what they wrote.
    current = json.loads((folder / "state.json").read_text())
    if parser.session_id:
        state["session_id"] = parser.session_id
    reply = (parser.final or parser.last_message or "").strip()
    seconds = round(time.time() - started)
    stopped = current.get("stop_requested")
    problem = ("timed out" if timed_out.is_set() else "was stopped" if stopped
               else f"failed: {clip(parser.failed, 300)}" if parser.failed
               else f"exited {code}" if code != 0 else "ended with no reply" if not reply else None)
    if reply:
        (folder / "final.md").write_text(reply + "\n")
    found = STATUS_RE.findall(reply)
    agent_status = found[-1][0].lower() if found else "unknown"
    # A reply ending in its STATUS line is the agent's finished answer: a failure the harness reports
    # after it (a dropped connection) is shown, not taken for the turn's outcome.
    if found and problem and not (timed_out.is_set() or stopped):
        log.emit(state["harness"], "error", f"{state['harness']} {problem} after its reply")
        problem = None
    state.update(pid=None, stop_requested=False, status="idle" if not problem or stopped else "error",
                 agent_status="stopped" if stopped else agent_status if not problem else "error")
    if current.get("status") == "closed":
        state["status"] = "closed"
    rule = "─" * 3
    if problem and not stopped:
        err = (folder / "stderr.log").read_text()[-1500:] + "\n".join(noise[-15:])
        hint = auth_hint(state["harness"], err)
        detail = hint or (clip(err, 600) if err.strip() else f"stderr: {folder / 'stderr.log'}")
        log.emit(state["harness"], "error", f"{state['harness']} {problem}. {detail}")
        print(f"\n{state['harness']} {problem}. {detail}")
    if reply:
        log.emit(state["harness"], "final", reply, status=state["agent_status"], seconds=seconds, usage=parser.usage)
        print(f"\n{rule} {state['harness']} · {state['id']} · turn {state['turns']} · {seconds}s · "
              f"STATUS: {state['agent_status']} {rule}\n{reply}\n{rule}")
    elif stopped:
        log.emit("user", "status", "stopped", echo=False)
    save(base, state)
    if state["status"] != "closed":
        print(f"reply:  python3 {SCRIPT} send {state['id']} \"...\"")
        if state.get("worktree"):
            print(f"diff:   python3 {SCRIPT} diff {state['id']}")
    return 1 if problem and not stopped else 0


def serve_queue(base, ident, fd, timeout, color):
    """Runs queued messages, one turn each, while holding the lock; then hands the lock back.

    A sender queues first and takes the lock second, and the holder looks at the queue again after
    letting go, so a message queued at the moment the holder finishes is never stranded."""
    code = 0
    while fd is not None:
        try:
            while (entry := dequeue(base, ident)) is not None:
                state = load(base, ident)
                if state.get("status") == "closed":
                    dequeue(base, ident, clear=True)
                    break
                code = run_turn(base, state, entry["text"], entry["from"], timeout, color, entry.get("attachments", []))
        finally:
            os.close(fd)
        path = base / ident / "queue.jsonl"
        fd = lock(base, ident) if path.exists() and path.read_text().strip() else None
    return code


def submit(base, state, text, sender, attachments, args):
    """Queue the message, then run the queue here or in a detached process, unless a turn is already running it."""
    waiting = enqueue(base, state["id"], {"from": sender, "text": text, "attachments": attachments, "ts": time.time()})
    fd = lock(base, state["id"])
    if fd is None:
        print(f"{state['id']} is mid-turn: queued, {waiting} waiting. The running turn's process runs it next.")
        return 0
    if not args.detach:
        return serve_queue(base, state["id"], fd, args.timeout, args.color)
    state.update(status="running", pid=None)
    save(base, state)
    with (base / state["id"] / "turn.log").open("a") as out:
        subprocess.Popen([sys.executable, str(SCRIPT), "--no-color", "_turn", state["id"],
                          "--timeout", str(args.timeout), "--lock-fd", str(fd)],
                         cwd=state["root"], stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT,
                         pass_fds=(fd,), start_new_session=True)
    os.close(fd)  # the child holds the lock now
    print(state["id"])
    return 0


# ---------------------------------------------------------------- commands

def read_message(args):
    if args.file:
        return Path(args.file).read_text()
    if args.message:
        return " ".join(args.message)
    sys.exit("give the message as arguments or with --file")


def lead_name(args):
    if args.lead:
        return args.lead
    return "claude" if os.environ.get("CLAUDECODE") == "1" else "lead"


def cmd_start(args):
    harness = ALIASES.get(args.harness, args.harness)
    if harness not in PARSERS:
        sys.exit(f"unknown harness {args.harness!r}: {', '.join(PARSERS)}")
    if not shutil.which(BINARIES[harness]):
        sys.exit(f"{BINARIES[harness]} is not on PATH")
    text = read_message(args)
    root, base = home()
    # The next free number; mkdir claims it, so starts running at the same moment each get their own.
    n = 1 + sum(1 for p in base.glob(f"{harness}-*") if p.is_dir())
    while True:
        ident, folder = f"{harness}-{n}", base / f"{harness}-{n}"
        try:
            folder.mkdir()
            break
        except FileExistsError:
            n += 1
    mode = "write" if args.write else "read"
    state = {"id": ident, "harness": harness, "mode": mode, "lead": lead_name(args),
             "title": args.title or clip(text.strip().splitlines()[0], 40), "root": str(root), "workdir": str(root),
             "turns": 0, "created": time.time(), "status": "idle", "new_session_id": str(uuid.uuid4())}
    apply_choice(state, args.model, args.effort, args.speed)
    if mode == "write":
        wt = folder / "worktree"
        try:
            state["base"] = git(root, "rev-parse", "HEAD")
            git(root, "worktree", "add", "-q", "-b", f"delegate/{ident}", str(wt), state["base"])
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            shutil.rmtree(folder)
            sys.exit(f"--write needs a git repository with a commit; git said: {getattr(e, 'stderr', e)}")
        if git(root, "status", "--porcelain"):
            print("note: the worktree starts from HEAD; uncommitted changes in the checkout are not in it.")
        state.update(workdir=str(wt), worktree=str(wt), branch=f"delegate/{ident}")
    save(base, state)
    if args.project:
        write_meta(base, ident, project=args.project)
    if not args.detach:
        print(f"delegation {ident}: {BRANDS[harness]['name']}, {mode}, in {state['workdir']}", flush=True)
    return submit(base, state, text, state["lead"], resolve_attachments(root, args.attach, text), args)


def cmd_send(args):
    root, base = home()
    state = load(base, args.id)
    if state.get("status") == "closed":
        sys.exit(f"{args.id} is closed")
    sender = "user" if args.as_user else lead_name(args)
    text = read_message(args)
    return submit(base, state, text, sender, resolve_attachments(root, args.attach, text), args)


def cmd_turn(args):
    """The detached half of start/send: serves the queue under the lock its parent handed over."""
    _, base = home()
    return serve_queue(base, args.id, args.lock_fd, args.timeout, False)


def cmd_models(args):
    harness = ALIASES.get(args.harness, args.harness)
    rows = list_models(harness)
    print(json.dumps(rows) if args.json else "\n".join(f"{r['id']:<36} {r['label']}" for r in rows))
    return 0


def apply_choice(state, model=None, effort=None, speed=None):
    """Sets model, effort and speed ("default" clears one) and the harness-specific id they resolve to."""
    for key, value in (("model", model), ("effort", effort), ("speed", speed)):
        if value is not None:
            state[key] = None if value == "default" else value
    state["model_id"], state["effort_in_id"] = resolve_model(
        state["harness"], state.get("model"), state.get("effort"), state.get("speed"))


def cmd_set(args):
    """Show or change the model, effort and speed a delegation uses; a change applies from its next turn."""
    _, base = home()
    state = load(base, args.id)
    if args.model or args.effort or args.speed:
        apply_choice(state, args.model, args.effort, args.speed)
        save(base, state)
        Log(base / args.id, state.get("turns", 0), False).emit("user", "status", (
            f"model {state.get('model') or 'default'} · effort {state.get('effort') or 'default'} · "
            f"speed {state.get('speed') or 'default'}, from the next turn"), echo=False)
    print(json.dumps({k: state.get(k) for k in ("model", "effort", "speed", "model_id")}))
    return 0


def cmd_meta(args):
    _, base = home()
    state = load(base, args.id)
    changes = {}
    if args.archive or args.unarchive:
        changes["archived"] = bool(args.archive)
    if args.project is not None or args.no_project:
        changes["project"] = (args.project or "").strip() or None
    if args.seen:
        changes["seen_turns"] = state.get("turns", 0)
    if args.name is not None:
        changes["name"] = args.name.strip() or None
    meta = write_meta(base, args.id, **changes) if changes else read_meta(base, args.id)
    print(json.dumps(meta))
    return 0


def cmd_rename_project(args):
    _, base = home()
    renamed = [p.parent.name for p in base.glob("*/state.json") if read_meta(base, p.parent.name).get("project") == args.old]
    for ident in renamed:
        write_meta(base, ident, project=args.new.strip() or None)
    print(f"renamed {args.old!r} to {args.new!r} on {len(renamed)} chat(s)")
    return 0


def cmd_delete(args):
    """Removes a delegation for good: its turn, worktree, branch and transcript."""
    if cmd_close(args) != 0:
        return 1
    _, base = home()
    shutil.rmtree(base / args.id)
    print(f"deleted {args.id}")
    return 0


def cmd_pick(args):
    """Opens the system's file dialog and prints the chosen paths as JSON ([] when cancelled)."""
    kind = "folder" if args.folders else "file"
    if sys.platform == "darwin":
        script = [f'set picked to choose {kind} with prompt "Attach to the delegation" with multiple selections allowed',
                  'set out to ""', "repeat with one in picked", "set out to out & POSIX path of one & linefeed",
                  "end repeat", "return out"]
        argv = ["osascript", "-e", "activate", *[x for line in script for x in ("-e", line)]]
    elif shutil.which("zenity"):
        argv = ["zenity", "--file-selection", "--multiple", "--separator=\n"] + (["--directory"] if args.folders else [])
    else:
        sys.exit("no file dialog here (macOS osascript or Linux zenity); attach with @path instead")
    done = subprocess.run(argv, capture_output=True, text=True)
    print(json.dumps([x.rstrip("/") or "/" for x in done.stdout.splitlines() if x.strip()] if done.returncode == 0 else []))
    return 0


# Each harness reports a turn's tokens in its own shape; these read them into one.
USAGE_KEYS = {
    # Claude writes new prompt text to its cache as it reads it: that is fresh input too.
    "input": ("input_tokens", "inputTokens", "prompt_tokens", "total_input_tokens", "cache_creation_input_tokens"),
    "cached": ("cached_input_tokens", "cacheReadTokens", "cache_read_tokens", "cache_read_input_tokens", "total_cached_tokens"),
    "output": ("output_tokens", "outputTokens", "candidates_tokens", "total_output_tokens"),
    "reasoning": ("reasoning_output_tokens", "thinking_tokens", "thoughts_tokens", "total_thought_tokens"),
}


def tokens(usage, harness=""):
    """input is fresh input: Codex and the Gemini API count cached tokens inside input, the others apart."""
    usage = usage or {}
    out = {name: sum(int(usage.get(k) or 0) for k in keys) for name, keys in USAGE_KEYS.items()}
    if harness in ("codex", "gemini-api"):
        out["input"] = max(0, out["input"] - out["cached"])
    out["cost_usd"] = float(usage.get("cost_usd") or 0)
    return out


def cmd_usage(args):
    """Tokens, time and turns per delegation and per harness, from each turn's final event."""
    _, base = home()
    rows = []
    for path in sorted(base.glob("*/events.jsonl")):
        state = json.loads((path.parent / "state.json").read_text())
        meta = read_meta(base, path.parent.name)
        finals = [json.loads(x) for x in path.read_text().splitlines() if '"kind": "final"' in x]
        row = {"id": state["id"], "harness": state["harness"], "model": state.get("model_id") or state.get("model") or "default",
               "effort": state.get("effort") or "", "name": meta.get("name") or state.get("title", ""),
               "project": meta.get("project") or "", "turns": len(finals),
               "seconds": sum(f.get("seconds") or 0 for f in finals)}
        for f in finals:
            for name, value in tokens(f.get("usage"), state["harness"]).items():
                row[name] = row.get(name, 0) + value
        rows.append(row)
    rows = [r for r in rows if not args.project or r["project"] == args.project]
    if args.json:
        print(json.dumps(rows, indent=1))
        return 0
    head = f"{'delegation':<16}{'harness':<12}{'model':<26}{'turns':>6}{'time':>8}{'input':>10}{'cached':>10}{'output':>9}{'reason':>9}{'cost':>8}"
    print(head)
    totals = {}
    for r in rows:
        print(f"{r['id']:<16}{r['harness']:<12}{clip(r['model'], 25):<26}{r['turns']:>6}{r['seconds']:>7}s{r.get('input', 0):>10}"
              f"{r.get('cached', 0):>10}{r.get('output', 0):>9}{r.get('reasoning', 0):>9}"
              f"{('$%.2f' % r['cost_usd']) if r.get('cost_usd') else '-':>8}")
        t = totals.setdefault(r["harness"], {"delegations": 0})
        t["delegations"] += 1
        for k in ("turns", "seconds", "input", "cached", "output", "reasoning", "cost_usd"):
            t[k] = t.get(k, 0) + r.get(k, 0)
    print("\nper harness")
    for h, t in totals.items():
        print(f"{h:<12}{t['delegations']:>3} delegations{t['turns']:>5} turns{t['seconds']:>7}s"
              f"  in {t['input']:,}  cached {t['cached']:,}  out {t['output']:,}  reasoning {t['reasoning']:,}"
              + (f"  ${t['cost_usd']:.2f}" if t["cost_usd"] else ""))
    return 0


def cmd_list(args):
    _, base = home()
    rows = [(json.loads(p.read_text()), read_meta(base, p.parent.name)) for p in sorted(base.glob("*/state.json"))]
    rows = [(s, m) for s, m in rows if args.all or not m.get("archived")]
    if not rows:
        print("no delegations")
    for s, m in rows:
        tag = f"[{m['project']}] " if m.get("project") else ""
        print(f"{s['id']:<14} {s['status']:<8} {s.get('agent_status', '-'):<8} {s['mode']:<5} "
              f"turns {s.get('turns', 0):<3} {tag}{s['title']}{'  (archived)' if m.get('archived') else ''}")
    return 0


def cmd_show(args):
    _, base = home()
    load(base, args.id)
    path, pos = base / args.id / "events.jsonl", 0
    while True:
        if path.exists():
            with path.open() as f:
                f.seek(pos)
                for raw in f:
                    print(line(json.loads(raw), args.color, full=True), flush=True)
                pos = f.tell()
        if not args.follow:
            return 0
        time.sleep(0.4)


def stop_turn(base, ident):
    """Ask a running turn to end and wait until it has released the lock. Returns the held lock."""
    fd = lock(base, ident)
    if fd is not None:
        return fd
    state = load(base, ident)
    state["stop_requested"] = True
    save(base, state)
    if alive(state.get("pid")):
        threading.Thread(target=terminate, args=(state["pid"],), daemon=True).start()
    return lock(base, ident, wait=True)


def cmd_stop(args):
    _, base = home()
    load(base, args.id)
    dequeue(base, args.id, clear=True)  # stopping drops what was queued behind the turn
    os.close(stop_turn(base, args.id))
    print(f"stopped {args.id}")
    return 0


def cmd_diff(args):
    _, base = home()
    state = load(base, args.id)
    if not state.get("worktree"):
        sys.exit(f"{args.id} worked read-only in the checkout; there is nothing to diff")
    wt = state["worktree"]
    git(wt, "add", "-A", "-N")  # untracked files show up in the diff
    # Against the commit it started from, so its own commits are included; --binary so images apply.
    out = subprocess.run(["git", "-C", wt, "diff", "--binary", "--no-ext-diff", "--no-textconv", state["base"]],
                         capture_output=True, text=True, check=True)
    sys.stdout.write(out.stdout)
    return 0


def cmd_close(args):
    root, base = home()
    load(base, args.id)
    dequeue(base, args.id, clear=True)
    fd = stop_turn(base, args.id)
    try:
        state = load(base, args.id)
        if state.get("worktree"):
            for cmd in (["worktree", "remove", "--force", "--force", state["worktree"]], ["branch", "-D", state["branch"]]):
                done = subprocess.run(["git", "-C", str(root), *cmd], capture_output=True, text=True)
                if done.returncode != 0 and "not a working tree" not in done.stderr and "not found" not in done.stderr:
                    sys.exit(f"could not close {args.id}: git {' '.join(cmd[:2])}: {done.stderr.strip()}")
        state.update(status="closed", pid=None, worktree=None)
        save(base, state)
    finally:
        os.close(fd)
    print(f"closed {args.id}; its transcript stays in {base / args.id}")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--color", action=argparse.BooleanOptionalAction, default=sys.stdout.isatty())
    sub = p.add_subparsers(dest="cmd", required=True)

    def talk(sp):
        sp.add_argument("message", nargs="*")
        sp.add_argument("--file", help="read the message from a file")
        sp.add_argument("--lead", help="name the sender (default: claude inside Claude Code)")
        sp.add_argument("--timeout", type=int, default=1800, help="seconds per turn (default 1800)")
        sp.add_argument("--detach", action="store_true", help="print the id and run the turn in the background")
        sp.add_argument("--attach", action="append", default=[], metavar="PATH",
                        help="a file, folder or image to send with the message (repeatable)")

    s = sub.add_parser("start", help="start a delegation and run its first turn")
    s.add_argument("harness")
    s.add_argument("--write", action="store_true", help="let it edit files, in a git worktree of its own")
    s.add_argument("--model")
    s.add_argument("--title")
    s.add_argument("--project", help="tag it with a project; the pane groups delegations by project")
    s.add_argument("--effort", help="reasoning effort, where the harness offers it (see `models`)")
    s.add_argument("--speed", help="fast, where the harness offers it")
    talk(s)
    s = sub.add_parser("send", help="run the next turn with a message")
    s.add_argument("id")
    s.add_argument("--as-user", action="store_true", help="the message is from the human, not the lead agent")
    talk(s)
    s = sub.add_parser("_turn")  # internal: the detached queue runner
    s.add_argument("id")
    s.add_argument("--timeout", type=int, required=True)
    s.add_argument("--lock-fd", type=int, required=True)
    sub.add_parser("list").add_argument("--all", action="store_true", help="include archived delegations")
    s = sub.add_parser("usage", help="tokens, time and turns per delegation and per harness")
    s.add_argument("--json", action="store_true")
    s.add_argument("--project", help="only this project's delegations")
    s = sub.add_parser("meta", help="archive, tag or mark a delegation seen")
    s.add_argument("id")
    s.add_argument("--archive", action="store_true")
    s.add_argument("--unarchive", action="store_true")
    s.add_argument("--project")
    s.add_argument("--no-project", action="store_true")
    s.add_argument("--seen", action="store_true", help="the person has seen its latest reply")
    s.add_argument("--name", help="what the chat is called in the pane")
    s = sub.add_parser("rename-project", help="rename a project tag on every chat that has it")
    s.add_argument("old")
    s.add_argument("new")
    sub.add_parser("delete", help="remove a delegation, its worktree and its transcript").add_argument("id")
    sub.add_parser("pick", help="open the system file dialog").add_argument("--folders", action="store_true")
    s = sub.add_parser("show")
    s.add_argument("id")
    s.add_argument("--follow", action="store_true")
    for name in ("stop", "diff", "close"):
        sub.add_parser(name).add_argument("id")
    s = sub.add_parser("models", help="list a harness's models")
    s.add_argument("harness")
    s.add_argument("--json", action="store_true")
    s = sub.add_parser("set", help="show or change a delegation's model, effort and speed")
    s.add_argument("id")
    s.add_argument("--model")
    s.add_argument("--effort")
    s.add_argument("--speed")

    args, extra = p.parse_known_args()  # a message may follow the flags: `start codex --write "fix it"`
    head, tail = (extra[: extra.index("--")], extra[extra.index("--") + 1:]) if "--" in extra else (extra, [])
    if extra and (not hasattr(args, "message") or any(x.startswith("-") for x in head)):
        p.error(f"unrecognized arguments: {' '.join(extra)}")
    if extra:
        args.message += head + tail
    handler = {"start": cmd_start, "send": cmd_send, "_turn": cmd_turn, "list": cmd_list, "show": cmd_show,
               "usage": cmd_usage,
               "stop": cmd_stop, "diff": cmd_diff, "close": cmd_close, "models": cmd_models,
               "set": cmd_set, "meta": cmd_meta,
               "rename-project": cmd_rename_project, "delete": cmd_delete, "pick": cmd_pick}[args.cmd]
    sys.exit(handler(args))


if __name__ == "__main__":
    main()
