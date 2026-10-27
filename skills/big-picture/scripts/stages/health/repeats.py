"""Stage 8: code that does the same thing in several places, found from the operations the project's
edge rules match. An operation is (rule, target, call): db-reads on table:orders through fetch_one.
- the same operation from two or more functions is a repeated operation, a health finding on each;
- the same rule and call on three or more targets is a repeated shape (8 services each reading their
  own table the same way), recorded as information, not counted as health.
Matching is on what the code does, never on its text, so `if (x)` everywhere never counts."""
import re

from graph import Graph

CALL = re.compile(r"(\w+)\s*\(")
SHAPE_MIN = 3
FIX = ("Put this operation in one function next to its data (e.g. {name}_by_id()) and call it from "
       "every place listed, so a change to how it runs happens once.")


def operations(graph: Graph, matches: list[tuple[dict, dict, int]]) -> dict[tuple[str, str, str], list[list]]:
    """(rule, target, call) -> [file, line, node id] for every edge-rule match."""
    found: dict[tuple[str, str, str], list[list]] = {}
    for match, meta, line in matches:
        if "edge" not in meta:
            continue
        call = CALL.search(match["text"])
        key = (match["ruleId"], meta["to"], call[1] if call else "")
        found.setdefault(key, []).append([match["file"], line, graph.enclosing(match["file"], line)])
    return found


def add_repeated_operations(graph: Graph, ops: dict[tuple[str, str, str], list[list]]) -> None:
    """The same operation from two or more functions: a finding on each, naming the others."""
    for (rule, target, call), sites in ops.items():
        nodes = sorted({site[2] for site in sites})
        if len(nodes) < 2:
            continue
        graph.repeats.append({"kind": "operation", "key": f"{call} {rule} {target}", "sites": sites})
        for node in nodes:
            others = ", ".join(n for n in nodes if n != node)
            graph.add_finding("repeated-operation", node, *next(s[:2] for s in sites if s[2] == node),
                              f"{call} on {target} ({rule}) also runs in {others}", "big-picture")
            graph.findings[f"repeated-operation:{node}"]["fix"] = FIX.format(name=target.split(":")[-1])


def add_repeated_shapes(graph: Graph, ops: dict[tuple[str, str, str], list[list]]) -> None:
    """The same rule and call on SHAPE_MIN or more targets: recorded as information, not health."""
    shapes: dict[tuple[str, str], tuple[set, list]] = {}
    for (rule, target, call), sites in ops.items():
        targets, all_sites = shapes.setdefault((rule, call), (set(), []))
        targets.add(target)
        all_sites.extend(sites)
    for (rule, call), (targets, sites) in shapes.items():
        if len(targets) >= SHAPE_MIN:
            graph.repeats.append({"kind": "shape", "key": f"{call} {rule} on {len(targets)} targets", "sites": sites})


def add_repeats(graph: Graph, matches: list[tuple[dict, dict, int]]) -> None:
    ops = operations(graph, matches)
    add_repeated_operations(graph, ops)
    add_repeated_shapes(graph, ops)
