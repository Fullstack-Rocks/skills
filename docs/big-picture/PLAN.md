# fullstack.rocks big picture: plan

Two skills that turn a codebase into a navigable graph: modules, endpoints, tables, infra, docs, rules and skills as nodes, with programmatic edges, codebase health on every node, and a written explanation of each one. The human gets an interactive map. The agent gets the same map through a CLI and MCP tools, so neither has to explore the code by hand. `big-picture` builds the map and shows it; `big-picture-query` answers questions from it.

Concepts (Nano Banana 2.1, 16:9): [Map](concepts/concept-1.jpg) · [Database](concepts/concept-2.jpg) · [Endpoints](concepts/concept-3.jpg)

## Principles

1. **Programs find, agents explain.** Every node and every edge comes from a parser (ast-grep, OpenAPI, SQL/ORM schema, SCIP indexes). An agent decides once *what to look for* and writes it down as an ast-grep rule with fixtures. From then on the rule finds it, in seconds and for free. Agents spend tokens only on prose: what a node is for, how to use it, and naming capsules.
2. **One graph, two readers.** The viewer and the agent CLI read the same `graph.json`. Every screen in the viewer is a `bp` command with the same name, so whatever a human can see, an agent can ask for.
3. **Files, not servers.** The graph is files in the repo. The viewer ships prebuilt inside the skill, so users never need Node. Live preview is a ~150-line Python stdlib server that serves files and pushes change events, and a static export works with no server at all.
4. **Health is a finding with a location.** Every health signal is a finding with an ID, a node, a `file:line`, a measured value, a limit and a proposed fix. That makes it something an agent can collect and turn into a fix spec.
5. **Built under its own rules.** The viewer and scripts follow `under-engineering` (function ≤ 80 lines, complexity ≤ 10, depth ≤ 3, ≤ 6 files per folder, no string-keyed dispatch) and `code-standards` (run `init` in the skill before the first line of code).

## What lives where

```
skills/big-picture/                  build + view: makes the graph and shows it to the human
  SKILL.md                           modes: build, learn (type discovery), explain, view
  references/                        build.md, node-types.md, similarity.md, graph-schema.md
  scripts/                           Python 3.11+, stdlib only
    build.py                         runs the deterministic stages, writes .big-picture/out/
    serve.py                         live preview: static files + SSE change stream + /src + /proxy
    export.py                        one standalone HTML file with the graph inlined
    install_tools.py                 ast-grep, lizard, SCIP indexers, pinned, user level
    stages/                          inventory.py, index.py, health.py, similarity.py, openapi.py, capsules.py
  graph.schema.json                  the contract between the two skills (schemaVersion)
  packs/                             starter node-type packs: python-fastapi/, ts-express/, sql/, prisma/, ...
  viewer/                            TypeScript + React + Vite source
  viewer/dist/index.html             prebuilt single file, committed

skills/big-picture-query/            query: answers codebase questions from the graph, for agents
  SKILL.md                           when to ask the graph instead of grepping, and how to read answers
  references/                        verbs.md, spec.md
  scripts/
    bp.py                            CLI entry: node | neighbors | leaves | find | path | db | lookups |
                                     endpoint | health | similar | spec
    mcp_server.py                    the same verbs as MCP tools, no panel
    graph/                           load.py (graph + indexes, schemaVersion check), walk.py
    verbs/                           node.py, find.py, data.py, endpoint.py, health.py, spec.py

<project>/.big-picture/              per project
  config.toml                        scope, packs enabled, limits (taken from the project's own config when it has them)
  types/*.yml                        node types the agent learned (ast-grep rule + extraction)
  edges/*.yml                        edge rules (calls, reads, writes, jsonb-lookup, publishes, ...)
  rule-tests/*.yml                   fixtures for each type and edge rule
  capsules.yml                       capsule names and pins (human-editable)
  docs/<node-id>.md                  agent-written explanation per node, with a source hash
  specs/*.md                         fix specs written from health findings
  out/                               generated, gitignored: graph.json, health.json, similar.json
```

