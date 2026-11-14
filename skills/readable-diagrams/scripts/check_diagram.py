#!/usr/bin/env python3
"""Checks diagram pages for layout defects reviewers penalise, from plain geometry exported by any tool."""

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass, field
from itertools import combinations

Point = tuple[float, float]
Segment = tuple[Point, Point]

STEP_REFERENCE = re.compile(r"\b(?:step|steps|at)\s+(\d+(?:\.\d+)*)\b", re.IGNORECASE)
EPSILON = 0.5


@dataclass(frozen=True)
class Box:
    x: float
    y: float
    w: float
    h: float

    @property
    def right(self) -> float:
        return self.x + self.w

    @property
    def bottom(self) -> float:
        return self.y + self.h

    def shrunk(self, by: float) -> "Box":
        return Box(self.x + by, self.y + by, max(self.w - 2 * by, 0), max(self.h - 2 * by, 0))

    def overlaps(self, other: "Box") -> bool:
        return self.x < other.right and other.x < self.right and self.y < other.bottom and other.y < self.bottom

    def contains(self, other: "Box") -> bool:
        return (self.x - EPSILON <= other.x and self.y - EPSILON <= other.y
                and other.right <= self.right + EPSILON and other.bottom <= self.bottom + EPSILON)

    def contains_point(self, point: Point) -> bool:
        return self.x < point[0] < self.right and self.y < point[1] < self.bottom


@dataclass
class Text:
    id: str
    box: Box
    text: str
    font: float
    owner: str | None


@dataclass
class Shape:
    id: str
    box: Box
    kind: str
    parent: str | None
    style: str | None


@dataclass
class Edge:
    id: str
    source: str
    target: str
    points: list[Point]
    style: str | None
    step: str | None
    label: Text | None

    @property
    def segments(self) -> list[Segment]:
        return list(zip(self.points, self.points[1:]))


@dataclass
class Page:
    id: str
    width: float
    height: float
    shapes: dict[str, Shape] = field(default_factory=dict)
    edges: list[Edge] = field(default_factory=list)
    texts: list[Text] = field(default_factory=list)
    legend: list[str] | None = None


@dataclass(frozen=True)
class Limits:
    max_width: float
    min_font: float
    min_gap: float
    min_edge: float
    max_steps: int


def text_box(raw: dict, default_font: float) -> tuple[Box, float]:
    """A text's box as given, or estimated from its characters and font size when the export has none."""
    font = float(raw.get("font", default_font))
    if "w" in raw and "h" in raw:
        return Box(float(raw["x"]), float(raw["y"]), float(raw["w"]), float(raw["h"])), font
    lines = str(raw.get("text", "")).split("\n")
    width = max(len(line) for line in lines) * font * 0.6
    return Box(float(raw["x"]), float(raw["y"]), width, len(lines) * font * 1.3), font


def read_text(raw: dict, fallback_id: str, owner: str | None, default_font: float) -> Text:
    box, font = text_box(raw, default_font)
    return Text(str(raw.get("id", fallback_id)), box, str(raw.get("text", "")), font, raw.get("owner", owner))


def read_page(raw: dict, default_font: float) -> Page:
    page = Page(str(raw["id"]), float(raw["width"]), float(raw["height"]), legend=raw.get("legend"))
    for item in raw.get("shapes", []):
        shape = Shape(str(item["id"]), Box(float(item["x"]), float(item["y"]), float(item["w"]), float(item["h"])),
                      str(item.get("kind", "box")), item.get("parent"), item.get("style"))
        page.shapes[shape.id] = shape
        if item.get("label"):
            page.texts.append(read_text(item["label"], f"{shape.id}.label", shape.id, default_font))
    for item in raw.get("edges", []):
        label = read_text(item["label"], f"{item['id']}.label", str(item["id"]), default_font) if item.get("label") else None
        page.edges.append(Edge(str(item["id"]), str(item["source"]), str(item["target"]),
                               [(float(x), float(y)) for x, y in item["points"]], item.get("style"),
                               item.get("step"), label))
    for index, item in enumerate(raw.get("texts", [])):
        page.texts.append(read_text(item, f"text{index}", None, default_font))
    return page


