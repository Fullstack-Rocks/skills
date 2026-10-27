"""Serve the big-picture viewer for a project, live: the page rechecks graph.json every 2 seconds and
reloads it after a rebuild. Python standard library only; listens on localhost.

Answers three things and 404s everything else:
  /             the viewer (viewer/dist/index.html)
  /graph.json   <root>/.big-picture/out/graph.json
  /src/<path>   a project file, only when the graph names it as a node's file

Usage: python3 serve.py [ROOT] [--port 7478]
"""
import sys

if sys.version_info < (3, 11):
    sys.exit(f"This script needs Python 3.11+ (this is {sys.version.split()[0]}). "
             "Rerun with python3.11+ or: uv run --no-project --python 3.12 -- python " + " ".join(sys.argv))

import argparse
import json
import subprocess
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

VIEWER = Path(__file__).resolve().parent.parent / "viewer" / "dist" / "index.html"
BUILD = Path(__file__).resolve().parent / "build.py"


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
        if route.startswith("/src/") and self.served.allowed(source):
            return str(self.served.root / source)
        return str(self.served.root / ".big-picture" / "out" / "not-served")

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
