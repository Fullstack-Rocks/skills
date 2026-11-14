# Repo rules

## Skills stay generic

Every skill under `skills/` must work for any project, so everything in it is generic: `SKILL.md`, references, agent prompts, scripts, comments, tests and fixtures.

- Write examples with invented, neutral names and data. The repo's demo shop (orders, refunds, carts, invoices) is the default domain.
- Name tools, languages, libraries and agent CLIs only where the skill works with them (Redis, ESLint, ast-grep, Codex), and describe models by tier ("the smallest model") rather than by product name.
- Never commit brand names, the names of real projects, products, companies or people, or anything taken from a real project: its examples, data, labels, screens, rules, dates or history. This holds even when a skill was first built inside that project.
- The one brand allowed is this repo's own: fullstack.rocks (Fullstack Rocks), in its install command, package metadata and the logo and name in a skill's own UI, such as the big-picture viewer.

Before every commit that touches `skills/`, re-read the changed lines for these and rewrite any you find in generic terms.
