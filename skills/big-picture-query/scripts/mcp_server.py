"""MCP server (stdio, JSON-RPC 2.0, one message per line) for hosts without a shell: every bp verb as a
tool. Each call runs bp.py itself, so tools and the command line give the same answers.

Register in Claude Code:  claude mcp add big-picture -- python3 <this file> --root <project folder>
"""
import sys

if sys.version_info < (3, 11):
    sys.exit(f"This script needs Python 3.11+ (this is {sys.version.split()[0]}).")

import argparse
import json
import subprocess
from pathlib import Path

BP = Path(__file__).resolve().parent / "bp.py"
PROTOCOL = "2025-06-18"
TARGET = {"target": {"type": "string", "description": "a node id, or a name or text that picks one (order_service.get_order)"}}
TOOLS = [
    ("bp_node", "A node: what it is, its entry points, every connection with file:line, its health and note.", TARGET, ["target"]),
    ("bp_neighbors", "Walk the graph from a node: downstream (out), upstream (in) or both.",
     TARGET | {"depth": {"type": "integer"}, "dir": {"type": "string", "enum": ["out", "in", "both"]},
               "kinds": {"type": "string", "description": "comma-separated edge kinds, e.g. calls,reads"}}, ["target"]),
    ("bp_find", "Find nodes whose id or module.name contains the text.",
     {"text": {"type": "string"}, "type": {"type": "string", "description": "endpoint, function, table, module, ..."}}, ["text"]),
    ("bp_health", "Every health finding on a part of the code and inside it, with where and how to fix it.", TARGET, ["target"]),
    ("bp_similar", "Operations a part of the code repeats, and every other place they run.", TARGET, ["target"]),
    ("bp_db", "Tables, views, keys, relations and JSON lookups.", {}, []),
    ("bp_endpoint", "An API operation: parameters, models, handler and everything it runs.", TARGET, ["target"]),
    ("bp_view", "A view the project defines (cache, config, ...), or the list of views.", {"id": {"type": "string"}}, []),
    ("bp_capsules", "Groups of modules that work together.", {}, []),
    ("bp_spec", "Write a fix spec for a part's health findings to .big-picture/specs/ and return its path.", TARGET, ["target"]),
]


def argv(tool: str, args: dict) -> list[str]:
    """The bp command line for a tool call."""
    match tool:
        case "bp_neighbors":
            extra = [f"--{key}={args[key]}" for key in ("depth", "dir", "kinds") if key in args]
            return ["neighbors", args["target"], *extra]
        case "bp_find":
            return ["find", args["text"], *(["--type", args["type"]] if args.get("type") else [])]
        case "bp_db" | "bp_capsules":
            return [tool.removeprefix("bp_")]
        case "bp_view":
            return ["view", *([args["id"]] if args.get("id") else [])]
        case _:
            return [tool.removeprefix("bp_"), args["target"]]


def call(tool: str, args: dict, root: Path) -> dict:
    result = subprocess.run([sys.executable, str(BP), *argv(tool, args)], cwd=root, capture_output=True, text=True, check=False)
    return {"content": [{"type": "text", "text": (result.stdout + result.stderr).strip()}], "isError": result.returncode != 0}


def answer(request: dict, root: Path) -> dict | None:
    """The JSON-RPC response to one request; None for notifications."""
    match request.get("method"):
        case "initialize":
            result = {"protocolVersion": PROTOCOL, "capabilities": {"tools": {}}, "serverInfo": {"name": "big-picture", "version": "1"}}
        case "tools/list":
            result = {"tools": [{"name": name, "description": text, "inputSchema": {"type": "object", "properties": props, "required": required}}
                                for name, text, props, required in TOOLS]}
        case "tools/call":
            result = call(request["params"]["name"], request["params"].get("arguments", {}), root)
        case "ping":
            result = {}
        case _:
            return None if "id" not in request else {"jsonrpc": "2.0", "id": request["id"], "error": {"code": -32601, "message": "unknown method"}}
    return {"jsonrpc": "2.0", "id": request["id"], "result": result}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=".", help="the project folder (the one holding .big-picture/)")
    root = Path(parser.parse_args().root).resolve()
    for line in sys.stdin:
        response = answer(json.loads(line), root) if line.strip() else None
        if response:
            print(json.dumps(response), flush=True)


if __name__ == "__main__":
    main()
