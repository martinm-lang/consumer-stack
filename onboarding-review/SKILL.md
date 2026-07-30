---
name: onboarding-review
version: 1.0.0
description: Activation & time-to-value audit — minutes-not-days bar, latent needs, accessibility. (consumer-stack)
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - WebFetch
  - AskUserQuestion
triggers:
  - onboarding review
  - activation
  - time to value
  - first session
---

## When to invoke this skill

Audit of the path from install/landing to first real value. Use when signups don't activate, the first session leaks users, or the founder can't say what their "aha moment" is.

## Persona rule

Coaches channel the **publicly stated principles** of real people, distilled into `knowledge/`. Apply their frameworks in their style, cite video IDs for quotes, never invent positions their playbook doesn't support.

## Preamble (run first)

```bash
_SKILL_SRC=$(readlink -f "$HOME/.claude/skills/onboarding-review/SKILL.md" 2>/dev/null || echo "")
STACK_DIR=$(cd "$(dirname "${_SKILL_SRC:-.}")/.." && pwd)
echo "STACK_DIR: $STACK_DIR"
```

## The bench
Also check `$STACK_DIR/knowledge/_synthesis.md` for pre-computed cross-coach consensus, live tensions and the metrics cheat-sheet — ground any numeric claim in it before stating a threshold, and reuse a named tension instead of re-deriving one.

Read from `$STACK_DIR/knowledge/`: `nikita-bier.md` (seconds-to-aha, taps-to-value), `david-lieb.md` (latent needs, what users actually do), `melanie-perkins.md` (accessibility, first-experience empathy), `kevin-systrom.md` (simplicity, do-one-thing-well), `luis-von-ahn.md` (frustration budget).

## Step 1 — Walk the actual onboarding

Do not review from description alone:
- Repo available → read the onboarding flow code: every screen, permission prompt, form field and network call between first open and first value. Count the taps.
- Landing page / TestFlight / store URL → fetch and walk it as a first-time visitor.
- Ask the founder: what is the aha moment, in one sentence? How many seconds/taps from open to that moment today? What % of installs reach it? (Unknown = finding.)

## Step 2 — Diagnostic passes

1. **Bier's stopwatch**: time-to-value in seconds and taps. Everything before the magic moment is a candidate for deletion — list each pre-value step with its justification, and mark the ones that have none. Permissions before value = named violation.
2. **Lieb's latent-need check**: does the first session deliver the value users actually come for, or the value the founder wishes they came for? What would the top-100-users interviews say?
3. **Systrom's knife**: which onboarding steps exist because the product does too many things? What would this flow look like if the product did one thing well?
4. **Perkins' empathy pass**: would a non-technical first-timer get through this? Where does jargon, choice overload or setup friction exclude the mainstream user?
5. **von Ahn's frustration budget**: the competition is one click away — where does this flow spend frustration it can't afford? Is anything hard that could be deferred until after the habit exists?

## Step 3 — Verdict

Per-coach scored verdicts, then:
- **The rebuilt flow** — the onboarding as the bench would ship it: numbered steps, nothing before value that doesn't earn its place.
- **Cut list** — every step to delete or defer, with the coach who demands it.
- **The activation metric to instrument this week** — definition, target, measurement method.

## Step 4 — Follow-up

Offer `/retention-review` (value delivered but users don't return) or `/product-review` (the value itself is the problem).
