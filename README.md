# Under-engineering skills

Agent skills that keep implementations to the least code that works.

- **[under-engineering](skills/under-engineering/SKILL.md)**: a minimum-code checkpoint to run before implementing. It sizes the task, finds the minimum requirement, checks call depth, module reuse and governance, and sets limits on function, file and folder size while writing.
- **[um-maybe](skills/um-maybe/SKILL.md)**: a hallway check on a plan. A weaker colleague agent with no context questions each piece and offers simpler options; whatever can't be proven goes to the human.

`under-engineering` calls `um-maybe` during its checkpoint. It also refers to a `call-depth` skill for measuring call-chain depth and complexity, and to `under-engineering-review` for reviewing existing code; neither is in this repository.

## Install

```bash
npx skills add theclocker/under-engineering-skills
```

Or copy a folder from `skills/` into your agent's skills directory, such as `~/.claude/skills/`.
