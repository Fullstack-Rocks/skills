"""Stage 9: the API as an OpenAPI document describes it. Each operation becomes a node with its
parameters, request and responses; each component schema an api-model node with its fields. An
operation is matched to the code endpoint with the same method and path, and the mismatches are
findings: an operation no code handles, an endpoint the document leaves out."""
import json
import re
from pathlib import PurePosixPath

from graph import Graph
from stages.files import load_data

SPEC_NAMES = re.compile(r"(openapi|swagger)[\w.-]*\.(json|ya?ml)$", re.I)
METHODS = ("get", "put", "post", "delete", "patch", "head", "options")
FIXES = {
    "operation-without-handler": "Implement the operation, or remove it from the OpenAPI document if it is gone.",
    "endpoint-not-in-spec": "Add the endpoint to the OpenAPI document, or remove the endpoint if nothing should call it.",
}


PARAMETER = re.compile(r"\{[^}]*\}")


def path_key(method: str, path: str) -> str:
    """GET /orders/{order_id} and GET /orders/{id} are the same route."""
    return method.upper() + " " + PARAMETER.sub("{}", path.rstrip("/") or "/")


REF = re.compile(r"#/components/schemas/([\w.-]+)")


def schema_name(schema: dict | None) -> str | None:
    """Components/schemas/Order -> Order, for a $ref directly or inside an array."""
    found = REF.search(json.dumps(schema)) if schema else None
    return found[1] if found else None


def fields(schema: dict) -> list[dict]:
    required = set(schema.get("required", []))
    found = []
    for name, prop in schema.get("properties", {}).items():
        ref = REF.search(json.dumps(prop))
        found.append({"name": name, "type": prop.get("type") or (ref[1] if ref else "object"), "required": name in required,
                      **({"ref": ref[1]} if ref else {})})
    return found


def add_models(graph: Graph, models: dict[str, list[dict]], file: str) -> None:
    """api-model nodes with their fields, and has-edges to the models their fields refer to."""
    for name, model_fields in models.items():
        graph.add_node(f"api-model:{name}", "api-model", name, file=file, fields=model_fields)
        graph.add_edge(f"schema:{file}", f"api-model:{name}", "defines", "openapi")
    for name, model_fields in models.items():
        for field in [f for f in model_fields if f.get("ref")]:
            graph.add_edge(f"api-model:{name}", f"api-model:{field['ref']}", "has", "openapi")


def operation_node(operation: dict) -> dict:
    """What the viewer and bp show for an operation: summary, parameters, request and responses."""
    body = operation.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema")
    responses = {code: schema_name(r.get("content", {}).get("application/json", {}).get("schema"))
                 for code, r in operation.get("responses", {}).items()}
    return {"summary": operation.get("summary") or operation.get("description", ""), "operationId": operation.get("operationId"),
            "tags": operation.get("tags", []), "request": schema_name(body), "responses": responses,
            "parameters": [{"name": p.get("name"), "in": p.get("in"), "required": p.get("required", False)}
                           for p in operation.get("parameters", [])]}


def add_operations(graph: Graph, operations: list[tuple[str, str, dict]], file: str, servers: list[str]) -> set[str]:
    """Operation nodes linked to their models; returns their route keys."""
    keys = set()
    for method, path, details in operations:
        node = graph.add_node(f"operation:{method.upper()} {path}", "operation", f"{method.upper()} {path}",
                              file=file, method=method.upper(), path=path, servers=servers, **details)
        graph.add_edge(f"schema:{file}", node, "defines", "openapi")
        for model, kind in [(details["request"], "accepts"), *[(m, "returns") for m in details["responses"].values()]]:
            if model:
                graph.add_edge(node, f"api-model:{model}", kind, "openapi")
        keys.add(path_key(method, path))
    return keys


def endpoint_keys(graph: Graph) -> dict[str, str]:
    """route key -> endpoint node id, for every endpoint the code declares."""
    return {path_key(*n["name"].split(" ", 1)): n["id"] for n in graph.nodes.values() if n["type"] == "endpoint"}


def match_operations(graph: Graph, endpoints: dict[str, str]) -> None:
    """operation -implemented-by-> endpoint, or a finding when no code endpoint matches."""
    for operation in [n for n in graph.nodes.values() if n["type"] == "operation"]:
        endpoint = endpoints.get(path_key(operation["method"], operation["path"]))
        if endpoint:
            graph.add_edge(operation["id"], endpoint, "implemented-by", "openapi")
            continue
        graph.add_finding("operation-without-handler", operation["id"], operation["file"], None,
                          "no code endpoint has this method and path", "openapi")
        graph.findings[f"operation-without-handler:{operation['id']}"]["fix"] = FIXES["operation-without-handler"]


def flag_undocumented(graph: Graph, endpoints: dict[str, str], documented: set[str]) -> None:
    for key, endpoint in [(k, e) for k, e in endpoints.items() if k not in documented]:
        node = graph.nodes[endpoint]
        graph.add_finding("endpoint-not-in-spec", endpoint, node["file"], node.get("start"), "the OpenAPI document leaves it out", "openapi")
        graph.findings[f"endpoint-not-in-spec:{endpoint}"]["fix"] = FIXES["endpoint-not-in-spec"]


def parse_spec(spec: dict) -> tuple[dict[str, list[dict]], list[tuple[str, str, dict]], list[str]]:
    """(models with their fields, (method, path, operation) for every operation, server URLs)."""
    models = {name: fields(schema) for name, schema in spec.get("components", {}).get("schemas", {}).items()}
    operations = [(m, path, operation_node(item[m])) for path, item in spec["paths"].items() for m in METHODS if m in item]
    return models, operations, [s["url"] for s in spec.get("servers", []) if s.get("url")]


def add_openapi(graph: Graph, files: list[str]) -> int:
    """Read every OpenAPI document; returns how many operations they describe."""
    documented: set[str] = set()
    for file in [f for f in files if SPEC_NAMES.search(PurePosixPath(f).name)]:
        spec = load_data(graph.root / file)
        if isinstance(spec, dict) and "paths" in spec:
            models, operations, servers = parse_spec(spec)
            add_models(graph, models, file)
            documented |= add_operations(graph, operations, file, servers)
    if documented:
        endpoints = endpoint_keys(graph)
        match_operations(graph, endpoints)
        flag_undocumented(graph, endpoints, documented)
    return len(documented)
