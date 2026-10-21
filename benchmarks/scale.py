"""How code-standards' scripts scale to a real repository, next to what reading that code would cost an LLM.

Runs init.py (if the repo has no .code-standards/ yet) and `review.py --all` three times, and reports the
median wall time. It also counts the reviewed files and their characters: at roughly 4 characters per token,
that is the least an LLM must read to look at every file once, before any reasoning or output.

Usage: python3 benchmarks/scale.py <repo-dir> [<name>]
Result: benchmarks/results/scale/<name>.json
"""
import json
import statistics
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent / "skills/code-standards/scripts"
CHARS_PER_TOKEN = 4


def main() -> None:
    repo = Path(sys.argv[1]).resolve()
    name = sys.argv[2] if len(sys.argv) > 2 else repo.name
    if not (repo / ".code-standards/config.toml").exists():
        subprocess.run([sys.executable, str(SCRIPTS / "init.py")], cwd=repo, capture_output=True, check=True)
    runs = []
    for _ in range(3):
        started = time.perf_counter()
        out = subprocess.run([sys.executable, str(SCRIPTS / "review.py"), "--all"], cwd=repo,
                             capture_output=True, text=True).stdout
        runs.append(time.perf_counter() - started)
    report = json.loads(out)
    chars = sum(len((repo / f).read_text(errors="ignore")) for f in report["files"])
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=repo, capture_output=True, text=True).stdout
    result = {
        "repo": name, "commit": commit.strip(), "files_reviewed": report["files_scanned"],
        "lines": sum((repo / f).read_text(errors="ignore").count("\n") for f in report["files"]),
        "seconds_median": round(statistics.median(runs), 2), "seconds_runs": [round(r, 2) for r in runs],
        "tool_timing": report["timing"], "findings": len(report["findings"]),
        "tools_missing": [w["tool"] for w in report["warnings"]], "errors": report["errors"],
        "llm_read_tokens_estimate": chars // CHARS_PER_TOKEN,
    }
    out_dir = HERE / "results" / "scale"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{name}.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
