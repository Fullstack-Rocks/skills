---
name: under-engineering-review
description: Reviews existing code against the under-engineering limits (call depth, memory hops, complexity, function, file and folder size). Use when asked to review, audit or assess a route, module, folder, package or diff for how complicated, deep or traceable it is.
---

# Under-engineering review

Produces one short report that the developer can decide from and an agent can act on. All measuring goes through the `call-depth` skill and its scripts; this skill decides the scope and the report. The code under review is **existing code**: propose fixes, and change nothing unless the developer asks.

## 1. Scope

Turn the request into:

- **files:** the paths, the package, or the files changed since a ref (`git diff --name-only <ref>`)
- **roots:** the routes, tools, jobs, commands or public functions in scope

Done when you have a root list and a starting file list.

## 2. Trace

Load `call-depth` and settle which tools you'll use (ask about any outside the project's environment). Run the language adapter on the starting files so the memory hops are known, then trace each root: weighted depth, memory hops, and the deepest path. For a route or feature, every file the trace reaches joins the file list, and the files on the traced paths are **on-path**.

Done when every root has a traced chain and the file list is complete.

## 3. Measure

Run everything programmatically over the file list:

1. `layout.py` on the folders
2. the language adapter on the files
3. the complexity tool at the project's threshold, or 10

Redirect output to `/tmp/uer-<scope>.txt` along with the full chains, and read it back with `grep`/`cut` in the terminal, so raw output never fills the context. Read code only to confirm flags and to measure nesting for over-threshold functions.

Done when every check has run, or is listed as blocked with the reason.

## 4. Spot governance

While tracing, note any code that enforces policy rather than product behaviour: IP or region allow-lists, retention and deletion schedules, compliance gates, policy-level rate limits. Each one is an infrastructure candidate. Report it; don't judge it.

## 5. Report

Use this format. Counts and findings cover **on-path** code only; give scope-wide totals in one line under the table. List the 10 worst findings; the rest stay in the raw file. Governance items get their own list and don't count toward the 10.

```
Under-engineering review: <scope>
Tools: <tool version (source)>, ...   Raw: /tmp/<file>

| Check           | Limit   | On-path | Worst              |
|-----------------|---------|---------|--------------------|
| Call depth      | 3       | <n>/<roots> | <depth> <root> |
| Memory hops     | 0       | <n>     | <kind> <location>  |
| Complexity      | <N>     | <n>     | <score> <function> (nesting <n>) |
| Function length | 80      | <n>     | <lines> <function> |
| File length     | 1000    | <n>     | <lines> <file>     |
| Folder size     | 6       | <n>     | <files> <folder>   |
| Folder names    | 3 words | <n>     | <folder>           |
Scope-wide: <n> complexity, <n> function length, ... (raw file)

Findings (worst first)
ID  Check  Location  Measured  Proposed fix
<D1 / M1 / C1 / F1 / L1 / S1 / N1 ...>   one line each
Sub-roots: <[dep]/[mw] chains over the limit, with depth>

Governance (reported, not judged)
G1  <location>  <policy>  <infrastructure option>

Fix first (at most 3): <ID>: <why this one unlocks the most>
```

Every fix is one line, and every finding has an ID so the developer can say "do M1 and C2". Done when each check has a row and each finding has a location, a measured value and a proposed fix.
