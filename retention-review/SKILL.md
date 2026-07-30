---
name: retention-review
version: 1.0.0
description: Habit & retention review — Hooked model, streak mechanics, freemium logic. (consumer-stack)
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - WebFetch
  - AskUserQuestion
triggers:
  - retention review
  - why is my retention bad
  - churn
  - habit loop
---

## When to invoke this skill

Focused review of retention, habit formation and engagement. Use when D7/D30 scares the founder, churn is the topic, or the question is "how do I make this a habit?".

## Persona rule

Coaches channel the **publicly stated principles** of real people, distilled into `knowledge/`. Apply their frameworks in their style, cite video IDs for quotes, never invent positions their playbook doesn't support.

## Preamble (run first)

```bash
_SKILL_SRC=$(readlink -f "$HOME/.claude/skills/retention-review/SKILL.md" 2>/dev/null || echo "")
STACK_DIR=$(cd "$(dirname "${_SKILL_SRC:-.}")/.." && pwd)
echo "STACK_DIR: $STACK_DIR"
```

## The bench
Also check `$STACK_DIR/knowledge/_synthesis.md` for pre-computed cross-coach consensus, live tensions and the metrics cheat-sheet — ground any numeric claim in it before stating a threshold, and reuse a named tension instead of re-deriving one.

Read from `$STACK_DIR/knowledge/`: `nir-eyal.md` (habit loops), `luis-von-ahn.md` (streaks, notification discipline), `daniel-ek.md` (freemium, dependability), `nikita-bier.md` (kill criteria, real engagement signals), `david-lieb.md` (cohort truth, frequency × value). Seat `antoine-martin.md` too if the product is social.

## Step 1 — Get the real numbers

Ask for: D1/D7/D30 by cohort (or whatever exists), session frequency, the action they count as "active", notification strategy, and what the user does in their very first session. "We don't track that" is a finding — log it. If there's a repo, read the analytics/notification code to see what's actually instrumented versus claimed.

## Step 2 — Diagnostic passes (run all, in order)

1. **Lieb's scoreboard first**: do cohort curves go flat, and at what level? Frequency × value quadrant — which one is this product honestly in? If curves don't flatten, everything else is decoration.
2. **Eyal's Hooked audit**: walk trigger → action → variable reward → investment for the core loop. Name which leg is missing or weakest, and whether the product even belongs in the habit zone (frequency + perceived utility) or should stop pretending to be a habit product.
3. **von Ahn's mechanics check**: what does the product do at exactly last-use + 24h? Is there a streak-equivalent, a loss-aversion mechanic, a hard stop after prolonged inactivity? Score the notification discipline against his rules.
4. **Ek's dependability lens**: is the product dependable enough that users return without being summoned? Where does it sit on discovery vs. dependability for its cost-of-trial?
5. **Bier's reality check**: is the engagement real (hourly actives, organic depth) or DAU cosmetics? Apply his binary test: if it's ambiguous whether retention is working, it isn't.

## Step 3 — Verdict

Per-coach scored verdicts (same format as `/panel` Step 3), then:
- **The one number that matters next** — which metric, measured how, target threshold, from whose heuristic.
- **Top 3 retention experiments this week** — each with mechanic, expected effect, and the coach whose playbook it comes from.
- **The uncomfortable option** — if the diagnostics say the core loop doesn't support a habit product, say so plainly (Lieb's Bump lesson) and name the pivot conversation to have (`/wedge`).

## Step 4 — Follow-up

Offer `/coach <slug>` for depth on the weakest diagnostic, or `/growth-review` if the real problem turned out to be top-of-funnel.
