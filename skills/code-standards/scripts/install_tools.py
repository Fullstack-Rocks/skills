"""Install parser tools (ast-grep, lizard, jscpd) at pinned versions, user-level.

The same file ships with the code-standards and call-depth skills; keep the copies identical.

Leaves the project alone: no manifests, lockfiles or project environments are touched. For each
missing tool it tries the installers below in order and keeps the first that works. Prints one
line per tool.

Usage: python3 install_tools.py [TOOL ...] [--dry-run]     (default: every tool below)
Exit codes: 0 every requested tool is available; 1 something could not be installed (a manual command is printed).
"""
import sys

if sys.version_info < (3, 10):
    sys.exit(f"This script needs Python 3.10+ (this is {sys.version.split()[0]}). "
             "Rerun with python3.10+ or: uv run --no-project --python 3.12 -- python " + " ".join(sys.argv))

import argparse
import shutil
import site
import subprocess
from pathlib import Path

PINNED = {"ast-grep": "0.50.0", "lizard": "1.24.1", "jscpd": "5.4.1"}
ENV_BIN_DIRS = [".venv/bin", "venv/bin", "node_modules/.bin"]
# Where uv/pipx, cargo and pip --user put tools, in case that folder isn't on PATH yet.
USER_BIN_DIRS = [Path.home() / ".local/bin", Path.home() / ".cargo/bin", Path(site.getuserbase()) / "bin"]


def find_tool(root: Path, name: str) -> str | None:
    """The project's own environment first, then PATH, then user-level tool folders. Never a downloader."""
    for folder in ENV_BIN_DIRS:
        candidate = root / folder / name
        if candidate.is_file():
            return str(candidate)
    found = shutil.which(name)
    if found:
        return found
    return next((str(d / name) for d in USER_BIN_DIRS if (d / name).is_file()), None)


def installers(name: str) -> list[list[str]]:
    """Install commands for a tool, most portable first. The first word must be on PATH to be tried."""
    version = PINNED[name]
    return {
        "ast-grep": [
            ["npm", "install", "-g", f"@ast-grep/cli@{version}"],
            ["uv", "tool", "install", f"ast-grep-cli=={version}"],
            ["pipx", "install", f"ast-grep-cli=={version}"],
            ["cargo", "install", "ast-grep", "--locked", "--version", version],
            [sys.executable, "-m", "pip", "install", "--user", f"ast-grep-cli=={version}"],
        ],
        "lizard": [
            ["uv", "tool", "install", f"lizard=={version}"],
            ["pipx", "install", f"lizard=={version}"],
            [sys.executable, "-m", "pip", "install", "--user", f"lizard=={version}"],
        ],
        "jscpd": [["npm", "install", "-g", f"jscpd@{version}"]],
    }[name]


def install_hint(name: str) -> str:
    return f"run python3 {Path(__file__).resolve()} {name}"


def version_of(binary: str) -> str:
    result = subprocess.run([binary, "--version"], capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        return "?"
    return (result.stdout or result.stderr).strip().splitlines()[0].split()[-1]  # "ast-grep 0.50.0" -> "0.50.0"


def try_installer(name: str, cmd: list[str], root: Path) -> bool:
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if result.returncode != 0:
        print(f"TRIED     {name}: `{' '.join(cmd)}` failed: {(result.stderr or result.stdout).strip()[-300:]}")
        return False
    binary = find_tool(root, name)
    if not binary:
        print(f"WARN      {name}: `{' '.join(cmd)}` succeeded but the binary is not on PATH; "
              "add the installer's bin folder to PATH")
        return False
    print(f"INSTALLED {name} {version_of(binary)} via `{' '.join(cmd)}` -> {binary}")
    return True


def install(name: str, root: Path, dry_run: bool) -> bool:
    available = [cmd for cmd in installers(name) if shutil.which(cmd[0])]
    if not available:
        tried = ", ".join(cmd[0] for cmd in installers(name))
        print(f"FAILED    {name}: none of these installers is available: {tried}. "
              f"Install one, then: {' '.join(installers(name)[0])}")
        return False
    if dry_run:
        print(f"WOULD RUN {name}: {' '.join(available[0])}")
        return True
    if any(try_installer(name, cmd, root) for cmd in available):
        return True
    print(f"FAILED    {name}: every installer failed. Manual: {' '.join(installers(name)[0])}")
    return False


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("tools", nargs="*", metavar="TOOL", help=f"tools to check (default: {' '.join(PINNED)})")
    parser.add_argument("--dry-run", action="store_true", help="print what would be installed, install nothing")
    args = parser.parse_args()
    unknown = [name for name in args.tools if name not in PINNED]
    if unknown:
        parser.error(f"unknown tool {', '.join(unknown)}; choose from {', '.join(PINNED)}")
    root = Path.cwd()
    ok = True
    for name in args.tools or PINNED:
        binary = find_tool(root, name)
        if binary:
            print(f"OK        {name} {version_of(binary)} -> {binary}")
        else:
            ok = install(name, root, args.dry_run) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
