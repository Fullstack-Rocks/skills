"""Stage 12: links between systems. An edge rule whose target is `~<key>` (a client's
`~http:GET /orders/{}`) is linked here to every node that carries that key in its `keys`: the endpoint
that serves it, the OpenAPI operation that documents it, from any system. The core knows no protocol:
HTTP, events, sockets and RPC are all keys the project's rules give. A key nothing carries is a finding."""
import re

from graph import Graph
from stages.rules import ROUTE_PARAMETER, filters, transform

FIX = ("Nothing declares this key: the call targets an endpoint, topic or message that no longer exists, "
       "or the rule that gives the other side its keys is missing (teach it with the big-picture skill).")


LATE = re.compile(r"\{@(\w+)(?::(\w+))?((?:\|(?:\\\||[^|}])+)*)\}")


def property_value(values: list, name: str | None) -> str:
    """The first value of a file's property, or with a name, the {name, value} entry of that name
    (the prefix of the router a route is declared on, when a file has several)."""
    if name is None:
        first = (values or [""])[0]
        return str(first["value"] if isinstance(first, dict) else first)
    return next((str(v["value"]) for v in values if isinstance(v, dict) and v.get("name") == name), "")


def holders(graph: Graph, node: dict) -> list[dict]:
    """The nodes around this one, innermost first (a router built inside a factory function), then its
    file's own node: where a property it names is looked up."""
    file, line = node.get("file", ""), node.get("start", 0)
    around = sorted((n for n in graph.code_by_file.get(file, []) if n["id"] != node.get("id") and n["start"] <= line <= n["end"]),
                    key=lambda n: n["end"] - n["start"])
    return [*around, graph.nodes.get(graph.file_node.get(file, ""), {})]


def late(graph: Graph, text: str, node_id: str) -> str:
    """Fill {@file} with the node's file and {@<property>} or {@<property>:<name>} from that property on
    the innermost node around it that has it, else the file's own node (a router's prefix), then apply their filters."""
    node = graph.nodes.get(node_id, {})
    def fill(found: re.Match) -> str:
        found_in = (property_value(h.get(found[1], []), found[2]) for h in holders(graph, node))
        value = node.get("file", "") if found[1] == "file" else next((v for v in found_in if v), "")
        for name in filters(found[3]):
            value = transform(value, name)
        return value
    return LATE.sub(fill, text)


def canonical(key: str) -> str:
    """One spelling per key: in its path (from the first /) every parameter is {}, no trailing slash,
    no doubled slashes. The head (`http:shop:GET `, `topic:orders.created`) is kept as written."""
    head, slash, path = key.partition("/")
    return head + (re.sub(r"/+", "/", ROUTE_PARAMETER.sub("{}", slash + path)).rstrip("/") or slash)


def key_index(graph: Graph) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    for node in [n for n in graph.nodes.values() if n.get("keys")]:
        node["keys"] = [canonical(late(graph, key, node["id"])) for key in node["keys"]]
        for key in node["keys"]:
            index.setdefault(key, []).append(node["id"])
    return index


def add_contracts(graph: Graph) -> int:
    """Resolve every pending ~key edge; returns how many found no node."""
    index, unresolved = key_index(graph), 0
    for source, raw, kind, via, site in graph.pending:
        key = canonical(late(graph, raw, source))
        for target in index.get(key, []):
            graph.add_edge(source, target, kind, via, site=site)
        if key not in index:
            unresolved += 1
            graph.add_finding("unresolved-contract", source, *site, f"{kind} {key}: no node has this key", "big-picture")
            graph.findings[f"unresolved-contract:{source}"]["fix"] = FIX
    return unresolved
