# graph.json, schema version 1

Written by `scripts/build.py` to `<root>/.big-picture/out/graph.json`; read by `big-picture-query`. Both check `schemaVersion`.

```json
{
  "schemaVersion": 1,
  "builtAt": "2026-10-27T18:00:00+00:00",
  "root": "/abs/path/to/project",
  "coverage": { "python": "scip", "typescript": "approx" },
  "nodes": [], "edges": [], "findings": []
}
```

Paths are relative to `root`. Lines are 1-based.

## Node

```json
{ "id": "fn:app/db.py#Database.insert", "type": "function", "name": "Database.insert",
  "file": "app/db.py", "start": 19, "end": 23,
  "signature": "insert( self , table : str , data : dict )", "complexity": 2, "lines": 5 }
```

| Type | Id | Source | Extra fields |
|---|---|---|---|
| `folder` | `folder:<path>` | inventory | `file` |
| `module` | `module:<path>` | inventory, one per code file | `file` |
| `function` | `fn:<path>#<name>` (`@<line>` when a name repeats in a file) | lizard; name from SCIP when defined there | `file`, `start`, `end`, `signature`, `complexity`, `lines` |
| `readme`, `doc`, `skill`, `agent-file`, `manifest`, `schema`, `migration`, `infra`, `standard` | `<type>:<path>` | inventory, by file name | `file` |
| `rule` | `rule:<file stem>` | inventory: `.code-standards/rules/*.yml` | `file` |
| any type a project rule names (`endpoint`, `model`, `table`, ...) | `<type>:<rendered id>` | `.big-picture/types`, `.big-picture/edges` | `file`, `start`, `end` for type-rule matches, which their module `contains`; list properties from `.big-picture/properties`, such as a model's `fields: [{name, type}]` |

## Edge

```json
{ "from": "fn:app/services/order_service.py#get_order", "to": "table:orders", "kind": "reads",
  "via": "db-reads", "resolved": "exact", "sites": [["app/services/order_service.py", 6]] }
```

- `kind`: `contains`, `calls`, `handled-by`, or a kind a project rule names (`reads`, `writes`, `maps-to`, ...).
- `via`: what produced it: `inventory`, `lizard`, `scip`, `ast-grep` (the calls fallback), or a project rule id.
- `resolved`: `exact`, or `approx` for calls matched by name and module where no SCIP index covered the file.
- `sites`: every `[file, line]` where the connection happens.

## Finding

```json
{ "id": "complexity:fn:app/services/order_service.py#order_total_cents", "rule": "complexity",
  "node": "fn:app/services/order_service.py#order_total_cents", "detail": "order_total_cents 14 > 10",
  "source": "call-depth", "sites": [["app/services/order_service.py", 27]] }
```

- `id` is `<rule>:<node>`: readable, and the same across builds while the node keeps its name. A rule that hits one node twice adds a site.
- `rule`: a `call-depth` kind in kebab case (`complexity`, `function-length`, `dynamic-call`, `folder-size`, ...) or the `code-standards` rule id (`cs-*`, a linter rule, `duplicate`).
- `node`: the innermost function holding the line, else the module, or the folder for folder findings.
