---
name: readable-diagrams
description: Builds architecture, network, sequence and pipeline diagrams that a newcomer can read, in any diagram tool, and proves it with geometry checks and scored rounds by fresh reviewer agents. Use when creating or redrawing a system or infrastructure diagram, when a diagram is hard to read (lines crossing, crowded pages), or when asked to score or review a diagram's readability.
---

# Readable diagrams

A diagram is **readable** when an engineer new to the system can answer concrete questions about it from the picture alone, and explain it afterwards. It is done when it passes the **gate**:

- `scripts/check_diagram.py` reports no findings on every page;
- fresh reviewers answer every checked question correctly;
- the median reviewer score is at least **8.5 / 10 for readability and for understanding** on every page (override the bar if the human sets another).

The rules here come from 40+ scored rounds on real architecture diagrams. What raised scores was almost always structure (splitting, lanes, frames, one meaning per mark), rarely polish.

## Step 1: Choose the tool

Ask the human which tool to draw in, with your environment's question tool if it has one. Offer the tools you can both write and render to PNG here, for example draw.io (`.drawio` XML), Mermaid, D2, PlantUML, Graphviz or Excalidraw, plus whatever the project already uses. Then read [`references/rendering.md`](references/rendering.md) for how to render that tool to PNG and how to export the geometry the checker needs.

Done when the tool is chosen and you have rendered one test file to a PNG you have looked at.

## Step 2: Gather the facts and the questions

Read the source of truth (code, infrastructure definitions, specs) before drawing. Every mark you draw is a claim; draw only what the source states, and label anything it leaves undefined as "not defined in the source" instead of guessing.

Write two things to a working file:

1. **The fact list**: each component with where it lives, and each relationship with caller, callee, protocol and port, and its source location. Generate every page from this one list, so pages can't contradict each other.
2. **The question bank**: 2–3 questions per planned page whose answers you checked against the source. Include at least one "why" or "what happens when X fails" question per page, so understanding doesn't saturate.

Done when every relationship you will draw has a source location, and every page has checked questions.

## Step 3: Plan pages and the decisions log

Split by **story**: one question per page. Read [`references/layout-rules.md`](references/layout-rules.md) and choose a page form for each story (topology, sequence, lanes, inventory table, overview map).

Write a **decisions log**: the style choices fixed before round 1 and closed to debate (legend scope, lane direction, colour per meaning, naming scheme, page ids). Reviewers get it, which stops them flipping each other's preferences.

Done when each page has one story, a form, its questions, and the log is written.

## Step 4: Build and check

Build every page following [`references/layout-rules.md`](references/layout-rules.md). After each build:

1. Export each page's geometry to the JSON format in [`references/geometry-format.md`](references/geometry-format.md) and run `python3 scripts/check_diagram.py <geometry.json>`. Treat every finding as a bug; fix it in the layout, never by hiding it.
2. Render every page to PNG and look at each one yourself, cropping where text is small. The render catches what geometry estimates miss: text overflowing a box, labels shifted by the tool's text layout, clipped lanes.
3. Be the first reviewer. Answer every question in the bank from your PNGs alone, and for each answer name the step label, table cell or frame title it came from. An answer that lives only in a side note, or nowhere, is a bug: move the fact onto the step (see "Put the answer on the step" in the layout rules). Then walk every arrow: it starts at the actor that acts, a reply is dashed, and a waiting step names its trigger; on sequence pages, a loop frame covers every repeating step and states its end condition.

Done when the checker prints `OK`, every question is answered from a label, cell or title on your own PNGs, and you have looked at every PNG of this build. These are the requests reviewers repeated round after round; settling them here is what lets pages pass in round 1.

## Step 5: Review rounds

Run rounds as in [`references/review-protocol.md`](references/review-protocol.md): three fresh reviewer agents per round, images only, checked questions, the rubric, then `python3 scripts/score_round.py` for medians and the gate. Fix what blocks understanding first, rebuild (Step 4), and rerun.

- **Freeze** a page once it passes. Edit it again only to fix a wrong answer; a partial misreading or a cleanup for consistency goes in the decisions log instead, because edits to passed pages cost them their pass. Keep the passed version, and when an edited page scores lower, restore it.
- **Restructure on a plateau.** When a page's median hasn't risen for two rounds, change its form (split it, turn prose into a table or a sequence, move detail to its own page) instead of polishing.
- Stop after 8 rounds. Deliver the best version that passed most pages, and report the score table and what still falls short.

Done when every page passes the gate, or the round limit is reached and reported.

## Step 6: Deliver

Commit the diagram source, the PNGs and the generator if you used one, so later edits don't mean hand-editing exports. Report the score table per round and page, each page's final medians, and any fact the source left undefined.
