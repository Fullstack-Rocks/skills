#!/usr/bin/env python3
"""Combines reviewers' JSON replies for one round: median scores per page, the gate, and the blocking problems.

A page passes at a median of --gate (8.5) on every metric, or at --floor (8.0) when no reviewer tags a
blocks-understanding problem on it. A page named with --wrong (a wrong answer came from it) fails either way.
"""

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


def page_key(page: object) -> str:
    """Page ids as reviewers write them: "03", "page-03" and "page 03" are the same page."""
    return str(page).strip().lower().removeprefix("page").strip(" -_") or str(page)


def blocked_pages(replies: list[dict]) -> set[str]:
    return {page_key(problem.get("page")) for reply in replies for problem in reply.get("problems", [])
            if problem.get("tag") == "blocks-understanding"}


def blocking_lines(replies: list[dict]) -> list[str]:
    lines = []
    for index, reply in enumerate(replies, start=1):
        for problem in reply.get("problems", []):
            if problem.get("tag") == "blocks-understanding":
                lines.append(f"BLOCKING\treviewer{index}/{problem.get('page', '?')}\t{problem.get('problem', '')} -> {problem.get('fix', '')}")
    return lines


def verdict(medians: dict[str, float], gate: float, floor: float, blocked: bool, wrong: bool) -> str:
    lowest = min(medians.values())
    if wrong:
        return "FAIL\ta checked answer from this page was wrong"
    if lowest >= gate:
        return "PASS"
    if lowest >= floor and not blocked:
        return f"PASS\tat the floor: median {lowest:.2f}, no blocking problem"
    if lowest >= floor:
        return f"FAIL\ta reviewer tagged a blocking problem; the floor needs none"
    return f"FAIL\tbelow the floor of {floor:g}"


def gate_pages(replies: list[dict], gate: float, floor: float, wrong: set[str]) -> list[str]:
    """Prints each page's medians and verdict, and returns the failing pages."""
    failing = []
    blocked = blocked_pages(replies)
    for page in sorted({page for reply in replies for page in reply.get("pages", {})}):
        medians = page_medians(replies, page)
        result = verdict(medians, gate, floor, page_key(page) in blocked, page_key(page) in wrong)
        if result.startswith("FAIL"):
            failing.append(page)
        scores = " ".join(f"{metric}={medians[metric]:.2f}" for metric in METRICS)
        print(f"PAGE\t{page}\t{scores}\t{result}")
    return failing


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("replies", nargs="+", help="one JSON reply file per reviewer")
    parser.add_argument("--gate", type=float, default=8.5, help="median on every metric that passes a page outright")
    parser.add_argument("--floor", type=float, default=8.0,
                        help="median that passes a page when no reviewer tags a blocking problem on it; set it to the gate to turn this off")
    parser.add_argument("--wrong", action="append", default=[], metavar="PAGE",
                        help="a page a wrong checked answer came from; it fails whatever its scores (repeatable)")
    args = parser.parse_args()
    replies = [read_reply(path) for path in args.replies]

    failing = gate_pages(replies, args.gate, args.floor, {page_key(page) for page in args.wrong})
    print("\n".join(blocking_lines(replies)) or "BLOCKING\t-\tnone")
    answers = sum(len(reply.get("answers", [])) for reply in replies)
    print(f"ANSWERS\t{answers}\tcheck each against the fact list; any wrong answer fails its page")
    print(f"GATE\t{'PASS' if not failing else 'FAIL'}\treviewers={len(replies)} failing={','.join(failing) or '-'}")
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
