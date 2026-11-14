#!/usr/bin/env python3
"""Renders every page of a .drawio file to PNG and exports the rendered geometry for check_diagram.py.

Both come from the draw.io viewer (viewer-static.min.js) in headless Chrome, so the geometry is what the PNG shows:
vertex boxes, routed edge polylines and text boxes. It reads a step number from a label that starts with one ("③ Run",
"3. Run", "3.1 Run"), whether the label is the arrow's own or a text box on it; treats an unlabeled vertical line with
no ends as a sequence lifeline; and treats a shape that encloses another shape or a text (a lane, a frame) as a container.

Usage: drawio_export.py <file.drawio> <out-dir> [--chrome PATH]
Writes <out-dir>/page-<n>.png and <out-dir>/geometry.json; needs network access to viewer.diagrams.net.
"""
import argparse
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BORDER = 24
CIRCLED = {chr(0x2460 + i): str(i + 1) for i in range(20)}
STEP = re.compile(r"^\s*([①-⑳]|\d+(?:\.\d+)*)[.)]?\s")

COLLECT = r"""
function collect(viewer) {
  var g = viewer.graph, m = g.getModel(), b = g.getGraphBounds(), ox = b.x - BORDER, oy = b.y - BORDER;
  var out = {width: Math.round(b.width + 2 * BORDER), height: Math.round(b.height + 2 * BORDER), shapes: [], edges: [], texts: []};
  function plain(s) {
    var d = document.createElement('div');
    d.innerHTML = String(s || '').replace(/<br\s*\/?>/gi, '\n').replace(/<\/(div|p)>/gi, '\n');
    return d.textContent.replace(/\n+$/, '');
  }
  function textOf(st, cell) {
    var v = m.getValue(cell), t = plain(v && v.nodeName ? v.getAttribute('label') : v);
    if (!st.text || !st.text.boundingBox || !t.trim()) return null;
    var bb = st.text.boundingBox;
    return {text: t, x: bb.x - ox, y: bb.y - oy, w: bb.width, h: bb.height, font: parseFloat(st.style.fontSize || 12)};
  }
  function vertexParent(c) { var p = m.getParent(c); while (p && !m.isVertex(p)) p = m.getParent(p); return p; }
  for (var id in m.cells) {
    var c = m.cells[id], st = g.view.getState(c);
    if (!st) continue;
    var style = st.style || {}, label = textOf(st, c);
    if (m.isVertex(c)) {
      var onEdge = m.getParent(c) && m.isEdge(m.getParent(c));
      if (onEdge || /^text(;|$)/.test(m.getStyle(c) || '') || style.text == 1 || style.shape === 'text' || (style.strokeColor === 'none' && style.fillColor === 'none')) {
        if (label) { label.id = c.id; if (onEdge) label.owner = m.getParent(c).id; out.texts.push(label); }
        continue;
      }
      var s = {id: c.id, x: st.x - ox, y: st.y - oy, w: st.width, h: st.height};
      if (m.getChildCount(c) > 0 || style.container == 1 || style.shape === 'swimlane' || style.swimlane !== undefined) s.kind = 'container';
      var vp = vertexParent(c); if (vp) s.parent = vp.id;
      if (label) s.label = label;
      out.shapes.push(s);
    } else if (m.isEdge(c) && st.absolutePoints) {
      var e = {id: c.id, source: c.source ? c.source.id : null, target: c.target ? c.target.id : null,
               points: st.absolutePoints.filter(Boolean).map(function (p) { return [p.x - ox, p.y - oy]; })};
      if (label) e.label = label;
      out.edges.push(e);
    }
  }
  return out;
}
GraphViewer.createViewerForElement(document.getElementById('d'), function (v) {
  setTimeout(function () { document.getElementById('out').textContent = JSON.stringify(collect(v)); }, 300);
});
""".replace("BORDER", str(BORDER))


def pages(path: Path):
    for number, diagram in enumerate(ET.parse(path).getroot().iter("diagram"), 1):
        one = ET.Element("mxfile")
        one.append(diagram)
        yield number, diagram.get("name") or f"page-{number}", ET.tostring(one, encoding="unicode")


def html(xml: str, extract: bool) -> str:
    config = json.dumps({"xml": xml, "toolbar": "", "nav": False, "zoom": 1, "border": BORDER, "resize": False})
    attr = config.replace("&", "&amp;").replace('"', "&quot;")
    script = f"<script>{COLLECT}</script>" if extract else ""
    cls = "" if extract else ' class="mxgraph"'
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:#fff}}</style></head>'
            f'<body><div id="d"{cls} data-mxgraph="{attr}"></div><pre id="out"></pre>'
            f'<script src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>{script}</body></html>')


