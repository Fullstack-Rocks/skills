# Delegation plan: the Kaelvorn redesign

project: mmorpg-demo
goal: the live site looks like its six concept mock-ups (`art/gallery/concept-*.png`): a painted logo, a redesigned navigation, crown-moulded frames, painterly brush-stroke edges on art and panels, painted icons, designed SVG or painted elements instead of CSS drawings, and one level of framing (no cards inside cards).

## audit
- role: Visual auditor
- agent: codex
- model: gpt-6.1-sol
- effort: high
- why: its browser compares the live pages with the mock-ups, with screenshots; Codex drives headless Chrome with Playwright and views the screenshots (reassigned from Antigravity, whose quota ran out)
- mode: write
- uses: art/gallery/concept-*.png (the target look), docs/STYLE.md (the art direction), docs/SPEC.md (routes and components)
- makes: docs/redesign/audit.md, docs/redesign/screens/*.jpg
- handed to: svg-art (the CSS-drawn elements to redraw), build-shell (what to change in the shared components), build-pages (cards inside cards and square art, by route)
- done when: every gap between the live site and the mock-ups is listed by route and component, with the CSS-drawn elements, the cards inside cards, the square art and the places for crown moulding and icons each named

## nav-concepts
- role: UI concept artist, navigation
- agent: codex
- model: gpt-6.1-sol
- effort: medium
- why: Codex paints UI and layout mock-ups in the style bible
- mode: write
- uses: docs/STYLE.md (the prompt prefix), art/gallery/concept-*.png (the site's look), art/style/anchor-4-icons.png (the painted icon style)
- makes: art/redesign/nav/*.png
- handed to: build-shell (the navigation to build, once one is chosen)
- done when: three distinct navigation concepts, each shown at desktop and phone width, readable as a build reference

## logo-concepts
- role: Logo designer, concepts
- agent: codex
- model: gpt-6.1-sol
- effort: medium
- why: Codex renders lettering and emblems well
- mode: write
- uses: docs/STYLE.md (the palette and medium), art/style/candidate-a.png (the look), content/lore.md (what Kaelvorn is)
- makes: art/redesign/logo-concepts/*.png
- handed to: logo-final (the concept to finish, once one is chosen)
- done when: three distinct logo concepts, each a wordmark and an emblem that also reads at favicon size

## logo-final
- role: Logo finisher
- agent: cursor
- model: gpt-5.6-sol
- effort: medium
- why: drives Nano Banana through `gemini-api image` with the chosen concept as reference, and keys the background out with Pillow; Cursor's shell runs `gemini-api image` (reassigned from Antigravity, whose quota ran out)
- mode: write
- uses: art/redesign/logo-concepts/*.png (the chosen concept is named in the brief), docs/STYLE.md (the palette)
- makes: art/brand/*.png
- handed to: build-shell (the logo for the header, the footer and the favicon)
- done when: the wordmark lockup, the emblem alone and a favicon, each a transparent PNG with clean edges on dark and light backgrounds

## ornaments
- role: Ornament painter, crown moulding
- agent: cursor
- model: gpt-5.6-sol
- effort: medium
- why: Nano Banana with the anchors as references keeps the ornaments in the painted brass style; Cursor's shell runs `gemini-api image` (reassigned from Antigravity, whose quota ran out)
- mode: write
- uses: docs/STYLE.md (the palette), art/style/anchor-4-icons.png (the brass rendering), art/gallery/concept-*.png (where frames sit)
- makes: art/ui/frames/*.png
- handed to: build-shell (the frame pieces for the card component)
- done when: a crown crest, four corners and edge strips that tile, as transparent PNGs, sized for a 9-slice frame, with a contact sheet showing them assembled

## masks
- role: Brush-stroke painter, masks
- agent: cursor
- model: gpt-5.6-sol
- effort: medium
- why: Nano Banana paints convincing oil brush edges; Cursor's shell runs `gemini-api image` (reassigned from Antigravity, whose quota ran out)
- mode: write
- uses: docs/STYLE.md (the brushwork), art/style/candidate-a.png (the stroke character)
- makes: art/ui/masks/*.png
- handed to: build-shell (CSS mask images for art and panels)
- done when: brush-edged masks for 16:9, 2:3, 3:2 and 1:1 art, a wide banner and two divider strokes, as white-on-transparent PNGs that work as CSS `mask-image`

## ui-icons
- role: Icon painter, interface
- agent: cursor
- model: gpt-5.6-sol
- effort: medium
- why: Nano Banana with the icon study as reference matches the painted icons; Cursor's shell runs `gemini-api image` (reassigned from Antigravity, whose quota ran out)
- mode: write
- uses: art/style/anchor-4-icons.png (the icon style to match), docs/STYLE.md (the palette)
- makes: art/ui/icons/*.png
- handed to: build-shell (the navigation and section icons)
- done when: painted icons for Home, World, Callings, Skills, Crafting, Adventures, Gallery, News, Launch, More, Close and Menu, each a transparent PNG readable at 32 px

## svg-art
- role: Illustrator, SVG elements
- agent: codex
- model: gpt-6.1-sol
- effort: high
- why: Codex writes clean, accessible SVG by hand
- mode: write
- uses: docs/redesign/audit.md (the CSS-drawn elements to redraw), art/gallery/concept-*.png (the look), docs/STYLE.md (the palette)
- makes: src/assets/svg/**
- handed to: build-shell (the SVGs that replace the CSS drawings)
- done when: every CSS-drawn decorative element the audit names has a designed SVG, or the audit's reason to drop it

## atlas
- role: Cartographer, painted atlas
- agent: codex
- model: gpt-6.1-sol
- effort: medium
- why: Codex paints in the style bible and can view its own image to place the region pins
- mode: write
- uses: docs/redesign/audit.md (the atlas must be painted art), art/gallery/concept-map.png (the parchment map look), content/lore.md (the continent's shape and regions), src/data/world.ts (the six region ids)
- makes: art/ui/atlas/*.png, art/ui/atlas/regions.json
- handed to: build-shell (the world map's backdrop and pin positions)
- done when: a painted parchment map of the crescent continent with the six regions in their places, and regions.json giving each region's pin as x and y percentages measured on the image

## build-shell
- role: Builder A, design system and shell
- agent: codex
- model: gpt-6.1-sol
- effort: xhigh
- why: the shared components every page is built on, and the hardest code of the redesign
- mode: write
- uses: docs/redesign/audit.md (what to change), docs/redesign/screens/*.jpg (the site before, beside the mock-ups), art/gallery/concept-*.png (the look to match), art/redesign/nav/*.png (the chosen navigation is named in the brief), art/brand/*.png (the logo), art/ui/frames/*.png (crown moulding), art/ui/masks/*.png (brush edges), art/ui/icons/*.png (painted icons), src/assets/svg/** (the redrawn elements), art/ui/atlas/* (the painted world map and its pin positions)
- makes: src/components/ui/**, src/shell/a/**, src/styles/**, src/features/b/**, public/images/ui/**
- handed to: build-pages (the frame, mask and icon components to apply), review (the shell and the interactive pages)
- done when: the header, navigation, frames, masks and icons match the mock-ups on every page at 375, 768 and 1440 px, with the checks green

## build-pages
- role: Builder C, content pages
- agent: cursor
- model: gpt-5.6-sol
- effort: high
- why: a second builder on another model, on the pages only
- mode: write
- uses: docs/redesign/audit.md (cards inside cards and square art, by route), docs/redesign/screens/*.jpg (the pages before), src/components/ui/** (the frame, mask and icon components), public/images/ui/** (the processed frame, mask and icon images), art/gallery/concept-*.png (the look)
- makes: src/pages/c/**, src/content/c/**
- handed to: review (the content pages)
- done when: no card sits inside a card, the art on every page has brush edges, and the checks are green

## review
- role: Visual reviewer
- agent: codex
- model: gpt-6.1-sol
- effort: high
- why: its browser, side by side with the mock-ups; Codex drives headless Chrome with Playwright and views the screenshots (reassigned from Antigravity, whose quota ran out)
- mode: write
- uses: src/** (the built site), art/gallery/concept-*.png (the target), docs/redesign/audit.md (the gaps that had to close)
- makes: docs/reviews/10-visual-review.md, docs/reviews/screens/redesign-*.jpg
- handed to: final
- done when: each audit item is marked closed or open with a screenshot, and the verdict says whether the site matches its mock-ups

## benchmark
- role: Benchmark writer
- agent: codex
- model: gpt-6.1-sol
- effort: medium
- why: careful arithmetic from the usage, price and image ledgers, and a self-contained SVG chart and HTML page
- mode: write
- uses: docs/benchmark/usage.json (every delegation), docs/benchmark/orchestrator.json (the orchestrator's cost, split by stage), docs/benchmark/prices.md (list prices with sources), docs/DECISIONS.md (what happened and why), art/prompts.md (the image ledger), delegation-plan.md (the redesign's units), docs/BENCHMARK.md (the first benchmark, to extend)
- makes: docs/BENCHMARK.md, docs/benchmark/chart.svg, docs/benchmark/index.html
- handed to: final
- done when: every agent's runs, time, tokens, images and dollars are shown for the build, the redesign and both together, beside the orchestrator's, with every figure traceable