def orientation(a: Point, b: Point, c: Point) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def proper_crossing(first: Segment, second: Segment) -> Point | None:
    """Where two segments cross through each other's interiors; None when they only touch, meet at an end or run collinear."""
    (a, b), (c, d) = first, second
    o1, o2, o3, o4 = orientation(a, b, c), orientation(a, b, d), orientation(c, d, a), orientation(c, d, b)
    if abs(o1) < EPSILON or abs(o2) < EPSILON or abs(o3) < EPSILON or abs(o4) < EPSILON:
        return None
    if (o1 > 0) == (o2 > 0) or (o3 > 0) == (o4 > 0):
        return None
    t = o3 / (o3 - o4)
    return (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))


def segment_hits_box(segment: Segment, box: Box) -> bool:
    """Whether a segment passes through a box's interior, checked by sampling every few pixels."""
    (x1, y1), (x2, y2) = segment
    steps = max(int(math.dist(segment[0], segment[1]) / 3), 1)
    return any(box.contains_point((x1 + (x2 - x1) * i / steps, y1 + (y2 - y1) * i / steps)) for i in range(steps + 1))


def axis(segment: Segment) -> str | None:
    (x1, y1), (x2, y2) = segment
    if abs(y1 - y2) < EPSILON:
        return "h"
    if abs(x1 - x2) < EPSILON:
        return "v"
    return None


def parallel_gap(first: Segment, second: Segment) -> tuple[float, float] | None:
    """The distance between two parallel axis-aligned segments and how far they run side by side."""
    kind = axis(first)
    if kind is None or kind != axis(second):
        return None
    along, across = (0, 1) if kind == "h" else (1, 0)
    low = max(min(first[0][along], first[1][along]), min(second[0][along], second[1][along]))
    high = min(max(first[0][along], first[1][along]), max(second[0][along], second[1][along]))
    return abs(first[0][across] - second[0][across]), high - low


def bends(points: list[Point]) -> int:
    """Real changes of direction along a polyline; collinear waypoints don't count."""
    turns = 0
    for a, b, c in zip(points, points[1:], points[2:]):
        if abs(orientation(a, b, c)) > EPSILON * max(math.dist(a, b), math.dist(b, c), 1):
            turns += 1
    return turns


def doubles_back(points: list[Point]) -> bool:
    """A U-shaped route: two segments along the same axis heading in opposite directions."""
    heading: dict[str, float] = {}
    for a, b in zip(points, points[1:]):
        kind = axis((a, b))
        if kind is None:
            continue
        sign = math.copysign(1, (b[0] - a[0]) if kind == "h" else (b[1] - a[1]))
        if heading.setdefault(kind, sign) != sign:
            return True
    return False


def edge_length(edge: Edge) -> float:
    return sum(math.dist(a, b) for a, b in edge.segments)


Finding = tuple[str, str, str]


def at(page: Page, item_id: str) -> str:
    return f"{page.id}/{item_id}"


def blocking_shapes(page: Page) -> list[Shape]:
    """Shapes a line or text must not run through: everything except containers and plain lifelines."""
    return [shape for shape in page.shapes.values() if shape.kind not in ("container", "lifeline")]


def all_texts(page: Page) -> list[Text]:
    return page.texts + [edge.label for edge in page.edges if edge.label]


def check_frame(page: Page, limits: Limits) -> list[Finding]:
    findings: list[Finding] = []
    if page.width > limits.max_width:
        findings.append(("PAGE_TOO_WIDE", page.id, f"{page.width:.0f} px wide; keep pages to {limits.max_width:.0f} px or split"))
    for shape in page.shapes.values():
        parent = page.shapes.get(shape.parent) if shape.parent else None
        if shape.parent and parent is None:
            findings.append(("MISSING_PARENT", at(page, shape.id), f"parent {shape.parent} does not exist"))
        elif parent and not parent.box.contains(shape.box):
            findings.append(("OUTSIDE_PARENT", at(page, shape.id), f"not inside its parent {parent.id}"))
    return findings


def edge_obstacles(page: Page, edge: Edge) -> list[Finding]:
    """Shapes, wait bars and texts the edge runs through."""
    findings: list[Finding] = []
    for shape in blocking_shapes(page):
        if shape.id in (edge.source, edge.target):
            continue
        if any(segment_hits_box(segment, shape.box.shrunk(2)) for segment in edge.segments):
            findings.append(("EDGE_THROUGH_SHAPE", at(page, edge.id), f"passes through {shape.id}"))
    for text in all_texts(page):
        if text.owner == edge.id:
            continue
        if any(segment_hits_box(segment, text.box.shrunk(1)) for segment in edge.segments):
            findings.append(("EDGE_THROUGH_TEXT", at(page, edge.id), f"runs through text {text.id}"))
    return findings


