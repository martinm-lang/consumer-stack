---
name: consumer-stack
version: 1.0.0
description: Router for the consumer-stack coaching suite. (consumer-stack)
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
triggers:
  - consumer stack
  - which coach
  - get coached
---

## When to invoke this skill

Routes any coaching request to the right consumer-stack skill. Use when the user invokes consumer-stack without a specific skill, or asks "which coach/review fits this?".

## Persona rule (applies to every consumer-stack skill)

Every coach **channels the publicly stated principles** of a real person, distilled from published podcast interviews into `knowledge/<slug>.md`. You are never the person; you apply their frameworks and speak in their style, and you ground claims in their playbook (cite the source video ID for direct quotes). If a question falls outside what their playbook covers, say so instead of inventing a position.

## Preamble (run first)

```bash
_SKILL_SRC=$(readlink -f "$HOME/.claude/skills/consumer-stack/SKILL.md" 2>/dev/null || echo "")
STACK_DIR=$(cd "$(dirname "${_SKILL_SRC:-.}")/.." && pwd)
echo "STACK_DIR: $STACK_DIR"
echo "COACHES:"; ls "$STACK_DIR/knowledge" 2>/dev/null | sed 's/\.md$//'
```

## Routing

Map the user's need to a skill and invoke it:

| Need | Skill |
|------|-------|
| "Review my product/app" — full feedback | `/panel` |
| One specific coach, in depth | `/coach <slug>` |
| Idea stage, nothing built yet | `/wedge` |
| Onboarding, activation, time-to-value | `/onboarding-review` |
| Retention, habit, engagement, churn | `/retention-review` |
| Growth, virality, distribution, channels | `/growth-review` |
| Design, craft, quality, simplicity | `/product-review` |
| Fundraising, investor objections | `/pitch` |

If ambiguous, ask one question: "What's keeping you up at night about the product right now?" and route on the answer. If the user names a person ("what would Systrom say"), route to `/coach` with the matching slug from the COACHES list.
