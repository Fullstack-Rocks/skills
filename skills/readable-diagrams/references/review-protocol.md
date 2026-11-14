# Review protocol

Fresh reviewers scoring rendered images are the readability test. One reviewer per round proved too noisy for a hard gate: unchanged pages moved by ±0.5 and sometimes a full point, and a fresh reviewer always finds new nits. So each round uses three reviewers and gates on the median.

## A round

1. Render every page to PNG (see `rendering.md`) and look at each one yourself first.
2. Start **three new reviewer agents** with your environment's subagent tool. Never reuse a reviewer, so none is anchored on an earlier round. A cheaper model is fine.
3. Give each the brief below, filled in. Score only pages that changed since they last passed; frozen pages stay frozen.
4. Save each reviewer's JSON reply to a file, then run `python3 scripts/score_round.py reviewer-1.json reviewer-2.json reviewer-3.json`. It prints the median per page and which pages pass.
5. Check every answer against your fact list. A wrong answer is an understanding defect whatever the score says; fix the page that misled.
6. Fix problems tagged `blocks-understanding` first. Take a `polish` request only when it removes a misreading and the decisions log doesn't settle it.

## Reviewer brief

Fill in the bracketed parts and send it as the reviewer's whole task:

```text
You are reviewing architecture diagrams for an engineer new to [system]. Open only these images,
with your image-reading tool, and nothing else (no code, repository or web):
[absolute PNG paths, in page order]

Who reads them and what they must take away:
[one paragraph]

Page roles: [for example "01a is an overview map; judge it as a map, not as a detail page"]

Design decisions that are fixed and not up for review:
[the decisions log, one line each]

1. Answer each question from the images alone, naming the page you used:
[the checked questions, numbered]

2. Score each page from 0 to 10 on:
- readability: line crossings and overlaps, label legibility and placement, alignment,
  whitespace, visual hierarchy, legend;
- understanding: how easily a newcomer could explain what the page shows, judged after
  answering the questions.
Anchor: 8.5 means a newcomer reads it easily with only minor nits; 10 means nothing to improve.
You may crop images to read small text.

3. List up to five problems, ranked. Tag each one "blocks-understanding" or "polish", and give
its page, its location on the page and a concrete fix. List fewer than five if fewer matter.

Reply with only this JSON:
{"pages": {"<page id>": {"readability": <0-10>, "understanding": <0-10>}},
 "answers": [{"question": <n>, "page": "<page id>", "answer": "<text>"}],
 "problems": [{"rank": <n>, "page": "<page id>", "tag": "blocks-understanding|polish",
               "where": "<location>", "problem": "<text>", "fix": "<text>"}]}
```

## What the evidence says

- **Checked questions are the most reliable signal.** Every wrong or partial answer pointed at a real defect: an ambiguous label, an unclear actor, a misread position.
- **Ranked problems with fixes make a clear work list.** Letting reviewers return fewer than five stops nits being promoted to fill the list.
- **Treat a single-reviewer change of 0.5 or less as noise.** That is why the gate uses the median of three.
- **Reviewing many pages at once thins each reviewer's attention**, and the densest page drags. Keep a round to the pages that changed.
- **Fix contradictions between pages first.** The largest single-round gain (+1.0 to +1.5 understanding) came from making pages agree with each other and answering the gaps a newcomer would ask about.
