import argparse
import ast
from dataclasses import dataclass, field
from pathlib import Path

DYNAMIC_FUNCTIONS = {"eval", "exec", "__import__", "globals", "locals"}
ATTRIBUTE_FUNCTIONS = {"getattr", "setattr"}
DYNAMIC_ATTRIBUTES = {"import_module", "call_function", "methodcaller"}
SKIPPED_PARTS = {".git", ".venv", "venv", "__pycache__", "node_modules", "build", "dist"}


@dataclass
class Scan:
    max_function_lines: int
    check_types: bool = False
    findings: list[str] = field(default_factory=list)
    protocols: dict[str, str] = field(default_factory=dict)
    implemented: set[str] = field(default_factory=set)


def base_name(node: ast.expr) -> str:
    if isinstance(node, ast.Subscript):
        return base_name(node.value)
    if isinstance(node, ast.Attribute):
        return node.attr
    return node.id if isinstance(node, ast.Name) else ""


def call_target(node: ast.Call) -> str:
    if isinstance(node.func, ast.Name):
        return node.func.id
    return node.func.attr if isinstance(node.func, ast.Attribute) else ""


def attribute_name(node: ast.Call) -> ast.expr | None:
    return node.args[1] if len(node.args) > 1 else None


def check_attribute_call(node: ast.Call, where: str, called: bool, scan: Scan) -> None:
    name = attribute_name(node)
    detail = ast.unparse(name) if name is not None else ""
    if called:
        scan.findings.append(f"DYNAMIC_CALL\t{where}\t{call_target(node)}({detail})(...)")
    elif not isinstance(name, ast.Constant):
        scan.findings.append(f"DYNAMIC_ATTR\t{where}\t{call_target(node)}({detail})")


def check_call(node: ast.Call, where: str, called: bool, scan: Scan) -> None:
    target = call_target(node)
    if target in ATTRIBUTE_FUNCTIONS:
        check_attribute_call(node, where, called, scan)
    elif target in DYNAMIC_FUNCTIONS or target in DYNAMIC_ATTRIBUTES:
        scan.findings.append(f"DYNAMIC_CALL\t{where}\t{target}(...)")
    elif isinstance(node.func, ast.Subscript):
        scan.findings.append(f"LOOKUP_CALL\t{where}\t{ast.unparse(node.func)}(...)")


def directly_called(tree: ast.AST) -> set[int]:
    return {id(node.func) for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Call)}


def untyped_parameters(node: ast.FunctionDef | ast.AsyncFunctionDef, in_class: bool) -> list[str]:
    arguments = node.args
    positional = [*arguments.posonlyargs, *arguments.args]
    is_static = any(base_name(decorator) == "staticmethod" for decorator in node.decorator_list)
    if in_class and positional and not is_static:
        positional = positional[1:]
    names = [arg.arg for arg in [*positional, *arguments.kwonlyargs] if arg.annotation is None]
    names += [f"*{arg.arg}" for arg in (arguments.vararg,) if arg is not None and arg.annotation is None]
    names += [f"**{arg.arg}" for arg in (arguments.kwarg,) if arg is not None and arg.annotation is None]
    return names


def any_parameters(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    arguments = node.args
    every = [*arguments.posonlyargs, *arguments.args, *arguments.kwonlyargs, arguments.vararg, arguments.kwarg]
    return [arg.arg for arg in every if arg is not None and arg.annotation is not None and _mentions_any(arg.annotation)]


def _mentions_any(annotation: ast.expr) -> bool:
    return any(base_name(node) == "Any" for node in ast.walk(annotation) if isinstance(node, (ast.Name, ast.Attribute)))


def check_function(
    node: ast.FunctionDef | ast.AsyncFunctionDef, where: str, in_class: bool, scan: Scan
) -> None:
    length = (node.end_lineno or node.lineno) - node.lineno + 1
    if length > scan.max_function_lines:
        scan.findings.append(f"FUNCTION_LENGTH\t{where}\t{node.name} {length} lines > {scan.max_function_lines}")
    if scan.check_types:
        missing = untyped_parameters(node, in_class)
        if missing:
            scan.findings.append(f"UNTYPED_PARAM\t{where}\t{node.name}({', '.join(missing)})")
        explicit_any = any_parameters(node)
        if explicit_any:
            scan.findings.append(f"ANY_PARAM\t{where}\t{node.name}({', '.join(explicit_any)})")


def check_class(node: ast.ClassDef, where: str, scan: Scan) -> None:
    bases = {base_name(base) for base in node.bases}
    if "Protocol" in bases:
        scan.protocols[node.name] = where
    scan.implemented.update(bases)


def scan_file(path: Path, scan: Scan) -> None:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (SyntaxError, UnicodeDecodeError) as error:
        scan.findings.append(f"PARSE_ERROR\t{path}\t{error}")
        return
    called = directly_called(tree)
    methods = class_methods(tree)
    for node in ast.walk(tree):
        where = f"{path}:{getattr(node, 'lineno', 0)}"
        if isinstance(node, ast.Call):
            check_call(node, where, id(node) in called, scan)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            check_function(node, where, id(node) in methods, scan)
        elif isinstance(node, ast.ClassDef):
            check_class(node, where, scan)


def class_methods(tree: ast.AST) -> set[int]:
    return {
        id(child)
        for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef)
        for child in node.body
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def python_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return [file for file in path.rglob("*.py") if not SKIPPED_PARTS.intersection(file.parts)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Report dynamic calls, unimplemented Protocols and long functions.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--max-function-lines", type=int, default=80)
    parser.add_argument("--check-types", action="store_true", help="report parameters without annotations")
    arguments = parser.parse_args()
    scan = Scan(arguments.max_function_lines, arguments.check_types)
    scan.findings.extend(f"MISSING_PATH\t{path}\tdoes not exist" for path in arguments.paths if not path.exists())
    files = sorted({file for path in arguments.paths for file in python_files(path.resolve())})
    for file in files:
        scan_file(file, scan)
    for name, where in sorted(scan.protocols.items()):
        if name not in scan.implemented:
            scan.findings.append(f"IMPLICIT_PROTOCOL\t{where}\t{name} has no explicit implementer in scanned files")
    print("\n".join(scan.findings) if scan.findings else "OK\tno findings")
    print(f"SCANNED\t{len(files)} Python files")


if __name__ == "__main__":
    main()
