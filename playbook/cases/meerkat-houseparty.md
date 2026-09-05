# Meerkat & Houseparty (Ben Rubin)

> **Era:** 2015–2019 | **Wedge:** live video on Twitter, then live presence with close friends | **Atomic network:** a Twitter follower graph (borrowed), then a friend group of ~6
> **Status:** **both gone.** Meerkat crippled by Twitter Mar 13 2015; Houseparty acquired by Epic Games 2019, shut down 2021.
> **Sources:** 2 founder talk transcripts (Ben Rubin), TechCrunch, VentureBeat, BuzzFeed News.

## TL;DR

**This is the platform-risk case, and it fills a gap the coach layer explicitly admits to.** `knowledge/_synthesis.md` names platform risk — "losing a distribution channel outright" — as a topic no coach in the panel addresses. Meerkat is the cleanest documented instance in consumer software.

Meerkat's viral growth was not built. It was **borrowed from Twitter's notification system**, which broadcast Meerkat activity to Twitter's user base for free. Rubin's account is unusually candid:

> "For the first month Twitter did the whole job for us in distributing Meerkat to their user base, because of the way their notification system worked." [iXQuzBgeGXI]

On **March 13, 2015 — the first day of SXSW, the same day Twitter announced it had bought Periscope — Twitter revoked Meerkat's access to its social graph.** New users could no longer be auto-connected to people they already followed. [Confirmed — VentureBeat, TechCrunch, BuzzFeed News] The growth engine was switched off by its owner, in public, at the moment of maximum attention.

Rubin pivoted to Houseparty, which worked far better and still ended. The two-company arc is the most complete "borrowed distribution → sudden death → rebuild on owned graph" sequence available.

## The machine (Meerkat)

> live video is too hard on existing tools (wedge) → **Twitter's follower graph, borrowed** (atomic network) → auto-connect new users to who they already follow (cold start) → **Twitter's own notifications and reactivation emails distribute you for free** (distribution) → tweet-a-stream (viral loop) → **platform revokes access** → collapse

## Timeline

| Date | Event |
|---|---|
| Pre-2015 | Rubin's team runs **Yevo/Air** — earlier live-video attempts. The signal: fans streaming Lady Gaga shows with the right hashtag got picked up on Twitter by superfans and went viral. [iXQuzBgeGXI] |
| ~Nov 2014 | Decision to pivot. |
| Jan 2015 | Raise $15M. |
| **Late Feb 2015** | **Meerkat launches** — "a live streaming button to Twitter." [iXQuzBgeGXI] |
| ~2 weeks pre-launch | The team notices Twitter pushing them notifications about each other's Meerkat activity. Rubin: *"Wait a second — Twitter has this whole viral mechanism… if Meerkat works, this is explosive."* |
| Feb–Mar 2015 | Explosive growth. Twitter's notification and reactivation emails do the distribution. |
| **Mar 13, 2015** | **Twitter announces the Periscope acquisition and revokes Meerkat's social-graph access on the same day** — day one of SXSW. [Confirmed] |
| Jul 2015 | Meerkat adds co-hosting and integrates with Facebook to rebuild social discovery. Activity has already stagnated. [Confirmed] |
| ~2016 | Pivot to **Houseparty** — private group video, ~10 months of development. |
| 2019 | Houseparty acquired by **Epic Games**. |
| 2021 | Houseparty shut down. |

## The borrowed-distribution mechanism, precisely

What Twitter was doing for Meerkat, for free:

1. **Graph import** — a new Meerkat user was auto-connected to the people they already followed on Twitter. **Night one was populated with no work.** This is the single hardest problem in social products, and Meerkat got it as an API call.
2. **Notification broadcast** — Twitter pushed notifications when people you followed started or favourited a Meerkat stream.
3. **Reactivation email** — Twitter's own lifecycle email included Meerkat activity.

**[Interpretation]** Meerkat did not have a growth team; it had *Twitter's* growth team, working for it unknowingly. The team's own realization — that Twitter's viral machinery would make Meerkat explosive *if the product worked* — is exactly right and exactly the trap. **A borrowed distribution channel is indistinguishable from product-market fit while it is switched on.**

**The asymmetry that killed it:** Meerkat's growth depended on a platform decision it had no contract over, no notice of, and no alternative to. When Twitter shipped a competitor, the same switch that created Meerkat's growth removed it, in one day.

## What Rubin learned, and Houseparty

The Houseparty thesis came from a specific observed failure of live video:

> "For a year we just focused on: the everyday person doesn't go live every day — and that's the problem with live video." [Yl1Q8LjF6nI]

**[Interpretation]** This is a sharp and generalizable diagnosis. Live broadcasting requires a **performance decision** — I am now going to be watched — and most people will not make that decision daily. Houseparty removed the performance: a video room with your close friends, join and leave freely, no audience, no broadcast, no start button in the psychological sense. It converted *broadcasting* (rare, effortful, high-status) into *presence* (ambient, effortless).

Houseparty also rebuilt on an **owned graph** — contacts and mutual friends, not a borrowed platform's follower list. It grew genuinely, spiked enormously during COVID lockdowns, was acquired by Epic in 2019, and was shut down in 2021.

