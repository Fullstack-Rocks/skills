"""Stage 3: calls edges. A SCIP index gives exact edges for the languages it covers; the other code
files fall back to ast-grep call sites resolved by name and module, marked approx."""
import json
import os
import shutil
import subprocess
import tomllib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path, PurePosixPath

from graph import Graph
from stages.code.scip_index import Occurrence

PACKS = Path(__file__).resolve().parents[3] / "packs"
PYTHON = {".py", ".pyi"}
TYPESCRIPT = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"}


def project_dirs(code: list[str], marker_names: set[str], files: list[str]) -> list[str]:
    """Folders holding one of the marker files (pyproject.toml, tsconfig.json) and code; innermost only."""
    marked = sorted({str(PurePosixPath(f).parent) for f in files if PurePosixPath(f).name in marker_names})
    with_code = [d for d in marked if any(c.startswith(d + "/") or d == "." for c in code)]
    return [d for d in with_code if not any(o != d and o.startswith(d + "/") for o in with_code)]


def python_project(root: Path, folder: str, out: Path) -> tuple[str, Path | None]:
    """scip-python for one project folder, named and versioned from its pyproject so other projects'
    references to it match; inside the project's own .venv when it has one."""
    where = root / folder
    meta = tomllib.loads((where / "pyproject.toml").read_text()) if (where / "pyproject.toml").exists() else {}
    project = meta.get("project") or meta.get("tool", {}).get("poetry", {})
    index = out / f"python-{folder.replace('/', '_')}.scip"
    command = ["scip-python", "index", "--project-name", project.get("name", where.name), "--output", str(index), "--quiet"]
    if project.get("version"):
        command += ["--project-version", project["version"]]
    venv = where / ".venv"
    env = {**os.environ, "VIRTUAL_ENV": str(venv), "PATH": f"{venv / 'bin'}:{os.environ['PATH']}"} if venv.is_dir() else None
    result = subprocess.run(command, cwd=where, env=env, capture_output=True, text=True, check=False)
    return folder, index if result.returncode == 0 and index.exists() else None


def typescript_projects(root: Path, group: str, projects: list[str], out: Path) -> tuple[str, Path | None]:
    """One scip-typescript run over every tsconfig project in a folder."""
    index = out / f"typescript-{group.replace('/', '_') or 'root'}.scip"
    relative = [str(PurePosixPath(p).relative_to(group)) if group != "." else p for p in projects]
    result = subprocess.run(["scip-typescript", "index", "--output", str(index), *relative], cwd=root / group,
                            capture_output=True, text=True, check=False)
    return group, index if result.returncode == 0 and index.exists() else None


def scip_indexes(root: Path, out: Path, code: list[str], files: list[str], include: list[str]) -> list[tuple[str, Path]]:
    """(folder its paths are relative to, index file) from every SCIP indexer that ran: one per Python
    project, one per included folder for its TypeScript projects. Missing indexers leave files approx."""
    python = [f for f in code if PurePosixPath(f).suffix in PYTHON]
    typescript = [f for f in code if PurePosixPath(f).suffix in TYPESCRIPT]
    jobs = []
    if python and shutil.which("scip-python"):
        jobs += [(python_project, (root, d, out)) for d in project_dirs(python, {"pyproject.toml", "setup.py"}, files) or ["."]]
    if typescript and shutil.which("scip-typescript"):
        projects = project_dirs(typescript, {"tsconfig.json"}, files)
        for group in include or ["."]:
            mine = [p for p in projects if group == "." or p == group or p.startswith(group + "/")]
            jobs += [(typescript_projects, (root, group, mine, out))] if mine else []
    with ThreadPoolExecutor(max_workers=4) as pool:
        done = list(pool.map(lambda job: job[0](*job[1]), jobs))
    for folder, index in done:
        print(f"calls: SCIP {'indexed' if index else 'failed for'} {folder}")
    return [(folder, index) for folder, index in done if index]


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
