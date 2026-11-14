"""bp endpoint: an API operation as the OpenAPI document describes it and as the code runs it."""
from graph.load import Graph
from graph.walk import neighbors

OPERATION_GRAPH = {"handled-by", "calls", "reads", "writes", "looks-up"}


def pair(graph: Graph, node: dict) -> tuple[dict | None, dict | None]:
    """(operation, endpoint) for either one: they are joined by implemented-by."""
    if node["type"] == "operation":
        linked = [e["to"] for e in graph.outgoing.get(node["id"], []) if e["kind"] == "implemented-by"]
        return node, graph.nodes.get(linked[0]) if linked else None
    linked = [e["from"] for e in graph.incoming.get(node["id"], []) if e["kind"] == "implemented-by"]
    return (graph.nodes.get(linked[0]) if linked else None), node


def model_text(graph: Graph, name: str | None) -> str:
    fields = graph.nodes.get(f"api-model:{name}", {}).get("fields", [])
    shown = ", ".join(f"{f['name']}{'' if f['required'] else '?'}: {f['type']}" for f in fields)
    return f"{name} {{{shown}}}" if name else "(no body)"


def show_endpoint(graph: Graph, node: dict) -> None:
    operation, endpoint = pair(graph, node)
    if operation:
        print(f"{operation['id']}  {operation.get('summary', '')}")
        print("  parameters: " + (", ".join(f"{p['name']} ({p['in']}{', required' if p['required'] else ''})" for p in operation["parameters"]) or "none"))
        print(f"  request:    {model_text(graph, operation.get('request'))}")
        for code, model in operation.get("responses", {}).items():
            print(f"  {code}:        {model_text(graph, model)}")
    else:
        print(f"{endpoint['id']}  (not in any OpenAPI document)")
    if not endpoint:
        print("  no code endpoint implements it")
        return
    print(f"\n{endpoint['id']} at {endpoint['file']}:{endpoint['start']}; what it runs:")
    for step, edge, other in neighbors(graph, endpoint["id"], 6, "out", OPERATION_GRAPH):
        print(f"  {'  ' * (step - 1)}{edge['kind']:<10} {other}")
