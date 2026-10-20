# Languages

`scan.py` doesn't depend on any one language. lizard measures length and complexity, and ast-grep runs one rule pack per language for memory hops. Neither needs a runtime from the target project. Use the project's own configured tools first when it has them (table below).

## What scan.py covers

**Function length and complexity (lizard):** C/C++, C#, Erlang, Fortran, GDScript, Go, Java, JavaScript/TypeScript/TSX, Kotlin, Lua, Objective-C, Perl, PHP, PL/SQL, Python, R, Ruby, Rust, Scala, Solidity, Swift, TTCN, Vue and Zig.

**Memory hops (ast-grep rule packs in `scripts/rules/`):**

| Pack | Language | `DYNAMIC_CALL` | `DYNAMIC_ATTR` | `LOOKUP_CALL` |
|---|---|---|---|---|
| `python.yml` | Python | `getattr(...)(...)`, `eval`, `exec`, `__import__`, `import_module`, `methodcaller`, `globals()`, `locals()` | `getattr`/`setattr` with a non-constant name | `handlers[k](...)` |
| `js-ts.yml` | JS, TS, TSX (all as Tsx) | `eval`, `new Function`, `require(x)`, `import(x)`, `Reflect.apply/construct/get` | — | `obj[k](...)` |
| `go.yml` | Go | `MethodByName`, `FieldByName`, reflect `.Call` | — | `m[k](...)` (or a generic instantiation; confirm) |
| `ruby.yml` | Ruby | `send`, `public_send`, `instance_eval`, `class_eval`, `define_method`, `eval` | `const_get`, `instance_variable_get` | `H[k].call(...)` |
| `java.yml` | Java | `Class.forName`, `getMethod`, `invoke`, `newInstance` | — | — |
| `csharp.yml` | C# | `Activator.CreateInstance`, `GetMethod`, `GetType`, `Invoke`, `InvokeMember` | — | — |
| `php.yml` | PHP | `call_user_func(_array)`, `$fn(...)`, `$obj->$method(...)` | — | — |

Any other language shows up as `NO_RULES`. Use the grep fallback for it, or add a pack.

## Adding a rule pack

1. Find the ast-grep language id: `ast-grep run -p '$X' --json=stream -c scripts/sgconfig.yml <file> | head -1` and read `"language"`.
2. Write `scripts/rules/<language>.yml`, one rule per document (separated by `---`). Each `id` must contain the finding kind (`<lang>-dynamic-call-<what>`, `<lang>-dynamic-attr-<what>` or `<lang>-lookup-call-<what>`); `scan.py` maps findings by that substring. The `message` says what the pattern means.
3. Write `scripts/rule-tests/<id>-test.yml` with `invalid` (must match) and `valid` (near-misses) cases, and run `ast-grep test -c scripts/sgconfig.yml --skip-snapshot-tests`.

Prefer `kind` + `has: {field: ...}` + `regex` over code patterns: they survive grammar quirks. In Go, Java, C# and other languages where a bare call isn't valid at the top level, wrap any `pattern` in `context` + `selector`, and wrap fixtures in a function. `--debug-query=ast` shows how a snippet parses. tree-sitter-go, for example, parses `m[k](x)` as a generic type conversion.

## Structural interfaces

Calls through a structural interface are memory hops: the implementation is found by search, not by go-to-definition.

| Language | Structural interfaces |
|---|---|
| Python | `typing.Protocol` (`python_scan.py` reports unimplemented ones) |
| TypeScript | all types: an object matching a type without `implements` |
| Go | all interfaces |
| Ruby | duck typing everywhere: count calls on untyped receivers only when the target is found by search |
| Rust, Java, Kotlin, C#, PHP | none (traits and interfaces are declared) |

## The project's own tools

When the project configures one of these, its threshold and its result win over `scan.py`.

| Language | Cyclomatic complexity | Function length | Parameter types |
|---|---|---|---|
| Python | ruff `C901` (`--config 'lint.mccabe.max-complexity=N'`), radon `cc` | — | basedpyright `reportMissingParameterType`, `reportUnknownParameterType`, `reportExplicitAny`; `python_scan.py --check-types` |
| JS / TS | ESLint `complexity` | ESLint `max-lines-per-function` | TypeScript `noImplicitAny`; ESLint `@typescript-eslint/no-explicit-any` |
| Go | `gocyclo -over N`, golangci-lint `cyclop` | golangci-lint `funlen` | — |
| Rust | clippy `cognitive_complexity` (closest available) | clippy `too_many_lines` | — |
| Java | PMD `CyclomaticComplexity`, Checkstyle | PMD `NcssCount`, Checkstyle `MethodLength` | — |
| Kotlin | detekt `CyclomaticComplexMethod` | detekt `LongMethod` | — |
| C# | Roslyn analyzer `CA1502` | — | — |
| Ruby | RuboCop `Metrics/CyclomaticComplexity` | RuboCop `Metrics/MethodLength` | — |
| PHP | PHPMD `CyclomaticComplexity` | PHPMD `ExcessiveMethodLength` | — |
| Swift | SwiftLint `cyclomatic_complexity` | SwiftLint `function_body_length` | — |

## Grep fallback

Use only for languages `scan.py` reports as `NO_RULES`. Label every result as approximate.

| Language | Dynamic-call patterns |
|---|---|
| Kotlin | `Class\.forName`, `getMethod\(`, `\.invoke\(`, `::class\.java`, `\.call\(` on `KFunction` |
| Rust | `dyn Any`, `downcast`, string-keyed `HashMap<.*fn` |
| Swift | `NSSelectorFromString`, `perform\(`, `value\(forKey:` |
| Scala | `Class\.forName`, `getMethod\(`, `\.invoke\(`, `selectDynamic` |
| Elixir | `apply\(`, `Kernel\.apply`, `String\.to_atom` |
| Lua | `_G\[`, `loadstring`, `load\(` |
| Any | `eval`, `invoke`, `reflect`, and maps whose values are functions |
