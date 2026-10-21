"""Benchmark the skills against the same agent with skills turned off.

Each run copies demo/ into a fresh git sandbox (plus a fixture for some suites), runs Claude Code
headless on one task, and measures the result with this repo's own scanners. "without" blocks the
Skill tool; "with" tells the agent which skill to load. Both get the same fixed reply when they stop
to ask a question, so a checkpoint doesn't end the run early.

Usage: python3 benchmarks/run.py [--suite NAME] [--task ID] [--condition with|without] [--jobs N]
Results: benchmarks/results/<suite>/<task>.<condition>.json (+ .diff for implementation tasks)
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DEMO = REPO / "demo"
SCAN = REPO / "skills/call-depth/scripts/scan.py"
REVIEW = REPO / "skills/code-standards/scripts/review.py"
TOOLS = "Bash Read Write Edit Glob Grep Skill Agent"
REPLY = "Go with your recommendation: the simplest option you proposed. Implement it now without further questions."
CODE = re.compile(r"\.(py|ts|tsx|js|jsx)$")
# The measuring scripts find the demo's linters on PATH; sandboxes get no links into demo/, so an
# agent installing or syncing packages can only change its own sandbox.
TOOL_ENV = {**os.environ, "PATH": f"{DEMO}/.venv/bin:{DEMO}/node_modules/.bin:{os.environ['PATH']}"}
SUITES = json.loads((HERE / "tasks.json").read_text())


def sh(cmd: list[str], cwd: Path, **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, **kw)


def sandbox(suite: dict) -> tuple[Path, str]:
    root = Path(tempfile.mkdtemp(prefix="fsr-bench-"))
    shutil.copytree(DEMO, root, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("node_modules", ".venv", "WALKTHROUGH.md", "__pycache__"))
    fixture = suite.get("fixture")
    if fixture and suite.get("fixture_committed", True):
        shutil.copytree(HERE / "fixtures" / fixture, root, dirs_exist_ok=True, ignore=shutil.ignore_patterns("*.json"))
    sh(["git", "init", "-q", "-b", "main"], root)
    (root / ".git/info/exclude").write_text("node_modules\n.venv\n")
    sh(["git", "add", "-A"], root)
    sh(["git", "-c", "user.name=bench", "-c", "user.email=bench@example.com", "commit", "-qm", "baseline"], root)
    if fixture and not suite.get("fixture_committed", True):  # the change under review stays uncommitted
        shutil.copytree(HERE / "fixtures" / fixture, root, dirs_exist_ok=True, ignore=shutil.ignore_patterns("*.json"))
    return root, sh(["git", "rev-parse", "HEAD"], root).stdout.strip()


def claude_command(prompt: str, condition: str, suite: dict, session: str | None) -> list[str]:
    cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose", "--strict-mcp-config",
           "--permission-mode", "acceptEdits", "--allowedTools", TOOLS]
    if condition == "without":
        cmd += ["--disallowedTools", "Skill"]
    else:
        cmd += ["--append-system-prompt", suite["skill_instruction"]]
    return cmd + (["--resume", session] if session else [])


def skills_loaded(events: list[dict]) -> list[str]:
    blocks = [b for e in events if e.get("type") == "assistant" for b in e["message"].get("content", [])]
    names = {b["input"].get("skill", "") for b in blocks if b.get("type") == "tool_use" and b["name"] == "Skill"}
    return sorted(name for name in names if name)


def claude(root: Path, prompt: str, condition: str, suite: dict, session: str | None) -> dict:
    out = sh(claude_command(prompt, condition, suite, session), root, timeout=1800).stdout
    events = [json.loads(line) for line in out.splitlines() if line.startswith("{")]
    result = next((e for e in reversed(events) if e.get("type") == "result"), {})
    init = next((e for e in events if e.get("type") == "system" and e.get("subtype") == "init"), {})
    return {"session": result.get("session_id") or init.get("session_id"), "text": result.get("result", ""),
            "cost_usd": result.get("total_cost_usd", 0), "turns": result.get("num_turns", 0),
            "model": init.get("model"), "skills_loaded": skills_loaded(events)}


def changed_code(root: Path, base: str) -> list[str]:
    sh(["git", "add", "-A"], root)
    names = sh(["git", "diff", "--cached", "--name-only", "--diff-filter=AM", base], root).stdout.split()
    return [n for n in names if CODE.search(n) and not n.startswith(".code-standards/")]


def finding_keys(cwd: Path, files: list[str]) -> set[tuple]:
    """Scanner and review findings for `files`, keyed without line numbers so before/after compare."""
    present = [f for f in files if (cwd / f).is_file()]
    if not present:
        return set()
    keys = set()
    for line in sh([sys.executable, str(SCAN), *present], cwd, env=TOOL_ENV).stdout.splitlines():
        kind, where, detail = (line.split("\t") + ["", ""])[:3]
        if kind in ("FUNCTION_LENGTH", "COMPLEXITY", "DYNAMIC_CALL", "DYNAMIC_ATTR", "LOOKUP_CALL"):
            keys.add((kind, where.rsplit(":", 1)[0], detail.split("  (")[0].split(" ")[0]))
    review = json.loads(sh([sys.executable, str(REVIEW), "--files", *present], cwd, env=TOOL_ENV).stdout or "{}")
    for f in review.get("findings", []):
        if f["source"] in ("ruff", "oxlint", "eslint", "biome", "ast-grep", "jscpd"):
            keys.add(("REVIEW", f["file"], f"{f['source']}:{f['rule_id']}:{re.sub(r'[0-9]+', '#', f['message'])}"))
    return keys


def new_findings(root: Path, base: str, files: list[str]) -> list[tuple]:
    """Findings in the changed files that the baseline versions of those files didn't have."""
    before = Path(tempfile.mkdtemp(prefix="fsr-bench-base-"))
    sh(["git", "worktree", "add", "-q", "--detach", str(before), base], root)
    try:
        return sorted(finding_keys(root, files) - finding_keys(before, files))
    finally:
        sh(["git", "worktree", "remove", "--force", str(before)], root)


