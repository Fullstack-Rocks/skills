# Geometry format

`scripts/check_diagram.py` checks plain geometry, so it works with any diagram tool. Export each page's final positions to this JSON, from your generator's own model or by parsing the tool's file (draw.io's `mxGeometry`, Excalidraw's elements, or an SVG export's boxes and paths). All coordinates are absolute page pixels, with the origin at the top left.

```json
{
  "pages": [
    {
      "id": "01a",
      "width": 1900,
      "height": 1200,
      "legend": ["request", "valkey", "operator"],
      "shapes": [
        {"id": "vpc", "x": 40, "y": 80, "w": 1400, "h": 900, "kind": "container",
         "label": {"text": "VPC", "x": 48, "y": 84, "font": 14}},
        {"id": "api", "x": 200, "y": 300, "w": 64, "h": 64, "parent": "vpc", "style": "service",
         "label": {"text": "Api\nFastAPI :8000", "x": 180, "y": 370, "w": 104, "h": 36, "font": 14}},
        {"id": "router-wait", "x": 896, "y": 220, "w": 10, "h": 400, "kind": "bar"}
      ],
      "edges": [
        {"id": "e1", "source": "api", "target": "db", "points": [[264, 332], [600, 332]],
         "style": "request", "step": "2",
         "label": {"text": "② Run query\nTCP 5432", "x": 380, "y": 300, "font": 14}}
      ],
      "texts": [
        {"id": "note1", "text": "At step 2 the Api logs in with IAM.", "x": 300, "y": 600, "font": 14}
      ]
    }
  ]
}
```

## Fields

- **Page:** `id`, `width` and `height` are required. `legend` is optional; when present, it lists the style names the page's legend shows, and the checker compares it with the styles used.
- **Shape:** `id`, `x`, `y`, `w` and `h` are required.
  - `kind` is `box` (the default), `container` (a group such as a VPC, subnet, lane or frame; lines and text may cross into it), `bar` (an active wait bar on a lifeline; nothing may cross it) or `lifeline` (a plain lifeline; lines may cross it).
  - `parent` is the id of the container the shape must sit inside.
  - `style` is the legend name the shape's look stands for.
  - `label` is the shape's own text, which may sit on the shape.
- **Edge:** `id`, `source`, `target` and `points` are required. `points` is the rendered polyline, ends included, with every waypoint.
  - `style` is the legend name of its line style.
  - `step` is its step number as drawn ("3", "1.2").
  - `label` is its text.
- **Text** (on a shape, an edge, or in `texts`): `text`, `x` and `y` are required.
  - Give `w` and `h` when the tool knows the box. Otherwise the checker estimates it from characters (0.6 × font per character, 1.3 × font per line), which is close for sans-serif text.
  - `font` is the size in px (14 when missing).
  - `owner` is the id of the shape or edge the text belongs to; it is set automatically for labels.

## Getting positions from a tool

- **Your own generator:** dump the positions it computed. This is the most exact export.
- **draw.io:** each `mxCell` has an `mxGeometry`. A child's x and y are relative to its parent, so add the parents' offsets. An edge's points are its `mxPoint`s in `<Array as="points">`, plus its two ends where it meets its source and target.
- **SVG export from any tool** (Mermaid, D2, PlantUML, Graphviz): take `rect` and `g` bounding boxes for shapes, `path` and `polyline` points for edges (sample curves into straight segments), and `text` elements for texts.

The render stays the final word on text sizes: the checker's estimates are within 20–30 px of the tool's layout. A clean check plus a PNG you have looked at is the bar.

## Output

The checker prints one finding per line, `KIND<TAB>page/id<TAB>detail`, preceded by `OK<TAB>summary` when there are none, and ends with `SCANNED<TAB>summary`. It exits with 1 when there are findings.

| Finding | Meaning |
|---|---|
| `EDGE_CROSSING` | Two lines cross |
| `SHARED_SEGMENT`, `PARALLEL_TOO_CLOSE` | Two unrelated lines run on top of each other, or closer than `--min-gap` (40 px) |
| `EDGE_THROUGH_SHAPE`, `EDGE_THROUGH_TEXT` | A line runs through a shape, a wait bar or a text |
| `LABEL_ON_BEND` | An edge label sits on a bend |
| `SHORT_EDGE` | An edge is shorter than `--min-edge` (40 px) |
| `TEXT_OVERLAP`, `TEXT_OVER_SHAPE`, `TEXT_ON_BORDER` | Texts collide, cover a shape, or straddle a container border |
| `OUTSIDE_PARENT`, `MISSING_PARENT`, `DANGLING_EDGE` | A shape sits outside its container, or an edge end is missing |
| `SMALL_TEXT`, `PAGE_TOO_WIDE` | Text under `--min-font` (13 px), or a page wider than `--max-width` (2000 px) |
| `TOO_MANY_STEPS`, `STEP_REF_MISSING` | More than `--max-steps` (15) numbered steps, or a text mentions a step the page doesn't number |
| `LEGEND_MISSING`, `LEGEND_UNUSED` | A style is used without a legend row, or the legend lists a style the page doesn't use |
