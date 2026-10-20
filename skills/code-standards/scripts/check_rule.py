"""Test one ast-grep rule and count its hits across the whole project.

Usage: python3 check_rule.py <rule-id> [--expected N] [--slack N] [--sample N]

Exit codes:
  0  SAVE    fixtures pass and repo hits are within expected + slack
  1  FIX     fixtures fail, or a rule/test file is missing or thin; fix and rerun
  2  ASK     fixtures pass but the rule hits more than expected; show the sample to the developer
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from review import STANDARDS_DIR, ToolMissing, all_files, find_root, load_config, review_files, tool

MIN_INVALID, MIN_VALID = 2, 2


def count_cases(test_text: str, section: str) -> int:
    """Count `- ` items directly under `valid:` or `invalid:` (two-space indented lists)."""
    match = re.search(rf"^{section}:\s*\n((?:[ \t]+.*\n?|\n)*)", test_text, re.MULTILINE)
    return len(re.findall(r"^  - ", match.group(1), re.MULTILINE)) if match else 0


def run_tests(root: Path, sg: str, rule_id: str) -> tuple[bool, str]:
    result = subprocess.run([sg, "test", "-c", f"{STANDARDS_DIR}/sgconfig.yml", "--skip-snapshot-tests",
                             "--filter", f"^{re.escape(rule_id)}$", "--color", "never"],
                            cwd=root, capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    return result.returncode == 0, output


def repo_hits(root: Path, sg: str, rule_id: str) -> list[dict]:
    files = review_files(root, all_files(root)[0], load_config(root))
    result = subprocess.run([sg, "scan", "-c", f"{STANDARDS_DIR}/sgconfig.yml", "--filter", f"^{re.escape(rule_id)}$",
                             "--json=stream", *files], cwd=root, capture_output=True, text=True)
    if result.returncode not in (0, 1):
        sys.exit(f"SCAN ERROR\n{result.stderr.strip()}")
    return [json.loads(line) for line in result.stdout.splitlines()]


def fixtures_ok(root: Path, sg: str, rule_id: str) -> bool:
    rule_file = root / STANDARDS_DIR / "rules" / f"{rule_id}.yml"
    test_file = root / STANDARDS_DIR / "rule-tests" / f"{rule_id}-test.yml"
    missing = [str(p.relative_to(root)) for p in (rule_file, test_file) if not p.is_file()]
    if missing:
        print(f"FIX  missing {', '.join(missing)}")
        return False
    test_text = test_file.read_text()
    invalid, valid = count_cases(test_text, "invalid"), count_cases(test_text, "valid")
    passed, output = run_tests(root, sg, rule_id)
    print(f"TEST {'PASS' if passed else 'FAIL'}  {rule_id}  invalid={invalid} valid={valid}")
    if not passed:
        print(output)
    if invalid < MIN_INVALID or valid < MIN_VALID:
        print(f"FIX  need at least {MIN_INVALID} invalid and {MIN_VALID} valid fixtures")
        return False
    return passed


def hits_ok(root: Path, sg: str, args: argparse.Namespace, limit: int) -> bool:
    hits = repo_hits(root, sg, args.rule_id)
    print(f"HITS {len(hits)}  (expected {args.expected}, ask above {limit})")
    for hit in hits[: args.sample]:
        print(f"  {hit['file']}:{hit['range']['start']['line'] + 1}  {hit['lines'].strip()[:120]}")
    if len(hits) > limit:
        print("ASK  more hits than expected: real violations, or tighten the rule?")
        return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("rule_id")
    parser.add_argument("--expected", type=int, default=1, help="sites the developer flagged or confirmed")
    parser.add_argument("--slack", type=int, default=2, help="extra hits allowed before asking")
    parser.add_argument("--sample", type=int, default=10)
    parser.add_argument("--root", type=Path)
    args = parser.parse_args()

    root = (args.root or find_root(Path.cwd())).resolve()
    try:
        sg = tool(root, "ast-grep")
    except ToolMissing as exc:
        sys.exit(str(exc))
    if not fixtures_ok(root, sg, args.rule_id):
        sys.exit(1)
    if not hits_ok(root, sg, args, args.expected + args.slack):
        sys.exit(2)
    print("SAVE")


if __name__ == "__main__":
    main()
