"""bp find, and turning what the agent typed into one node id."""
import sys

from graph.load import Graph
from graph.walk import find

LIST_MAX = 40


def location(node: dict) -> str:
    if "start" in node:
        return f"{node['file']}:{node['start']}-{node['end']}"
    return node.get("file", "")


def print_hits(hits: list[dict], heading: str) -> None:
    print(f"{len(hits)} nodes match {heading}")
    for node in hits[:LIST_MAX]:
        print(f"  {node['type']:<10} {node['id']:<64} {location(node)}")
    if len(hits) > LIST_MAX:
        print(f"  ... {len(hits) - LIST_MAX} more: narrow the text or add --type")


def show_find(graph: Graph, text: str, node_type: str | None) -> None:
    print_hits(find(graph, text, node_type), repr(text) + (f" of type {node_type}" if node_type else ""))


def pick(graph: Graph, text: str) -> dict:
    """The node with this id, else the one node named it, else the one node whose id contains it;
    otherwise list the candidates and exit."""
    if text in graph.nodes:
        return graph.nodes[text]
    hits = find(graph, text)
    named = [h for h in hits if h["name"].lower() == text.lower()]
    if len(named) == 1 or len(hits) == 1:
        return (named or hits)[0]
    print_hits(hits, repr(text))
    sys.exit(0 if hits else 1)
