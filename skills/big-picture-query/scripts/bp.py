"""bp: answer questions about a codebase from its big-picture graph (.big-picture/out/graph.json).

  bp node <id or text>                       the node, its entry points, every edge, its health findings
  bp neighbors <id or text> [--depth 2] [--dir out|in|both] [--kinds calls,reads]
  bp find <text> [--type endpoint]           nodes whose id contains the text

Edges marked ~ were matched by name (approx), not by a type-aware index.
Run from anywhere inside the project; the nearest .big-picture/ above the current folder is used.
"""
import sys

if sys.version_info < (3, 11):
    sys.exit(f"This script needs Python 3.11+ (this is {sys.version.split()[0]}). "
             "Rerun with python3.11+ or: uv run --no-project --python 3.12 -- python " + " ".join(sys.argv))

import argparse
from pathlib import Path

from graph.load import load
from graph.walk import entry_points
from verbs.find import pick, show_find
from verbs.node import show_neighbors, show_node


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="bp", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    verbs = parser.add_subparsers(dest="verb", required=True)
    verbs.add_parser("node").add_argument("target")
    walk = verbs.add_parser("neighbors")
    walk.add_argument("target")
    walk.add_argument("--depth", type=int, default=2)
    walk.add_argument("--dir", choices=["out", "in", "both"], default="both")
    walk.add_argument("--kinds", help="comma-separated edge kinds, e.g. calls,reads")
    search = verbs.add_parser("find")
    search.add_argument("text")
    search.add_argument("--type")
    return parser.parse_args()


def main() -> None:
    args = parse()
    graph = load(Path.cwd())
    match args.verb:
        case "node":
            node = pick(graph, args.target)
            show_node(graph, node, entry_points(graph, node["id"]))
        case "neighbors":
            kinds = set(args.kinds.split(",")) if args.kinds else None
            show_neighbors(graph, pick(graph, args.target), args.depth, args.dir, kinds)
        case "find":
            show_find(graph, args.text, args.type)


if __name__ == "__main__":
    main()
