# Distillation brief — consumer-stack coach playbooks

You are distilling podcast transcripts into a **coach playbook**: a knowledge file that lets an AI agent give product feedback the way this person actually thinks, so a founder running a slash command gets coached with their real frameworks — not generic startup advice.

## Input
Plain-text transcripts (auto-captions: no punctuation, no speaker labels, occasional mis-transcriptions — infer speakers from context). Each file is named `<youtube-video-id>.txt`.

## Output format
Write one markdown file per coach at the path you were given. Structure:

```markdown
# <Coach Name> — <one-line identity, e.g. "Co-founder & CEO, Instagram">

> Sources: <video-id> (<show name>), <video-id> (...), ...

## Worldview
3-6 bullet points: what they fundamentally believe about consumer products. Each bullet is a claim they actually made, not a paraphrase of common knowledge.

## Frameworks
Their named or nameable frameworks, each as `### <Framework name>` with a concrete explanation of how to apply it. Only frameworks genuinely present in the transcripts.

## Heuristics & rules of thumb
Bullet list of specific, actionable rules they use (metrics thresholds, tests, decision rules). The more concrete the better ("if X then Y", numbers, timeframes).

## Red flags they call out
What makes them say "this won't work" — patterns they explicitly criticize.

## Questions they ask founders
5-10 questions this person would ask when reviewing a product, in their style. Derive from how they actually interrogate problems in the transcripts.

## Voice
3-5 bullets on how they talk: tone, vocabulary, what they praise, how they deliver criticism. Include 3-6 SHORT verbatim quotes (each under 20 words, in quotes, tagged with [video-id]) that capture their voice.
```

## Rules
- **Distill, never reproduce.** No long verbatim passages. Max 8 short quotes per file, each under 20 words. Everything else in your own words.
- **Only what's in the transcripts.** No outside knowledge about the person beyond a one-line identity. If a transcript turns out to feature a different speaker than expected, say so in your final report and extract from who is actually speaking.
- **Concrete beats abstract.** Prefer "kill any feature under 60% D1 adoption" over "focus on retention".
- **Interviewer content is noise.** Extract only the coach's own thinking. For panel/firm episodes (a16z, YC), attribute to the firm's collective view and name speakers if identifiable.
- Aim for 150-300 lines per playbook. Dense, no filler.
