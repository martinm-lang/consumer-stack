# consumer-stack

**Get coached like the best consumer founders coach.** consumer-stack turns Claude Code into a panel of consumer product coaches — each one distilled from hours of podcast interviews with the founders and operators who built Instagram, Snap, Airbnb, Spotify, Canva, Duolingo, Zynga, Musical.ly, Zenly, BeReal, Figma, WHOOP and Google Photos, plus the YC and a16z consumer playbooks.

Every coach is a knowledge file extracted from what these people actually said — their frameworks, their heuristics, their red flags, the questions they ask founders — not generic startup advice. The skills read your repo, your landing page, your metrics, and give you the feedback session you'd never get in real life.

Structure and mechanics are modeled on [garrytan/gstack](https://github.com/garrytan/gstack): every tool is a Markdown slash command, installed by symlink, updated by `git pull`.

> Each coach channels the **publicly stated principles** of a real person, distilled from published interviews. It is a study aid, not the person. Sources are cited per playbook in [`knowledge/`](knowledge/).

## Install — 30 seconds

**Requirements:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Git.

```bash
git clone git@github.com:martinm-lang/consumer-stack.git ~/.claude/skills/consumer-stack-repo
cd ~/.claude/skills/consumer-stack-repo && ./setup
```

Restart Claude Code. Type `/panel`.

## Quick start

1. `cd` into your product's repo (or have your landing page / App Store URL ready)
2. Run `/panel` — the whole panel reviews your product
3. Run `/coach nikita-bier` when you want one voice, in depth
4. Run `/retention-review` when your D7 scares you
5. Run `/pitch` before you talk to investors

## The panel

| Coach | Built | Sharpest on |
|-------|-------|-------------|
| Nikita Bier | tbh, Gas | Virality, teen distribution, time-to-value, kill criteria |
| Evan Spiegel | Snap | Product intuition, design-led invention, competing with giants |
| Kevin Systrom | Instagram | Simplicity, solving your own problem, craft, scaling |
| Brian Chesky | Airbnb | 10-star experiences, founder mode, AI-era product design |
| Melanie Perkins | Canva | Vision-led persistence, accessible design, pricing |
| Cameron Adams | Canva | Unconventional growth levers, product-led growth |
| Daniel Ek | Spotify | Freemium, platform bets, long-term thinking |
| Gustav Söderström | Spotify | Product strategy, ML products, bets & tradeoffs |
| Luis von Ahn | Duolingo | Gamification, streaks, A/B culture, retention mechanics |
| Mark Pincus | Zynga | Metrics-driven games, consumer investability, patterns |
| David Lieb | Bump, Google Photos | Pivots, toothbrush test, latent needs |
| Alex Zhu | Musical.ly | Cold-start, content networks, community seeding |
| Dylan Field | Figma | Craft & quality as moat, design tools |
| Will Ahmed | WHOOP | Hardware + subscription, perseverance |
| Julien Martin | Amo | Design that hits different, consumer delight |
| Antoine Martin | Zenly | Social maps, retention through emotion |
| Alexis Barreyat | BeReal | Authenticity, anti-social-media positioning |
| Nir Eyal | Hooked | Habit loops, behavioral design, ethics tests |
| Peter Thiel | PayPal, Founders Fund | Monopoly vs competition, contrarian bets |
| Michael Skok | Harvard i-lab | Value propositions, 4U problem test, MVS |
| Y Combinator | — | First 10 customers, growth channels, founder mindsets |
| a16z consumer | — | Consumer AI landscape, new growth loops, moats |

Full source list per coach: [`knowledge/`](knowledge/). Episode index: [`ingest/meta/index.tsv`](ingest/meta/index.tsv). Source-quality caveats (e.g. `alexis-barreyat.md` is secondhand — Barreyat has never given a primary interview) are in [`ingest/README.md`](ingest/README.md).

**[`knowledge/_synthesis.md`](knowledge/_synthesis.md)** — a pre-computed cross-coach reference: 31 consensus positions, 10 named live tensions (e.g. "ship fast" vs "polish before launch", with which stage each side fits), a 117-row metrics cheat-sheet pulling every concrete number the coaches gave, 6 clusters of independently-invented equivalent frameworks, and an honest list of what the panel has no strong opinion on (hardware, B2B2C, localization, platform risk, downturns, paid acquisition, marketplace cold-start). `/panel` and the review skills read this before improvising a synthesis live.

## The skills

| Skill | Your session | What happens |
|-------|--------------|--------------|
| `/panel` | **Full panel review** | Your product goes in front of the whole panel. Each relevant coach gives a verdict, the disagreements get surfaced, you leave with a prioritized action list. |
| `/coach <name>` | **1:1 deep dive** | One coach, full attention. Their frameworks applied step by step to your product, in their voice. |
| `/wedge` | **Idea stage** | You have an idea, not a product. YC-style interrogation: who is it for, what's the wedge, how do you get the first 10 users. |
| `/onboarding-review` | **Activation** | Time-to-value audit. Bier's minutes-not-days bar, Lieb's toothbrush test, Perkins' accessibility lens. |
| `/retention-review` | **Habit & retention** | Eyal's Hooked model, von Ahn's streak mechanics, Ek's freemium logic applied to your retention curves. |
| `/growth-review` | **Distribution** | Bier's virality playbook, YC's channel frameworks, Zhu's cold-start strategies, Pincus' metrics discipline. |
| `/product-review` | **Craft & quality** | Chesky's 10-star exercise, Systrom's simplicity test, Field's quality-as-moat, Julien Martin's design bar. |
| `/pitch` | **Investor simulation** | Pitch the panel as investors. a16z and YC lenses, real objections, scored verdict. |

## How a session works

```
You:    /panel
Claude: [detects your product from the repo / asks for your landing page + metrics]
        [reads the relevant coach playbooks]

        NIKITA BIER — Growth: 4/10
        "Your onboarding asks for 6 permissions before showing any value.
        I'd cut everything before the magic moment..."

        BRIAN CHESKY — Experience: 6/10
        "What does the 10-star version of this look like? You've built
        the 5-star version..."

        WHERE THE PANEL DISAGREES: Bier says ship the viral loop now,
        Systrom says strip two features first...

        TOP 3 MOVES THIS WEEK: ...
```

## Regenerating / extending the knowledge base

The `ingest/` directory holds the pipeline: `video_ids.txt` (episode list), `yt-dlp` for captions, `vtt2txt.py` for cleaning. Raw transcripts are **not** committed — only the distilled playbooks in `knowledge/` are. To add a coach: add episode IDs, re-run the pipeline, distill a new playbook following `ingest/DISTILL_BRIEF.md`.

## License

MIT for the code and structure. Coach playbooks are distilled study notes from published interviews, with per-file source attribution; short quotes are used under fair-use-style citation. This repo is private and not intended for redistribution of the playbooks.