def diff_size(root: Path, base: str, files: list[str]) -> tuple[int, int]:
    if not files:
        return 0, 0
    numstat = sh(["git", "diff", "--cached", "--numstat", base, "--", *files], root).stdout.splitlines()
    counts = [line.split("\t")[:2] for line in numstat]
    return sum(int(a) for a, _ in counts if a.isdigit()), sum(int(r) for _, r in counts if r.isdigit())


def implementation_metrics(root: Path, base: str) -> dict:
    files = changed_code(root, base)
    added, removed = diff_size(root, base, files)
    new_files = sh(["git", "diff", "--cached", "--name-only", "--diff-filter=A", base], root).stdout.split()
    introduced = new_findings(root, base, files)
    kinds = [key[0] for key in introduced]
    return {
        "code_files_changed": len(files), "code_files_added": len([f for f in new_files if CODE.search(f)]),
        "other_files_added": [f for f in new_files if not CODE.search(f)],
        "lines_added": added, "lines_removed": removed,
        "new_memory_hops": kinds.count("DYNAMIC_CALL") + kinds.count("LOOKUP_CALL"),
        "new_complexity_over_10": kinds.count("COMPLEXITY"),
        "new_functions_over_80_lines": kinds.count("FUNCTION_LENGTH"),
        "new_review_findings": kinds.count("REVIEW"),
        "introduced": [list(key) for key in introduced],
    }


def recall_metrics(text: str, suite: dict) -> dict:
    truth = json.loads((HERE / "fixtures" / suite["fixture"] / "ground_truth.json").read_text())
    found = [item["id"] for item in truth if re.search(item["pattern"], text, re.IGNORECASE)]
    # A keyword match over the whole answer: quick but approximate. It can credit a smell the answer only
    # mentions in passing, so the published numbers are graded by hand (results/code-standards/grading.md).
    return {"planted": len(truth), "auto_found": len(found), "auto_found_ids": found,
            "auto_missed_ids": [item["id"] for item in truth if item["id"] not in found]}


