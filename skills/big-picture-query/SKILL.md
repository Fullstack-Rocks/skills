---
name: big-picture-query
description: Answers codebase questions from the big-picture graph instead of exploring files, such as what a function, endpoint or table touches, who calls it, which endpoints reach it, and where it is unhealthy. Use before grepping or reading code to understand an area, in any repo with a .big-picture/ folder.
---

# Big picture query

`scripts/bp.py` answers from `.big-picture/out/graph.json`, the graph the `big-picture` skill builds with parsers. One `bp` call replaces a round of grep and file reads, so **ask the graph first**, then read only the code it points you to.

If the repo has no `.big-picture/` folder, say so in one line, mention the `big-picture` skill can build one, and continue the usual way. If the folder exists but the graph doesn't, `bp` builds it first.

## Ask

Run `python3 scripts/bp.py <verb>` from anywhere inside the project:

| Question | Command |
|---|---|
| What is this, what does it touch, who uses it, is it healthy? | `bp node <id or name>` |
| What happens downstream of this endpoint? | `bp neighbors "POST /orders" --dir out --depth 4 --kinds handled-by,calls,reads,writes` |
| What breaks if this changes? | `bp neighbors <name> --dir in --depth 3` |
| Where is X? | `bp find <text> [--type endpoint\|table\|function\|module\|folder\|readme\|...]` |
| What is wrong here, and how do I fix it? | `bp health <id or name>` (findings on it and inside it, with where and how) |
| Does this repeat work done elsewhere? | `bp similar <id or name>` |
| What does the database look like? | `bp db`, then `bp node table:<name>` for a table's columns, keys, constraints and indexes |

Names work as well as ids: `bp node order_service.get_order`, `bp node table:orders`, `bp node "GET /orders/{id}"`. An ambiguous name prints the candidates; pick an id from them.

## Read the answer

- `bp node` prints the node's **entry points** (endpoints, jobs and CLIs that reach it), its outgoing edges by kind, its incoming edges by kind (`called by`, `read by`, `handles`, `in`), and its **health** findings with the rule that raised them.
- Each edge shows where it happens (`file:line`, `+n` more sites). Open those lines when you need the code itself.
- To fix health findings, run `bp health <part>` and work from its list: each rule's line says how, each finding says where. Rebuild after fixing and run it again.
- An edge marked `~` was matched by name because no type-aware index covered that file. Confirm it in the code before relying on it.
- A missing edge may be a convention the graph hasn't been taught. When you find one (a route style, a data-access call), tell the developer and offer to teach it with the `big-picture` skill.

## Keep it current

After a change that adds, renames or moves functions, endpoints or tables, rebuild with the `big-picture` skill's `scripts/build.py` before the next question.
