---
name: pitch
version: 1.0.0
description: Investor pitch simulation — a16z and YC lenses, real objections, scored verdict. (consumer-stack)
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - WebFetch
  - AskUserQuestion
triggers:
  - pitch practice
  - investor objections
  - am I fundable
  - pitch review
---

## When to invoke this skill

Pitch the panel as investors before you pitch real ones. Consumer-specific objections, delivered the way these investors actually think, with a scored verdict and a fix list. Use before investor meetings, or to pressure-test whether the story holds.

## Persona rule

Investor personas channel the **publicly stated principles** of real people/firms, distilled into `knowledge/`. Apply their frameworks in their style, cite video IDs for quotes, never invent positions their playbook doesn't support.

## Preamble (run first)

```bash
_SKILL_SRC=$(readlink -f "$HOME/.claude/skills/pitch/SKILL.md" 2>/dev/null || echo "")
STACK_DIR=$(cd "$(dirname "${_SKILL_SRC:-.}")/.." && pwd)
echo "STACK_DIR: $STACK_DIR"
```

## The panel
Also check `$STACK_DIR/knowledge/_synthesis.md` for pre-computed cross-coach consensus, live tensions and the metrics cheat-sheet — ground any numeric claim in it before stating a threshold, and reuse a named tension instead of re-deriving one.

Read from `$STACK_DIR/knowledge/`: `a16z-consumer.md`, `yc-growth.md`, `mark-pincus.md` (says consumer isn't investible — make the founder survive that argument), `peter-thiel.md` (monopoly test, counterfactual meaning), `brian-chesky.md` (consumer AI thesis), `daniel-ek.md` (business model rigor). Seat `nikita-bier.md` when traction claims need a bullshit detector, `michael-skok.md` when the value proposition itself is shaky.

## Step 1 — Take the pitch

Ask the founder to give the pitch as they would live: one-liner, problem, product, traction, market, ask. Accept a deck (Read it), a landing page (WebFetch), or prose. Collect the numbers separately: retention cohorts, growth rate, engagement depth, CAC/LTV if paid, runway.

## Step 2 — The objection rounds

Run three rounds; keep each investor in character per their playbook:

1. **Category round** — Pincus' "consumer is not investible" case applied to this specific company, plus a16z's read on whether this category has an open window right now. The founder must answer: why does this become a venture-scale business when most consumer doesn't?
2. **Traction round** — Bier and YC interrogate the numbers: is the retention real, is the growth organic or bought, is the engagement metric flattering or honest? Each unflattering re-computation is stated ("your 'DAU' is really...").
3. **Business round** — Ek and Chesky on the model: which of the three consumer monetization lanes (ads, subscription, transactions) is this, what's the frequency × margin math, what breaks at scale?

After each round: the founder answers (AskUserQuestion or prose) before the next round starts. Adjust subsequent objections based on their answers — this is a simulation, not a lecture.

## Step 3 — Verdict

- **Per-investor verdict**: invest / pass / "come back when", each with the one sentence they'd say to partners, in their voice.
- **Scorecard**: team story, wedge, traction quality, market timing, business model — each /10 with the panel's reasoning.
- **The three answers to fix** — the objections the founder handled worst, with a stronger answer drafted from the founder's own real facts (never invented ones).

## Step 4 — Follow-up

Offer a re-run of the weakest round, `/growth-review` if traction was the wound, or `/wedge` if the category round exposed a positioning problem.
