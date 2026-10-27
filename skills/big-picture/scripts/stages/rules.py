"""Stage 4: the project's own ast-grep rules in .big-picture/types, edges and properties.

A rule's `metadata` says what a match means (references/node-types.md):
  type rule:      node: endpoint, id: "{METHOD} {PATH}", link: handled-by, to: HANDLER
                  links: [{kind: maps-to, to: "table:{NAME|snake|plural}"}]   (only to nodes that exist)
  edge rule:      edge: reads, to: "table:{TABLE}"
  property rule:  property: fields, value: {name: "{FIELD}", type: "{TYPE}"}
  lookup rule:    lookup: {table: ..., column: ..., path: ..., to_table: ..., to_column: ...}
`{NAME}` is the text of that capture, with string quotes stripped; `|lower`, `|snake` and `|plural`
transform it. Type rules run first, so edges and properties can land inside the nodes they make.
"""
import json
import re
import subprocess

from graph import Graph
from stages.data.lookups import add_lookup

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


def render_meta(value: object, captures: dict) -> object:
    """Every template in a rule's metadata filled from one match's captures (strings, lists, dicts)."""
    if isinstance(value, dict):
        return {key: render_meta(item, captures) for key, item in value.items()}
    if isinstance(value, list):
        return [render_meta(item, captures) for item in value]
    if not isinstance(value, str):
        return value
    rendered, end = "", 0
    for placeholder in PLACEHOLDER.finditer(value):
        text = captures[placeholder[1]]["text"].strip("\"'`")
        for name in filter(None, placeholder[2].split("|")):
            text = transform(text, name)
        rendered, end = rendered + value[end:placeholder.start()] + text, placeholder.end()
    return rendered + value[end:]


def add_type_match(graph: Graph, match: dict, meta: dict, line: int) -> None:
    """A new node of the rule's type, linked to the function a capture names (its handler)."""
    node_id = graph.add_node(f"{meta['node']}:{meta['id']}", meta["node"], meta["id"],
                             file=match["file"], start=line, end=match["range"]["end"]["line"] + 1)
    if match["file"] in graph.file_node:  # the file's own node holds it: a module, or infra, config, ...
        graph.add_edge(graph.file_node[match["file"]], node_id, "contains", match["ruleId"])
    if "link" in meta:
        target_line = match["metaVariables"]["single"][meta["to"]]["range"]["start"]["line"] + 1
        graph.add_edge(node_id, graph.enclosing(match["file"], target_line), meta["link"], match["ruleId"],
                       site=(match["file"], line))


def add_edge_match(graph: Graph, match: dict, meta: dict, line: int) -> None:
    """An edge from the code around the match to the node the rule names, created if new."""
    target_type, target_name = meta["to"].split(":", 1)
    graph.add_node(meta["to"], target_type, target_name)
    graph.add_edge(graph.enclosing(match["file"], line), meta["to"], meta["edge"], match["ruleId"],
                   site=(match["file"], line))


def add_property_match(graph: Graph, match: dict, meta: dict, line: int) -> None:
    """A value appended to a list property of the node around the match (a model's fields)."""
    graph.nodes[graph.enclosing(match["file"], line)].setdefault(meta["property"], []).append(meta["value"])


def add_type_links(graph: Graph, match: dict, meta: dict) -> None:
    """Edges a type rule declares from its node, kept only when the target exists (model -> its table)."""
    for link in meta.get("links", []):
        if link["to"] in graph.nodes:
            graph.add_edge(f"{meta['node']}:{meta['id']}", link["to"], link["kind"], match["ruleId"],
                           site=(match["file"], match["range"]["start"]["line"] + 1))


def scan_rules(graph: Graph) -> list[dict]:
    """Every project rule match, with its rule's metadata; none when the project has no rules."""
    config = graph.root / ".big-picture" / "sgconfig.yml"
    if not config.exists():
        return []
    result = subprocess.run(["ast-grep", "scan", "-c", str(config), "--json=compact", "--include-metadata"],
                            cwd=graph.root, capture_output=True, text=True, check=False, stdin=subprocess.DEVNULL)
    return json.loads(result.stdout or "[]")


def add_rule_matches(graph: Graph, pattern_matches: list[dict]) -> list[tuple[dict, dict, int]]:
    """Run every project rule, ast-grep's and the pattern rules' (patterns.py): nodes first, then edges,
    properties and lookups, then the nodes' own links. Returns the matches, for the repeated-operation stage."""
    matches = [(m, render_meta(m.get("metadata", {}), m["metaVariables"]["single"]), m["range"]["start"]["line"] + 1)
               for m in [*scan_rules(graph), *pattern_matches]]
    kind = {key: [m for m in matches if key in m[1]] for key in ("node", "edge", "property", "lookup")}
    for match, meta, line in kind["node"]:
        add_type_match(graph, match, meta, line)
    for match, meta, line in kind["edge"]:
        add_edge_match(graph, match, meta, line)
    for match, meta, line in kind["property"]:
        add_property_match(graph, match, meta, line)
    for match, meta, line in kind["lookup"]:
        add_lookup(graph, meta["lookup"], (match["file"], line), match["ruleId"])
    for match, meta, _ in kind["node"]:
        add_type_links(graph, match, meta)
    return matches
