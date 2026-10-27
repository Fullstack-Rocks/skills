"""Install the SCIP indexers big-picture uses for exact calls edges, pinned, at user level (npm -g).

ast-grep and lizard come from the call-depth skill's own install_tools.py. The indexers are npm
packages, so they need Node.js; without it, calls in those languages fall back to approx edges.

Usage: python3 install_tools.py [python] [typescript]      (default: both)
Exit codes: 0 every requested indexer is available; 1 something could not be installed.
"""
import argparse
import shutil
import subprocess
import sys

PINNED = {
    "python": ("scip-python", "@sourcegraph/scip-python@0.6.8"),
    "typescript": ("scip-typescript", "@sourcegraph/scip-typescript@0.5.2"),
}


def install(language: str) -> bool:
    binary, package = PINNED[language]
    if shutil.which(binary):
        print(f"{binary}: already installed")
        return True
    if not shutil.which("npm"):
        print(f"{binary}: needs Node.js and npm, then: npm install -g {package}")
        return False
    result = subprocess.run(["npm", "install", "-g", package], capture_output=True, text=True, check=False)
    ok = result.returncode == 0 and shutil.which(binary) is not None
    print(f"{binary}: {'installed ' + package if ok else 'failed, run: npm install -g ' + package}")
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("languages", nargs="*", choices=list(PINNED))
    results = [install(language) for language in parser.parse_args().languages or PINNED]
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
