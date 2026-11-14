#!/usr/bin/env python3
"""Combines reviewers' JSON replies for one round: median scores per page, the gate, and the blocking problems."""

import argparse
import json
import re
import statistics
import sys

METRICS = ("readability", "understanding")


def read_reply(path: str) -> dict:
    """A reviewer's JSON reply, also when the reviewer wrapped it in prose or a code fence."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError(f"{path}: no JSON object found")
    return json.loads(text[start:end + 1])


def page_medians(replies: list[dict], page: str) -> dict[str, float]:
    reviews = [reply["pages"][page] for reply in replies if page in reply.get("pages", {})]
    return {metric: statistics.median(float(review[metric]) for review in reviews) for metric in METRICS}


def blocking_lines(replies: list[dict]) -> list[str]:
    lines = []
    for index, reply in enumerate(replies, start=1):
        for problem in reply.get("problems", []):
            if problem.get("tag") == "blocks-understanding":
                lines.append(f"BLOCKING\treviewer{index}/{problem.get('page', '?')}\t{problem.get('problem', '')} -> {problem.get('fix', '')}")
    return lines


def gate_pages(replies: list[dict], gate: float) -> list[str]:
    """Prints each page's medians and returns the pages below the gate."""
    failing = []
    for page in sorted({page for reply in replies for page in reply.get("pages", {})}):
        medians = page_medians(replies, page)
        passed = all(value >= gate for value in medians.values())
        if not passed:
            failing.append(page)
        scores = " ".join(f"{metric}={medians[metric]:.2f}" for metric in METRICS)
        print(f"PAGE\t{page}\t{scores}\t{'PASS' if passed else 'FAIL'}")
    return failing


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("replies", nargs="+", help="one JSON reply file per reviewer")
    parser.add_argument("--gate", type=float, default=8.5, help="minimum median on every metric")
    args = parser.parse_args()
    replies = [read_reply(path) for path in args.replies]

    failing = gate_pages(replies, args.gate)
    print("\n".join(blocking_lines(replies)) or "BLOCKING\t-\tnone")
    answers = sum(len(reply.get("answers", [])) for reply in replies)
    print(f"ANSWERS\t{answers}\tcheck each against the fact list; any wrong answer fails its page")
    print(f"GATE\t{'PASS' if not failing else 'FAIL'}\treviewers={len(replies)} failing={','.join(failing) or '-'}")
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
