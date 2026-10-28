# graph.json, schema version 1

Written by `scripts/build.py` to `<root>/.big-picture/out/graph.json`; read by `big-picture-query`. Both check `schemaVersion`.

```json
{
  "schemaVersion": 1,
  "builtAt": "2026-10-27T18:00:00+00:00",
  "root": "/abs/path/to/project",
  "coverage": { "python": "scip", "typescript": "approx" },
  "nodes": [], "edges": [], "findings": [], "repeats": [], "views": []
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

### Tables, views and lookups

A `table` node also carries what it is, from SQL DDL (`*.sql`, or the output of a `schema_commands` entry in `.big-picture/config.yml`, saved as `.big-picture/out/schema-<n>.sql` under a `schema` node; `stages/data/schema.py`) or, when no DDL declares it, from the model that `maps-to` it:

```json
{ "id": "table:orders", "type": "table", "kind": "table | view | materialized view | temporary table",
  "declared": true, "schema": "crm", "file": "db/schema.sql", "start": 9, "end": 16,
  "columns": [{ "name": "customer_id", "type": "integer", "pk": false, "nullable": true, "unique": false,
                "references": "customers.id", "default": "...", "check": "...", "inferred": false }],
  "constraints": ["CONSTRAINT orders_status_check CHECK (status IN ('new', 'paid'))"],
  "indexes": [{ "name": "orders_customer_idx", "unique": false, "columns": ["customer_id"] }] }
```

`schema` is the database schema a qualified name declares (`crm.orders`); the Database tab frames tables by it. `declared: false` with `inferred: true` columns means the model's fields, with `id` as the key and `<x>_id` referencing `<x>s` by naming convention.

A `lookup` node is a join or filter through a JSON column (`stages/data/lookups.py`, or a project lookup rule):

```json
{ "id": "lookup:orders.meta.customer_ref→customers.ref", "type": "lookup", "table": "orders", "column": "meta",
  "path": "customer_ref", "to_table": "customers", "to_column": "ref", "expression": "c.ref = o.meta->>'customer_ref'" }
```

### Systems and keys

- `system:<name>` nodes (`file`: the system's folder); every node with a file has `system`: the system holding it, or null.
- `keys`: names other systems reach a node by (`http:GET /orders/{}`), from type rules and OpenAPI operations.
- A node in no system with edges from two or more systems is a contract between them (a topic, a socket message).

### Notes, hashes and capsules

- Every node with source lines has `hash`: 12 hex characters of a SHA-1 of its lines (a module's whole file).
- A node with a note in `.big-picture/docs` has `doc` (its path), `docText` (the note without front matter) and `docStale` (its `source_hash` differs from `hash`).
- `capsule:<central member path>` nodes (`name`, `members`) have a `groups` edge to each member module or table.
- `views`: `{id, title, types, edges, neighbors, colors}` from `.big-picture/views`, one viewer tab each.

## Edge

```json
{ "from": "fn:app/services/order_service.py#get_order", "to": "table:orders", "kind": "reads",
  "via": "db-reads", "resolved": "exact", "sites": [["app/services/order_service.py", 6]] }
```

- `kind`: `contains`, `calls`, `handled-by`, a kind a project rule names (`reads`, `writes`, `maps-to`, ...), or from the schema and lookup stages: `defines` (a SQL file to its tables), `references` (a table to a table it has a foreign key to), `selects-from` (a view to its base tables), `looks-up` (code or a view to a lookup), `through` and `finds` (a lookup to its JSON table and the table it finds).
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
- `fix`: what to do about it, from the under-engineering and call-depth skills, or the rule's message for linter and code-standards findings.

## Repeat

```json
{ "kind": "operation", "key": "fetch_one db-reads table:orders",
  "sites": [["app/reports.py", 23, "fn:app/reports.py#order_total"], ["app/reports.py", 27, "fn:app/reports.py#order_status"]] }
```

An operation is an edge-rule match: (rule, target, call name). `operation`: the same one from two or more functions; each also gets a `repeated-operation` finding. `shape`: the same rule and call on three or more targets (8 services reading their own table the same way), information only.
