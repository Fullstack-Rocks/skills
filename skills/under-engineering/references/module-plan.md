# Module plan

The developer confirmed this is a module. Write the plan, have it scored and get it approved before you write any implementation code.

## 1. Choose where the plan lives

Look for a docs or task system: a `docs/` folder, ADRs, `CONTEXT.md`, task or issue files, or a tracker you can reach. Ask the developer whether to:

- **keep** the plan there (name the location you found), or
- keep it **disposable**, in this chat only.

If you found no docs or task system, say so and default to disposable. Wait for the answer.

## 2. Write the plan

Write the plan as documentation, in **pseudocode written in the implementation language**: real signatures, names and types, with bodies elided. It must contain:

- **Purpose:** one sentence on what the module does and what it leaves out.
- **Usage:** documentation-style examples of a caller using the module, one per feature the developer wants.
- **Boilerplate:** the complete code a new caller writes, from import to first result. Keep it to one import and a few lines.
- **Public surface:** each public function or type, with its signature and a one-line contract.
- **Implementation style:** 2–3 options (for example: plain functions, a class, or an interface with implementations), each with its trade-off. Ask which one the developer prefers.
- **Layout:** the folders and files the module will add, following the folder limits in the main skill.

## 3. Score readability

Spawn a subagent on a **weaker model** than yours, using whatever subagent and model-selection tools your environment provides. Give it [`../agents/readability-scorer.md`](../agents/readability-scorer.md) and the plan **and nothing else**: no repo context, and nothing it may read besides the plan itself. Tell it to deliver its reply through whatever channel its environment uses to report back to you. Give it a usage task the plan does not show, so it has to apply the module rather than copy an example. It represents a new developer meeting this module for the first time.

Without subagents, apply the scorer's rubric yourself, reading only the plan's text, and say that you self-scored.

### Grade its understanding

The scorer's own scores say how the plan *felt*. Its `Understanding` and `My usage` show what it actually *understood*. Grade those against the design you intended before deciding anything:

1. List the plan's **key behaviours**: what a caller must get right to use the module correctly. Examples: which entrypoint to call, which arguments, when it takes effect, what the caller owns (commit, cleanup), what it deliberately does not do.
2. Mark each one in the scorer's answer as **right**, **guessed right** (correct but stated as a guess), or **wrong** (missed, or would cause a bug).
3. Separate the plan's gaps from the task's gaps. A guess about something outside the module (the scorer's invented model fields or endpoints) is not a plan defect.

Then decide:

- **Close enough:** no key behaviour is wrong, and every guess is outside the module. Stop scoring, even if a score is below 4, and record why it is below 4 (usually a deliberate trade-off for the developer to decide).
- **Keep going:** any key behaviour is wrong, or a guess concerns the module's own surface. Revise the parts of the plan that caused it, then score again with a fresh scorer and a different usage task.
- **Stop and ask:** after three rounds without reaching close enough, or when the remaining misreading comes from a design choice rather than wording. Present the grade to the developer as a decision.

Record the scores, the understanding grade and the decision for each round in the plan.

## 4. Confirm coverage

Present the plan and ask the developer:

- whether they want more or more detailed examples
- whether the examples together cover **every feature** they want from the module, and which are missing if not
- which implementation style they prefer

Loop through steps 2 to 4 until the developer approves. If they chose to keep the plan, save the approved version to the docs location.

Done when the developer has approved coverage and a style. Then return to Step 5 of the main skill.
