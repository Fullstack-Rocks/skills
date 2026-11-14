# Layout rules

What raised and lowered scores across 40+ reviewer rounds on four architecture diagrams. A reviewer's score on an unchanged page moves by about ±0.5, so the rules below are the ones that moved scores repeatedly or by a point or more.

## Pages

- **One story per page.** No polishing rescues an overloaded page: pages carrying two stories sat at 7–8 for eight rounds, then scored 8 or more on the first try once split. Split before polishing whenever a page mixes a main flow with failure handling, or topology with identity.
- **At most about 15 numbered steps per page.** Beyond that, split.
- **Pick the form for the story:**

  | Story | Form |
  |---|---|
  | Where things live and how traffic gets in and out | Topology page with containers and lanes |
  | A request or event over time | Sequence diagram |
  | A pipeline of jobs | One lane per job, steps left to right |
  | Every rule, permission or link of one kind | Inventory table page |
  | "What does X have?" | Per-entity table: one row per entity, one column per attribute |
  | The whole system | Overview map |

- **Draw all of a kind, or none of it.** When a page draws some relationships of a kind as arrows and lists the rest, readers take the missing arrows as "not allowed". Give each kind of relationship a page where every instance is an arrow, and put the complete inventory on a table page.
- **The overview is only a map.** A few boxes, one line each, ending with "Details: page X". Every attempt to answer a detail question on the overview lowered its score. Tell reviewers it is the map.
- **Put the hardest idea on its own page as a picture with concrete values.** For example, a tag explained with real tag values, or a strip of numbered runs with "why this order". Reviewers called these the best teaching parts every time.
- **Keep the page about 2,000 px wide or less, with text at 13–16 px.** Reviewers see a scaled-down image; a 2,800 px strip made 12 px text unreadable and scored 5.

## Layout and lines

- **Zero crossings, by construction.** Lay out lanes before drawing a single edge: pick the main flow's direction, and reserve separate lanes for ingress, egress and back-references. Route each edge by hand with fixed ports; automatic routers gave detours and colliding labels. The checker must report zero crossings before any styling.
- **Put the hubs in the middle.** Place the busiest targets (databases, caches) centrally, and put each source that reaches two hubs between them, with one arrow up and one down.
- **Put each target under its step.** In a pipeline, each step's target sits directly below it with one short vertical arrow, and chains continue downward.
- **Order columns so unavoidable crossings hit plain lifelines.** In a sequence diagram, a crossing over an active wait bar or a text box is read as a defect; one over a plain lifeline mostly isn't.
- **Keep parallel lines at least 40 px apart.** Lines 12–25 px apart read as one line, and their labels can't be assigned.
- **Make arrows at least 40 px long.** Shorter arrows hide their dashing and arrowhead.
- **One box per concept.** Two boxes for the same thing (two "version N" boxes) read as two things.
- **Size boxes to their text.** Empty boxes and notes taller than their text drew complaints every round; sizing to content gained about 0.5 each time.
- **A leftover empty region costs less than breaking the flow's direction.** Filling empty space by moving lanes side by side lowered scores.

## Marks are claims

- **Position is a claim.** Readers take an icon's container as fact, and a caption doesn't override it. A resource spanning two zones needs a drawn replica (a faded copy in the other zone, with a legend row), not a note.
- **An arrow does what its label says.** A label saying "through X" on an arrow that skips X made a reviewer call the diagram self-contradicting.
- **A note sits inside the container it describes.**
- **Start an arrow at the real caller.** An arrow starting from a group's border means "every member"; use that only for group-level rules, and give it a legend row.
- **Name each concept once.** Two meanings for one word ("stage", "live", "record") were found quickly and cost understanding. Codes for steps or lanes must not collide with page ids.

## Labels

- **Labels only on clear straight segments.** Keep them off bends, shared trunk segments, container borders and other lines, and give each label a white background.
- **Label = purpose in plain words, then protocol and port on a second, smaller line**, for example "Run batches" over "TCP 6379".
- **Number the path a reader must follow** with badges set apart from data: "3 443" was read as port 3443, so use circled numbers or badges, and dotted numbers (1.1, 1.2) when notes refer to steps.
- **Put a step's detail beside the step, in a full sentence with a subject**, never in a far column. A detail box must not cover a lifeline's wait bar.
- **Name every token and identifier where it first appears**, with a one-clause "why".
- **Explain jargon next to where it's used**, and put plain words before raw syntax.

## Sequence diagrams

- **Keep container zones to the header row** around the participant icons. Full-height zone columns put labels on their borders.
- **Draw each alternative outcome in a dashed frame** whose tab states the condition ("If ai-runtime answers 2xx"). A header band alone reads as "next steps".
- **Use a solid band for a separate scenario** ("Each time the relay starts…"), visibly different from an alternative's frame.
- **Draw a held-open wait as a bar on the lifeline**, and a resumed wait as a dashed bar.
- **Draw every answer that decides something or ends the flow** (a branch's reply, a token check, the stream ending), and leave out plain acknowledgements.
- **Label what triggers each section** ("After step 9, while a delegated Run still streams").

## Legend and style

- **One visual language on every page:** the same colour and line style mean the same thing everywhere.
- **Each page's legend lists only the styles that page uses.** A shared legend of every style lowered every page by 0.5–1.
- **One meaning per style.** Reusing a style for a second concept was a top complaint; so were near-identical colours and line weights.
- **Make the legend sample match its real use** on that page.
- **Use a neutral style for footnotes**, distinct from an actor's action box.

## Requests to decline

Reviewers contradict each other; chasing every request causes churn. Decline any change that adds a crossing, makes a mark untrue, or puts a label on a bend or shared segment. Among the rest, take the ones that remove a misreading, and ignore aesthetic preferences that flip between reviewers. Record each such decision in the decisions log.
