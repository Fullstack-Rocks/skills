"""Stage 10: notes agents write about nodes, in .big-picture/docs/<slug of node id>.md:

  ---
  node: fn:app/services/order_service.py#get_order
  source_hash: 3f2a9c1b7e44      # the node's `hash` when the note was written (bp node prints it)
  ---
  What it does, how to call it, an example.

Every node with source lines gets a `hash` of them; a note whose source_hash differs is stale."""
import hashlib
import re

from graph import Graph

FRONT = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)


def slug(node_id: str) -> str:
    """fn:app/db.py#Database.insert -> fn_app_db.py_Database.insert (big-picture-query and the viewer use the same)."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", node_id)


def add_hashes(graph: Graph) -> None:
    """A short hash of each node's own source lines (a module's whole file)."""
    texts: dict[str, list[str]] = {}
    for node in [n for n in graph.nodes.values() if n.get("file") and (n.get("start") or n["type"] == "module")]:
        lines = texts.setdefault(node["file"], (graph.root / node["file"]).read_text(errors="replace").splitlines())
        chosen = lines[node["start"] - 1:node["end"]] if node.get("start") else lines
        node["hash"] = hashlib.sha1("\n".join(chosen).encode()).hexdigest()[:12]


def add_docs(graph: Graph) -> int:
    """Attach each note to its node, marking it stale when the code moved on; returns how many attached."""
    add_hashes(graph)
    attached = 0
    for path in sorted((graph.root / ".big-picture" / "docs").glob("*.md")):
        front = FRONT.match(path.read_text())
        meta = dict(line.split(":", 1) for line in front[1].splitlines() if ":" in line) if front else {}
        node = graph.nodes.get(meta.get("node", "").strip())
        if node is None:
            print(f"docs: {path.name} names no node in the graph ({meta.get('node', 'no node: line')})")
            continue
        node.update(doc=str(path.relative_to(graph.root)), docText=front[2].strip(),
                    docStale=meta.get("source_hash", "").strip() != node.get("hash"))
        attached += 1
    return attached
