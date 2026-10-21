---
name: under-engineering
description: Minimum-code checkpoint to run before implementing. Use before writing or changing code for a feature, fix, module or refactor; when adding functions, files or folders; or when a change touches auth, compliance, regulation or access policy.
---

# Under-engineering

To review existing code without changing it, use `under-engineering-review` instead.

The goal is the **least code that works**, written so a developer can read it with **nothing in memory**. They should never need to remember which file they came from, or how a function gets called when the editor can't show it. Every step below protects one of those two goals.

## Ownership

Who owns the code decides whether you fix a violation or ask first:

- **Owned code** is code you wrote in this session. Fix violations in it right away, without asking.
- **Existing code** is everything else, including existing functions you edit. Report the violation and ask before you fix it.

## Step 1: Size the task

A **small task** is one local edit (a rename, typo, added field, changed constant or one-line fix) that adds no new function, file or call path. For a small task, go straight to Step 5. Otherwise continue in order.

Done when you have decided whether the task is small.

## Step 2: Find the minimum

Ask: *what is the minimum requirement to get this to work?* Write the answer in one or two sentences, then plan the smallest change that meets it. Prefer editing existing code to adding new code, a function to a class, and a direct call to a new abstraction.

Then run the `um-maybe` skill on the plan, up to the message in its Step 4. Hold that message for the checkpoint.

Done when every planned piece maps to the requirement, the pieces that don't are cut, and the `um-maybe` message is ready.

## Step 3: Checkpoint

Run the three checks below. Send **one message** with the `um-maybe` block first, then every hit, and wait for the developer.

- **Depth.** Use the `call-depth` skill to trace the chain from the root to your planned next step. It hits when the step's weighted depth is over 3; calls that go-to-definition can't follow count double. Report the full chain from `call-depth`, then 2–3 alternatives to the planned step, each with its trade-off. Examples: call from a shallower function, inline into the caller, or reshape the entrypoint. End with your recommendation.
- **Module.** Ask whether other features will want this, and whether they could use it with one import and minimal boilerplate. It hits unless the answer is a clear no. Name the features likely to reuse it, and ask whether to build it as a module.
- **Governance.** It hits when the change enforces policy rather than product behaviour. Examples: legal or regulatory compliance, data retention, audit trails, restricting access by network, IP or region, and policy-level rate limits. Write governance code only with the developer's explicit approval. Offer an infrastructure option next to the code option. Examples: firewall, WAF, API gateway, IAM, storage lifecycle rules or database policies. Authentication belongs in code; an allow-list of login IPs belongs in the firewall.

Use this message format:

```
Checkpoint before implementing <task>
Minimum: <one sentence>

<um-maybe block>

[Depth] <chain from call-depth>
  A) <alternative>: <trade-off>
  B) <alternative>: <trade-off>
  Recommend: <letter, why>
[Module] <what could be reused, by which features>. Build it as a module?
[Governance] <what policy>. Code option: <...>. Infrastructure option: <...>. Which do you want?
```

If a hit appears during implementation (for example, the chain grows deeper than planned), stop and send a checkpoint for that hit.

Done when the developer has answered the `um-maybe` questions and every hit.

## Step 4: Module plan

When the developer confirms a module, read [`references/module-plan.md`](references/module-plan.md) and follow it. Write no implementation code until it is complete.

## Step 5: Limits while writing

Apply every limit to each function, file and folder as you write it. After finishing each function, measure with `call-depth`'s `scan.py` rather than by reading; it covers length, complexity and memory hops in any language, installs its own tools, and leaves the project's environment alone. Exceeding a limit needs a reason you state in the final report.

- **Screen rule.** A function fits on one screen: aim for at most 80 lines. Go past 80 only with a stated reason, and only if its complexity stays under the threshold. Never let a function reach hundreds of lines. **One function does one thing.** An **entrypoint** is the function the developer knows to call. It may orchestrate: a sequence of well-named calls plus simple gates (guard clauses, plain `if`s). The developer should understand what it does, and when, from the names it calls. The real work lives in the functions it calls.
- **Complexity.** Measure each function's cyclomatic complexity with `call-depth`. If it is over the threshold, inspect its nesting and flatten it: early returns, or a named function per branch.
- **File length.** Keep files under 900–1000 lines. Before a file gets near that, split it by responsibility or extract a shared helper.
- **Folders.** Put at most 5–6 code files in one folder unless there is a stated reason. Prefer nested folders to long flat lists. Name each folder in 1–3 words after what it holds. Subfolders continue the parent's sentence: `payments/` → `payments/refunds/` → `payments/refunds/disputes/`.
- **Traceable calls.** Every call must resolve with the editor's go-to-definition. Make each call a direct call, a method on a public interface or abstract base class, or a `match`/`switch` on a typed value whose branches make direct calls. Hard guardrail: no string-to-function lookups (`getattr`, `eval`, reflection, handler dicts keyed by strings), and no methods shared between classes by naming convention alone. A reader should understand each function on its own, not only as part of a set.

Done when every function, file and folder you touched is within its limits or has a stated reason.

## Step 6: Report

In the final message, list:

- every limit you exceeded, with its reason
- every violation you found in existing code and left alone, for the developer to decide on
