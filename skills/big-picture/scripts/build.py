"""Build the big-picture graph of a project into <root>/.big-picture/out/graph.json.

Every node and edge comes from a parser: lizard (functions), SCIP indexers (calls), ast-grep (the
project's rules in .big-picture/), SQL DDL and JSON lookups in SQL, and the call-depth and
code-standards skills (health).
A full rebuild every run.

Usage: python3 build.py [ROOT]      (default: the current directory)
"""
import sys

if sys.version_info < (3, 11):
    sys.exit(f"This script needs Python 3.11+ (this is {sys.version.split()[0]}). "
             "Rerun with python3.11+ or: uv run --no-project --python 3.12 -- python " + " ".join(sys.argv))

import argparse
import shutil
import time
from pathlib import Path, PurePosixPath

from graph import Graph
from stages.code.calls import PYTHON, TYPESCRIPT, add_approx_calls, add_scip_calls, scip_indexes
from stages.code.functions import add_functions
from stages.code.scip_index import read_index
from stages.data.lookups import add_lookups
from stages.data.openapi import add_openapi
from stages.data.schema import add_schema, generated_schema
from stages.health.findings import add_fixes, add_health
from stages.health.repeats import add_repeats
from stages.files import load_data
from stages.inventory import add_inventory, code_files, list_files
from stages.patterns import scan_patterns
from stages.rules import add_rule_matches
from stages.knowledge.capsules import add_capsules
from stages.knowledge.contracts import add_contracts
from stages.knowledge.docs import add_docs
from stages.knowledge.systems import add_systems
from stages.knowledge.views import add_views

REQUIRED = ["ast-grep", "lizard"]


def prepare_out(big_picture: Path) -> Path:
    """Create out/ and keep it out of git without touching the project's own .gitignore."""
    (big_picture / "out").mkdir(parents=True, exist_ok=True)
    ignore = big_picture / ".gitignore"
    if not ignore.exists():
        ignore.write_text("out/\n")
    return big_picture / "out"


def top_level(paths: list[str]) -> list[str]:
    """The top folders (or root files) holding these paths, for tools that take folders."""
    return sorted({PurePosixPath(p).parts[0] for p in paths})


def note_coverage(graph: Graph, code: list[str], indexed: set[str]) -> list[str]:
    """Record which call source each language used; returns the files left for the fallback."""
    for language, suffixes in (("python", PYTHON), ("typescript", TYPESCRIPT)):
        files = [f for f in code if PurePosixPath(f).suffix in suffixes]
        if files:
            graph.coverage[language] = "scip" if any(f in indexed for f in files) else "approx"
    return [f for f in code if f not in indexed]


def project_config(root: Path) -> dict:
    """.big-picture/config.yml: `include` (the project's folders; none means the whole root) and
    `schema_commands` (commands printing SQL DDL, for schemas held in ORM code)."""
    path = root / ".big-picture" / "config.yml"
    return (load_data(path) if path.exists() else None) or {}


def included(config: dict) -> list[str]:
    return [folder.strip("/") for folder in config.get("include", [])]


def read_indexes(root: Path, out: Path, code: list[str], files: list[str], include: list[str]) -> dict:
    """Occurrences by root-relative path from every SCIP index, for listed code only (an index can
    reach into node_modules typings)."""
    index, listed = {}, set(code)
    for folder, scip_file in scip_indexes(root, out, code, files, include):
        documents = {(path if folder == "." else f"{folder}/{path}"): occurrences for path, occurrences in read_index(scip_file).items()}
        index |= {path: occurrences for path, occurrences in documents.items() if path in listed}
    return index


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", default=".")
    root = Path(parser.parse_args().root).resolve()
    missing = [t for t in REQUIRED if not shutil.which(t)]
    if missing:
        sys.exit(f"missing {', '.join(missing)}: run call-depth's scripts/install_tools.py {' '.join(missing)}")
    started, out = time.monotonic(), prepare_out(root / ".big-picture")
    graph = Graph(root)
    config = project_config(root)
    include = included(config)
    files = list_files(root, include)
    code = code_files(files)
    add_inventory(graph, files)
    index = read_indexes(root, out, code, files, include)
    by_symbol = add_functions(graph, code, index)
    add_scip_calls(graph, index, by_symbol)
    unindexed = note_coverage(graph, code, set(index))
    ambiguous = add_approx_calls(graph, unindexed) if unindexed else 0
    matches = add_rule_matches(graph, include, scan_patterns(root, files))
    add_schema(graph, files + generated_schema(graph, config.get("schema_commands", []), Path(__file__).parent))
    lookups = add_lookups(graph, files, code)
    operations = add_openapi(graph, files)
    unresolved = add_contracts(graph)
    systems = add_systems(graph, files)
    add_repeats(graph, matches)
    add_health(graph, top_level(code), out)
    add_fixes(graph)
    add_views(graph)
    capsules = add_capsules(graph)
    docs = add_docs(graph)
    graph.write(out / "graph.json")
    coverage = ", ".join(f"{lang} {source}" for lang, source in graph.coverage.items())
    print(f"big-picture: {len(graph.nodes)} nodes, {len(graph.edges)} edges, {len(graph.findings)} findings, "
          f"{len(matches)} rule matches, {lookups} JSON lookup sites, {operations} API operations, {len(graph.repeats)} repeats, "
          f"{capsules} capsules, {docs} node docs, {systems} systems, {unresolved} unresolved contracts, "
          f"calls: {coverage or 'none'}, {ambiguous} ambiguous call sites, "
          f"{time.monotonic() - started:.1f}s -> {out / 'graph.json'}")


if __name__ == "__main__":
    main()
