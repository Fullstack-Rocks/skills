# Rendering and tools

Reviewers judge PNGs, and so do you. For each tool, you need three things: a source file you can write, a PNG for every page, and the page geometry for `scripts/check_diagram.py` (see `geometry-format.md`).

## Generate, don't hand-edit

Write a small generator (a script that builds the tool's file from the fact list) whenever the tool's format is text. Explicit coordinates, ports and waypoints gave far better results than automatic layout or automatic routing, and the generator can dump exact geometry for the checker. Commit it with the diagram; without it, every later change means hand-editing the export.

## Per tool

- **draw.io:** write `.drawio` XML (`mxfile` > `diagram` per page > `mxGraphModel`). Use the `aws4`, `azure` or `gcp` shape libraries for cloud icons, and look the shape names up instead of guessing.
  - **Render and export in one command:** `python3 scripts/drawio_export.py diagram.drawio out/` writes `out/page-<n>.png` and `out/geometry.json` from the draw.io viewer itself, so it works on a hand-edited file too. It reads steps from labels that start with a number ("③ Run"), and treats bare vertical lines as lifelines and frames as containers. It needs headless Chrome (`--chrome PATH` if it isn't the macOS default) and network access to viewer.diagrams.net.
  - **How it renders, if you need your own:** write an HTML page that loads `https://viewer.diagrams.net/js/viewer-static.min.js`, with one page's XML embedded in a `div class="mxgraph"`'s `data-mxgraph` JSON (`{"xml": "<mxfile>…</mxfile>", "toolbar": "", "nav": false, "zoom": 1, "border": 16}`). Screenshot it with headless Chrome: `chrome --headless=new --disable-gpu --hide-scrollbars --window-size=<w>,<h> --virtual-time-budget=15000 --screenshot=<page>.png file://<page>.html`, sized from the page's bounds plus a margin.
  - Write the log to a file: piping the render script into `head` stopped it early and left stale PNGs.
- **Mermaid:** `mmdc -i diagram.mmd -o diagram.png -w 1900` (`@mermaid-js/mermaid-cli`). Mermaid places nodes itself, so you control crossings only through node order, subgraphs and direction. Prefer it for sequence diagrams, where its layout is predictable.
- **D2:** `d2 --layout=elk diagram.d2 diagram.png`. Fix positions with `near` or grid layouts when the automatic layout crosses lines.
- **PlantUML:** `plantuml -tpng diagram.puml`. It is strong for sequence diagrams: `alt`/`else` frames, `activate` bars and `group` bands map directly onto the sequence rules in `layout-rules.md`.
- **Graphviz:** `dot -Tpng diagram.dot -o diagram.png`, and `-Tjson` for exact geometry. Use `rank=same`, clusters and ports to steer the layout.
- **Excalidraw:** write the `.excalidraw` JSON with explicit coordinates, and export a PNG with the Excalidraw CLI or by opening the file in a headless browser. Its JSON already holds the geometry.

Whatever the tool, open every PNG yourself and crop the dense areas. The render is the only reliable check of text overflow and of label positions after the tool's own text layout.
