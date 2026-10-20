# Languages

Per-language options for each measurement, best first. Use what the project already has before anything on this list. Every adapter you write prints the same TAB-separated finding kinds as the bundled ones: `KIND<TAB>path:line<TAB>detail`.

## Parsers for an adapter

When no bundled adapter covers the language, write a short script against the language's own parser, using the bundled adapters as the model. Report function length and dynamic calls; report interfaces only where they are structural.

| Language | Parser | Structural interfaces |
|---|---|---|
| Python | `ast` (stdlib); bundled `adapters/python_scan.py` | `typing.Protocol` |
| JS / TS | `typescript` compiler API from the project; bundled `adapters/ts_scan.mjs` | TS types are structural: an object matching a type without `implements` |
| Go | `go/ast`, run with `go run` | All Go interfaces |
| Rust | `syn` crate, or `cargo clippy` output | none (traits are explicit) |
| Java / Kotlin | JavaParser, or PSI via detekt | none |
| C# | Roslyn (`Microsoft.CodeAnalysis`) | none |
| Ruby | `Prism` / `Ripper` (stdlib) | Duck typing everywhere: count calls on untyped receivers only when the target is found by search |
| PHP | `nikic/php-parser` | none |
| Any | `tree-sitter` CLI with the language grammar, if installed | depends on language |

## Complexity, function length and parameter types

| Language | Cyclomatic complexity | Function length | Parameter types |
|---|---|---|---|
| Python | ruff `C901` (`--config 'lint.mccabe.max-complexity=N'`), radon `cc` | bundled adapter | basedpyright `reportMissingParameterType`, `reportUnknownParameterType`, `reportExplicitAny`; bundled adapter `--check-types` |
| JS / TS | ESLint `complexity` | ESLint `max-lines-per-function`, bundled adapter | TypeScript `noImplicitAny`; ESLint `@typescript-eslint/no-explicit-any` |
| Go | `gocyclo -over N`, golangci-lint `cyclop` | golangci-lint `funlen` | — |
| Rust | clippy `cognitive_complexity` (closest available) | clippy `too_many_lines` | — |
| Java | PMD `CyclomaticComplexity`, Checkstyle | PMD `NcssCount`, Checkstyle `MethodLength` | — |
| Kotlin | detekt `CyclomaticComplexMethod` | detekt `LongMethod` | — |
| C# | Roslyn analyzer `CA1502` | an adapter with Roslyn | — |
| Ruby | RuboCop `Metrics/CyclomaticComplexity` | RuboCop `Metrics/MethodLength` | — |
| PHP | PHPMD `CyclomaticComplexity` | PHPMD `ExcessiveMethodLength` | — |
| Swift | SwiftLint `cyclomatic_complexity` | SwiftLint `function_body_length` | — |
| Many languages | `lizard` (one tool for CCN and length) | `lizard` | — |

## Grep fallback

Use only when no parser runs. Label every result as approximate.

| Language | Dynamic-call patterns |
|---|---|
| Python | `getattr\(`, `setattr\(`, `importlib`, `__import__`, `\beval\(`, `\bexec\(`, `\]\(` |
| JS / TS | `\[[^\]'"]+\]\(`, `\beval\(`, `new Function`, `require\([^'"]`, `import\([^'"]`, `Reflect\.` |
| Go | `MethodByName`, `reflect\.`, `map\[string\]func` |
| Rust | `dyn Any`, `downcast`, string-keyed `HashMap<.*fn` |
| Java / Kotlin | `Class\.forName`, `getMethod\(`, `\.invoke\(`, `::class\.java` reflection |
| C# | `Activator\.CreateInstance`, `GetMethod\(`, `\.Invoke\(`, `\bdynamic\b` |
| Ruby | `\.send\(`, `public_send`, `method_missing`, `const_get`, `define_method` |
| PHP | `call_user_func`, `\$\w+->\$\w+\(`, `\$\w+\(` |
