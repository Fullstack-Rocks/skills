"""Stage 12: links between systems. An edge rule whose target is `~<key>` (a client's
`~http:GET /orders/{}`) is linked here to every node that carries that key in its `keys`: the endpoint
that serves it, the OpenAPI operation that documents it, from any system. The core knows no protocol:
HTTP, events, sockets and RPC are all keys the project's rules give. A key nothing carries is a finding."""
from graph import Graph

FIX = ("Nothing declares this key: the call targets an endpoint, topic or message that no longer exists, "
       "or the rule that gives the other side its keys is missing (teach it with the big-picture skill).")


def key_index(graph: Graph) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    for node in graph.nodes.values():
        for key in node.get("keys", []):
            index.setdefault(key, []).append(node["id"])
    return index


def add_contracts(graph: Graph) -> int:
    """Resolve every pending ~key edge; returns how many found no node."""
    index, unresolved = key_index(graph), 0
    for source, key, kind, via, site in graph.pending:
        for target in index.get(key, []):
            graph.add_edge(source, target, kind, via, site=site)
        if key not in index:
            unresolved += 1
            graph.add_finding("unresolved-contract", source, *site, f"{kind} {key}: no node has this key", "big-picture")
            graph.findings[f"unresolved-contract:{source}"]["fix"] = FIX
    return unresolved
