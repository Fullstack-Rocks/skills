# Building the inventory and task sets

Tasks come from what users do in today's product, never from what the new UI happens to offer. A rebuilt page keeps every capability of today's page: simplifying means re-arranging things, never dropping them.

## Inventory

Hand one read-only agent the product's source of truth for the area under test (its screens or compositions, its locale strings, its specs) and ask it to list today's capabilities with exact label strings and file paths:

- views, groups and filters;
- what each list row shows;
- the sections of a record;
- every item of every menu, including the "more" menus;
- dialogs and their fields;
- empty states and keyboard shortcuts.

Save it as `<records>/inventory-<area>.md`. Done when every screen of the area has its section and every label is quoted as the product shows it.

## Journeys

Turn the inventory into numbered journeys: what a user comes to do, end to end ("return one item from an order and get a refund"). Every capability in the inventory belongs to at least one journey.

## Sets

A set is 4–6 tasks run by one tester in order, in one area, on one screen size:

- a laptop at 1440 × 900;
- a smaller laptop at 1280 × 800;
- a phone at 390 × 844.

Mix three kinds of task: **find and read** (an answer to report), **act** (an end state to reach) and **act, then verify** (change something, then read it back). Give each set its persona and how to reach it (a URL parameter, a role switch, a start page).

Write each task as a **goal**:

- It says what to achieve: "Have the order from yesterday shipped to the second address on your account."
- It names no button, menu or path, and never quotes the label the tester has to find.
- It carries everything the task needs: a name to invite, an amount to enter.
- Names in another language or script come with an English gloss, so the tester can match them.

Write the **expected answer** or end state in brackets after the task. It never reaches the tester.

```markdown
### Set 2 — Orders, laptop 1440 × 900, customer
1. Find your most recent order of a lamp and tell me what it cost with delivery. [<amount from the seed data>]
2. Change that order's delivery to the following Monday. [<the new date, shown on the order>]
```

## Seed data

Each answer must exist in the seed data and be unique, with a **near-miss** beside it: two orders placed on the same day, so the tester has to check the time. Add seed rows where an answer is missing; a task the data can't answer measures nothing.

## Keeping sets stable

Keep sets the same across rounds so scores compare. Add a set when a page is rebuilt. Reword a task only when the task itself caused a miss, and note the change under the round.

Done when every set has 4–6 goal-worded tasks, each with a bracketed expected answer that the seed data supports, and every journey is covered by some set.
