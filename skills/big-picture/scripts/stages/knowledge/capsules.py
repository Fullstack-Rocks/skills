"""Stage 11: capsules, groups of modules (and the tables they share) that work together. Label
propagation over the module graph finds them: every module starts in its own group and repeatedly
joins the group most of its connections lead to. The agent names them, and can pin a module into
another's capsule, in .big-picture/capsules.yml:

  names: { app/services/order_service.py: Orders }        # key: the capsule's id, its central module
  pins:  { app/models/order.py: app/services/order_service.py }

Each capsule is a `capsule:<central member>` node with a `groups` edge to each member."""
from collections import Counter
from pathlib import PurePosixPath

from graph import Graph
from stages.files import load_data

LINKS = {"calls", "reads", "writes", "looks-up", "maps-to", "handled-by", "implemented-by"}
ROUNDS = 20
HUB_SHARE, HUB_MIN = 0.15, 6  # a member linked to more than this share of all members (and HUB_MIN) is shared


def owner(graph: Graph, node_id: str) -> str | None:
    """The module a node lives in, or the table itself; None for anything else."""
    node = graph.nodes.get(node_id, {})
    if node.get("type") in ("module", "table"):
        return node_id
    file = node.get("file")
    return f"module:{file}" if file and f"module:{file}" in graph.nodes else None


def without_hubs(links: dict[str, Counter]) -> tuple[dict[str, Counter], list[str]]:
    """Drop shared infrastructure (a db helper, an HTTP layer): linked to nearly everything, it would
    pull every module into one capsule. Returns the remaining links and the hubs."""
    limit = max(HUB_MIN, HUB_SHARE * len(links))
    hubs = sorted(m for m, others in links.items() if len(others) > limit)
    return {m: Counter({o: w for o, w in others.items() if o not in hubs}) for m, others in links.items() if m not in hubs}, hubs


def module_links(graph: Graph) -> dict[str, Counter]:
    """module or table -> how many connections it has to each other module or table."""
    links: dict[str, Counter] = {}
    for source, target, kind in graph.edges:
        a, b = owner(graph, source), owner(graph, target)
        if kind in LINKS and a and b and a != b:
            links.setdefault(a, Counter())[b] += 1
            links.setdefault(b, Counter())[a] += 1
    return links


def propagate(links: dict[str, Counter], pins: dict[str, str]) -> dict[str, str]:
    """Label propagation, in a fixed order so every build gives the same capsules."""
    label = {member: pins.get(member, member) for member in links}
    for _ in range(ROUNDS):
        changed = False
        for member in sorted(links):
            if member in pins:
                continue
            votes = Counter()
            for other, weight in links[member].items():
                votes[label[other]] += weight
            best = max(sorted(votes), key=lambda candidate: votes[candidate]) if votes else label[member]
            changed |= best != label[member]
            label[member] = best
        if not changed:
            break
    return label


def capsule_config(graph: Graph) -> tuple[dict[str, str], dict[str, str]]:
    """(pins, names) from .big-picture/capsules.yml, keyed by module node id."""
    path = graph.root / ".big-picture" / "capsules.yml"
    config = (load_data(path) if path.exists() else None) or {}
    pins = {f"module:{m}": f"module:{t}" for m, t in config.get("pins", {}).items()}
    return pins, {f"module:{k}": v for k, v in config.get("names", {}).items()}


def add_capsule(graph: Graph, members: list[str], links: dict[str, Counter], names: dict[str, str]) -> None:
    """One capsule node, named after its most connected member unless capsules.yml names it."""
    central = max(sorted(members), key=lambda m: sum(links[m].values()))
    name = names.get(central) or PurePosixPath(central.split(":", 1)[1]).stem
    capsule = graph.add_node(f"capsule:{central.split(':', 1)[1]}", "capsule", name, members=len(members))
    for member in members:
        graph.add_edge(capsule, member, "groups", "capsules")


def add_capsules(graph: Graph) -> int:
    """Capsule nodes for every group of two or more; returns how many."""
    pins, names = capsule_config(graph)
    links, hubs = without_hubs(module_links(graph))
    graph.coverage["shared modules"] = ", ".join(h.split(":", 1)[1] for h in hubs) or "none"
    groups: dict[str, list[str]] = {}
    for member, label in propagate(links, pins).items():
        groups.setdefault(label, []).append(member)
    capsules = [members for members in groups.values() if len(members) > 1]
    for members in capsules:
        add_capsule(graph, members, links, names)
    return len(capsules)
