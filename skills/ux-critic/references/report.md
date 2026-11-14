# Recording a round

Task rounds go in `<records>/ux-tasks.md`, below the task sets; glance and action rounds go in `<records>/glance-test.md`. Newest round last.

## Task round

```markdown
## Round 3 (what changed since round 2, in one line)

| Set | Reached | Steps | Navigation | Know where I am | Calm | Slowed most by |
|---|---|---|---|---|---|---|
| 1 Orders, laptop | 5 of 5 | 16 | 8 | 8 | 8 | <the tester's "slowed me most", in a few words> |
| 3 Returns, laptop 1280 | 3 of 4, 1 partly | 20 | 6 | 7 | 7 | <…> |

Misses:
- Set 3, task 2 (partly): <what happened, at which step, and its kind: product, wording, harness or owner rule>.

Fixed after the round:
- <the fix, and the screenshot that verified it>.

Open:
- <finding>: <why it stays open>.
```

Steps come from the session logs. A set reached through a re-worded task is marked so.

## Glance round

| Page | Rater's "what this page is for" | Matches? | Unclear labels | Sure (0–10) |
|---|---|---|---|---|

End with the average sureness, the pages under 7, and what was renamed.

## Action round

List per page the labels marked "??" and "~", the rater's suggested wording, and what was done (renamed to …, (?) added, accepted as generic).

## Owner reviews

Quote every owner review between rounds under the round it followed, and turn each into a rule in `<records>/design-rules.md` the same day:

```markdown
### Owner review, <date>
> "<the owner's words>"
→ added to design-rules.md as "<the rule>".
```

## Report to the owner

Send the round's table, what changed since the last round, what is still open, and whether the pass bars held. Then ask whether to run the next round.
