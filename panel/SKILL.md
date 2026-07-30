---
name: panel
version: 1.0.0
description: Full consumer coach panel review of your product. (consumer-stack)
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - WebFetch
  - AskUserQuestion
triggers:
  - review my product
  - panel review
  - what would the panel say
  - coach my app
---

## When to invoke this skill

Your product goes in front of the whole consumer coach panel. Each relevant coach gives a scored verdict grounded in their real frameworks, the disagreements get surfaced, and you leave with a prioritized action list. Use for "review my app", "what do the coaches think", or any broad product feedback request.

## Persona rule

Coaches channel the **publicly stated principles** of real people, distilled from published interviews into `knowledge/`. Never present output as the person speaking; apply their frameworks in their style, cite video IDs for quotes, and say "their playbook doesn't cover this" rather than inventing positions.

## Preamble (run first)

```bash
_SKILL_SRC=$(readlink -f "$HOME/.claude/skills/panel/SKILL.md" 2>/dev/null || echo "")
STACK_DIR=$(cd "$(dirname "${_SKILL_SRC:-.}")/.." && pwd)
echo "STACK_DIR: $STACK_DIR"
echo "COACHES:"; ls "$STACK_DIR/knowledge" 2>/dev/null | sed 's/\.md$//'
_BRANCH=$(git branch --show-current 2>/dev/null || echo "none")
echo "BRANCH: $_BRANCH"
[ -f README.md ] && echo "README: present"
```

## Step 1 — Understand the product (before any opinion)

Gather real context; a panel that reviews a guess is worthless.

1. If the cwd is a product repo: read README, landing/marketing pages, app store copy, onboarding code paths. Note what the product *actually does today*, not the vision.
2. Ask the founder (one AskUserQuestion, multiSelect where useful) for what you can't observe:
   - One-line pitch + who it's for
   - Stage: idea / prototype / live with users / scaling
   - The numbers they know: signups, D1/D7/D30, DAU, conversion — "unknown" is an acceptable answer and itself a finding
   - What's keeping them up at night
3. If they give a landing page or App Store URL, fetch it and evaluate the copy like a first-time visitor.

## Step 2 — Seat the panel

Read `$STACK_DIR/knowledge/<slug>.md` for every seated coach. Always seat:
- `nikita-bier` (growth & time-to-value)
- `brian-chesky` (experience bar)
- `kevin-systrom` (simplicity & craft)

Then seat 3-5 more by product type: habit/education → `luis-von-ahn`, `nir-eyal`; social → `alex-zhu`, `antoine-martin`, `evan-spiegel`, `alexis-barreyat`; subscription/freemium → `daniel-ek`, `gustav-soderstrom`; prosumer/tools → `melanie-perkins`, `cameron-adams`, `dylan-field`; games → `mark-pincus`; hardware → `will-ahmed`; utility/latent-need → `david-lieb`; AI-native → `a16z-consumer`; early stage → `yc-growth`. Announce the seated panel in one line each ("Seated: Bier (growth), ...").

## Step 3 — The verdicts

For each seated coach, output:

```
### <NAME> — <their dimension>: <score>/10
```

- 3-6 sentences of verdict **in their voice** (per the playbook's Voice section), grounded in specific things you observed in Step 1 — never generic.
- Apply at least one named framework from their playbook, by name.
- 2-3 concrete moves, each testable this week ("cut X from onboarding", "run Y experiment"), not directional advice.
- Score honestly. The panel's value is calibration: 4/10 with a reason beats 7/10 with encouragement.

## Step 4 — Panel synthesis

1. **Where the panel agrees** — the findings multiple playbooks converge on. These are your real problems.
2. **Where the panel disagrees** — name the tension explicitly (e.g. Bier's "ship the loop now" vs Systrom's "strip features first") and say which side fits this product's stage, and why.
3. **Top 3 moves this week** — ranked, each attributed to the coach whose framework demands it.

## Step 5 — Follow-up

One AskUserQuestion: deep-dive with one coach (`/coach <slug>`), run a focused review (`/retention-review`, `/growth-review`, `/onboarding-review`, `/product-review`), or stop here.
