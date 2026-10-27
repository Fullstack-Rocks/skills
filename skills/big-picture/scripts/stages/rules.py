"""Stage 4: the project's own ast-grep rules in .big-picture/types, edges and properties.

A rule's `metadata` says what a match means (references/node-types.md):
  type rule:      node: endpoint, id: "{METHOD} {PATH}", link: handled-by, to: HANDLER
                  links: [{kind: maps-to, to: "table:{NAME|snake|plural}"}]   (only to nodes that exist)
  edge rule:      edge: reads, to: "table:{TABLE}"
  property rule:  property: fields, value: {name: "{FIELD}", type: "{TYPE}"}
`{NAME}` is the text of that capture, with string quotes stripped; `|lower`, `|snake` and `|plural`
transform it. Type rules run first, so edges and properties can land inside the nodes they make.
"""
import json
import re
import subprocess

from graph import Graph

PLACEHOLDER = re.compile(r"\{(\w+)((?:\|\w+)*)\}")


def transform(text: str, name: str) -> str:
    match name:
        case "lower":
            return text.lower()
        case "snake":
            return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()
        case "plural":
            return text[:-1] + "ies" if text.endswith("y") else text + ("es" if text.endswith("s") else "s")
    raise ValueError(f"unknown template filter |{name}")


def render(template: str, match: dict) -> str:
    def fill(placeholder: re.Match) -> str:
        text = match["metaVariables"]["single"][placeholder[1]]["text"].strip("\"'`")
        for name in filter(None, placeholder[2].split("|")):
            text = transform(text, name)
        return text
    return PLACEHOLDER.sub(fill, template)


def add_type_match(graph: Graph, match: dict, meta: dict, line: int) -> None:
    """A new node of the rule's type, linked to the function a capture names (its handler)."""
    node_type = meta["node"]
    node_id = graph.add_node(f"{node_type}:{render(meta['id'], match)}", node_type, render(meta["id"], match),
                             file=match["file"], start=line, end=match["range"]["end"]["line"] + 1)
    graph.add_edge(f"module:{match['file']}", node_id, "contains", match["ruleId"])
    if "link" in meta:
        target_line = match["metaVariables"]["single"][meta["to"]]["range"]["start"]["line"] + 1
        graph.add_edge(node_id, graph.enclosing(match["file"], target_line), meta["link"], match["ruleId"],
                       site=(match["file"], line))


def add_edge_match(graph: Graph, match: dict, meta: dict, line: int) -> None:
    """An edge from the code around the match to the node the rule names, created if new."""
    target = render(meta["to"], match)
    target_type, target_name = target.split(":", 1)
    graph.add_node(target, target_type, target_name)
    graph.add_edge(graph.enclosing(match["file"], line), target, meta["edge"], match["ruleId"],
                   site=(match["file"], line))


def add_property_match(graph: Graph, match: dict, meta: dict, line: int) -> None:
    """A value appended to a list property of the node around the match (a model's fields)."""
    value = {key: render(template, match) for key, template in meta["value"].items()}
    node = graph.nodes[graph.enclosing(match["file"], line)]
    node.setdefault(meta["property"], []).append(value)


def add_type_links(graph: Graph, match: dict, meta: dict) -> None:
    """Edges a type rule declares from its node, kept only when the target exists (model -> its table)."""
    node_id = f"{meta['node']}:{render(meta['id'], match)}"
    for link in meta.get("links", []):
        target = render(link["to"], match)
        if target in graph.nodes:
            graph.add_edge(node_id, target, link["kind"], match["ruleId"], site=(match["file"], match["range"]["start"]["line"] + 1))


def scan_rules(graph: Graph) -> list[tuple[dict, dict, int]]:
    """(match, its rule's metadata, 1-based line) for every project rule match; none without a config."""
    config = graph.root / ".big-picture" / "sgconfig.yml"
    if not config.exists():
        return []
    result = subprocess.run(["ast-grep", "scan", "-c", str(config), "--json=compact", "--include-metadata"],
                            cwd=graph.root, capture_output=True, text=True, check=False, stdin=subprocess.DEVNULL)
    return [(m, m.get("metadata") or {}, m["range"]["start"]["line"] + 1) for m in json.loads(result.stdout or "[]")]


def add_rule_matches(graph: Graph) -> int:
    """Run every project rule: nodes first, then edges and properties, then the nodes' own links."""
    matches = scan_rules(graph)
    nodes = [m for m in matches if "node" in m[1]]
    for match, meta, line in nodes:
        add_type_match(graph, match, meta, line)
    for match, meta, line in matches:
        if "edge" in meta:
            add_edge_match(graph, match, meta, line)
        elif "property" in meta:
            add_property_match(graph, match, meta, line)
    for match, meta, _ in nodes:
        add_type_links(graph, match, meta)
    return len(matches)
