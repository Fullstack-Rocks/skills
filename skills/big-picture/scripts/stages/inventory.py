"""Stage 1: list the project's files and add folder, module and knowledge nodes (READMEs, manifests,
agent files, skills, rules, schemas, infra)."""
import subprocess
from pathlib import Path, PurePosixPath

from graph import Graph

CODE_EXTENSIONS = {".py", ".pyi", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".go", ".rs", ".java",
                   ".kt", ".rb", ".php", ".cs", ".swift", ".scala", ".lua", ".c", ".h", ".cc", ".cpp", ".hpp"}
SKIPPED_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".big-picture"}
MINIFIED_LINE = 5000  # a JavaScript file with a longer line is built output (a bundle), not source
BUNDLED = {".js", ".mjs", ".cjs"}  # what bundlers emit; generated TypeScript has long lines too, and is source

# First match wins. Patterns match from the right of the path, like PurePosixPath.match.
KNOWLEDGE = [
    ("skill", "SKILL.md"),
    ("agent-file", "CLAUDE.md"), ("agent-file", "AGENTS.md"), ("agent-file", "GEMINI.md"),
    ("agent-file", ".cursorrules"), ("agent-file", ".github/copilot-instructions.md"),
    ("rule", ".code-standards/rules/*.yml"), ("standard", ".code-standards/standards.md"),
    ("readme", "README*"), ("readme", "readme*"),
    ("manifest", "package.json"), ("manifest", "pyproject.toml"), ("manifest", "requirements*.txt"),
    ("manifest", "go.mod"), ("manifest", "Cargo.toml"), ("manifest", "Gemfile"), ("manifest", "pom.xml"),
    ("manifest", "build.gradle*"), ("manifest", "composer.json"),
    ("migration", "migrations/*"), ("migration", "alembic/versions/*.py"),
    ("schema", "*.sql"), ("schema", "schema.prisma"), ("schema", "*.graphql"),
    ("schema", "openapi*.yaml"), ("schema", "openapi*.yml"), ("schema", "openapi*.json"), ("schema", "swagger*"),
    ("infra", "Dockerfile*"), ("infra", "docker-compose*.yml"), ("infra", "compose*.yml"), ("infra", "*.tf"),
    ("infra", ".github/workflows/*.yml"), ("infra", "Procfile"), ("infra", "fly.toml"), ("infra", "vercel.json"),
    ("infra", "nginx*.conf"), ("config", ".env*"), ("config", "*.ini"), ("config", "*.cfg"), ("config", "*.conf"),
    ("doc", "*.md"),
]


def folder_files(folder: Path) -> list[str]:
    """Paths relative to folder: git's view (tracked + untracked, minus ignored) when it is in a repo."""
    result = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                            cwd=folder, capture_output=True, text=True, check=False)
    if result.returncode == 0:
        return result.stdout.splitlines()
    return [str(p.relative_to(folder)) for p in folder.rglob("*") if p.is_file()]


def minified(path: Path) -> bool:
    """A committed bundle: indexing its one huge line per call site would take gigabytes."""
    with path.open(errors="replace") as handle:
        return any(len(line) > MINIFIED_LINE for line in handle)


def list_files(root: Path, include: list[str]) -> list[str]:
    """Paths relative to root, from each included folder (.big-picture/config.yml) or the whole root,
    without skipped folders and minified JavaScript."""
    paths = [f"{folder}/{p}" for folder in include for p in folder_files(root / folder)] if include else folder_files(root)
    kept = [p for p in paths if not SKIPPED_DIRS & set(PurePosixPath(p).parts[:-1]) and (root / p).is_file()]
    return sorted(p for p in kept if PurePosixPath(p).suffix not in BUNDLED or not minified(root / p))


def code_files(files: list[str]) -> list[str]:
    return [f for f in files if PurePosixPath(f).suffix in CODE_EXTENSIONS]


def knowledge_type(path: str) -> str | None:
    pure = PurePosixPath(path)
    return next((kind for kind, pattern in KNOWLEDGE if pure.match(pattern)), None)


def add_folder(graph: Graph, path: str) -> str:
    """The node for the folder holding path, with its parent folders chained by contains edges."""
    parent = str(PurePosixPath(path).parent)
    folder_id = f"folder:{parent}"
    if folder_id not in graph.nodes:
        graph.add_node(folder_id, "folder", parent, file=parent)
        if parent != ".":
            graph.add_edge(add_folder(graph, parent), folder_id, "contains", "inventory")
    return folder_id


def add_inventory(graph: Graph, files: list[str]) -> None:
    for path in code_files(files):
        graph.file_node[path] = graph.add_node(f"module:{path}", "module", path, file=path)
        graph.add_edge(add_folder(graph, path), f"module:{path}", "contains", "inventory")
    for path in files:
        kind = knowledge_type(path)
        if kind is None:
            continue
        node_id = f"rule:{PurePosixPath(path).stem}" if kind == "rule" else f"{kind}:{path}"
        graph.file_node.setdefault(path, graph.add_node(node_id, kind, path, file=path))
        graph.add_edge(add_folder(graph, path), node_id, "contains", "inventory")
