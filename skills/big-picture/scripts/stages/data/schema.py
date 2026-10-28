"""Stage 6: what each table is. SQL DDL (*.sql, and the output of each `schema_commands` entry in
.big-picture/config.yml, such as an ORM's DDL printer) declares tables, views, materialized views and
temporary tables with their columns, keys, constraints and indexes. A table no DDL declares takes its
columns from the model mapped to it, with keys inferred by naming convention and marked inferred."""
import os
import re
import subprocess
from pathlib import Path, PurePosixPath

from graph import Graph

CREATE = re.compile(r"create\s+(?:or\s+replace\s+)?(?P<temp>(?:global\s+|local\s+)?temp(?:orary)?\s+|unlogged\s+)?"
                    r"(?P<kind>materialized\s+view|view|table)\s+(?:if\s+not\s+exists\s+)?(?P<name>[\w.\"`]+)", re.I)
INDEX = re.compile(r"create\s+(?P<unique>unique\s+)?index\s+(?:concurrently\s+)?(?:if\s+not\s+exists\s+)?(?P<name>[\w\"]+)\s+"
                   r"on\s+(?P<table>[\w.\"]+)\s*(?:using\s+\w+\s*)?\((?P<columns>[^)]*)\)", re.I)
ALTER_FK = re.compile(r"alter\s+table\s+(?:only\s+)?(?P<table>[\w.\"]+)\s+add\s+(?:constraint\s+\w+\s+)?foreign\s+key\s*"
                      r"\((?P<column>[^)]*)\)\s*references\s+(?P<target>[\w.\"]+)\s*(?:\((?P<target_column>[^)]*)\))?", re.I)
REFERENCES = re.compile(r"references\s+(?P<table>[\w.\"]+)\s*(?:\((?P<column>[^)]*)\))?", re.I)
DEFAULT = re.compile(r"default\s+((?:'[^']*'|\([^)]*\)|[\w.:]+)(?:\([^)]*\))?)", re.I)
CHECK = re.compile(r"check\s*\((.*)\)", re.I | re.S)
TYPE_END = re.compile(r"\s(?:primary|not|null|unique|default|references|check|constraint|generated|collate)\b", re.I)
TABLE_CONSTRAINT = re.compile(r"(constraint|primary|foreign|unique|check)\b", re.I)
FROM_JOIN = re.compile(r"\b(?:from|join)\s+([\w.\"]+)", re.I)


def schema_of(name: str) -> str | None:
    """crm."Orders" -> crm: the schema a qualified name declares, or None."""
    parts = name.strip().split(".")
    return parts[-2].strip("\"`").lower() if len(parts) > 1 else None


def bare(name: str) -> str:
    """public."Orders" -> orders: the name code uses, without schema or quotes."""
    return name.strip().split(".")[-1].strip("\"`").lower()


def statements(text: str) -> list[tuple[str, int]]:
    """SQL statements with their 1-based start line; comments dropped, string contents kept."""
    clean = re.sub(r"--[^\n]*", "", re.sub(r"/\*.*?\*/", lambda m: "\n" * m[0].count("\n"), text, flags=re.S))
    found, start = [], 0
    for part in re.split(r";(?=(?:[^']*'[^']*')*[^']*$)", clean):
        if part.strip():
            found.append((part.strip(), clean.count("\n", 0, start + len(part) - len(part.lstrip())) + 1))
        start += len(part) + 1
    return found


def split_top_level(body: str) -> list[str]:
    """Comma-separated items of a CREATE TABLE body, not splitting inside parentheses or strings."""
    items, depth, quoted, current = [], 0, False, ""
    for char in body:
        quoted ^= char == "'"
        depth += (char == "(") - (char == ")") if not quoted else 0
        if char == "," and depth == 0 and not quoted:
            items.append(current.strip())
            current = ""
        else:
            current += char
    return [i for i in [*items, current.strip()] if i]


def table_body(statement: str, after: int) -> str:
    """The text between the parenthesis that opens after `after` and the one that closes it."""
    opening = statement.find("(", after)
    depth = 0
    for i in range(max(opening, 0), len(statement)):
        depth += (statement[i] == "(") - (statement[i] == ")")
        if depth == 0:
            return statement[opening + 1:i]
    return ""


def column(item: str) -> dict:
    """One column definition; a REFERENCES target stays raw until add_references names it."""
    name, _, rest = item.partition(" ")
    lowered = rest.lower()
    type_end = TYPE_END.search(" " + rest)
    found = {"name": name.strip("\"`").lower(), "type": (rest[:type_end.start()] if type_end else rest).strip(),
             "pk": "primary key" in lowered, "nullable": "not null" not in lowered and "primary key" not in lowered,
             "unique": " unique" in f" {lowered}"}
    if (default := DEFAULT.search(rest)):
        found["default"] = default[1]
    if (reference := REFERENCES.search(rest)):
        found["references"] = (reference["table"], reference["column"] or "id")
    if (check := CHECK.search(rest)):
        found["check"] = check[1].strip()
    return found


def table_constraint(item: str, named: list[str], columns: dict[str, dict]) -> str:
    """Apply a table-level PRIMARY KEY / FOREIGN KEY / UNIQUE to the columns it names; returns its text."""
    lowered = item.lower()
    reference = REFERENCES.search(item)
    for name in named:
        target = columns.get(name, {})
        if "primary key" in lowered:
            target.update(pk=True, nullable=False)
        elif "foreign key" in lowered and reference:
            target["references"] = (reference["table"], reference["column"] or "id")
        elif "unique" in lowered and len(named) == 1:
            target["unique"] = True
    return " ".join(item.split())


def create_kind(create: re.Match) -> str:
    """table, temporary table, view or materialized view."""
    kind = " ".join(create["kind"].lower().split())
    return f"temporary {kind}" if "temp" in (create["temp"] or "").lower() else kind


