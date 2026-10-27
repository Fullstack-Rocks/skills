"""Views (.big-picture/views/*.yml): extra tabs in the viewer, defined by files, not code. A view
names the node types it shows, the connection kinds it follows, and the colour of each type and kind,
taken from the technology's own branding (Redis red, Valkey's blue-to-purple gradient).

  title: Cache
  types: [cache-key, cache-store]          # nodes of these types are the view
  edges: [reads-cache, writes-cache]       # connections it draws; omitted: all but contains
  neighbors: true                          # also show the code on the other end of those edges
  colors: { cache-store: "#DC382D", cache-key: "linear-gradient(90deg, #6366F1, #A855F7)" }
"""
from graph import Graph
from stages.files import definitions


def add_views(graph: Graph) -> None:
    for path, view in definitions(graph.root / ".big-picture" / "views"):
        if not view.get("types"):
            print(f"views: {path.name} has no types, skipped")
            continue
        graph.views.append({"id": path.stem, "title": view.get("title", path.stem.title()), "types": view["types"],
                            "edges": view.get("edges"), "neighbors": bool(view.get("neighbors", True)),
                            "colors": view.get("colors", {})})
