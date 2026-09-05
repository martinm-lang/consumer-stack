# consumer-stack

This repo is a skill pack for Claude Code: consumer product coaching distilled from podcast interviews with top consumer founders.

## Layout

- `<skill>/SKILL.md` — one directory per slash command (panel, coach, retention-review, growth-review, onboarding-review, product-review, pitch, wedge, consumer-stack router)
- `knowledge/*.md` — one playbook per coach: worldview, frameworks, heuristics, red flags, questions, voice. **This is the product.** Skills read these at runtime.
- `knowledge/_synthesis.md` — pre-computed cross-coach consensus/tensions/metrics/gaps (underscore prefix excludes it from the coach-listing `ls` in skill preambles). Regenerate when playbooks are added or materially edited — read it in full, don't hand-patch it, since consensus/tension counts must stay accurate to what's actually in `knowledge/*.md`.
- `playbook/` — **the case layer**: reconstructed growth machines, one file per *company*. Governed by `playbook/RULES.md`, NOT by the `knowledge/` sourcing rule below — it uses web research and requires evidence labels ([Confirmed] / [Founder-reported] / [Interpretation] / [Transferable] / [Zimo hypothesis]). Never move web-researched material into `knowledge/`, and never mix the two layers in one file.
- `ingest/` — reproducible pipeline (episode IDs, yt-dlp caption download, VTT→txt cleaning, distillation brief). Raw transcripts are gitignored, never committed.
- `setup` — symlinks each skill into `~/.claude/skills/`.

## Rules

- `knowledge/` playbooks contain only what the coaches actually said in the sourced episodes. No outside biography, no invented positions. Max 8 short quotes (<20 words) per playbook, always tagged with the source video ID.
- Coaches are framed as "channels the publicly stated principles of X", never as X speaking.
- A skill must Read the relevant `knowledge/*.md` files before giving any coach feedback — never improvise a coach from general knowledge.
- Keep skill routing consistent with the table in README.md when adding skills.
- `playbook/` claims must carry an evidence label and end in a Sources section. Never invent a number; unsourced figures go to `playbook/RESEARCH_GAPS.md`. When sources disagree, show the disagreement and say which is stronger.

## Skill routing

When the user's request matches a skill, invoke it via the Skill tool:
- Full product feedback / "review my app" → /panel
- One specific coach ("what would Chesky say") → /coach
- Idea stage, no product yet → /wedge
- Activation / onboarding / time-to-value → /onboarding-review
- Retention / habit / engagement → /retention-review
- Growth / virality / distribution → /growth-review
- Design / craft / quality → /product-review
- Fundraising / investor prep → /pitch
