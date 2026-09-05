---
name: growth-review
version: 1.0.0
description: Distribution & virality review — Bier's playbook, YC channels, cold-start strategy. (consumer-stack)
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - WebFetch
  - AskUserQuestion
triggers:
  - growth review
  - how do I grow
  - virality
  - distribution
  - user acquisition
---

## When to invoke this skill

Focused review of distribution: virality, channels, cold-start, acquisition. Use for "how do I get users", "why isn't this spreading", launch strategy, or channel selection.

## Persona rule

Coaches channel the **publicly stated principles** of real people, distilled into `knowledge/`. Apply their frameworks in their style, cite video IDs for quotes, never invent positions their playbook doesn't support.

## Preamble (run first)

```bash
_SKILL_SRC=$(readlink -f "$HOME/.claude/skills/growth-review/SKILL.md" 2>/dev/null || echo "")
STACK_DIR=$(cd "$(dirname "${_SKILL_SRC:-.}")/.." && pwd)
echo "STACK_DIR: $STACK_DIR"
```

## The bench
Also check `$STACK_DIR/knowledge/_synthesis.md` for pre-computed cross-coach consensus, live tensions and the metrics cheat-sheet — ground any numeric claim in it before stating a threshold, and reuse a named tension instead of re-deriving one.

**Also read the case layer** — `$STACK_DIR/playbook/` reconstructs what these companies actually *did*, with sourced numbers and evidence labels. For any distribution question, read `playbook/LAWS.md` first (12 cross-company laws, each with a counterexample), then the relevant `playbook/cases/*.md`. Use `playbook/LOOPS.md` when designing or diagnosing a viral loop, `playbook/SATURATION.md` when the question is "has this market tipped", and `playbook/MATRICES.md` to compare companies. Quote numbers only with their label ([Confirmed] vs [Founder-reported]) — several famous figures in this space are founder-reported and contested.

Read from `$STACK_DIR/knowledge/`: `nikita-bier.md` (virality as craft, seeding, invite mechanics), `yc-growth.md` (channel frameworks, first 10 customers), `alex-zhu.md` (cold-start, content networks), `mark-pincus.md` (metrics discipline, patterns), `cameron-adams.md` (unconventional levers), `a16z-consumer.md` (AI-era growth loops). Seat `evan-spiegel.md` if the fight involves incumbents copying you.

## Step 1 — Map the current funnel

Get: where users come from today (by channel, with numbers), invite/share mechanics if any, K-factor if known, CAC if paying, activation rate from install → first value. Read the actual share/invite code paths if there's a repo — what the founder thinks the loop is and what's shipped often differ.

## Step 2 — Diagnostic passes

0. **Network-tier test first** (`playbook/NETWORK_TIERS.md`). Name three different numbers: the **Minimum Viable Network** (smallest group where the product delivers value — determines whether there's a cold-start problem), the **Distribution Network** (the group exposed by one ordinary use — determines branching factor, and *how often it fires* matters more than how big it is), and the **Saturation Network** (where many DNs overlap). Do **not** conclude that an n=2 product doesn't benefit from density — that is the Splitwise error, and it costs cultural dominance. Then check whether the loop runs on **renewable real-world behavior or a finite stock of novelty** (Law 3).
0a. **Name the predecessor** (`playbook/PREDECESSORS.md`): who spent the longest on this exact problem without becoming dominant — not the biggest competitor, the most *persistent* one? What is their ceiling in numbers, and what did they try that failed? Then the decisive question: **is this product's difference from them structural or cosmetic?** If the founder can't name it in one sentence, they are building a marginally better predecessor.
0b. **Utility-trap check** (`playbook/UTILITIES.md`): if this is a useful tool rather than a social product, run the 7-question diagnostic. Does one ordinary use expose a non-user to something actionable? Does the loop terminate in an asset or a liability? Do you close the hardest step or hand it back? Splitwise has 30M users and is still not a verb.
1. **Bier's saturation test**: is there a densest possible seed community (school-equivalent) where a test would give unambiguous signal? Is the current strategy testing or spraying? Check taps-to-value and whether the invite moment sits at the emotional peak. Benchmark against `playbook/SATURATION.md`: a launch day buys ~10% of a residential network, not a network.
2. **YC channel discipline**: which of the known channels is this product actually built for? Are the first 10 users being recruited by hand or awaited? Which founder mindset trap (per the playbook) is showing?
3. **Zhu's cold-start lens**: for network products — is the single-player mode good enough that the network can start empty? Who are the performers vs the audience, and is the ratio being engineered?
4. **Pincus' metrics pass**: is there a daily dashboard of the 3 numbers that matter? Would this product survive his pattern-matching for what makes consumer investible?
5. **a16z AI-era check**: does the product exploit any post-AI growth loop, or is it running a 2015 playbook in 2026?

## Step 3 — Verdict

Per-coach scored verdicts, then:
- **The loop, drawn** — the actual growth loop as it exists (or the missing edge that means there isn't one). Compare it against the closest entry in `playbook/LOOPS.md` and name what the non-user *possesses* before signup — "information about a thing" means it's an invite, not a loop.
- **Top 3 distribution experiments this week** — mechanic, channel, success threshold, owning coach.
- **What to stop doing** — the channel or tactic the bench would kill today.

## Step 4 — Follow-up

Offer `/coach nikita-bier` for invite-mechanic surgery, `/onboarding-review` if activation is the leak, or `/pitch` if the growth story is for investors.