Everything outside `out/` is committed: the rules and docs are the team's memory of the codebase, reviewed in PRs like `.code-standards/`. `out/` is never committed: the first `build.py` run writes `.big-picture/.gitignore` with `out/`, so the project's own `.gitignore` stays untouched. When `out/graph.json` is missing (a fresh clone, CI), `serve.py` and the `bp` verbs run `build.py` first and say so in one line.

### Two skills (decided)

The split exists so the query skill can trigger on every codebase question without dragging the build instructions into each answer.

| | `big-picture` | `big-picture-query` |
|---|---|---|
| For | the human who wants the map, and the agent that builds it | any agent that needs to understand code |
| Description (draft) | Builds and shows fullstack.rocks big picture, an interactive map of a codebase: modules, endpoints, tables, infra and docs with their connections and health. Use when asked to map, visualize or document a codebase, to set up or rebuild the map, to open the viewer, or to teach it a new kind of node. | Answers questions about a codebase from its big-picture graph instead of exploring files: what a module, endpoint or table does, who calls what, how an endpoint reaches the database, where the same query repeats, what is unhealthy. Use before grepping or reading code to understand an area, and to write a fix spec from health findings. |
| Writes | `.big-picture/` (rules, docs, capsules, `out/`) | only `.big-picture/specs/` |
| Spends tokens on | type discovery, docs, capsule names | nothing: reads `graph.json` |

How they meet:
- **Contract.** `graph.schema.json` in `big-picture` defines `graph.json`, which carries `schemaVersion`. `bp` checks it on load; on a mismatch it names the skill to update instead of guessing.
- **Installed apart.** Each skill is self-contained and installs on its own (`npx skills add Fullstack-Rocks/skills --skill big-picture-query`). When `bp` finds no graph, it runs `build.py` from the `big-picture` skill installed next to it; if that skill is missing, it prints the install command once and the agent carries on with ordinary exploration.
- **No graph, no noise.** In a repo without `.big-picture/`, `big-picture-query` says so in one line and steps aside, so triggering on every question costs nothing there.
- **Same answers.** `walk.py` (query skill) and `viewer/src/data/walk.ts` (build skill) are tested against one fixture graph in this repo.

## The graph

### Node

```json
{
  "id": "fn:orders/service.py#OrderService.place",
  "type": "function",
  "name": "OrderService.place",
  "capsule": "orders",
  "tags": ["checkout", "writes:orders"],
  "loc": { "file": "orders/service.py", "start": 27, "end": 61 },
  "hash": "sha1 of the node's source",
  "props": { "signature": "place(user_id: str, cart_id: str) -> Order" },
  "doc": "docs/fn:orders~service.py#OrderService.place.md",
  "docStale": false,
  "health": { "grade": "C", "findings": ["D3", "C7", "S2"] }
}
```

IDs are `<type>:<qualified name>`, readable and stable across builds: `endpoint:POST /orders`, `table:orders`, `model:CreateOrderInput`, `lookup:orders.meta.customer_ref→customers.ref`, `capsule:orders`.

### Node types

| Family | Types | Found by |
|---|---|---|
| Code | `module`, `function`, `class`, `component`, `job`, `cli` | ast-grep packs per language and framework |
| API | `endpoint`, `operation`, `model`, `middleware` | framework rules, OpenAPI documents |
| Data | `table`, `column`, `view`, `migration`, `lookup`, `query` | SQL DDL, ORM models, migrations, learned edge rules |
| Infra | `service`, `queue`, `bucket`, `env`, `ci-job`, `container` | Dockerfile, compose, Terraform, k8s, CI YAML |
| Knowledge | `readme`, `rule`, `skill`, `adr`, `standard` | Markdown, `CLAUDE.md`/`AGENTS.md`, `.code-standards/`, `skills/*/SKILL.md` |
| Grouping | `capsule` | community detection + agent naming + `capsules.yml` |

New types are learned per project (see **Type discovery**).

### Edge

```json
{ "from": "endpoint:POST /orders", "to": "fn:...#create_order", "kind": "handled-by",
  "via": "types/endpoint.fastapi.yml", "sites": [{ "file": "routes/orders.py", "line": 26 }] }
```

Edge kinds: `calls`, `handled-by`, `guards`, `reads`, `writes`, `lookup`, `references` (FK), `validates` (model), `publishes`/`consumes`, `configures`, `documents`, `duplicates`. Every edge names the rule (`via`) that produced it, so a wrong edge is fixed by fixing a rule, never by hand.

