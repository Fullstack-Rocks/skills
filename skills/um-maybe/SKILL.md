---
name: um-maybe
description: Hallway check that challenges an implementation plan's complexity. A weaker colleague agent with no context questions it and offers simpler options, then the human decides. Use on a plan before implementing, or when under-engineering calls for it.
---

# Um, maybe?

A **hallway** check: you pitch your plan to a colleague who knows nothing about the task. Their view is simple because they lack the context, and that is the point. Their counter is usually "um, maybe you could just ...": strip most of the work and get to the point. Your job is to **defend** each piece of the plan with **proof**, or concede it. Whatever you can't prove goes to the human.

**Proof** that a piece is needed is one of:

- **Requested:** the human asked for it. Quote their words.
- **Demanded:** something the human asked for can't work without it. State the chain in one or two sentences, ending at a quote.

Your own judgement isn't proof. That includes "best practice", "future-proofing", "it's cleaner" and "other code does it this way". A piece backed only by judgement is **unproven**.

## Step 1: Write the pitch

Write the plan the way you would explain it in a hallway, in plain language and under 15 lines:

- the problem, in one sentence
- what the human asked for, quoted
- each piece you plan to build, one line each, with why

Leave out file paths and code. Name every **extra**: a piece beyond the bare request, such as validation, retries, caching, config, abstraction layers, audit, permissions, backfills or new modules.

Done when every planned piece appears in the pitch.

## Step 2: Hallway rounds

Spawn a subagent on a **weaker model** than yours, using whatever subagent and model-selection tools your environment provides. Give it [`agents/colleague.md`](agents/colleague.md) followed by the pitch, **and nothing else**. Tell it to work only from the pitch, looking nothing up, and to deliver each reply through whatever channel its environment uses to report back to you.

For each question it asks, write a reply:

- **Concede:** its simpler option meets the request. Adopt it in the plan.
- **Defend:** give the proof, plus only the context it needs to judge the proof. Say what goes wrong in the simpler option, concretely.
- **Can't defend:** say so plainly. The piece is unproven.

Before you defend a piece, take the colleague's view seriously: a plain question you can only answer with judgement is a finding, not a misunderstanding. When you add context, give it facts in the message; never tell it to go and look something up.

Send all replies in one follow-up message to the same subagent, so it keeps the conversation so far. If your environment can't continue a subagent, start a fresh one with the colleague prompt, the pitch and the full exchange so far. Run at most **three rounds**. Stop early when it reports "Still unsure on: nothing".

Without subagents, play the colleague yourself, using only the pitch text, and say in your report that you did.

Done when three rounds are complete, or the colleague is convinced on every question.

## Step 3: Weigh each piece

For every piece of the plan, including the ones the colleague didn't question, decide which group it belongs to:

- **Simplified:** you conceded, or the talk revealed a simpler shape. Note what it was before and what it is now.
- **Kept:** it has proof, and you can name no simpler option that still meets the request.
- **Unproven:** it has no proof, or a simpler option might still meet the request. List every simpler option you found, each with what it gives up.
- **Belongs elsewhere:** it is a decision or job for someone other than this codebase. Examples: infrastructure (firewall, IAM, storage lifecycle, gateway limits), legal or compliance, product decisions (behaviour the human hasn't specified), or another team. Name the owner.

Also check that the kept pieces fit the codebase without adding more complexity than they save.

Done when every piece is in exactly one group.

## Step 4: Ask the human

Send one message, then wait. Always end by asking whether the simpler plan makes sense. List every unproven piece with its options. Make no unproven piece part of the plan without the human's answer.

```
Um, maybe? Hallway check on <task>
Rounds: <n>. Colleague's view: <its one-sentence summary of the point>

Simplified:
  - <piece>: <before> -> <now>
Kept, with proof:
  - <piece>: <quote, or the chain to a quote>
Unproven:
  - <piece>: <why I planned it>
    A) Keep as planned: <cost in code and upkeep>
    B) <simpler option>: <what it gives up>
    Do you accept the original, or B?
Belongs elsewhere:
  - <piece>: <owner>. Keep it in code, or hand it off?

Does the simpler plan make sense to you?
```

Leave out empty groups. When `under-engineering` calls this skill, put this block into its checkpoint message instead of sending it on its own.

Done when the human has answered every unproven and belongs-elsewhere item.