def depth_metrics(text: str, suite: dict) -> dict:
    truth = json.loads((HERE / "fixtures" / suite["fixture"] / "ground_truth.json").read_text())
    depths = [int(d) for d in re.findall(r"(?i)(?:weighted )?depth[^0-9\n]{0,40}(\d+)", text)]
    hops = [hop["file"] for hop in truth["memory_hops"] if re.search(hop["pattern"], text)]
    return {"expected_depth": truth["weighted_depth"], "reported_depths": depths,
            "depth_correct": truth["weighted_depth"] in depths[:3],
            "hops_expected": len(truth["memory_hops"]), "hops_found": len(hops), "hops_found_in": hops}


def run_one(suite_name: str, task: dict, condition: str) -> dict:
    suite = SUITES[suite_name]
    root, base = sandbox(suite)
    started = time.time()
    turn = claude(root, task["prompt"], condition, suite, None)
    transcript = [turn["text"]]
    cost, turns, skills = turn["cost_usd"], turn["turns"], set(turn["skills_loaded"])
    for _ in range(2):  # a checkpoint asks first; answer the same way in both conditions
        if suite["kind"] != "implementation" or changed_code(root, base):
            break
        turn = claude(root, REPLY, condition, suite, turn["session"])
        transcript.append(turn["text"])
        cost, turns, skills = cost + turn["cost_usd"], turns + turn["turns"], skills | set(turn["skills_loaded"])
    record = {"suite": suite_name, "task": task["id"], "condition": condition, "model": turn["model"],
              "skills_loaded": sorted(skills), "cost_usd": round(cost, 2), "turns": turns,
              "minutes": round((time.time() - started) / 60, 1), "sandbox": str(root), "answers": transcript}
    record["metrics"] = score(record, suite)
    out = HERE / "results" / suite_name
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{task['id']}.{condition}.json").write_text(json.dumps(record, indent=2))
    if suite["kind"] == "implementation":
        (out / f"{task['id']}.{condition}.diff").write_text(sh(["git", "diff", "--cached", base], root).stdout)
    print(f"done {suite_name}/{task['id']}/{condition}: {json.dumps(record['metrics'])[:160]}", flush=True)
    return record


def score(record: dict, suite: dict) -> dict:
    root = Path(record["sandbox"])
    if suite["kind"] == "implementation":
        base = sh(["git", "rev-list", "--max-parents=0", "HEAD"], root).stdout.split()[0]
        return implementation_metrics(root, base)
    text = "\n".join(record["answers"])
    return recall_metrics(text, suite) if suite["kind"] == "recall" else depth_metrics(text, suite)


def rescore() -> None:
    for path in sorted((HERE / "results").glob("*/*.json")):
        record = json.loads(path.read_text())
        record["metrics"] = score(record, SUITES[record["suite"]])
        path.write_text(json.dumps(record, indent=2))
        print(f"rescored {path.relative_to(HERE)}: {json.dumps(record['metrics'])[:150]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--suite", choices=list(SUITES))
    parser.add_argument("--task")
    parser.add_argument("--condition", choices=["with", "without"])
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--rescore", action="store_true", help="recompute metrics for saved runs; runs no agent")
    args = parser.parse_args()
    if args.rescore:
        return rescore()
    runs = [(name, task, condition) for name, suite in SUITES.items() if args.suite in (None, name)
            for task in suite["tasks"] if args.task in (None, task["id"])
            for condition in ("without", "with") if args.condition in (None, condition)]
    print(f"{len(runs)} runs", flush=True)
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        list(pool.map(lambda run: run_one(*run), runs))


if __name__ == "__main__":
    main()