### Health finding

```json
{ "id": "C7", "kind": "complexity", "node": "fn:...#apply_discounts",
  "loc": { "file": "billing/discounts.py", "line": 40 }, "measured": 14, "limit": 10,
  "fix": "split per discount kind; early returns", "source": "call-depth/scan.py" }
```

IDs follow `under-engineering-review`'s letters (D depth, M memory hop, C complexity, F function length, L file length, S folder size, N folder name), plus R for a code-standards rule, P for a duplicated operation and K for a structural clone. An ID is a hash of kind + node, so it survives rebuilds.

## Build pipeline

`python3 scripts/build.py` (in `big-picture`) runs the deterministic stages; the agent stages run only when the skill tells the agent to.

| # | Stage | Who | Cost | Output |
|---|---|---|---|---|
| 1 | **Inventory**: file census, manifests, READMEs, agent files, skills, OpenAPI files, schemas, migrations, infra files | script | seconds | candidate files per family |
| 2 | **Type discovery**: study how this codebase is structured; write `types/` and `edges/` rules with fixtures | agent, once per new pattern | tokens, once | rules that pass `check_rule` |
| 3 | **Index**: run every rule with `ast-grep scan --json`, parse OpenAPI and schemas, resolve calls | script | seconds | nodes + edges |
| 4 | **Health**: `call-depth` `scan.py` + `layout.py`, `code-standards` `review.py --all`, mapped onto nodes by line range | script | seconds | `health.json` |
| 5 | **Similarity**: operation fingerprints + structural clones | script | seconds | `similar.json`, P/K findings |
| 6 | **Capsules**: label propagation over the graph proposes groups; agent names them; `capsules.yml` pins win | script + agent | small | capsule nodes |
| 7 | **Explain**: write `docs/<id>.md` for nodes that are new or whose hash changed | agents, fanned out per capsule (`delegate` when the human wants it) | tokens, incremental | node docs |

Rebuilds are incremental: stage 3 re-scans changed files only, and stage 7 touches only stale docs. A doc whose `source_hash` no longer matches is shown as stale, never silently trusted.

### Call resolution

Name-matching call graphs are wrong often enough to mislead. Use the most precise source available, in the `call-depth` order (decided: SCIP first, ast-grep fallback). SCIP indexers install at user level through `install_tools.py`, pinned like ast-grep and lizard, and never into the project's manifests. A missing indexer is not an error: that language falls back to step 2, and `build.py` prints one line per language saying which source it used. Each edge carries `"resolved": "scip" | "approx" | "unresolved"`, the viewer draws `approx` edges lighter, and `bp` prints them with a `~`.

1. a **SCIP index** when the language has an indexer (`scip-typescript`, `scip-python`, `scip-go`, ...): exact definitions and references
2. **ast-grep + imports**: resolve a call through the file's imports to a definition; edges marked `approx`
3. **unresolved**: kept as an edge to `?name` and counted, so coverage is visible

Dynamic calls (`DYNAMIC_CALL`, `LOOKUP_CALL` from `scan.py`) become edges marked as memory hops, drawn dashed.

### Type discovery (part 1.4)

The agent learns the codebase's own conventions and writes them down as rules, so the next build costs nothing:

