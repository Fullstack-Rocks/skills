"""Install the tools code-standards needs (ast-grep, lizard, jscpd) at pinned versions, user-level.

Leaves the project alone: no manifests, lockfiles or project environments are touched. For each
missing tool it tries the installers below in order and keeps the first that works. Prints one
line per tool.

Usage: python3 install_tools.py [--dry-run]
Exit codes: 0 every tool is available; 1 something could not be installed (a manual command is printed).
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from detect_linters import find_tool

PINNED = {"ast-grep": "0.50.0", "lizard": "1.24.1", "jscpd": "5.4.1"}


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
    return f"run python3 {Path(__file__).resolve()}"


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
    parser.add_argument("--dry-run", action="store_true", help="print what would be installed, install nothing")
    args = parser.parse_args()
    root = Path.cwd()
    ok = True
    for name in PINNED:
        binary = find_tool(root, name)
        if binary:
            print(f"OK        {name} {version_of(binary)} -> {binary}")
        else:
            ok = install(name, root, args.dry_run) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
