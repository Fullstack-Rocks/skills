# Maison Lumen

A luxury brand and marketing agency, founded in Paris with a studio in Milan. Maison Lumen builds digital flagships for houses whose customers buy rarely and expect a lot: the website is treated as the boutique, not the brochure.

**Positioning.** Quiet luxury. Restraint over spectacle, craft over campaigns, and proof over adjectives. Every client site has to feel like walking into the house itself, and still meet WCAG 2.2 AA.

**What the agency does for a client**
- Brand story and voice: the house's history, what it refuses to do, and who it is for
- Identity: logo, monogram, icon set, art direction for imagery
- The digital flagship: a website that sells the experience before the product
- Case studies the agency can publish afterwards

**The three clients for this showcase** (invented brands; each is profiled by its own agent)
1. A luxury automaker: an electric grand tourer, built in small numbers
2. A haute horology house: independent, hand-finished mechanical watches
3. A private hospitality house: one estate or island, by invitation, for very few guests

## How this project is laid out

| Folder | What goes there | Who writes it |
|---|---|---|
| `research/` | One file per research topic | Antigravity agents (Gemini), via the lead |
| `clients/<slug>/profile.md` | The client: name, story, niche, audience, competitors, differentiation, voice | Codex |
| `clients/<slug>/design.jpg`, `design.md` | The homepage design image and its spec (sections, colours as hex, type, spacing) | Codex |
| `clients/<slug>/assets/` | Logo, icon set, hero and section imagery (PNG/SVG/WebP) | Antigravity (Nano Banana) |
| `sites/<slug>/` | The website: `index.html`, `styles.css`, optional `main.js`, no build step | Claude Opus 5.5 |
| `reviews/<slug>.md` | Accessibility, usability, copy and UX findings, each tagged | Grok |

**Rules every agent follows**
- Static sites only: HTML, CSS and a little JavaScript, no frameworks, no build step, no external requests except Google Fonts.
- Images are referenced relatively, from `../../clients/<slug>/assets/`.
- Accessibility is not optional: WCAG 2.2 AA contrast, real text (not text in images), keyboard focus that shows, `prefers-reduced-motion` respected, alt text that says something.
- Every brand is invented. No real company names, logos or trademarks.
