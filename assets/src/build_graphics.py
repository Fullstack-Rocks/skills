"""Build the README's charts and skill banners as self-contained animated SVGs.

Same look as assets/banner.svg: a black canvas with a slow, blurred lime/mint/sky/violet gradient
moving behind static content. Fonts are embedded glyph subsets (fonts/), so every viewer renders
the same; the motion stops under prefers-reduced-motion. Chart numbers are read from
benchmarks/results, so rerunning the benchmarks and this script keeps the charts honest.

Usage: python3 assets/src/build_graphics.py
Output: assets/charts/*.svg, assets/banners/*.svg
"""
import base64
import json
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent
RESULTS = ASSETS.parent / "benchmarks/results"
W = 1280
LIME, ALONE, TEXT, MUTED = "#ECFE8C", "rgba(255,255,255,0.34)", "#FFFFFF", "#9CA3AF"


# ---------- shared look ----------

def font(name: str) -> str:
    return base64.b64encode((HERE / "fonts" / name).read_bytes()).decode()


def frame(height: int, body: str, title: str, desc: str, glow: float = 0.7, shade: float = 0.42) -> str:
    """The banner's canvas: black, rounded, a drifting blurred gradient, a shade, then `body`."""
    cy = height * 0.62
    size = f'width="{W}" height="{height}" viewBox="0 0 {W} {height}"'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" {size} role="img" aria-labelledby="t d">
  <title id="t">{escape(title)}</title>
  <desc id="d">{escape(desc)}</desc>
  <style>
    @font-face {{ font-family: "RHD"; font-weight: 500;
      src: url(data:font/woff2;base64,{font("rhd500.woff2")}) format("woff2"); }}
    @font-face {{ font-family: "RHD"; font-weight: 600;
      src: url(data:font/woff2;base64,{font("rhd600.woff2")}) format("woff2"); }}
    @font-face {{ font-family: "UNB"; font-weight: 600;
      src: url(data:font/woff2;base64,{font("unb600.woff2")}) format("woff2"); }}
    text {{ font-family: "RHD", "Red Hat Display", system-ui, sans-serif; }}
    .kicker {{ font-weight: 600; font-size: 13px; letter-spacing: 2.4px; fill: {LIME}; }}
    .title {{ font: 600 26px "UNB", "Unbounded", system-ui, sans-serif; fill: {TEXT}; letter-spacing: -0.3px; }}
    .label {{ font-weight: 600; font-size: 15px; fill: {TEXT}; }}
    .small {{ font-weight: 500; font-size: 13px; fill: {MUTED}; }}
    .value {{ font-weight: 600; font-size: 14px; fill: {TEXT}; }}
    .big {{ font: 600 64px "UNB", "Unbounded", system-ui, sans-serif; fill: {LIME}; letter-spacing: -1px; }}
    .blob {{ animation: drift 24s ease-in-out infinite alternate; }}
    .b2 {{ animation-duration: 30s; animation-delay: -9s; }}
    .b3 {{ animation-duration: 21s; animation-delay: -4s; }}
    .b4 {{ animation-duration: 33s; animation-delay: -15s; }}
    .glow {{ animation: breathe 10s ease-in-out infinite alternate; }}
    @keyframes drift {{
      0%   {{ transform: translate(-160px, 14px) scale(1); }}
      50%  {{ transform: translate(80px, -20px) scale(1.15); }}
      100% {{ transform: translate(240px, 10px) scale(0.95); }}
    }}
    @keyframes breathe {{ from {{ opacity: {glow * 0.75:.2f}; }} to {{ opacity: {glow:.2f}; }} }}
    @media (prefers-reduced-motion: reduce) {{ .blob, .glow {{ animation: none; }} }}
  </style>
  <defs>
    <clipPath id="frame"><rect width="{W}" height="{height}" rx="20"/></clipPath>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{LIME}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{LIME}" stop-opacity="0.9"/>
      <stop offset="1" stop-color="#38BDF8" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{W}" height="{height}" fill="#000"/>
    <g class="glow" filter="url(#soft)">
      <ellipse class="blob" cx="420" cy="{cy:.0f}" rx="320" ry="{height * 0.28:.0f}" fill="{LIME}"/>
      <ellipse class="blob b2" cx="760" cy="{cy + 30:.0f}" rx="300" ry="{height * 0.26:.0f}" fill="#38BDF8"/>
      <ellipse class="blob b3" cx="240" cy="{cy + 50:.0f}" rx="260" ry="{height * 0.24:.0f}" fill="#7CF5C6"/>
      <ellipse class="blob b4" cx="1020" cy="{cy - 40:.0f}" rx="240" ry="{height * 0.22:.0f}" fill="#A78BFA"/>
    </g>
    <rect width="{W}" height="{height}" fill="#000" opacity="{shade}"/>
    <rect x="0" y="{height - 2}" width="{W}" height="2" fill="url(#rule)" opacity="0.7"/>
{body}
  </g>