def check_edge(page: Page, edge: Edge, limits: Limits) -> list[Finding]:
    missing = [end for end in (edge.source, edge.target) if end not in page.shapes]
    findings = [("DANGLING_EDGE", at(page, edge.id), f"end {end} is not a shape on this page") for end in missing]
    if len(edge.points) < 2:
        return findings + [("DANGLING_EDGE", at(page, edge.id), "fewer than two points")]
    length = edge_length(edge)
    if length < limits.min_edge:
        findings.append(("SHORT_EDGE", at(page, edge.id), f"{length:.0f} px long; arrowheads and dashes need {limits.min_edge:.0f}"))
    turns = bends(edge.points)
    direct = math.dist(edge.points[0], edge.points[-1])
    if turns >= 3 or doubles_back(edge.points) or (length > 200 and length > 2 * max(direct, 1)):
        findings.append(("EDGE_DETOUR", at(page, edge.id), f"runs {length:.0f} px with {turns} bends to cover {direct:.0f} px "
                         "or turns back on itself; place its ends side by side or on one row"))
    if edge.label and any(edge.label.box.contains_point(bend) for bend in edge.points[1:-1]):
        findings.append(("LABEL_ON_BEND", at(page, edge.id), "label sits on a bend; move it to a straight segment"))
    return findings + edge_obstacles(page, edge)


def check_edge_pair(page: Page, first: Edge, second: Edge, limits: Limits) -> list[Finding]:
    findings: list[Finding] = []
    shares_end = {first.source, first.target} & {second.source, second.target}
    for a in first.segments:
        for b in second.segments:
            point = proper_crossing(a, b)
            if point:
                findings.append(("EDGE_CROSSING", at(page, f"{first.id}x{second.id}"), f"lines cross at ({point[0]:.0f}, {point[1]:.0f})"))
            gap = None if shares_end else parallel_gap(a, b)
            if gap and gap[1] > limits.min_gap and gap[0] < limits.min_gap:
                kind = "SHARED_SEGMENT" if gap[0] < EPSILON else "PARALLEL_TOO_CLOSE"
                findings.append((kind, at(page, f"{first.id}|{second.id}"),
                                 f"{gap[0]:.0f} px apart for {gap[1]:.0f} px; keep {limits.min_gap:.0f} px between lines"))
    return findings


def text_findings(page: Page, text: Text, limits: Limits) -> list[Finding]:
    findings: list[Finding] = []
    if text.font < limits.min_font:
        findings.append(("SMALL_TEXT", at(page, text.id), f"{text.font:g} px; use {limits.min_font:g} px or more"))
    for shape in blocking_shapes(page):
        if shape.id != text.owner and text.box.overlaps(shape.box.shrunk(1)):
            findings.append(("TEXT_OVER_SHAPE", at(page, text.id), f"overlaps {shape.id}"))
    return findings + border_findings(page, text)


def border_findings(page: Page, text: Text) -> list[Finding]:
    """Texts that straddle a container's border, which reviewers read as collisions."""
    containers = [shape for shape in page.shapes.values() if shape.kind == "container" and shape.id != text.owner]
    straddled = [c for c in containers if text.box.overlaps(c.box) and not c.box.contains(text.box)]
    return [("TEXT_ON_BORDER", at(page, text.id), f"straddles the border of {c.id}") for c in straddled]


def check_texts(page: Page, limits: Limits) -> list[Finding]:
    texts = all_texts(page)
    findings = [finding for text in texts for finding in text_findings(page, text, limits)]
    overlapping = [(a, b) for a, b in combinations(texts, 2) if a.box.shrunk(1).overlaps(b.box.shrunk(1))]
    return findings + [("TEXT_OVERLAP", at(page, f"{a.id}|{b.id}"), "texts overlap") for a, b in overlapping]


