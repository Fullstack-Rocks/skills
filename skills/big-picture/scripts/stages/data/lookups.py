"""Stage 7: lookups through JSON columns. A lookup joins or filters one table by a path inside
another table's JSON column (orders.meta->>'customer_ref' = customers.ref). SQL in .sql files and in
code strings is scanned for the JSON operators of Postgres, SQLite and MySQL; table aliases come from
the statement's FROM and JOIN. Each distinct lookup is one node, with an edge from every place that
runs it. ORM-style lookups come in through project rules (rules.py) and land on the same nodes."""
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

from graph import Graph
from stages.data.schema import statements

PACKS = Path(__file__).resolve().parents[3] / "packs"
# A JSON path on alias.column, in each dialect's spelling; `path` is the raw path text.
JSON_PATHS = [
    r"(?P<alias>\w+)\.(?P<column>\w+)\s*(?P<path>(?:->>?\s*'[^']+'\s*)+)",                      # Postgres ->, ->>
    r"(?P<alias>\w+)\.(?P<column>\w+)\s*#>>?\s*'(?P<path>\{[^}]+\})'",                          # Postgres #>> '{a,b}'
    r"json_(?:extract|value)\s*\(\s*(?P<alias>\w+)\.(?P<column>\w+)\s*,\s*'(?P<path>\$[^']*)'\s*\)",  # SQLite, MySQL
    r"jsonb?_extract_path(?:_text)?\s*\(\s*(?P<alias>\w+)\.(?P<column>\w+)\s*,(?P<path>[^)]*)\)",  # Postgres functions
]
CAST = r"\s*\)?\s*(?:::\s*\w+)?\s*"
PLAIN = r"(?P<other_alias>\w+)\.(?P<other_column>\w+)\b(?!\s*(?:->|#>))"
LOOKUPS = [re.compile(p + CAST + r"=\s*\(?\s*" + PLAIN, re.I) for p in JSON_PATHS] + \
          [re.compile(PLAIN + r"\s*=\s*\(?\s*" + p, re.I) for p in JSON_PATHS]
TABLE_REFERENCE = re.compile(r"\b(?:from|join)\s+([\w.\"]+)(?:\s+(?:as\s+)?(?!(?:on|where|join|left|right|inner|outer|cross|full|group|order|limit|using)\b)(\w+))?", re.I)
WORTH_SCANNING = re.compile(r"->|#>|json_", re.I)


def path_of(raw: str) -> str:
    """'customer_ref' / '$.customer.ref' / '{customer,ref}' / 'customer', 'ref' -> customer.ref"""
    keys = re.findall(r"'([^']*)'", raw) or [raw]
    return ".".join(k.strip("{}$. ").replace(",", ".") for k in keys if k.strip("{}$. "))


def aliases(sql: str) -> dict[str, str]:
    """alias (and bare table name) -> table, from the statement's FROM and JOIN clauses."""
    found = {}
    for table, alias in TABLE_REFERENCE.findall(sql):
        name = table.split(".")[-1].strip('"').lower()
        found[name] = name
        if alias:
            found[alias.lower()] = name
    return found


def add_lookup(graph: Graph, spec: dict, site: tuple[str, int], via: str) -> None:
    """One lookup node per distinct (table.column.path -> table.column), with an edge from the code at `site`."""
    name = f"{spec['table']}.{spec['column']}.{spec['path']}→{spec['to_table']}.{spec['to_column']}"
    lookup = graph.add_node(f"lookup:{name}", "lookup", name, **spec)
    for table, kind in ((spec["table"], "through"), (spec["to_table"], "finds")):
        graph.add_node(f"table:{table}", "table", table)
        graph.add_edge(lookup, f"table:{table}", kind, via)
    graph.add_edge(graph.enclosing(*site), lookup, "looks-up", via, site=site)


def scan_sql(sql: str, file: str, first_line: int) -> list[tuple[dict, tuple[str, int]]]:
    """Every lookup in one SQL statement, with the file and line it happens at."""
    tables, found = aliases(sql), []
    for pattern in LOOKUPS:
        for m in pattern.finditer(sql):
            json_table, other_table = tables.get(m["alias"].lower()), tables.get(m["other_alias"].lower())
            if not json_table or not other_table:
                continue
            spec = {"table": json_table, "column": m["column"].lower(), "path": path_of(m["path"]),
                    "to_table": other_table, "to_column": m["other_column"].lower(), "expression": " ".join(m[0].split())}
            found.append((spec, (file, first_line + sql.count("\n", 0, m.start()))))
    return found


def code_strings(root: Path, files: list[str]) -> list[tuple[str, str, int]]:
    """(text, file, 1-based line) of every string literal that might hold JSON SQL."""
    found = []
    for rule in sorted(PACKS.glob("*/strings*.yml")):
        result = subprocess.run(["ast-grep", "scan", "--rule", str(rule), "--json=compact", *files],
                                cwd=root, capture_output=True, text=True, check=False, stdin=subprocess.DEVNULL)
        found += [(m["text"], m["file"], m["range"]["start"]["line"] + 1) for m in json.loads(result.stdout or "[]")
                  if WORTH_SCANNING.search(m["text"])]
    return found


def add_lookups(graph: Graph, files: list[str], code: list[str]) -> int:
    """Scan .sql files statement by statement and code strings; returns the number of lookup sites."""
    found = []
    for file in (f for f in files if PurePosixPath(f).suffix == ".sql"):
        for sql, line in statements((graph.root / file).read_text(errors="replace")):
            found += scan_sql(sql, file, line) if WORTH_SCANNING.search(sql) else []
    for text, file, line in code_strings(graph.root, code) if code else []:
        found += scan_sql(text, file, line)
    for spec, site in found:
        add_lookup(graph, spec, site, "sql")
    return len(found)
