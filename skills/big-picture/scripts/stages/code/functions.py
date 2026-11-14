"""Stage 2: function nodes from lizard (any language it parses), named from SCIP definitions when an
index has one at the same line, so methods read Database.fetch_one rather than fetch_one."""
import csv
import io
import subprocess
from pathlib import Path

from graph import Graph
from stages.code.scip_index import Occurrence

LIZARD_BATCH = 400  # files per lizard run, to stay under the command-line length limit


def lizard_rows(root: Path, files: list[str]) -> list[list[str]]:
    rows = []
    for i in range(0, len(files), LIZARD_BATCH):
        result = subprocess.run(["lizard", "--csv", *files[i:i + LIZARD_BATCH]], cwd=root,
                                capture_output=True, text=True, check=False)
        rows += [r for r in csv.reader(io.StringIO(result.stdout)) if len(r) >= 11]
    return rows


def qualified_name(symbol: str) -> str | None:
    """`... app.http`/Request#json(). -> Request.json, and a term `.../sdk.gen.ts`/getUser. -> getUser
    (a const holding an arrow function); None for locals and anything else."""
    if symbol.startswith("local ") or not symbol.endswith("."):
        return None
    descriptors = symbol.split(" ", 4)[-1].rsplit("/", 1)[-1]
    return descriptors.replace("().", ".").replace("#", ".").rstrip(".")


def definition_names(index: dict[str, list[Occurrence]]) -> dict[tuple[str, int], tuple[str, str]]:
    """(file, line) -> (qualified name, symbol) for every function a SCIP index defines."""
    names = {}
    for path, occurrences in index.items():
        for occ in occurrences:
            name = qualified_name(occ.symbol) if occ.is_definition else None
            # parameters look like f().(x); a method beats a term defined on the same line
            if name and "(" not in name and ((path, occ.line) not in names or occ.symbol.endswith(").")):
                names[(path, occ.line)] = (name, occ.symbol)
    return names


def add_functions(graph: Graph, files: list[str], index: dict[str, list[Occurrence]]) -> dict[str, str]:
    """Add one node per function; returns SCIP symbol -> node id for the calls stage."""
    names = definition_names(index)
    by_symbol = {}
    for row in lizard_rows(graph.root, files):
        path, short_name, start, end = row[6], row[7], int(row[9]), int(row[10])
        name, symbol = names.get((path, start), (short_name, None))
        node_id = f"fn:{path}#{name}"
        if node_id in graph.nodes:  # same name twice in a file (overloads, nested helpers)
            node_id = f"{node_id}@{start}"
        graph.add_node(node_id, "function", name, file=path, start=start, end=end,
                       signature=row[8], complexity=int(row[1]), lines=int(row[0]))
        graph.add_edge(f"module:{path}", node_id, "contains", "lizard")
        if symbol:
            by_symbol[symbol] = node_id
    return by_symbol
