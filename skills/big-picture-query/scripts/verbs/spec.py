"""bp spec: a fix spec from health findings, for an agent to complete and implement.

It lists each finding with where it is and how to fix it, the callers each change can break (blast
radius), the entry points to test, a suggested order, and checks phrased as bp results."""
import re
from datetime import date
from pathlib import Path

from graph.load import Graph
from verbs.health import inside

# Fixes that remove other findings come first: one shared function ends the repeats, a split function
# is short and simple again.
ORDER = ["repeated-operation", "duplicate", "complexity", "function-length", "dynamic-call", "lookup-call"]
CALLERS_SHOWN = 5


def chosen_findings(graph: Graph, node: dict, ids: list[str] | None) -> list[dict]:
    found = [f for n in inside(graph, node["id"]) for f in graph.findings.get(n, [])]
    return [f for f in found if f["id"] in ids] if ids else found


def finding_lines(graph: Graph, finding: dict) -> list[str]:
    file, line = finding["sites"][0]
    callers = sorted({e["from"] for e in graph.incoming.get(finding["node"], []) if e["kind"] == "calls"})
    shown = ", ".join(callers[:CALLERS_SHOWN]) + (f" and {len(callers) - CALLERS_SHOWN} more" if len(callers) > CALLERS_SHOWN else "")
    return [f"- `{finding['id']}` at {file}:{line or ''}: {finding['detail']}", f"  - callers that could break: {shown or 'none'}"]


def spec_text(graph: Graph, node: dict, findings: list[dict], entries: list[str]) -> str:
    rules = sorted({f["rule"] for f in findings}, key=lambda r: (ORDER.index(r) if r in ORDER else len(ORDER), r))
    lines = [f"# Fix spec: {node['id']}", "",
             f"From the big-picture graph built {graph.built_at}. Complete the open questions, then work in order.", "",
             f"## Findings ({len(findings)})"]
    for rule in rules:
        group = [f for f in findings if f["rule"] == rule]
        lines += ["", f"### {rule} ({len(group)}, {group[0]['source']})", f"How: {group[0].get('fix', '')}", ""]
        lines += [text for f in group for text in finding_lines(graph, f)]
    return "\n".join(lines + closing_lines(node, findings, rules, entries)) + "\n"


def closing_lines(node: dict, findings: list[dict], rules: list[str], entries: list[str]) -> list[str]:
    """Entry points to test, the order to work in, the checks that say it is done, and open questions."""
    tests = [f"- {e}" for e in entries] or ["- (none found: test the callers above)"]
    return ["", "## Entry points to test", *tests, "", "## Order", *[f"{i}. {rule}" for i, rule in enumerate(rules, 1)],
            "", "## Done when", f"- `bp health {node['id']}` no longer lists: {', '.join(f['id'] for f in findings)}",
            "- the entry points above behave as before (their tests pass, or Try it gives the same responses)",
            "- `bp similar` shows no new repeated operation", "", "## Open questions", "- "]


def write_spec(graph: Graph, node: dict, findings: list[dict], entries: list[str], root: Path) -> None:
    """findings: from chosen_findings; entries: the entry points that reach them."""
    if not findings:
        print(f"{node['id']}: no health findings to write a spec for")
        return
    path = root / ".big-picture" / "specs" / f"{date.today().isoformat()}-{re.sub(r'[^A-Za-z0-9._-]+', '_', node['id'])}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(spec_text(graph, node, findings, entries))
    print(f"wrote {path} ({len(findings)} findings); complete its open questions, then implement it in order")
