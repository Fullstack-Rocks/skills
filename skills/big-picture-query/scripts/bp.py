"""bp: answer questions about a codebase from its big-picture graph (.big-picture/out/graph.json).

  bp node <id or text>                       the node, its entry points, every edge, its health findings
  bp neighbors <id or text> [--depth 2] [--dir out|in|both] [--kinds calls,reads]
  bp find <text> [--type endpoint]           nodes whose id contains the text
  bp health <id or text>                     every finding on it and inside it, with where and how to fix
  bp similar <id or text>                    operations it repeats, and every other place they run
  bp db                                      tables, views, keys, relations and JSON lookups
  bp endpoint "<METHOD> <path>"              an API operation: parameters, models, handler, what it runs
  bp view [<id>]                             a view the project defines (cache, config, ...), or the list of them
  bp capsules                                groups of modules that work together
  bp spec <id or text> [--findings a,b]      write a fix spec for its health findings to .big-picture/specs/

Edges marked ~ were matched by name (approx), not by a type-aware index.
Run from anywhere inside the project; the nearest .big-picture/ above the current folder is used.
"""
import sys

if sys.version_info < (3, 11):
    sys.exit(f"This script needs Python 3.11+ (this is {sys.version.split()[0]}). "
             "Rerun with python3.11+ or: uv run --no-project --python 3.12 -- python " + " ".join(sys.argv))

import argparse
from pathlib import Path

from graph.load import Graph, load
from graph.walk import entry_points
from verbs.api import show_endpoint
from verbs.data import show_capsules, show_db, show_view
from verbs.find import pick, show_find
from verbs.health import show_health, show_similar
from verbs.node import show_neighbors, show_node
from verbs.spec import chosen_findings, write_spec


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="bp", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    verbs = parser.add_subparsers(dest="verb", required=True)
    verbs.add_parser("node").add_argument("target")
    walk = verbs.add_parser("neighbors")
    walk.add_argument("target")
    walk.add_argument("--depth", type=int, default=2)
    walk.add_argument("--dir", choices=["out", "in", "both"], default="both")
    walk.add_argument("--kinds", type=lambda value: set(value.split(",")), help="comma-separated edge kinds, e.g. calls,reads")
    search = verbs.add_parser("find")
    search.add_argument("text")
    search.add_argument("--type")
    verbs.add_parser("health").add_argument("target", nargs="?", default="folder:.")
    verbs.add_parser("similar").add_argument("target", nargs="?", default="folder:.")
    verbs.add_parser("db")
    verbs.add_parser("endpoint").add_argument("target")
    verbs.add_parser("view").add_argument("id", nargs="?")
    verbs.add_parser("capsules")
    spec = verbs.add_parser("spec")
    spec.add_argument("target")
    spec.add_argument("--findings", type=lambda value: value.split(","), help="comma-separated finding ids; default: every finding on it and inside it")
    return parser.parse_args()


def show_listing(graph: Graph, args: argparse.Namespace) -> None:
    """The verbs that list the whole project rather than one node."""
    match args.verb:
        case "find":
            show_find(graph, args.text, args.type)
        case "db":
            show_db(graph)
        case "view":
            show_view(graph, args.id)
        case "capsules":
            show_capsules(graph)


def main() -> None:
    args = parse()
    graph = load(Path.cwd())
    if args.verb in ("find", "db", "view", "capsules"):
        show_listing(graph, args)
        return
    node = pick(graph, args.target)
    match args.verb:
        case "node":
            show_node(graph, node, entry_points(graph, node["id"]))
        case "neighbors":
            show_neighbors(graph, node, args.depth, args.dir, args.kinds)
        case "health":
            show_health(graph, node)
        case "similar":
            show_similar(graph, node)
        case "endpoint":
            show_endpoint(graph, node)
        case "spec":
            findings = chosen_findings(graph, node, args.findings)
            write_spec(graph, node, findings, sorted({e for f in findings for e in entry_points(graph, f["node"])}), graph.root)


if __name__ == "__main__":
    main()
