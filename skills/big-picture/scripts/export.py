"""Export the viewer and a project's graph as one HTML file that opens from disk, for sharing.

The file is a snapshot: it doesn't follow rebuilds, and it shows no source code (serve.py does).

Usage: python3 export.py [ROOT] [--out FILE]      (default: <root>/.big-picture/out/big-picture.html)
"""
import sys

if sys.version_info < (3, 11):
    sys.exit(f"This script needs Python 3.11+ (this is {sys.version.split()[0]}). "
             "Rerun with python3.11+ or: uv run --no-project --python 3.12 -- python " + " ".join(sys.argv))

import argparse
from pathlib import Path

VIEWER = Path(__file__).resolve().parent.parent / "viewer" / "dist" / "index.html"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--out")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    graph = root / ".big-picture" / "out" / "graph.json"
    if not graph.exists():
        sys.exit(f"no graph at {graph}: run build.py first")
    data = graph.read_text().replace("</", "<\\/")  # keep the JSON from closing the script tag
    page = VIEWER.read_text().replace("<head>", f"<head><script>window.__BP_GRAPH__ = {data};</script>", 1)
    out = Path(args.out) if args.out else graph.parent / "big-picture.html"
    out.write_text(page)
    print(f"big-picture: {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