def chrome(binary: str, *args: str) -> str:
    run = subprocess.run([binary, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=20000", *args],
                         capture_output=True, text=True, timeout=180)
    return run.stdout


def extract(binary: str, page_html: Path) -> dict:
    for _ in range(4):  # the viewer script sometimes loads too late on the first run
        found = re.search(r'<pre id="out">(.*?)</pre>', chrome(binary, "--dump-dom", page_html.as_uri()), re.S)
        if found and found.group(1).strip():
            return json.loads(unescape(found.group(1)))
    sys.exit(f"{page_html.name}: the viewer produced no geometry")


def length(points: list) -> float:
    return sum(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5 for a, b in zip(points, points[1:]))


def distance(point: tuple, points: list) -> float:
    """From a point to the nearest segment of a polyline."""
    best = float("inf")
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        dx, dy = x2 - x1, y2 - y1
        t = max(0.0, min(1.0, ((point[0] - x1) * dx + (point[1] - y1) * dy) / ((dx * dx + dy * dy) or 1)))
        best = min(best, ((point[0] - x1 - t * dx) ** 2 + (point[1] - y1 - t * dy) ** 2) ** 0.5)
    return best


def encloses(outer: dict, inner: dict) -> bool:
    return (outer["x"] <= inner["x"] and outer["y"] <= inner["y"]
            and inner["x"] + inner["w"] <= outer["x"] + outer["w"] and inner["y"] + inner["h"] <= outer["y"] + outer["h"])


def tidy(page: dict) -> None:
    """Steps from labels, lifelines from bare vertical lines, containers from enclosing shapes."""
    edges = []
    for edge in page["edges"]:
        points = edge["points"]
        if (not edge["source"] and not edge["target"] and "label" not in edge and len(points) == 2
                and abs(points[0][0] - points[1][0]) < 1 and abs(points[0][1] - points[1][1]) >= 300):
            top, bottom = sorted((points[0][1], points[1][1]))
            page["shapes"].append({"id": edge["id"], "x": points[0][0] - 1, "y": top, "w": 2, "h": bottom - top, "kind": "lifeline"})
            continue
        if not edge["source"] and not edge["target"] and "label" not in edge and length(points) < 80:
            continue  # a legend sample stroke, not a flow
        for end in ("source", "target"):  # a free-standing arrow (a sequence message) gets a point-sized end
            if not edge[end]:
                x, y = points[0] if end == "source" else points[-1]
                edge[end] = f"{edge['id']}.{end}"
                page["shapes"].append({"id": edge[end], "x": x, "y": y, "w": 0, "h": 0, "kind": "lifeline"})
        step = STEP.match(edge.get("label", {}).get("text", ""))
        if step:
            edge["step"] = CIRCLED.get(step.group(1), step.group(1))
        edges.append(edge)
    page["edges"] = edges
    for text in page["texts"]:  # a label drawn as its own text box numbers the arrow it sits on
        step = STEP.match(text["text"])
        if step and not text.get("owner") and edges:
            centre = (text["x"] + text["w"] / 2, text["y"] + text["h"] / 2)
            edge = min(edges, key=lambda e: distance(centre, e["points"]))
            if distance(centre, edge["points"]) <= text["h"] / 2 + 40 and "step" not in edge:
                edge["step"] = CIRCLED.get(step.group(1), step.group(1))
                text["owner"] = edge["id"]
    boxes = [s for s in page["shapes"] if s.get("kind") != "lifeline"]
    for outer in boxes:  # a lane, a frame or a card holding its own text boxes
        if any(inner is not outer and encloses(outer, inner) for inner in boxes + page["texts"]):
            outer["kind"] = "container"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("drawio")
    parser.add_argument("out_dir")
    parser.add_argument("--chrome", default=CHROME)
    args = parser.parse_args()
    out = Path(args.out_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    geometry = {"pages": []}
    for number, name, xml in pages(Path(args.drawio)):
        work = out / f".page-{number}.html"
        work.write_text(html(xml, True))
        page = extract(args.chrome, work)
        tidy(page)
        page.update(id=str(number), name=name)
        geometry["pages"].append(page)
        work.write_text(html(xml, False))
        png = out / f"page-{number}.png"
        chrome(args.chrome, f"--window-size={page['width'] + 16},{page['height'] + 16}", f"--screenshot={png}", work.as_uri())
        work.unlink()
        print(f"{png.name}\t{name}\t{page['width']}x{page['height']}\t{len(page['edges'])} edges")
    (out / "geometry.json").write_text(json.dumps(geometry, indent=1))
    print(f"{out / 'geometry.json'}")


if __name__ == "__main__":
    main()
