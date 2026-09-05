# Rules for `playbook/`

`playbook/` is the **case-study layer**: reconstructed growth machines of consumer companies,
built from web research plus primary interview transcripts.

It is governed by different rules than `knowledge/`, and the two must not be mixed.

| | `knowledge/` (coach layer) | `playbook/` (case layer) |
|---|---|---|
| Unit | a **person** | a **company** |
| Answers | how they think | what they did |
| Sources | sourced podcast transcripts only | transcripts **+** reporting, blogs, posts, archives |
| Outside knowledge | forbidden | required, if cited |
| Consumed by | `/coach`, `/panel`, review skills | `/growth-review`, future `/saturation` skill |

`CLAUDE.md`'s "only what the coaches actually said in the sourced episodes" rule applies to
`knowledge/` and is **not** relaxed by anything here. Never move web-researched material into a
coach playbook.

## Evidence labels — mandatory, never blended

Every factual claim carries one of these. A paragraph mixing two labels is a bug.

- **[Confirmed]** — independently reported by a credible outlet, or corroborated by two
  independent sources. Cite both.
- **[Founder-reported]** / **[Company-reported]** — the number or claim originates with the
  company and has not been independently verified. Applies even when a journalist repeats it:
  what matters is where it came from, not who printed it.
- **[Interpretation]** — our explanation of *why* a tactic worked. Never stated as fact.
- **[Transferable]** — the general principle extracted from the case.
- **[Zimo hypothesis]** — a proposed experiment. Never a finding.

Additional rules:

- **Never invent a number.** If a figure can't be sourced, write "not sourced" and add it to
  `RESEARCH_GAPS.md`.
- **Trace anecdotes to origin.** A story repeated across twenty growth blogs counts as one
  source until the earliest credible telling is found. Widely-repeated startup lore that
  bottoms out in a blog citing another blog gets labeled **[Unverified lore]**.
- **Show disagreements.** When sources conflict, state both, say which is stronger and why.
  Do not resolve a conflict silently.
- **Quotes:** max 8 per case file, each under 20 words, tagged with the source ID.
- **Every case file ends with a Sources section.** Transcript-derived claims cite the
  YouTube ID; web claims cite the URL.

## The durability interrogation — mandatory for every case

This playbook must not become fifty stories in which a founder retrospectively explains why they
are a genius. **Explosive growth is the beginning of the question, not the answer.** Every case file
must answer these, or say explicitly that the evidence doesn't exist:

1. **How long did the growth stay durable?** Not peak — duration.
2. **What was retention at 3 months and beyond?**
3. **Did the loop still work once incentives were removed?** (If there were never incentives, say so
   — that is a strong finding.)
4. **If it was acquired and shut down, why did the acquirer close it?** Performance, overlap,
   monetizability, or competitive threat.
5. **Was the market monetizable?** Zenly's 40M users were closed partly because its best markets
   weren't.
6. **Was there still organic growth at the end?** Zenly was growing faster than ever when Snap
   killed it. tbh and Gas were not.

A case that cannot answer #1 and #2 is a launch anecdote, not a case study. Label it as such.

## Source hierarchy

1. Founder/operator interviews, talks, blog posts, company materials, direct employee accounts
2. TechCrunch, The Information, Forbes, Bloomberg, WSJ, NYT, Business Insider, Wired,
   Fast Company, reputable university newspapers, reputable VC case studies
3. Newsletters, independent blogs, Reddit, community discussion

Never use a tier-3 summary where a tier-1 source exists. For campus-era stories, **university
newspapers are tier 2 and are often the only contemporaneous record** — they carry the
launch-day detail national outlets skipped, and the student critics national outlets never quote.

## File layout

- `cases/<company>.md` — one growth machine per file, following `TEMPLATE_CASE.md`
- `PREDECESSORS.md` — **direct predecessors & failed-to-expand analogues.** Companies that spent
  years on the same problem and plateaued rather than collapsed. A distinct category from a failure
  case: a failure case teaches how growth dies, a predecessor shows where the category's ceiling is.
  Every product in this playbook should have its predecessor named.
- `LAWS.md` — cross-company principles, each with evidence, counterexample, mechanism, failure mode
- `LOOPS.md` — the viral loop library
- `SATURATION.md` — the saturation model and its state ladder
- `MATRICES.md` — cross-company comparison tables, incl. the founder mental-model matrix
- `ZIMO.md` — the translation layer: prioritized experiments, each with a historical analogue
- `SOURCES.md` — the full source library
- `RESEARCH_GAPS.md` — open questions, weak claims, people worth reaching

There is deliberately **no `founders/` directory**. Founder-level thinking belongs in `knowledge/`
(the coach layer); the founder mental-model matrix in `MATRICES.md` covers the cross-case comparison
without duplicating it. Add one only if a founder needs a profile that `knowledge/` cannot hold
because it depends on outside-sourced biography.