def parse_create(statement: str, create: re.Match) -> dict:
    """A CREATE TABLE / VIEW / MATERIALIZED VIEW statement as its name, kind, columns, constraints or base tables."""
    kind = create_kind(create)
    parsed = {"name": bare(create["name"]), "schema": schema_of(create["name"]), "kind": kind, "lines": statement.count("\n")}
    if "view" in kind:
        return parsed | {"bases": sorted({bare(t) for t in FROM_JOIN.findall(statement[create.end():])})}
    items = split_top_level(table_body(statement, create.end()))
    columns = {c["name"]: c for c in (column(i) for i in items if not TABLE_CONSTRAINT.match(i))}
    constraints = [table_constraint(i, [bare(c) for c in table_body(i, 0).split(",") if c.strip()], columns)
                   for i in items if TABLE_CONSTRAINT.match(i)]
    return parsed | {"columns": list(columns.values()), "constraints": constraints}


def put_table(graph: Graph, parsed: dict, site: tuple[str, int]) -> None:
    """A parsed CREATE statement onto its table node, linked to the file that defines it and, for a view, its bases."""
    file, line = site
    table_id = graph.add_node(f"table:{parsed['name']}", "table", parsed["name"], file=file, start=line,
                              end=line + parsed["lines"], kind=parsed["kind"], schema=parsed["schema"], declared=True,
                              columns=parsed.get("columns"), constraints=parsed.get("constraints"))
    holder = f"schema:{file}" if f"schema:{file}" in graph.nodes else f"migration:{file}"
    graph.add_edge(holder, table_id, "defines", "schema", site=site)
    for base in parsed.get("bases", []):
        graph.add_node(f"table:{base}", "table", base)
        graph.add_edge(table_id, f"table:{base}", "selects-from", "schema", site=site)


def add_index_or_fk(graph: Graph, statement: str) -> None:
    """CREATE INDEX and ALTER TABLE ... ADD FOREIGN KEY onto the table they name."""
    if (index := INDEX.match(statement)):
        table = graph.nodes.get(f"table:{bare(index['table'])}")
        if table is not None:
            table.setdefault("indexes", []).append({"name": bare(index["name"]), "unique": bool(index["unique"]),
                                                    "columns": [c.strip() for c in index["columns"].split(",")]})
    elif (fk := ALTER_FK.match(statement)):
        for col in graph.nodes.get(f"table:{bare(fk['table'])}", {}).get("columns", []):
            if col["name"] == bare(fk["column"]):
                col["references"] = (fk["target"], fk["target_column"] or "id")


def infer_from_model(graph: Graph, table: dict) -> None:
    """Columns for a table no DDL declares: its model's fields; id is the key, <x>_id points at <x>s."""
    models = [source for source, target, kind in graph.edges if target == table["id"] and kind == "maps-to"]
    columns = []
    for field in graph.nodes[models[0]].get("fields", []) if models else []:
        name, kind = field["name"], field["type"]
        found = {"name": name, "type": kind, "pk": name == "id", "nullable": "None" in kind or "Optional" in kind,
                 "unique": name == "id", "inferred": True}
        if name.endswith("_id") and f"table:{name.removesuffix('_id')}s" in graph.nodes:
            found["references"] = (f"{name.removesuffix('_id')}s", "id")
        columns.append(found)
    if columns:
        table.update(columns=columns, kind="table", declared=False)


def add_references(graph: Graph, table: dict) -> None:
    """Name each column's REFERENCES target (orders.id) and draw the table-to-table edge."""
    for col in table.get("columns", []):
        if isinstance(col.get("references"), tuple):
            target_table, target_column = col["references"]
            col["references"] = f"{bare(target_table)}.{bare(target_column)}"
            target = graph.add_node(f"table:{bare(target_table)}", "table", bare(target_table))
            declared = bool(table.get("declared"))
            graph.add_edge(table["id"], target, "references", "schema" if declared else "naming convention",
                           "exact" if declared else "approx", site=(table.get("file", ""), table.get("start", 0)) if declared else None)


def generated_schema(graph: Graph, commands: list[str], scripts: Path) -> list[str]:
    """Run each schema command from the project root ({scripts} is big-picture's scripts folder) and keep
    its DDL as .big-picture/out/schema-<n>.sql, a schema node; returns those paths for add_schema."""
    paths = []
    for number, command in enumerate(commands, 1):
        result = subprocess.run(command.replace("{scripts}", str(scripts)), shell=True, cwd=graph.root, capture_output=True,
                                text=True, check=False, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        if result.returncode != 0:
            print(f"schema: command {number} failed: {(result.stderr.strip().splitlines() or ['no output'])[-1]}")
            continue
        path = f".big-picture/out/schema-{number}.sql"
        (graph.root / path).write_text(result.stdout)
        graph.add_node(f"schema:{path}", "schema", f"schema from command {number}", file=path, command=command)
        paths.append(path)
    return paths


def add_schema(graph: Graph, files: list[str]) -> None:
    for file in [f for f in files if PurePosixPath(f).suffix == ".sql"]:
        for statement, line in statements((graph.root / file).read_text(errors="replace")):
            create = CREATE.match(statement)
            if create:
                put_table(graph, parse_create(statement, create), (file, line))
            else:
                add_index_or_fk(graph, statement)
    finish_tables(graph)


def finish_tables(graph: Graph) -> None:
    """Columns for tables no DDL declares, then every table's references named and drawn."""
    tables = [n for n in graph.nodes.values() if n["type"] == "table"]
    for table in [t for t in tables if not t.get("declared")]:
        infer_from_model(graph, table)
    for table in tables:
        add_references(graph, table)
