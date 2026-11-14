---
name: ux-critic
description: Tests whether a first-time user can understand and work a UI. Fresh agents with no context try real tasks in a step browser, and weaker ones rate each page at a glance and each label by name; findings are triaged, fixed and re-tested in rounds until the UI passes. Use when a UI or prototype changes in ways users notice, a page is rebuilt, or asked for a UX critique, task sets, a glance test or an action-name test.
---

# UX critic

Fresh agents stand in for people who have never seen the UI. They see only the screen. The loop turns what they report into fixes and runs the next round, until the pass bars hold.

```
inventory → task sets → pre-flight → round → triage → fix → verify → record → owner review → next round
```

This is not for unit tests, visual diffs or checking code against a spec.

## Inputs

Ask for whatever the conversation hasn't given:

- the URL, and how to reach each persona (a URL parameter, a role switch, a start page);
- the area under test;
- where the product's source of truth lives: its screens, locale strings and specs;
- the **record folder**, which keeps everything that outlives a session: `ux.json`, `inventory-*.md`, `ux-tasks.md`, `glance-test.md` and `design-rules.md`.

## Setup, once per machine

```bash
npm install --prefix <skill>/scripts
npx --prefix <skill>/scripts playwright-core install chromium-headless-shell
```

## Setup, once per project

1. Write `<records>/ux.json`: the page list `pages.mjs` visits, plus the options described at the top of [`scripts/lib.mjs`](scripts/lib.mjs). Every page a task set touches, and every modal worth rating, gets an entry.

   ```json
   { "base": "http://localhost:5173/", "hide": ".proto-bar", "rowName": ".row-name", "help": ".help",
     "labelScope": "main, [role=dialog]", "labelSkip": "nav",
     "pages": [ { "name": "cart", "path": "#cart", "width": 1440, "height": 900, "steps": [] } ] }
   ```

2. Copy [`references/design-rules.md`](references/design-rules.md) to `<records>/design-rules.md` unless the project has one.
3. Build the inventory and task sets with [`references/task-sets.md`](references/task-sets.md).

Done when `ux.json` lists every page the sets touch, and every set has its tasks and bracketed expected answers in `ux-tasks.md`.

## Step 1: Pre-flight

1. Run the project's own checks (build, lint, type check), and `call-depth`'s `scan.py` on the changed code when that skill is installed.
2. Run `node <skill>/scripts/pages.mjs <records>/ux.json <scratch>/pages`. It doubles as the smoke run.
3. Open the screenshot of every changed page and look at it yourself. Check it against every rule in `design-rules.md`.

Done when the checks pass, `pages.mjs` prints `ERRORS []`, and you have looked at every changed page. Testers never start on a page you haven't looked at.

## Step 2: Run the round

Pick the sets. The first round runs all of them. Later rounds run the sets the change touches plus one **control set** it doesn't touch, unless the owner asks for all. Add a glance round when titles, subheaders or layout changed, and an action round when labels changed.

Say how many agents the round starts, and ask first when that is more than this session's agent budget. Then start every agent in the background, in parallel:

| Agent | Model | Gets | One per |
|---|---|---|---|
| **Task tester** | mid-tier model | [`agents/tester.md`](agents/tester.md), filled in | task set |
| **Glance rater** | smallest model | [`agents/glance.md`](agents/glance.md) and one page screenshot | page |
| **Action-name rater** | smallest model | [`agents/actions.md`](agents/actions.md) and about four pages' screenshots and `.txt` label lists | batch of pages |

The smallest model plays a busy user who gives the screen a few seconds: if it understands a label, a person will.

Every agent is **fresh**: a new agent each round, which never sees its earlier report or another agent's. Its prompt is the filled-in template and nothing else: no hypothesis, no "we changed X", no expected answers, no product terms beyond what the screen shows. Names in another language or script get an English gloss (`{NAMES}` in the tester template). In the tester template, `{UX}` is `<skill>/scripts/ux.mjs`, `{DIR}` is a fresh folder in scratch per tester, and `{CONFIG}` is ` <records>/ux.json`.

While testers run, the UI they can reach stays as it is: the step browser replays clicks by label. Work meanwhile on pages no running set touches, prepare fixes, or write up the round. When the planned fixes include renames on pages a running set reaches, run the round on a frozen copy of the UI instead.

Done when every agent has reported.

## Step 3: Triage

Sort every finding with [`references/triage.md`](references/triage.md), checking each against the tester's screenshot of the step where it went wrong.

Done when every finding has a kind and is either queued to fix or recorded with a reason to stay open.

## Step 4: Fix and verify

Fix every queued finding in this loop. Then re-run Step 1, plus a short script or `ux.mjs` session that walks each fixed flow, and look at each screenshot yourself.

Done when every fix has a screenshot you looked at, and pre-flight is clean again.

## Step 5: Record and report

Record the round with [`references/report.md`](references/report.md), report to the owner, and ask whether to run the next round. Every owner review becomes a quoted rule in `design-rules.md` before the next round.

Done when the round is in `ux-tasks.md` (and `glance-test.md` for rating rounds) and the owner has answered.

## Pass bars

A round passes when all of these hold:

- every task reached, or its miss explained as task wording or a harness limitation;
- navigation, knowing where I am, and calm each at 8 or above, for every set;
- no "??" in action names, except generic controls the owner accepted;
- glance sureness at 7 or above on every page;
- no rule in `design-rules.md` broken;
- pre-flight clean.

Stop when the bars hold for two rounds in a row, or when the owner says so.
