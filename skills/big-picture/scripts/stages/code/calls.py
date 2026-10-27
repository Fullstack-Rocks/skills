"""Stage 3: calls edges. A SCIP index gives exact edges for the languages it covers; the other code
files fall back to ast-grep call sites resolved by name and module, marked approx."""
import json
import shutil
import subprocess
from pathlib import Path, PurePosixPath

from graph import Graph
from stages.code.scip_index import Occurrence

PACKS = Path(__file__).resolve().parents[3] / "packs"
PYTHON = {".py", ".pyi"}
TYPESCRIPT = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"}


def run_indexer(root: Path, out: Path, language: str) -> Path | None:
    """Index root with the language's SCIP indexer; None when it is missing or fails."""
    index = out / f"{language}.scip"
    if language == "python":
        command = ["scip-python", "index", "--project-name", root.name, "--output", str(index), "--quiet"]
    else:
        command = ["scip-typescript", "index", "--output", str(index)]
    if not shutil.which(command[0]):
        print(f"calls: {command[0]} not installed, {language} calls are approx (python3 scripts/install_tools.py)")
        return None
    result = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    if result.returncode != 0 or not index.exists():
        print(f"calls: {command[0]} failed, {language} calls are approx\n{result.stderr.strip()[-600:]}")
        return None
    return index


def scip_indexes(root: Path, out: Path, code: list[str]) -> list[Path]:
    """Index files from every SCIP indexer the project's languages need and that ran."""
    suffixes = {PurePosixPath(f).suffix for f in code}
    indexes = []
    if suffixes & PYTHON:
        indexes.append(run_indexer(root, out, "python"))
    if suffixes & TYPESCRIPT and (root / "tsconfig.json").exists():
        indexes.append(run_indexer(root, out, "typescript"))
    return [i for i in indexes if i]


def add_scip_calls(graph: Graph, index: dict[str, list[Occurrence]], by_symbol: dict[str, str]) -> None:
    """A reference to a project function inside another function is a calls edge."""
    for path, occurrences in index.items():
        for occ in occurrences:
            target = by_symbol.get(occ.symbol)
            if occ.is_definition or target is None:
                continue
            caller = graph.enclosing(path, occ.line)
            if caller.startswith("fn:") and caller != target:
                graph.add_edge(caller, target, "calls", "scip", "exact", (path, occ.line))


def call_sites(root: Path, files: list[str]) -> list[dict]:
    """ast-grep matches of the packs' call rules: callee text, file and 1-based line."""
    sites = []
    for rule in sorted(PACKS.glob("*/calls*.yml")):
        result = subprocess.run(["ast-grep", "scan", "--rule", str(rule), "--json=compact", *files],
                                cwd=root, capture_output=True, text=True, check=False, stdin=subprocess.DEVNULL)
        for match in json.loads(result.stdout or "[]"):
            callee = match["metaVariables"]["single"]["CALLEE"]["text"]
            sites.append({"callee": callee, "file": match["file"], "line": match["range"]["start"]["line"] + 1})
    return sites


def language(file: str) -> str:
    """Files that can call each other by name: Python with Python, the JS family together."""
    suffix = PurePosixPath(file).suffix
    return "python" if suffix in PYTHON else "javascript" if suffix in TYPESCRIPT else suffix


def resolve(callee: str, by_name: dict[str, list[dict]]) -> dict | None:
    """order_service.get_order -> the one get_order, or the one in order_service.*; None if unsure.
    by_name holds only functions in the caller's language."""
    parts = callee.split(".")
    candidates = by_name.get(parts[-1], [])
    if len(candidates) > 1 and len(parts) > 1:
        candidates = [c for c in candidates if parts[-2] in (PurePosixPath(c["file"]).stem, c["name"].split(".")[0])]
    return candidates[0] if len(candidates) == 1 else None


def add_approx_calls(graph: Graph, files: list[str]) -> int:
    """Calls edges for files no index covered; returns how many call sites matched more than one
    project function and stayed unresolved (calls into libraries aren't counted)."""
    by_language: dict[str, dict[str, list[dict]]] = {}
    for node in [n for n in graph.nodes.values() if n["type"] == "function"]:
        by_language.setdefault(language(node["file"]), {}).setdefault(node["name"].split(".")[-1], []).append(node)
    unresolved = 0
    for site in call_sites(graph.root, files):
        by_name = by_language.get(language(site["file"]), {})
        target = resolve(site["callee"], by_name)
        caller = graph.enclosing(site["file"], site["line"])
        if target is None:
            unresolved += site["callee"].split(".")[-1] in by_name
        elif caller.startswith("fn:") and caller != target["id"]:
            graph.add_edge(caller, target["id"], "calls", "ast-grep", "approx", (site["file"], site["line"]))
    return unresolved
