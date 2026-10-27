# Teaching node types and edges

The project's rules live in `<root>/.big-picture/`:

```
.big-picture/
  sgconfig.yml          ruleDirs: [types, edges, properties]; testConfigs: [{testDir: rule-tests}]
  types/<id>.yml        a match is a new node
  edges/<id>.yml        a match is an edge from the code around it
  properties/<id>.yml   a match adds a value to the node around it (a model's fields)
  rule-tests/<id>-test.yml
```

`sgconfig.yml`:

```yaml
# big-picture: this project's node and edge rules. Format: big-picture's references/node-types.md.
ruleDirs: [types, edges, properties]
testConfigs:
  - testDir: rule-tests
```

Each rule is an ordinary ast-grep rule (`id`, `language`, `rule`, optional `constraints`, `message`). Its `metadata` says what a match means. In templates, `{NAME}` is the text of capture `$NAME` with string quotes stripped, and filters transform it: `{NAME|snake|plural}` turns `OrderItem` into `order_items` (`lower`, `snake`, `plural`).

The build applies type rules first, then edge and property rules (so they can land inside the nodes type rules made), then type rules' `links`.

## Type rule: a match is a node

```yaml
id: endpoint-route
language: Python
message: HTTP endpoint registered with app.http.route
rule:
  kind: decorated_definition
  all:
    - has: { field: definition, pattern: def $HANDLER($$$PARAMS) }
    - has: { kind: decorator, has: { pattern: route($METHOD, $PATH) } }
metadata:
  node: endpoint            # node type
  id: "{METHOD} {PATH}"     # node id becomes endpoint:GET /orders/{id}
  link: handled-by          # optional: an edge from the new node...
  to: HANDLER               # ...to the function whose definition holds this capture
```

The node gets the match's file and line range, and its module `contains` it.

A type rule can also declare `links`: edges from the new node to a node named by a template, kept only when that node exists. This is how a model finds its table by naming convention:

```yaml
id: model-dataclass
language: Python
rule:
  kind: decorated_definition
  all:
    - has: { kind: decorator, regex: ^@dataclass }
    - has: { field: definition, kind: class_definition, has: { field: name, pattern: $NAME } }
metadata:
  node: model
  id: "{NAME}"
  links:
    - kind: maps-to
      to: "table:{NAME|snake|plural}"   # Order -> table:orders, only if the code accesses that table
```

## Edge rule: a match is an edge

```yaml
id: db-reads
language: Python
message: reads a table through app.db.Database
rule:
  any:
    - pattern: $DB.fetch_one($TABLE, $$$REST)
    - pattern: $DB.fetch_many($TABLE, $$$REST)
constraints:
  TABLE: { kind: string }   # only literal table names
metadata:
  edge: reads               # edge kind
  to: "table:{TABLE}"       # target id: <type>:<name>; created when new
```

The edge starts at the innermost function (or endpoint) holding the match, else the file's `module:` node.

## Property rule: a match adds to the node around it

```yaml
id: model-field
language: Python
rule:
  kind: expression_statement
  has:
    kind: assignment
    all:
      - has: { field: left, pattern: $FIELD }
      - has: { field: type, pattern: $TYPE }
  inside: { kind: block, inside: { kind: class_definition, inside: { kind: decorated_definition, has: { kind: decorator, regex: ^@dataclass } } } }
metadata:
  property: fields              # a list on the node around the match
  value: { name: "{FIELD}", type: "{TYPE}" }
```

The values are appended in source order to the innermost node with a line range around the match (here the model). A table's columns are the `fields` of the model that `maps-to` it.

Edge kinds in use: `contains`, `calls`, `handled-by`, `reads`, `writes`, `maps-to`. Name a new kind as a verb from the source's side (`publishes`, `guards`, `lookup`), and reuse an existing kind when the meaning matches.

## Fixtures

```yaml
id: db-reads
valid:                       # near-misses: same names, other shapes
  - db.fetch_one(table, row_id)
  - fetch_one("orders", 1)
invalid:                     # must match
  - db.fetch_one("orders", order_id)
  - get_db().fetch_many("orders", limit=limit)
```

Quote a case in YAML when it holds `{`, `:` or `#`.
