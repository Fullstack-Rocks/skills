"""Stage 13: systems, the deployable units that talk to each other (a backend, a frontend, a worker).
They come from .big-picture/systems.yml ({name: folder}) or, without it, from the folders that hold a
manifest; when one manifest covers the whole project, each top-level folder with code is a system.
Every node in a system's folder gets `system`; an edge between two systems, or a node two systems
use (a topic, a message), is how they connect."""
from pathlib import PurePosixPath

from graph import Graph
from stages.files import load_data
from stages.inventory import code_files

MANIFESTS = {"package.json", "pyproject.toml", "go.mod", "Cargo.toml", "pom.xml", "build.gradle", "build.gradle.kts",
             "composer.json", "Gemfile", "setup.py", "requirements.txt", "deno.json"}
NOT_SYSTEMS = {"test", "tests", "docs", "doc", "scripts", "examples", ".github"}


def declared_systems(graph: Graph) -> dict[str, str]:
    """name -> folder from .big-picture/systems.yml; empty when there is none."""
    config = graph.root / ".big-picture" / "systems.yml"
    declared = load_data(config) if config.exists() else None
    systems = declared.get("systems", {}) if isinstance(declared, dict) else {}
    return {name: folder.strip("/") for name, folder in systems.items()}


def inferred_systems(files: list[str]) -> dict[str, str]:
    """Folders holding a manifest; when one manifest covers everything, each top-level folder with code."""
    roots = sorted({str(PurePosixPath(f).parent) for f in files if PurePosixPath(f).name in MANIFESTS} - {"."})
    if len(roots) < 2:
        roots = sorted({PurePosixPath(f).parts[0] for f in code_files(files) if len(PurePosixPath(f).parts) > 1} - NOT_SYSTEMS)
    return {PurePosixPath(root).name: root for root in roots}


def system_of(file: str, roots: dict[str, str]) -> str | None:
    """The system whose folder holds the file; the deepest when folders nest."""
    holding = [(len(folder), name) for name, folder in roots.items() if file == folder or file.startswith(folder + "/")]
    return max(holding)[1] if holding else None


def add_systems(graph: Graph, files: list[str]) -> int:
    """System nodes, and `system` on every node with a file; returns how many systems."""
    roots = declared_systems(graph) or inferred_systems(files)
    for name, folder in roots.items():
        graph.add_node(f"system:{name}", "system", name, file=folder)
    for node in [n for n in graph.nodes.values() if n.get("file") and n["type"] != "system"]:
        node["system"] = system_of(node["file"], roots)
    return len(roots)
