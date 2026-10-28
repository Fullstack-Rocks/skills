"""Serve the big-picture viewer for a project, live: the page rechecks graph.json every 2 seconds and
reloads it after a rebuild. Python standard library only; listens on localhost.

Answers three things and 404s everything else:
  /             the viewer (viewer/dist/index.html)
  /graph.json   <root>/.big-picture/out/graph.json
  /src/<path>   a project file, only when the graph names it as a node's file, or a note in .big-picture/docs
  POST /proxy   the viewer's Try it: forwards one request to a localhost URL and returns the response

Usage: python3 serve.py [ROOT] [--port 7478]
"""
import sys

if sys.version_info < (3, 11):
    sys.exit(f"This script needs Python 3.11+ (this is {sys.version.split()[0]}). "
             "Rerun with python3.11+ or: uv run --no-project --python 3.12 -- python " + " ".join(sys.argv))

import argparse
import json
import subprocess
import time
import urllib.error
import urllib.request
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

VIEWER = Path(__file__).resolve().parent.parent / "viewer" / "dist" / "index.html"
BUILD = Path(__file__).resolve().parent / "build.py"


LOCAL_HOSTS = {"localhost", "127.0.0.1", "::1"}


def forward(call: dict) -> dict:
    """One HTTP request, timed; an error status comes back as a response, not an exception."""
    request = urllib.request.Request(call["url"], method=call["method"], headers=call.get("headers", {}),
                                     data=call["body"].encode() if call.get("body") else None)
    started = time.monotonic()
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status, headers, body = response.status, dict(response.headers), response.read()
    except urllib.error.HTTPError as error:
        status, headers, body = error.code, dict(error.headers), error.read()
    except (urllib.error.URLError, TimeoutError) as error:
        return {"status": 0, "headers": {}, "body": str(error), "ms": round((time.monotonic() - started) * 1000)}
    return {"status": status, "headers": headers, "body": body.decode(errors="replace"), "ms": round((time.monotonic() - started) * 1000)}


class Served:
    """The files the graph names, reread whenever graph.json changes."""

    def __init__(self, root: Path) -> None:
        self.root, self.graph = root, root / ".big-picture" / "out" / "graph.json"
        self.mtime, self.files = 0.0, set()

    def allowed(self, path: str) -> bool:
        mtime = self.graph.stat().st_mtime
        if mtime != self.mtime:
            nodes = json.loads(self.graph.read_text())["nodes"]
            self.mtime, self.files = mtime, {n["file"] for n in nodes if n.get("file")}
        return path in self.files


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args: object, served: Served, **kwargs: object) -> None:
        self.served = served
        super().__init__(*args, **kwargs)

    def translate_path(self, path: str) -> str:
        """Map the three routes to files; anything else maps to a path that doesn't exist."""
        route = unquote(urlparse(path).path)
        if route in ("/", "/index.html"):
            return str(VIEWER)
        if route == "/graph.json":
            return str(self.served.graph)
        source = route.removeprefix("/src/")
        note = source.startswith(".big-picture/docs/") and source.endswith(".md") and ".." not in source
        if route.startswith("/src/") and (note or self.served.allowed(source)):
            return str(self.served.root / source)
        return str(self.served.root / ".big-picture" / "out" / "not-served")

    def do_GET(self) -> None:
        """A note not written yet is an empty answer, not an error: the pane asks for it every few seconds."""
        source = unquote(urlparse(self.path).path).removeprefix("/src/")
        if source.startswith(".big-picture/docs/") and ".." not in source and not (self.served.root / source).exists():
            self.send_response(204)
            self.end_headers()
            return
        super().do_GET()

    def do_POST(self) -> None:
        """Try it: {method, url, headers, body} -> {status, headers, body, ms}, for localhost URLs only."""
        if urlparse(self.path).path != "/proxy":
            self.send_error(404)
            return
        call = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        if urlparse(call["url"]).hostname not in LOCAL_HOSTS:
            self.send_error(403, "Try it only calls localhost")
            return
        self.send_json(forward(call))

    def send_json(self, data: dict) -> None:
        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, format: str, *args: object) -> None:
        pass  # the page polls every 2 s; logging each request would bury real output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--port", type=int, default=7478)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    served = Served(root)
    if not served.graph.exists():
        subprocess.run([sys.executable, str(BUILD), str(root)], check=True)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(Handler, served=served))
    print(f"big-picture: http://localhost:{args.port}  (Ctrl+C stops it; rebuild with build.py and the page follows)")
    server.serve_forever()


if __name__ == "__main__":
    main()