def check_steps(page: Page, limits: Limits) -> list[Finding]:
    steps = {edge.step for edge in page.edges if edge.step}
    findings: list[Finding] = []
    if len(steps) > limits.max_steps:
        findings.append(("TOO_MANY_STEPS", page.id, f"{len(steps)} numbered steps; split the page at about {limits.max_steps}"))
    if not steps:
        return findings
    for text in all_texts(page):
        missing = [ref for ref in STEP_REFERENCE.findall(text.text) if ref not in steps]
        findings += [("STEP_REF_MISSING", at(page, text.id), f"mentions step {ref}, which this page doesn't number") for ref in missing]
    return findings


def step_key(step: str) -> tuple[int, ...] | None:
    return tuple(int(part) for part in step.split(".")) if re.fullmatch(r"\d+(?:\.\d+)*", step) else None


def step_anchor(edge: Edge) -> Point:
    if edge.label:
        return (edge.label.box.x + edge.label.box.w / 2, edge.label.box.y + edge.label.box.h / 2)
    a, b = edge.points[len(edge.points) // 2 - 1], edge.points[len(edge.points) // 2]
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


def check_step_order(page: Page, limits: Limits) -> list[Finding]:
    """Each step number on one arrow, and the numbers following reading order: down the page or along a row."""
    findings: list[Finding] = []
    first: dict[str, str] = {}
    numbered: list[tuple[tuple[int, ...], Edge]] = []
    for edge in page.edges:
        if not edge.step or len(edge.points) < 2:
            continue
        if edge.step in first:
            findings.append(("STEP_DUPLICATE", at(page, edge.id), f"step {edge.step} is also on {first[edge.step]}; "
                             "give each arrow its own number and leave side effects unnumbered"))
            continue
        first[edge.step] = edge.id
        key = step_key(edge.step)
        if key:
            numbered.append((key, edge))
    numbered.sort(key=lambda item: item[0])
    for (_, before), (_, after) in zip(numbered, numbered[1:]):
        (bx, by), (ax, ay) = step_anchor(before), step_anchor(after)
        if ay < by - limits.min_gap and ax < bx + limits.min_gap:
            findings.append(("STEP_ORDER", at(page, after.id), f"step {after.step} sits above and left of step {before.step}; "
                             "number steps in reading order, top to bottom and left to right"))
    return findings


def check_legend(page: Page) -> list[Finding]:
    if page.legend is None:
        return []
    used = {edge.style for edge in page.edges if edge.style} | {shape.style for shape in page.shapes.values() if shape.style}
    legend = set(page.legend)
    return ([("LEGEND_MISSING", page.id, f"style {style} is used but not in the legend") for style in sorted(used - legend)]
            + [("LEGEND_UNUSED", page.id, f"legend lists {style}, which this page doesn't use") for style in sorted(legend - used)])


def check_page(page: Page, limits: Limits) -> list[Finding]:
    findings = check_frame(page, limits)
    for edge in page.edges:
        findings += check_edge(page, edge, limits)
    drawable = [edge for edge in page.edges if len(edge.points) >= 2]
    for first, second in combinations(drawable, 2):
        findings += check_edge_pair(page, first, second, limits)
    return (findings + check_texts(page, limits) + check_steps(page, limits) + check_step_order(page, limits)
            + check_legend(page))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("geometry", nargs="+", help="geometry JSON files (see references/geometry-format.md)")
    parser.add_argument("--max-width", type=float, default=2000)
    parser.add_argument("--min-font", type=float, default=13)
    parser.add_argument("--min-gap", type=float, default=40, help="minimum distance between parallel lines")
    parser.add_argument("--min-edge", type=float, default=40, help="minimum edge length")
    parser.add_argument("--max-steps", type=int, default=15)
    parser.add_argument("--default-font", type=float, default=14, help="font size assumed for texts that don't state one")
    args = parser.parse_args()
    limits = Limits(args.max_width, args.min_font, args.min_gap, args.min_edge, args.max_steps)

    pages: list[Page] = []
    for path in args.geometry:
        with open(path, encoding="utf-8") as handle:
            pages += [read_page(raw, args.default_font) for raw in json.load(handle)["pages"]]
    findings = [finding for page in pages for finding in check_page(page, limits)]

    summary = f"pages={len(pages)} shapes={sum(len(p.shapes) for p in pages)} edges={sum(len(p.edges) for p in pages)} findings={len(findings)}"
    if not findings:
        print(f"OK\t{summary}")
    for kind, location, detail in findings:
        print(f"{kind}\t{location}\t{detail}")
    print(f"SCANNED\t{summary}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
