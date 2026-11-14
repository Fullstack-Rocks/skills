# Triage

A tester's report is **evidence**, not a verdict. Before acting on a finding, open the tester's screenshot of the step where it went wrong (`<session dir>/step-NN.png`) and its `session.json`, which logs every action. Count steps and wrong turns from the log, not from the tester's memory.

Sort every finding into exactly one kind:

| Kind | What happened | What it needs |
|---|---|---|
| **Product issue** | The UI misled, hid, cropped or contradicted something | Fix the UI |
| **Task wording** | The task was ambiguous or left out something it needed | Fix the task and note it under the round |
| **Harness limitation** | The step browser could not do what a person can, such as pick a dropdown option | Fix the harness, then ask whether a person would struggle there too; if so, it is also a product issue |
| **Owner rule** | A design rule in `design-rules.md` was broken | Fix it everywhere it occurs, not only where it was found |

Glance and action findings are product issues by default:

- **Glance:** where the rater's "what this page is for" differs from the page's purpose, or its sureness is under 7, rename the title or subheader, or add a (?) to the unclear term. A subheader says what the thing is; it never lists capabilities.
- **Action names:** every "??" gets a new label or a (?) icon. Review every "~", and rename it when the guess was wrong. Generic controls the owner has accepted, such as a "More actions" menu, may stay "??".

Every finding is fixed in the same loop or recorded with its reason for staying open. A fix that renames a label waits until no running tester can reach it, because the step browser replays clicks by label.

Done when every finding of every report has a kind, was checked against its screenshot, and is either fixed or recorded with a reason.