**[Interpretation]** The Houseparty ending belongs with Zenly's: a product with real usage, closed by an acquirer for strategic reasons rather than performance. Two of the eight Tier A cases end this way. That is a base rate worth knowing.

Rubin's own framing across both talks is about luck and purpose — *"clear sense of purpose… that's the reason we've been able to be lucky"* [Yl1Q8LjF6nI] — which reads differently once you know the growth was Twitter's notification system and the ending was a platform's decision.

## Metrics

Deliberately thin. Meerkat's headline numbers were SXSW-era press figures that varied wildly and were never independently established; the meaningful, verifiable fact is the **date of the cutoff and its immediate effect on engagement.** Anything more precise is logged in `RESEARCH_GAPS.md` rather than guessed.

| Fact | Label |
|---|---|
| Twitter revoked social-graph access, Mar 13 2015, day one of SXSW, same day as the Periscope announcement | **[Confirmed]** — VentureBeat, TechCrunch, BuzzFeed News |
| Activity stagnated after the cutoff; sharp drop in engagement and daily streams | **[Confirmed]** |
| Added co-hosting + Facebook integration by Jul 2015 to rebuild discovery | **[Confirmed]** |
| Houseparty → Epic Games, 2019; shut down 2021 | **[Confirmed]** |

## Transferable principles

1. **[Transferable] A borrowed distribution channel is indistinguishable from product-market fit while it is switched on.** The only way to tell them apart is to ask who owns the switch.
2. **[Transferable] Audit your growth for platform dependency explicitly.** For each of graph import, notifications, discovery and reactivation, name the owner. Any of them owned by a company that could plausibly compete with you is a countdown, not a channel.
3. **[Transferable] The platform will ship your feature and cut you off on the same day.** Not sequentially, and not with notice — the cutoff *is* the announcement.
4. **[Transferable] Broadcasting requires a performance decision most people won't make daily. Presence doesn't.** If your product needs users to choose to be watched, expect low frequency regardless of execution.
5. **[Transferable] Rebuild on an owned graph after any borrowed-graph shock** — and accept that it will be slower, because you now have the cold-start problem you were previously exempt from.
6. **[Transferable] Two of eight Tier A cases were closed by acquirers while working.** An acquisition transfers control over whether your product continues to exist.

## Reproducibility in 2026

Sharper than in 2015, not softer. Contact-book access is restricted (Bier: iOS 18 selective contact permissions largely kill contact sync), platform APIs are more locked down, and every major platform now has a competing first-party product in most consumer categories. **[Interpretation]** The Meerkat trade — rent a graph to skip the cold start — is both more tempting (graphs are harder to build than ever) and more dangerous (platforms are quicker to close). Anything that depends on a third party's social graph should carry an explicit assumption about how long it will last.

## What Zimo can test

All **[Zimo hypothesis]**.

- **[Zimo hypothesis] Write down Zimo's platform-dependency audit now, before it matters.** For each growth input — contact permissions, SMS deliverability, iMessage extension, App Store discovery, payment rails, bank connections — name the owner, the plausible competing product, and the plan B. Meerkat's founders did not know they were renting until the day the rent stopped.
- **[Zimo hypothesis] Assume contact sync will keep degrading.** Bier's warning plus Saturn's contact-book settlement plus platform trends all point one direction. Zimo's graph should be constructible from **the transaction itself** (Venmo's model) rather than from the address book.
- **[Zimo hypothesis] Beware the iMessage/group-chat dependency specifically.** Zimo's natural home is the group chat, which is Apple's and Meta's territory. Being *inside* iMessage is powerful and is exactly the Meerkat position. The defensible version is a product that works better with the group chat but does not require it.
- **[Zimo hypothesis] Prefer presence over performance.** Houseparty's lesson translated: a Zimo action that requires a user to *announce* something (posting a trip, publishing a ledger) will be rare. One that just reflects what already happened (the split appears because the dinner happened) will be frequent.

## Sources

**Primary (transcripts, `ingest/transcripts/`):**
- `iXQuzBgeGXI` — Ben Rubin, Traction, "The Story Behind Meerkat's Viral Growth" (22:22) — the Yevo/Air prehistory, the Lady Gaga superfan signal, and the crucial admission that Twitter's notification system did the distribution for the first month
- `Yl1Q8LjF6nI` — Ben Rubin, Startupfest, "Good luck, bad luck, and serendipity" (17:59) — the pivot timeline ($15M raise, launch end of Feb 2015), and the "everyday person doesn't go live every day" diagnosis

**Secondary:**
- "Twitter cripples Meerkat by cutting off access to its social graph," **VentureBeat**, Mar 13 2015 — https://venturebeat.com/2015/03/13/twitter-cripples-meerkat-by-cutting-off-access-to-its-social-graph/
- "Twitter Starts Breaking Meerkat Features By Limiting Social Graph Access," **TechCrunch**, Mar 13 2015 — https://techcrunch.com/2015/03/13/twitter-starts-breaking-meerkat-features-by-limiting-social-graph-access/
- "Twitter Chokes Off Meerkat's Access To Its Social Network," **BuzzFeed News**, Mar 13 2015
- Wikipedia, *Meerkat (app)* — post-cutoff stagnation, Jul 2015 co-hosting and Facebook integration, Houseparty redirect
