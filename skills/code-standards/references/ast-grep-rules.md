# ast-grep rule authoring (code-standards)

Checked against ast-grep 0.50. When something here disagrees with the installed version, `ast-grep scan --help` and <https://ast-grep.github.io/reference/rule.html> win.

## Files

- Rule: `.code-standards/rules/<id>.yml`, one rule per file, `id` equals the file name, prefix `cs-`.
- Fixtures: `.code-standards/rule-tests/<id>-test.yml`.
- Run everything **from the project root** with `-c .code-standards/sgconfig.yml`. `files`/`ignores` globs resolve against the paths you scan, so a root-relative path is what makes `src/api/**` match.

## Rule file

```yaml
id: cs-env-outside-config
language: Python            # the ast-grep language of the target files: Python, Tsx, Go, Ruby, Rust, Java, ...
severity: warning           # error | warning | info | hint | off
message: Read settings from app.config, not the environment   # what to do instead, one line
note: Env reads scattered across modules hide config. Taught 2026-10-20.  # the developer's reason
files: ["src/**"]           # optional: only these paths
ignores: ["src/config.py"]  # optional: never these paths
rule:
  pattern: os.getenv($$$ARGS)
# fix: optional rewrite template; see "fix" below
```

`language` is the ast-grep language of the files the rule targets. To find it for a file, honouring the project's `languageGlobs`:

```bash
ast-grep run -p '$X' --json=stream -c .code-standards/sgconfig.yml <file> | head -1   # "language": "Go"
```

The template's `languageGlobs` parses the whole JS/TS family (`.js .jsx .mjs .cjs .ts .tsx .mts .cts`) as `Tsx`, so one rule covers all of it. Every other extension uses ast-grep's built-in mapping. A rule for two languages is two files: `cs-<slug>-py` and `cs-<slug>-go`.

## Metavariables

| Syntax | Matches |
|---|---|
| `$X` | exactly one node, captured; reusing `$X` requires the same text (`$A == $A`) |
| `$$$ARGS` | zero or more nodes (arguments, statements, imports), captured |
| `$$$` | zero or more, not captured |
| `$_` | one node, not captured, no same-text constraint |

Names are UPPER_SNAKE. A pattern must parse as valid code on its own: `os.environ[$K]`, `from $M import $$$NAMES`, `import $X from "axios"`, `console.log($$$)`, `useState<$T>($$$)`, and multi-line blocks like:

```yaml
pattern: |
  try:
      $$$BODY
  except Exception:
      pass
```

In languages where a bare expression isn't valid at the top level (Go, Java, C#, Kotlin, Rust, …), a call pattern can parse as something else. `--debug-query=pattern` shows the parse: in Go, `os.Getenv($KEY)` parses as a `type_conversion_expression`. Wrap such fragments in `context` + `selector`:

```yaml
rule:
  pattern:
    context: 'func _() { os.Getenv($KEY) }'
    selector: call_expression
```

The same applies to a fragment that can't stand alone in any language, such as a class field or an object key:

```yaml
rule:
  pattern:
    context: "class A { $F = $V }"
    selector: public_field_definition
```

## Rule keys

**Atomic:** what a node is.
- `pattern`: code shape (above).
- `kind`: tree-sitter node type, e.g. `function_definition`, `call`, `class_definition` (Python), `arrow_function`, `jsx_element`, `predefined_type` (Tsx).
- `regex`: Rust regex over the node's text. Pair it with `kind` or `pattern`.

**Relational:** where a node is. Add `stopBy: end` to search all ancestors or descendants, not just the direct parent or child.
- `inside: {kind: class_definition, stopBy: end}`: the node is somewhere inside a class.
- `has: {kind: keyword_argument, regex: "^timeout", stopBy: end}`: the node contains such a descendant.
- `follows` / `precedes`: siblings before or after.
- `field: name`: inside `has`/`inside`, restrict to a named child field, such as a function's `name`.

**Composite:**
- `all: [...]`: every sub-rule matches. Without it, the keys of one rule object are an implicit "all".
- `any: [...]`: one of several spellings. This is the main refinement tool.
- `not: {...}`: carve out near-misses.
- `matches: util-id`: reuse a sub-rule defined under `utils:`.

```yaml
rule:
  any:
    - pattern: os.getenv($$$ARGS)
    - pattern: os.environ[$KEY]
    - pattern: os.environ.get($$$ARGS)
  not:
    inside:
      kind: function_definition
      has: {field: name, regex: "^_?load_"}
      stopBy: end
```

**constraints:** filter what a metavariable captured. They apply to single `$X` only, not `$$$X`.

```yaml
constraints:
  KEY: {kind: string}              # os.environ["X"] yes, os.environ[name] no
  M: {regex: "^(get|post|put|delete)$"}
```

**labels:** extra highlighted spans in the report. They only appear when that metavariable matched.

```yaml
labels:
  KEY: {style: secondary, message: the variable read here}
```

## fix

`fix` is a template using the captured metavariables. `review.py` reports it as `fix`. Apply only when the developer asks:

```bash
ast-grep scan -c .code-standards/sgconfig.yml --filter '^cs-id$' -U <files>
```

- Every metavariable in `fix` must be captured by **every** `any` branch. A missing one becomes an empty string, which produces broken code. If the branches capture different things, leave `fix` out.
- An unnamed `$$$` is not substituted, so name it: `$$$ARGS`.
- Only add `fix` when the rewrite is mechanical and always correct. Otherwise `message` says what to do.

## Fixtures

```yaml
id: cs-env-outside-config
invalid:          # must match: the flagged code verbatim, plus at least one variant
  - x = os.getenv("DB_URL")
  - |
    def connect():
        return os.getenv("DB_URL", "sqlite://")
valid:            # near-misses that must NOT match: same names, different shape or allowed context
  - x = settings.DB_URL
  - os.path.join(a, b)
  - |
    def _load_settings():
        return os.getenv("DB_URL")
```

- Keep the two-space `  - ` list style, because `check_rule.py` counts items by it.
- Quote a one-line fixture, or use a `|` block, when it contains `: `, starts with `{`, `[`, `*`, `&`, `!`, `%`, `@` or a quote, or ends with `:`. Otherwise YAML reads it as a map or tag, and `ast-grep test` fails with "invalid type: map".
- Fixtures are single snippets, so `files`/`ignores` don't apply to them. Test path scoping with the repo-wide hit count instead.
- `ast-grep test -c .code-standards/sgconfig.yml --skip-snapshot-tests --filter '^cs-id$'`. Snapshots are skipped on purpose; the valid/invalid lists are the spec.

## Debugging a pattern

```bash
ast-grep run -l python -p 'os.environ[$K]' src/           # try a pattern
ast-grep run -l python -p 'os.environ["A"]' --debug-query=ast   # see node kinds and fields
ast-grep run -l go -p 'os.Getenv($K)' --debug-query=pattern     # how the pattern itself parsed
ast-grep scan -c .code-standards/sgconfig.yml --filter '^cs-id$' --inspect entity src/x.py   # why a file was skipped
```

When a pattern doesn't match, the cause is usually one of these:
- the snippet parses differently than you expect (check `--debug-query`)
- the match sits inside a construct that a `not` excludes
- the file is outside the rule's `files` globs

## Suppression

Developers suppress one finding with a comment on the line above:

```python
# ast-grep-ignore: cs-env-outside-config
```

They can also put `// ast-grep-ignore` above a TS line, or list several ids separated by commas. ast-grep reports a suppression that no longer suppresses anything as `unused-suppression` (severity hint). Developers add suppressions; the agent never does.
