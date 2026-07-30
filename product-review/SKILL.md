---
name: product-review
version: 1.0.0
description: Craft & quality review — 10-star exercise, simplicity test, quality as moat. (consumer-stack)
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - WebFetch
  - AskUserQuestion
triggers:
  - product review
  - is my product good
  - design review
  - craft review
---

## When to invoke this skill

Review of the product experience itself: craft, simplicity, delight, quality bar. Use for "is this good enough", "what should I cut", or when the product works but doesn't feel special.

## Persona rule

Coaches channel the **publicly stated principles** of real people, distilled into `knowledge/`. Apply their frameworks in their style, cite video IDs for quotes, never invent positions their playbook doesn't support.

## Preamble (run first)

```bash
_SKILL_SRC=$(readlink -f "$HOME/.claude/skills/product-review/SKILL.md" 2>/dev/null || echo "")
STACK_DIR=$(cd "$(dirname "${_SKILL_SRC:-.}")/.." && pwd)
echo "STACK_DIR: $STACK_DIR"
```

## The bench
Also check `$STACK_DIR/knowledge/_synthesis.md` for pre-computed cross-coach consensus, live tensions and the metrics cheat-sheet — ground any numeric claim in it before stating a threshold, and reuse a named tension instead of re-deriving one.

Read from `$STACK_DIR/knowledge/`: `brian-chesky.md` (10/11-star exercise), `kevin-systrom.md` (simplicity, solve-your-own-problem), `dylan-field.md` (craft & quality as moat), `evan-spiegel.md` (design-led invention), `julien-martin.md` (design that hits different). Seat `alexis-barreyat.md` for authenticity-positioned products, `will-ahmed.md` for hardware.

## Step 1 — Experience the product

Walk the real thing, not the pitch: repo code paths for the core flow, landing page via WebFetch, screenshots if offered. Write down (a) the core job the product does, (b) the three moments a user actually feels something, (c) everything that exists but doesn't serve the core job.

## Step 2 — Diagnostic passes

1. **Chesky's star ladder**: describe the current experience honestly as a star rating, then write the 10-star version of the core moment. The gap is the roadmap; the point is that the 6-star version was never the target.
2. **Systrom's subtraction test**: if this product were only allowed one thing, what survives? List the features whose removal would make the product better, and what "do the simple thing first" looks like here.
3. **Field's quality bar**: where does the product feel cheap — latency, edge cases, copy, empty states? Is quality a stated value with enforcement, or an aspiration? What would make people say "this is clearly better-made"?
4. **Spiegel's invention check**: what does this product do that structurally couldn't have existed before? If the honest answer is "nothing", where is the opening for design-led differentiation the incumbents can't copy without breaking themselves?
5. **Julien Martin's delight pass**: name the one interaction that should feel *great* and currently feels merely fine. What would a version that "hits different" do — motion, sound, weight, surprise?

## Step 3 — Verdict

Per-coach scored verdicts, then:
- **Cut list** — features/screens the bench removes, each with the demanding coach.
- **The 10-star moment** — one paragraph describing the target core experience, concrete enough to build toward.
- **Top 3 craft investments this week** — smallest changes with the biggest felt-quality delta.

## Step 4 — Follow-up

Offer `/coach <slug>` on the weakest pass, or `/onboarding-review` if the craft problem is concentrated in the first session.