1. Start from the packs that match the census (FastAPI, Express, Prisma, SQLAlchemy, ...).
2. Sample files the packs did not explain (high fan-in, names that repeat, decorators and base classes used many times) and ask: *what kind of thing is this, and what does it connect to?*
3. For each answer, write `types/<name>.yml` or `edges/<name>.yml` (ast-grep rule, captures that give the node's name and target) and `rule-tests/<name>-test.yml`.
4. Accept the rule only when `check_rule` passes and its hit count matches what the agent expected; otherwise refine or drop it. This reuses `code-standards`' `check_rule.py` flow.

**Example: a JSONB lookup (part 1.3).** The agent sees `orders.meta->>'customer_ref' = customers.ref` in a query. It writes `edges/jsonb-lookup.yml`, which matches `$T.$COL->>'$KEY'` compared with `$T2.$COL2` across SQL strings, query-builder calls and ORM expressions. Each match becomes one `lookup` node between the two tables, with every site where the lookup happens. The Database view draws it as a diamond between the tables, the pane shows the rule and the site list, and P findings flag the sites that run the same lookup.

## Similarity (part 1.5)

Text similarity flags `if (x) return` everywhere and misses the same query written two ways. Instead, compare **what code does**, at three levels:

1. **Operation fingerprints** (main signal). Effect rules capture the operations that matter and normalize them into a canonical key:
   - query → `query(orders, where=[customer_id, status], select=[id,total], order=[created_at])`
   - HTTP call → `http(POST, payments-api:/charges)`
   - cache, queue, file and env access → `cache(get, user:{id})`, `publish(order.created)`
   Same key at two or more sites is a **P finding**: "this query runs in 4 places". Keys are compared after normalization (column order, alias names, literal values), so `select(Order).where(Order.customer_id == x)` and `SELECT ... WHERE customer_id = $1` match. Trivial code never produces a fingerprint because only effect rules create them.
2. **Structural clones** (K finding). AST subtrees with identifiers and literals anonymized, above a size floor (default 8 statements or 60 tokens), hashed. `jscpd` from `code-standards` already does the token form; this adds the AST form for clones with renamed variables.
3. **Semantic neighbours** (opt-in). Embeddings over node docs to suggest "these two functions describe the same job". Off by default because it costs tokens; every suggestion is labelled as a suggestion, never a finding.

Score per group: `sites × fragment size × (1 if same capsule else 2)`. Duplication across capsules weighs more, because that is where a shared module is missing.

## Health to spec (part 1.6)

The health output is built for an agent to walk:

```
$ bp health --capsule orders
orders  grade C  · 9 findings · 14 nodes · entry points: POST /orders, GET /orders/{id}, job:nightly_invoices
D3  depth 4/3      endpoint:POST /orders → ... → LedgerService.record     inline PaymentStep.run into place()
C7  complexity 14  fn:billing/discounts.py#apply_discounts:40             split per discount kind
P2  same query ×4  query(orders, where=[customer_id])                     one orders.by_customer()
...
$ bp spec --findings D3,C7,P2 > .big-picture/specs/2026-10-27-orders.md
```

`bp spec` writes a skeleton the agent completes: findings with locations, the affected nodes and their callers (blast radius), the entry points to test, suggested order (the fix that unlocks most first, like `under-engineering-review`'s "Fix first"), and acceptance checks phrased as `bp health` results ("C7 gone, no new D findings"). The Health screen has the same flow: select findings → **Add to fix spec**.

## Agent interface (part 2)

`bp` prints compact text by default and JSON with `--json`. Every viewer screen has a twin:

| Viewer | Agent |
|---|---|
| Map, focus on a node | `bp node <id>`: purpose, usage, called by, calls, entry points, health |
| Dive into subgraph | `bp neighbors <id> --depth 2 --dir in\|out\|both --kinds calls,reads` |
| Show leaves | `bp leaves <id>` (tables, external calls, queues it ends at) |
| Search ⌘K | `bp find <text> [--type endpoint] [--tag payments] [--capsule orders]` |
| Path between two nodes | `bp path <a> <b>` |
| Database | `bp db [table]`, `bp lookups [table]` |
| Endpoints | `bp endpoint "POST /orders"` (operation graph + request/response models) |
| Health | `bp health [--capsule X] [--kind C,D]`, `bp spec --findings ...` |
| Similar | `bp similar <id>` |

Each answer ends with the deep link for the human (`http://localhost:7478/#/n/<id>`), so the agent can point at exactly what it is talking about.

- **Skill.** `big-picture-query`'s `SKILL.md` tells agents to run `bp find` / `bp node` before grepping an unfamiliar area, and to rebuild with `big-picture`'s `build.py` after structural changes.
- **MCP.** `big-picture-query/scripts/mcp_server.py` exposes the same verbs as tools for hosts without a shell. Tools only: no panel.

## OpenAPI (part 3)

- **Find**: `openapi*.{yaml,yml,json}`, `swagger*`, and frameworks that generate one (FastAPI app → export `/openapi.json` once at build time, when the user allows running the app).
- **Map**: each operation becomes an `operation` node, matched to the code `endpoint` by method + path, then `operationId`. Schemas become `model` nodes, matched to code classes by name; mismatches (operation with no handler, handler with no spec) are findings.
- **Operation graph**: from the handler, walk `guards`, `calls`, `reads`, `writes` edges to the leaves. Show depth against the limit, like `call-depth`'s report.
- **Models**: request and response schemas as collapsible trees (type, required, enum, examples), each field linked to the column it ends up in when an edge says so.
- **Try it**: method + base URL selector (from `servers`, plus `localhost`), body editor pre-filled from examples, response viewer with status and timing, **Copy as curl**. Requests go straight from the browser; `serve.py /proxy` forwards to `localhost` targets only, for APIs without CORS. Saved requests live in `.big-picture/requests/*.http`.

## Live preview without a Node server (part 1.7)

| Option | Live updates | Needs | Use for |
|---|---|---|---|
| **`serve.py`** (chosen) | yes, within a second | Python stdlib, one process, ~10 MB | daily use, agents writing docs while you watch |
| **`export.py`** (chosen) | no (reload) | nothing: one HTML file with the graph inlined as a script | sharing, CI artifact, an Artifact page |

`serve.py`:
- serves `viewer/dist/index.html` and `.big-picture/`
- `/events`: Server-Sent Events, by polling mtimes once a second (no watcher dependency); the viewer refetches only the files that changed, so a doc an agent writes appears in the pane while you read it
- `/src?file=&start=&end=`: live source lines for the Code tab; the viewer falls back to the snippet stored in the graph when there is no server
- `/proxy`: Try-it forwarding to localhost only

Docs are **Markdown, not MDX**. MDX needs a compile step per file; Markdown renders in the browser at load. Rich parts use fenced blocks the viewer knows: ` ```bp-node <id>``` ` embeds a mini graph, ` ```bp-code file:start-end``` ` embeds live source. Agents write plain files; nothing rebuilds.

Node is needed only to work on the viewer itself (`vite build`); the built file is committed in the skill.

## The viewer

### Layout

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ [logo] fullstack.rocks big picture   Map  Database  Endpoints  Health   ⌘K  ● built 2m  ⟳ │
├──────────────┬─────────────────────────────────────────────┬────────────────┤
│ Sidebar      │ Breadcrumb: Map / Orders / orders.place()   │ Detail pane    │
│  capsules    │                                             │  overview      │
│  node types  │            canvas (React Flow)              │  code          │
│  tags        │                                             │  usage         │
│  health      │                                             │  callers       │
│  overlay     │  minimap · zoom · layout                    │  health        │
└──────────────┴─────────────────────────────────────────────┴────────────────┘
```

- **Top nav** (48 px): rock-hand logo, `fullstack.rocks` in white, `big picture` in lime; tabs Map, Database, Endpoints, Health; ⌘K search over nodes, docs and findings; build status from `graph.json`'s timestamp; Rebuild shows the command to run (the viewer never runs builds).
- **Sidebar** (260 px, collapsible): capsule tree with counts, node-type chips, tag filter, health overlay toggle.
- **Canvas**: React Flow with ELK layered layout in a web worker; capsules are group nodes that collapse and expand. Positions cached in `localStorage` per view.
- **Detail pane** (380 px, resizable): tabs below.
- **Theme**: dark first, from the brand: `#0B0D10` background, lime `#ECFE8C` accent, sky `#38BDF8`, mint `#7CF5C6`, violet `#A78BFA`, coral `#FB7185` for unhealthy. A light theme from the same tokens.

### Screens

| Screen | Canvas | Pane |
|---|---|---|
| **Map** (concept 1) | capsules → nodes, edges by kind; health rings on nodes | node overview |
| **Database** (concept 2) | UML ER: tables with columns, PK/FK, crow's-foot edges; lookup diamonds with site counts | table: columns, migrations, readers/writers; lookup: rule, sites, similar queries |
| **Endpoints** (concept 3) | operation graph left to right with depth counter; request/response trees below | Try it |
| **Health** | treemap of capsules by grade, or the graph tinted by grade | findings table → select → **Add to fix spec** |

### Node interactions (part 4)

- **Click**: opens the pane.
- **Double-click / Open subgraph**: the node's neighbourhood becomes the canvas; a breadcrumb records the dive, and Back pops it.
- **Show leaves**: collapses everything between the node and its terminal nodes into one path per leaf.
- **Fullscreen**: the node's subgraph with the pane as an overlay; route `#/n/<id>/full`.
- **Open in editor**: a `vscode://file/...` (or the configured editor) link; needs no server.
- **Copy for agent**: copies `bp node <id>`.
- Every state is a hash route (`#/map/n/<id>`, `#/db/table/orders`, `#/endpoints/POST%20/orders`, `#/health?capsule=orders`), so links are shareable and agents can print them.

### Detail pane (part 5)

| Tab | Shows |
|---|---|
| **Overview** | type badge, one-paragraph purpose, when it runs (entry points), capsule and tags, staleness of the doc |
| **Code** | the source with line numbers, live from `/src` or the stored snippet |
| **Usage** | how to call it (signature, import line), 1–3 examples from the doc, and real call sites from the graph |
| **Connections** | called by / calls / reads / writes, each clickable |
| **Health** | the node's findings with measured vs limit, similar code, "Add to fix spec" |

## Viewer source (TypeScript, React, Vite, React Flow, zustand, styled-components)

Folders hold at most six code files and name what they hold.

```
viewer/src/
  main.tsx                       mount, theme, router
  app/        App.tsx  routes.ts  theme.ts  GlobalStyle.ts
  nav/        TopNav.tsx  Search.tsx  BuildStatus.tsx
  sidebar/    Sidebar.tsx  CapsuleTree.tsx  Filters.tsx
  canvas/     Canvas.tsx  layout.worker.ts  toFlow.ts  Breadcrumb.tsx
  canvas/nodes/   CodeNode.tsx  EndpointNode.tsx  TableNode.tsx  LookupNode.tsx  CapsuleNode.tsx
  pane/       DetailPane.tsx  Overview.tsx  CodeTab.tsx  Usage.tsx  Connections.tsx  HealthTab.tsx
  database/   ErView.tsx  toEr.ts
  endpoints/  OperationView.tsx  SchemaTree.tsx  TryIt.tsx
  health/     HealthView.tsx  FindingsTable.tsx  SpecTray.tsx
  store/      graph.ts  view.ts
  data/       load.ts  live.ts  walk.ts
```

- **State.** Two zustand stores. `graph` holds what was loaded (nodes, edges, findings, docs) and indexes built once on load (`byId`, `out`, `in`, `byCapsule`, `byType`). `view` holds what the person is doing (tab, selection, dive stack, filters, overlay). Components select narrow slices.
- **Node renderers.** One component per visual family, picked by a `switch` on `node.type` in `toFlow.ts`: a typed switch with direct branches, not a lookup table, so every renderer resolves with go-to-definition.
- **Walks.** `data/walk.ts` (neighbors, leaves, path, subgraph) mirrors `big-picture-query/scripts/graph/walk.py`; both are tested against the same fixture graph, so the viewer and `bp` never disagree.
- **Libraries.** `@xyflow/react`, `elkjs`, `zustand`, `styled-components`, `react-markdown` + `remark-gfm`, `prism-react-renderer`. Build with `vite-plugin-singlefile`. Nothing else without a reason.

## Phases

| Phase | Delivers | Done when |
|---|---|---|
| 0 | `code-standards init` in both skills; this plan through the `under-engineering` checkpoint (`um-maybe`, depth, module) | checkpoint answered |
| 1 | both skill folders with draft `SKILL.md`s; `schemaVersion` + written schema (no JSON Schema file); inventory; function nodes from lizard; SCIP calls (scip-python, scip-typescript) with the ast-grep fallback; demo rules for routes and table calls, with fixtures; health from `call-depth` and `code-standards`; `bp node/neighbors/find`, text output | `bp node` answers on `demo/`, then on a larger real repo |
| 2 | Viewer: top nav, Map, pane, live `serve.py`, export | a doc written by an agent appears in the pane without reload |
| 3 | Database view, lookups, operation fingerprints, P/K findings | the demo's repeated query shows as one P finding |
| 4 | OpenAPI: operations, models, operation graph, Try it | `POST /orders` round-trips from the viewer |
| 5 | Type discovery loop with `check_rule`; capsules; agent fan-out for docs (`delegate`) | a pattern no pack knows becomes a node type with fixtures |
| 6 | Health screen, `bp spec`, MCP tools | an agent writes a fix spec from `bp health` alone |

## Phase 1 checkpoint (2026-10-27)

Hallway check, three rounds, colleague convinced. Answers: SCIP stays in phase 1, the inventory stays in phase 1, rules keep their fixtures. Simplified: `schemaVersion` plus a written schema instead of a JSON Schema file; finding IDs are readable `<rule>:<node id>` instead of hashes; full rebuilds (no incremental); source hashes wait for docs; `bp` prints text only. Other skills use `bp` through its CLI, not by importing its modules, so each skill installs on its own. After the demo, phase 1 is tested on a much larger real repo.

### Phase 1 as built (2026-10-27)

- **Functions** come from lizard (any language it parses), named from SCIP definitions, so methods read `Database.insert`.
- **SCIP** is read by a ~60-line standard-library protobuf reader (`stages/scip_index.py`), so the `scip` CLI is not needed. scip-python and scip-typescript are pinned in `big-picture/scripts/install_tools.py`. The TypeScript indexer runs only when the project root has a `tsconfig.json`.
- **Fallback** calls resolve by name and module stem, without reading imports. Without SCIP, methods have no class names, so same-named methods (`json`, `label`) stay unresolved and are counted as ambiguous.
- **Health** findings live inside `graph.json` (no separate `health.json`), with readable `<rule>:<node>` ids and a `detail` string in place of separate measured/limit/fix fields.
- **Demo** results: 214 nodes, 324 edges (95 exact calls, 17 handled-by, 16 reads, 8 writes), 22 findings, built in about 5 s. Most of that time is the two indexers, which run one after the other.

## Phase 2 checkpoint (2026-10-27)

Hallway check, three rounds, colleague convinced. Answers: search box and node-id URL hashes stay in phase 2. Simplified:
- **Layout:** dagre on the main thread instead of ELK in a worker.
- **Live updates:** the page checks `graph.json`'s modified time every 2 s instead of listening to a change stream.
- **`serve.py`:** Python's built-in file server answering only the viewer page, `graph.json` and files the graph names; everything else is a 404, and it listens on localhost only.
- **Graph walks:** two short walks in the page, with no shared test graph against Python.
- **Health:** a dot on each node, coloured by its finding count, with no overlay toggle.
- **Dropped:** the disabled Database/Endpoints/Health tabs, the light theme and the sidebar filters.
- **Links:** the URL hash holds the selected node id and nothing else.

### Phase 2 as built (2026-10-27)

- **Viewer:** `skills/big-picture/viewer/` (Vite 8, React 19, @xyflow/react 12, dagre 3, zustand 5, styled-components 6, TypeScript 7) builds to one 514 KB `dist/index.html`.
- **Map:** opens on the project's top folders. Double-click a folder or module to see its children, with the edges between everything inside them rolled up into one labelled edge per pair (`calls ×17`, `writes · reads`). Double-click any other node to see its subgraph: 3 steps downstream and 1 upstream.
- **Node pane:** type, location, signature, entry points, connections grouped by kind (each one moves the map to that node), health findings, and the live source lines. Buttons: Open subgraph, Fullscreen, Show leaves, Open in editor (a `vscode://` link).
- **Search and links:** ⌘K search uses the same matching as `bp find`. The URL hash `#/n/<id>` opens the map at that node.
- **Health:** a dot on each card, coloured by its finding count, rolled up through folders and modules.
- **Build change:** nodes made by a type rule (endpoints) are now `contains` children of their module, so they show up when you dive into a module.

### Viewer feedback round (2026-10-27)

- **Birds-eye project page:** every module and file, nested inside folder frames, with tables in a Database frame. Calls, reads and writes are rolled up per pair of modules.
- **Diving into a folder:** the same picture for that folder, plus the outside modules and tables it talks to.
- **Diving into a module:** its full usage graph, function by function: callers, callees and tables, each inside its own module frame.
- **Layout:** ELK replaced dagre, because nested frames need per-group layout. Groups whose members connect are layered; groups whose members don't are packed into a grid. Edges between groups are lifted to the level where they cross, with room reserved for labels.
- **Interaction:** nodes can be dragged. Selecting a node or frame animates its edges in both directions and fades the rest. The pane can be resized, and its width is remembered.
- **Pane:**
  - a plain-language description for every node type
  - tables list each access with its line of code
  - the source opens in Monaco, with the language picked from the file extension, scrolled to and highlighting the node's lines
- **Brand:** the logo is white, and "big picture" is set in the brand gradient.
- **Size:** the viewer file is now 5.5 MB (1.5 MB gzipped), mostly Monaco. The DOMPurify that Monaco depends on is pinned to 3.4.17 for security advisories.

### Phase 3 and 4 as built (2026-10-27)

- **Phase 3, data:** SQL DDL gives tables, views, materialized views and temporary tables with keys, constraints and indexes. Tables no DDL declares are inferred from their models and marked so. JSON lookups in SQL become lookup nodes.
- **Phase 3, health:** repeated operations are health findings, while repeated shapes across tables are recorded as information only. Every finding has a fix, and agents get `bp health`, `bp similar` and `bp db`.
- **Phase 3, viewer:** the Database tab, connection focus, dragging that pushes cards and grows frames, and frame options (Arrange with Reset, Fit, Open).
- **Phase 4:** OpenAPI JSON or YAML gives operation and api-model nodes. Operations are matched to code endpoints across parameter names, and both kinds of mismatch are findings. Agents get `bp endpoint`; the viewer gets an Endpoints tab, model trees and a Try it panel through `serve.py`'s localhost-only proxy.
- **Lenses (asked for during phase 4):**
  - `.big-picture/patterns/` holds regex rules for files ast-grep can't parse.
  - `.big-picture/views/` files add viewer tabs and `bp view` listings, with brand colours and gradients per type and kind.
  - The fixture carries a Cache lens (Redis, Valkey) and a Config lens (`.env` keys).

### Phase 5 and 6 as built (2026-10-27)

- **Notes:** agents write `.big-picture/docs/<slug>.md` with the node's hash. The pane shows a note live, before any rebuild, and the build marks it stale when the code changes. `bp node` prints the note. Fanning out note writing goes through `delegate`, as an instruction in the skill.
- **Capsules:** label propagation over modules and tables, with hubs (shared helpers) left out. Capsules are named and pinned in `capsules.yml`. Agents get `bp capsules`; the viewer gets a Capsules tab.
- **Health:** the Health tab shows every node with findings. `bp spec <part>` writes a fix spec with findings, fixes, callers that could break, entry points to test, an order, done-when checks and open questions.
- **MCP:** `big-picture-query/scripts/mcp_server.py` (standard-library stdio JSON-RPC) offers every `bp` verb as a tool, by running `bp.py`.
- **Limits exceeded, with reasons:**
  - `viewer/src/data/describe.ts` `subtitle` (complexity about 16): a flat switch from node type to a one-line summary. Splitting it would push its helpers past depth 3.
  - `Graph.add_edge`, `Graph.add_finding` (7 parameters each): every parameter is a field of the stored record.
  - Measurement artifact: lizard misreads part of `viewer/src/pane/ApiPanel.tsx` as one long function; its real functions are short.

## Decisions for you

1. ~~**Live preview**~~ **Decided 2026-10-27:** Python stdlib `serve.py` for live preview, plus `export.py` for static sharing. No Claude Code pane and no MCP App panel: the viewer lives in the browser only.
2. ~~**Call graph precision**~~ **Decided 2026-10-27:** SCIP indexers where a language has one, ast-grep import resolution as the fallback with edges marked `approx`.
3. ~~**One skill or two**~~ **Decided 2026-10-27:** two. `big-picture` (build + view) and `big-picture-query` (agent queries and fix specs), joined by `graph.schema.json`; see **Two skills**.
4. ~~**Commit `out/graph.json`?**~~ **Decided 2026-10-27:** no. `.big-picture/out/` stays gitignored and `build.py` regenerates it.
5. ~~**First stack**~~ **Decided 2026-10-27:** phase 1 runs on the `demo/` shop in this repo.
