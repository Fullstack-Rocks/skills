import sys

if sys.version_info < (3, 10):
    sys.exit(f"This script needs Python 3.10+ (this is {sys.version.split()[0]}). "
             "Rerun with python3.10+ or: uv run --no-project --python 3.12 -- python " + " ".join(sys.argv))

import argparse
import re
import subprocess
from collections import Counter
from pathlib import Path

CODE_EXTENSIONS = {
    ".py", ".pyi", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".go", ".rs", ".java", ".kt", ".kts",
    ".scala", ".cs", ".fs", ".rb", ".php", ".swift", ".m", ".mm", ".c", ".h", ".cc", ".cpp", ".hpp",
    ".dart", ".ex", ".exs", ".erl", ".clj", ".lua", ".r", ".jl", ".sh", ".vue", ".svelte", ".sql",
}
SKIPPED_PARTS = {
    ".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", "target", "vendor",
    ".next", ".nuxt", "coverage", ".mypy_cache", ".ruff_cache", ".pytest_cache", "generated",
}

TEST_FILE = re.compile(r"(^test_|_test\.|\.test\.|\.spec\.|Tests?\.)")
TEST_FOLDERS = {"tests", "test", "__tests__", "spec"}


def is_test(path: Path) -> bool:
    return bool(TEST_FILE.search(path.name)) or bool(TEST_FOLDERS.intersection(path.parts))


def git_files(root: Path) -> list[Path] | None:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "."],
        cwd=root, capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None
    return [root / line for line in result.stdout.splitlines() if line]


def walked_files(root: Path) -> list[Path]:
    return [path for path in root.rglob("*") if path.is_file()]


def code_files(root: Path) -> list[Path]:
    candidates = git_files(root) if root.is_dir() else [root]
    if candidates is None:
        candidates = walked_files(root)
    return [
        path for path in candidates
        if path.suffix in CODE_EXTENSIONS and not SKIPPED_PARTS.intersection(path.parts)
    ]


def line_count(path: Path) -> int:
    with path.open("rb") as handle:
        return sum(1 for _ in handle)


def name_words(name: str) -> int:
    spaced = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    return len([word for word in re.split(r"[\s_\-.]+", spaced) if word])


def report(files: list[Path], limits: argparse.Namespace) -> list[str]:
    findings = []
    for path in sorted(files):
        lines = line_count(path)
        if lines > limits.max_file_lines:
            findings.append(f"FILE_LENGTH\t{path}\t{lines} lines > {limits.max_file_lines}")
    counted = files if limits.include_tests else [path for path in files if not is_test(path)]
    folders = Counter(path.parent for path in counted)
    for folder, count in sorted(folders.items()):
        if count > limits.max_folder_files:
            findings.append(f"FOLDER_SIZE\t{folder}\t{count} code files > {limits.max_folder_files}")
        if name_words(folder.name) > limits.max_folder_words:
            findings.append(f"FOLDER_NAME\t{folder}\t'{folder.name}' > {limits.max_folder_words} words")
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Report file length, folder size and folder name findings.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--max-file-lines", type=int, default=1000)
    parser.add_argument("--max-folder-files", type=int, default=6)
    parser.add_argument("--max-folder-words", type=int, default=3)
    parser.add_argument("--include-tests", action="store_true", help="count test files toward folder size")
    limits = parser.parse_args()
    missing = [f"MISSING_PATH\t{path}\tdoes not exist" for path in limits.paths if not path.exists()]
    files = [file for path in limits.paths if path.exists() for file in code_files(path.resolve())]
    findings = missing + report(files, limits)
    print("\n".join(findings) if findings else "OK\tno layout findings")
    print(f"SCANNED\t{len(files)} code files")


if __name__ == "__main__":
    main()