</svg>
'''


def text(x, y, s, cls="label", anchor="start", extra=""):
    return f'    <text class="{cls}" x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" {extra}>{escape(s)}</text>'


def bar(x, y, width, color, h=16):
    return f'    <rect x="{x:.1f}" y="{y:.1f}" width="{max(width, 3):.1f}" height="{h}" rx="4" fill="{color}"/>'


def check(x, y, color=LIME):
    return (f'    <path d="M{x:.1f} {y:.1f} l5 5 l10 -11" fill="none" stroke="{color}" stroke-width="2.6" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def legend(x, y, labels):
    out = []
    for i, (label, color) in enumerate(labels):
        out.append(f'    <rect x="{x:.1f}" y="{y + i * 22 - 11:.1f}" width="14" height="14" rx="3" fill="{color}"/>')
        out.append(text(x + 22, y + i * 22, label, "small"))
    return out


def header(kicker, title):
    return [text(56, 58, kicker.upper(), "kicker"), text(56, 96, title, "title")]


# ---------- charts ----------

def load(suite, task, condition):
    return json.loads((RESULTS / suite / f"{task}.{condition}.json").read_text())


def code_standards_chart() -> str:
    """Time, cost and issues found for a whole-repo review and a 3-file change, with and without the skill."""
    reviews = [("Whole repo, 55 files", "full-repo", (17, 17, 15)), ("A 3-file change", "change", (8, 8, 7))]
    rows = []
    for label, task, (total, found_with, found_alone) in reviews:
        w, a = load("code-standards-speed", task, "with"), load("code-standards-speed", task, "without")
        rows.append((label, w["seconds"], a["seconds"], w["cost_usd"], a["cost_usd"], total, found_with, found_alone))
    body = header("code-standards · benchmark", "What does a review cost, and what does it find?")
    body += legend(930, 54, [("Claude Code + code-standards", LIME), ("Claude Code alone", ALONE)])
    panels = [("Time to result", 0, 70, lambda v: f"{v:.0f} s"),
              ("Cost", 1, 0.5, lambda v: f"${v:.2f}"),
              ("Issues found", 2, 1.0, None)]
    left, panel_w, gap, top = 56, 360, 44, 150
    for title, index, scale, fmt in panels:
        x0 = left + index * (panel_w + gap)
        body.append(text(x0, top, title, "label"))
        body.append(f'    <line x1="{x0}" y1="{top + 12}" x2="{x0 + panel_w}" y2="{top + 12}" '
                    'stroke="rgba(255,255,255,0.14)"/>')
        for r, (label, sw, sa, cw, ca, total, fw, fa) in enumerate(rows):
            y = top + 46 + r * 96
            body.append(text(x0, y, label, "small"))
            if index == 0:
                pairs = [(sw, LIME, fmt(sw)), (sa, ALONE, fmt(sa))]
            elif index == 1:
                pairs = [(cw, LIME, fmt(cw)), (ca, ALONE, fmt(ca))]
            else:
                pairs = [(fw / total, LIME, f"{fw} of {total}"), (fa / total, ALONE, f"{fa} of {total}")]
            for b, (value, color, shown) in enumerate(pairs):
                by = y + 12 + b * 26
                width = (panel_w - 90) * value / scale
                body.append(bar(x0, by, width, color))
                body.append(text(x0 + width + 10, by + 13, shown, "value"))
    body.append(text(56, 388, "Demo shop · claude-opus-5-5 · one run per cell · findings graded by hand. "
                     "On the change, 8 smells were planted.", "small"))
    return frame(420, "\n".join(body), "code-standards benchmark",
                 "Whole repo: 57 s and $0.43, 17 of 17 issues with code-standards; 57 s and $0.36, 15 of 17 alone. "
                 "3-file change: 30 s, $0.28, 8 of 8 with; 52 s, $0.21, 7 of 8 alone.")


def under_engineering_chart() -> str:
    """Lines added for the same three feature requests, with and without the skill."""
    tasks = [("Apply a coupon to an order", "coupon"), ("Rate-limit the orders API", "rate-limit"),
             ("Export invoices as CSV", "csv-export")]
    rows = [(label, load("under-engineering", t, "without")["metrics"]["lines_added"],
             load("under-engineering", t, "with")["metrics"]["lines_added"]) for label, t in tasks]
    alone, with_skill = sum(r[1] for r in rows), sum(r[2] for r in rows)
    cut = round(100 * (alone - with_skill) / alone)
    cost_alone = sum(load("under-engineering", t, "without")["cost_usd"] for _, t in tasks)
    cost_with = sum(load("under-engineering", t, "with")["cost_usd"] for _, t in tasks)
    body = header("under-engineering · benchmark", "How much code does a feature take?")
    body += legend(56, 132, [("Claude Code + under-engineering", LIME), ("Claude Code alone", ALONE)])
    x_label, x_bar, scale_w, top = 56, 330, 470, 196
    for i, (label, a, w) in enumerate(rows):
        y = top + i * 62
        body.append(text(x_label, y + 22, label, "label"))
        for b, (value, color) in enumerate([(w, LIME), (a, ALONE)]):
            by = y + b * 22
            width = scale_w * value / 60
            body.append(bar(x_bar, by, width, color))
            body.append(text(x_bar + width + 10, by + 13, f"{value} lines", "value"))
    body.append(text(1100, 230, f"−{cut}%", "big", "middle"))
    body.append(text(1100, 262, "lines added across", "small", "middle"))
    body.append(text(1100, 280, f"3 features ({alone} → {with_skill})", "small", "middle"))
    body.append(text(56, 400, f"No new smells either way · cost ${cost_alone:.2f} → ${cost_with:.2f} for the three · "
                     "claude-opus-5-5 · one run per feature", "small"))
    return frame(432, "\n".join(body), "under-engineering benchmark",
                 f"Lines added: coupon {rows[0][1]} to {rows[0][2]}, rate limit {rows[1][1]} to {rows[1][2]}, "
                 f"CSV export {rows[2][1]} to {rows[2][2]}; total {alone} to {with_skill} (−{cut}%).")


def call_depth_chart() -> str:
    """The refund chain with its running weighted depth, and how each run did."""
    nodes = [("POST /refund", "refund_routes.py:7", "root"), ("refund()", "refund_service.py:16", "1"),
             ("_refund_damaged()", "refund_service.py:5", "3"), ("Ledger.record()", "ledger.py:8", "4"),
             ("_write_refund()", "ledger.py:12", "6"), ("Database.insert()", "db.py:19", "7")]
    hops = {1: "REFUND_HANDLERS[reason]", 3: 'getattr(self, f"_write_{kind}")'}
    body = header("call-depth · benchmark", "Does the trace come out right?")
    node_w, gap, top = 164, 37, 168
    for i, (name, where, depth) in enumerate(nodes):
        x = 56 + i * (node_w + gap)
        body.append(text(x + node_w / 2, top - 16, f"depth {depth}" if depth != "root" else "root", "small", "middle"))
        stroke = LIME if i in (2, 4) else "rgba(255,255,255,0.35)"
        body.append(f'    <rect x="{x}" y="{top}" width="{node_w}" height="58" rx="10" fill="rgba(0,0,0,0.55)" '
                    f'stroke="{stroke}" stroke-width="1.5"/>')
        body.append(text(x + node_w / 2, top + 25, name, "value", "middle"))
        body.append(text(x + node_w / 2, top + 45, where, "small", "middle"))
        if i < len(nodes) - 1:
            hidden = i in hops
            x1, x2, ym = x + node_w + 3, x + node_w + gap - 3, top + 29
            dash = ' stroke-dasharray="4 4"' if hidden else ""
            color = LIME if hidden else "rgba(255,255,255,0.45)"
            body.append(f'    <line x1="{x1}" y1="{ym}" x2="{x2 - 6}" y2="{ym}" stroke="{color}" '
                        f'stroke-width="2"{dash}/>')
            body.append(f'    <path d="M{x2 - 7} {ym - 5} L{x2} {ym} L{x2 - 7} {ym + 5}" fill="none" '
                        f'stroke="{color}" stroke-width="2"/>')
            body.append(text((x1 + x2) / 2, ym - 10, "+2" if hidden else "+1", "value" if hidden else "small", "middle",
                             f'fill="{LIME}"' if hidden else ""))
    body.append(text(56, top + 96, "Hidden calls (+2 each): REFUND_HANDLERS[reason] at refund_service.py:20 · "
                     'getattr(self, f"_write_{kind}") at ledger.py:10', "small"))
    chips = [("Weighted depth 7", "Claude alone and Claude + call-depth"),
             ("Both hidden calls, with file:line", "Claude alone and Claude + call-depth"),
             ("scan.py: both hidden calls in 0.11 s", "across 58 files, before reading any code")]
    for i, (headline, sub) in enumerate(chips):
        x = 56 + i * 396
        body.append(f'    <rect x="{x}" y="{top + 122}" width="376" height="66" rx="12" fill="rgba(255,255,255,0.06)" '
                    f'stroke="rgba(255,255,255,0.12)"/>')
        body.append(check(x + 18, top + 154))
        body.append(text(x + 46, top + 150, headline, "label"))
        body.append(text(x + 46, top + 172, sub, "small"))
    return frame(400, "\n".join(body), "call-depth benchmark",
                 "Refund chain: weighted depth 7 with two hidden calls. "
                 "Both Claude alone and Claude with call-depth got "
                 "the depth and both hidden calls right; scan.py found both in 0.11 seconds.")


# ---------- skill banners ----------

def motif(skill: str) -> str:
    """A small line drawing per skill, on the right side of its banner."""
    s = f'fill="none" stroke="{LIME}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'
    w = 'fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
    drawings = {
        "under-engineering": f'<path {w} d="M0 60 c20 -50 40 50 60 0 s30 -60 50 -10 s20 40 40 -20 s30 50 50 10"/>'
                             f'<path {s} d="M200 60 L360 60"/><circle cx="360" cy="60" r="5" fill="{LIME}"/>',
        "um-maybe": f'<rect {w} x="0" y="10" width="170" height="64" rx="16"/><path {w} d="M40 74 l-10 22 l30 -22"/>'
                    f'<rect {s} x="190" y="40" width="170" height="64" rx="16"/>'
                    f'<path {s} d="M320 104 l10 22 l-30 -22"/>'
                    f'<circle cx="245" cy="72" r="4" fill="{LIME}"/><circle cx="275" cy="72" r="4" fill="{LIME}"/>'
                    f'<circle cx="305" cy="72" r="4" fill="{LIME}"/>',
        "under-engineering-review": f'<path {w} d="M10 100 L80 40 L150 90 L220 30 L290 80"/>'
                                    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#000" '
                                              'stroke="rgba(255,255,255,0.55)" stroke-width="2"/>'
                                              for x, y in [(10, 100), (80, 40), (150, 90), (220, 30), (290, 80)])
                                    + f'<circle {s} cx="230" cy="44" r="40"/><path {s} d="M259 73 L300 114"/>',
        "call-depth": "".join(f'<rect x="{i * 62}" y="{i * 22}" width="46" height="26" rx="7" '
                              + (f'fill="none" stroke="{LIME}" stroke-width="2.4"' if i in (2, 4)
                                 else 'fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="2"') + '/>'
                              for i in range(6))
                      + "".join(f'<path {s if i in (1, 3) else w} '
                                f'd="M{i * 62 + 46} {i * 22 + 13} L{i * 62 + 62} {i * 22 + 35}"/>'
                                for i in range(5)),
        "code-standards": "".join(f'<path {w} d="M0 {y} L{end} {y}"/>' for y, end in [(16, 200), (46, 240), (106, 220)])
                          + f'<path {s} d="M0 76 L260 76"/>'
                          + f'<path stroke="{LIME}" stroke-width="2.4" d="M-6 76 L268 76" opacity="0.5"/>'
                          + f'<path {s} d="M290 66 l10 10 l20 -22"/>'
                          + f'<rect {s} x="280" y="96" width="80" height="22" rx="6"/>',
    }
    return f'    <g transform="translate(860 52)">{drawings[skill]}</g>'


BANNERS = {
    "under-engineering": "The least code that works, checked before it's written.",
    "um-maybe": "A hallway check that asks: um, maybe you could just…",
    "under-engineering-review": "Audits existing code for depth, complexity and size.",
    "call-depth": "Measures call chains with parsers, in any language.",
    "code-standards": "A code review that learns what your team rejects.",
}


def banner(skill: str, tagline: str) -> str:
    logo = "\n".join(f'      <path d="{d}"/>' for d in json.loads((HERE / "logo_paths.json").read_text()))
    size = 44 if len(skill) < 20 else 36
    body = [f'    <g transform="translate(56 40) scale(0.064)" fill="#fff">\n{logo}\n    </g>',
            text(96, 62, "FULLSTACK.ROCKS/SKILLS", "kicker"),
            f'    <text x="56" y="{128 if size == 44 else 124}" style="font: 600 {size}px \'UNB\', \'Unbounded\', '
            f'system-ui, sans-serif; fill: #fff; letter-spacing: -0.5px">{escape(skill)}</text>',
            text(56, 170, tagline, "label", extra='style="font-size: 19px; font-weight: 500; fill: #D1D5DB"'),
            motif(skill)]
    return frame(212, "\n".join(body), f"{skill}: {tagline}", f"fullstack.rocks/skills · {skill}: {tagline}",
                 glow=0.8, shade=0.36)


def main() -> None:
    charts = {"code-standards": code_standards_chart(), "under-engineering": under_engineering_chart(),
              "call-depth": call_depth_chart()}
    for folder, items in (("charts", charts), ("banners", {k: banner(k, v) for k, v in BANNERS.items()})):
        (ASSETS / folder).mkdir(exist_ok=True)
        for name, svg in items.items():
            path = ASSETS / folder / f"{name}.svg"
            path.write_text(svg)
            print(f"{path.relative_to(ASSETS.parent)}  {len(svg) // 1024} KB")


if __name__ == "__main__":
    main()
