# tbh & Gas (Nikita Bier / Midnight Labs)

> **Era:** tbh 2017 · Gas 2022–23 | **Wedge:** one American high school | **Atomic network:** a single high school
> **Status:** **both dead.** tbh → Facebook (~$100M, Oct 2017), **shut down Jul 2018.** Gas → Discord (Jan 2023), **shut down Nov 2023.**
> **Sources:** 2 founder interview transcripts, Facebook newsroom, TechCrunch ×2, Bloomberg, Variety, Washington Post, Appfigures.

## TL;DR

The most reproducible school-launch machine ever documented, run twice, five years apart, by the same person. Both times it produced explosive, verifiable, top-of-the-App-Store growth. **Both times the product was dead within about a year.**

tbh: launched Aug 3 2017 → 5M downloads and 2.5M DAU in nine weeks → term sheet within six weeks of launch → acquired by Facebook for ~$100M on day 73 → **shut down for low usage, July 2018.**

Gas: launched Aug 2022 → 30,000 new users *per hour* in October → briefly #1 on the US App Store, above TikTok and BeReal → ~$7M consumer spend on 7.4M installs → acquired by Discord Jan 2023 → **shut down for steep decline, Nov 2023.**

**This is the corpus's cleanest answer to "did the distribution system create a durable product or merely a spike?"** It created a spike, twice, and the founder says so himself: growth is a repeatable science, retention in consumer social is "a black swan event." Read this file as the definitive demonstration that **you can be world-class at distribution and still not have a company.**

## The machine

> teens want to hear good things about themselves (latent demand) → one high school (atomic network) → **saturate one school synchronously so nobody opens an empty app** (cold start) → geo-targeted ads + a per-school Instagram account, ~3 exposures (distribution) → poll results push notifications naming the recipient (viral loop) → **the loop is the retention, and it exhausts** → 40% of one school in 24h → spreads to neighbouring schools unprompted → state-by-state geofenced rollout → #1 US App Store → decay → shutdown

## Timeline

### tbh

| Date | Event |
|---|---|
| ~2012–2017 | Midnight Labs builds **~15 consumer apps** across a pivot to consumer. All fail. [Founder-reported] |
| Pre-launch | Bier sees **Sarahah — an app entirely in Arabic — at #1 in the US App Store.** "The strongest signal that you could ever have that people want something." [bhnfZhJWCWY] |
| Aug 3, 2017 | tbh launches, seeded into **one high school in Georgia — chosen because it had the earliest start date in the United States**, since the company was nearly out of money. [Founder-reported] |
| +24 hours | **40% of that school downloads it.** Spreads to neighbouring schools unprompted. [Founder-reported] |
| ~6 weeks | Term sheet. [Founder-reported] |
| Sep–Oct 2017 | State-by-state **geofenced** rollout. Hits #1 in the US the morning California is switched on. |
| Oct 2017 | **5M downloads, 2.5M DAU, >1B messages sent, in nine weeks.** [Confirmed — TechCrunch/Bloomberg] |
| Oct 16, 2017 | **Facebook acquires tbh, ~$100M — day 73 from launch.** [Confirmed] |
| **Jul 2, 2018** | **Facebook shuts tbh down, citing low usage.** [Confirmed — Facebook newsroom] |

### Gas

| Date | Event |
|---|---|
| Aug 2022 | Gas launches — same core mechanic, rebuilt. |
| — | Launched as **"Crush"** with a pink icon; invite rates tanked. Rebranded **"Gas," black icon, flame** to fix a 60–65% female skew. Invite rates jumped. [Founder-reported] |
| Oct 2022 | **30,000 new users per hour**; >1M DAU; briefly **#1 on the US App Store, above TikTok and BeReal.** [Confirmed — Appfigures] |
| Oct 2022 | A **human-trafficking hoax** spreads about the app. Full-spectrum response (below). |
| Dec 2022 | ~$6M in sales, 10M downloads. [Confirmed — Appfigures] |
| Jan 17, 2023 | **Discord acquires Gas.** Terms undisclosed. Lifetime: 7.4M installs, ~$7M consumer spend. [Confirmed] |
| **Nov 7, 2023** | **Discord shuts Gas down, citing a steep decline in users.** [Confirmed] |

## Initial conditions

**The latent demand, stated precisely.** Teens were posting emoji-key images to Snapchat stories to solicit compliments — a laborious, improvised workaround. Simultaneously, Sarahah (anonymous feedback, Arabic-only, unlocalized) was **#1 in the United States**. Bier's reading: an app nobody could read was #1 because the underlying motivation was overwhelming.

**[Interpretation]** This is the single best worked example of latent-demand detection available. The signal was not "teens like compliments" — it was two *independent distorted processes* running at once: a manual workaround inside another app, and a foreign-language app charting on raw motivation with zero product-market localization. Neither alone is conclusive; together they specify both the demand *and* that the existing supply is terrible.

**The product crystallized it with a constraint:** authored, positive-only, multiple-choice polls. Not free text.

**Why one high school is the right atomic network:** teens see each other daily (physical density), invite aggressively, and — per Bier's own cohort data — invites per user fall ~20% for every year of age from 13 to 18, and organic invite-driven growth is effectively dead past 22.

## Cold start — the seeding operation

This is the mechanic everyone copies and, per Bier, almost everyone misunderstands.

**The three-exposure rule and how it was engineered:**

> "To be convinced to download an app, you need to see it… the marketing message like three times or so. So you basically need to saturate an area with every kind of marketing you [have]." [bhnfZhJWCWY]

The two channels, run simultaneously against the same school:

1. **Geo-targeted ads** fenced to the school's area.
2. **A dedicated Instagram account per school**, built on a specific piece of teen behavior:

> "High schoolers identify their school in their bio. So it says RHS on their bio. And so that was how we tried to get the entire school to adopt synchronously. We would follow them and then accept the follow-backs." [bhnfZhJWCWY]

**[Interpretation]** This is a beautiful, cheap, and now largely un-repeatable hack. The school abbreviation in an Instagram bio is a **free, self-declared, machine-readable membership roster for a physical network.** Follow every account containing "RHS," accept follow-backs, and you have opted-in reach into one high school — no ad spend, no list purchase, no permission. It converts a public profile field into a targeting primitive.

**Why synchronous saturation, not gradual growth:** a social product opened by one student in isolation is empty and they churn. Everyone must arrive at once so the first session is populated. Bier's related rule: the user must see all their friends on the app **the first night** or they're gone.

**Choosing the seed school on an operational constraint, not a strategic one.** Georgia was picked because it had the **earliest school start date in the country** and the company was nearly out of cash. **[Transferable]** When time is the binding constraint, select the network whose *calendar* is soonest, not the one that is best. A perfect network that starts in six weeks is worth less than an adequate one that starts Monday.

**Test the ideal version.** Manufacture the best possible conditions even with unscalable manual work — get an entire school on, so everyone has ~10 friends; run 24/7 live human chat support in-app. You must never end a test saying "maybe the execution was bad." The live chat doubled as the best user-research channel they had.

**The critical nuance almost everyone gets wrong:** seeding is how you **test**, not how you **grow**. It buys the first ~100 users and eliminates confounds so you can say with conviction whether the app has legs. After the seed, the app must grow by itself. Bier notes imitators who ran school-seeding at 15 schools as a growth strategy and stalled — they copied the surface and missed that it was an experiment design.

## Launch mechanism — geofencing as a throttle

The state-by-state rollout, with every state geofenced, is the most under-copied tactic here. Its purpose was **not** demand generation — it was **demand suppression**:

- The infrastructure broke roughly every three days under real PMF.
- The AWS bill hit ~$120,000 against a nearly empty bank account.
- Geofencing let them meter growth to what the servers and the balance sheet could survive.

Bier's supporting claim: if it is genuinely working at small scale, you can switch it off and relaunch any time — **the demand does not evaporate.** They hit #1 in the US the morning they unfenced California.

**[Transferable] Build the throttle before you need it.** A geofence is a valve on a viral product. Founders build the accelerator and discover at #1 that there is no brake.

## Viral loop

> **User A votes in a poll about User B** → **B gets a push notification: someone chose you, with a gendered/grade hint but not a name**
> → B opens the app to find out who → **B must vote / invite to progress** → B's votes generate notifications to C, D, E → repeat

| Dimension | tbh / Gas |
|---|---|
| Trigger | Another user voting for you |
| Receiver value before signup | **Very high, and purely emotional** — someone said something nice about you |
| Friction | Low; but you must be *in* the school's network for the poll to exist |
| Incentive | Curiosity + flattery. Not money, not utility. |
| Intrinsic? | Yes — the loop *is* the product |
| Speed | Minutes |
| **Survived?** | **No. This is the whole point.** |

**Why it burns out — the core structural diagnosis. [Interpretation]**

The loop's fuel is **novelty of social information**. In a fixed network of ~1,000 students, the set of things that can be said about you is finite and small. Once you have learned who thinks you have the best smile, the same poll delivers a diminishing signal. There is:

- no new content supply (the questions are authored by the company, not users),
- no accumulating asset (no library, no history, no artifact you keep),
- no external utility (nothing you need it for),
- and no outside world (the network is capped at one school).

Compare Venmo, whose trigger is regenerated by real life every week forever, and Saturn, whose trigger is regenerated by the school bell every morning. **tbh and Gas had no external clock.** Once the novelty in a closed network is consumed, the product is finished there — and the network cannot grow, because it is a high school.

**This is why both apps died on almost identical ~12-month timelines despite five years, a rebuild, and two different acquirers.** It was not execution. It was the shape of the loop.

## Retention — and the honest verdict

Bier's own framing, in his coach playbook: retention for consumer social is **"a black swan event"** — roughly one durable social product per decade — while growth "can be a science."

tbh and Gas are the empirical support for both halves of that sentence, by the same author. He built the science. He did not get the black swan. Twice.

| | tbh | Gas |
|---|---|---|
| Launch → acquisition | 73 days | ~5 months |
| Acquisition → shutdown | ~8.5 months | ~10 months |
| Stated shutdown reason | "low usage" | "steep decline in users" |

**[Interpretation]** Both acquirers were sophisticated (Facebook, Discord) and both concluded within a year that there was nothing to keep. The market cleared this question twice with real money and reached the same answer.

**[Transferable] An acquisition is not evidence of durability. It is often evidence that the founder correctly identified the peak.** Bier sold both apps near their maximum. Reading tbh's $100M as validation of the product is a misread; reading it as world-class timing is correct.

## Metrics

| Metric | Value | Label |
|---|---|---|
| tbh, seed school day 1 | **40% downloaded in 24 hours** | [Founder-reported] |
| tbh, 9 weeks | 5M downloads, 2.5M DAU, >1B messages | **[Confirmed]** — TechCrunch, Bloomberg |
| tbh, day-1 messages per user | ~60 (vs. "3–4 is lucky" for a messaging app) | [Founder-reported] |
| tbh, one school, first 7 days | 450,000 messages | [Founder-reported] |
| tbh, peak installs/day | 360,000 | [Founder-reported] |
| tbh acquisition | ~$100M, Oct 16 2017, day 73 | **[Confirmed]** |
| Gas, peak signup rate | **30,000 new users per hour** (Oct 2022) | **[Confirmed]** — Appfigures |
| Gas, peak DAU | >1M | **[Confirmed]** |
| Gas, App Store rank | Briefly **#1 US**, above TikTok and BeReal | **[Confirmed]** |
| Gas, lifetime | 7.4M installs, ~$7M consumer spend | **[Confirmed]** |
| App Store #1 threshold | historically ~80–100K installs/day; now up to ~300K on competitive days | [Founder-reported] |
| Contact-permission consent rate | ~65% average across apps; higher for teens | [Founder-reported] |
| Peak AWS bill at #1 | ~$120,000 | [Founder-reported] |

**Note the asymmetry:** the growth numbers are independently confirmed; the *seeding* numbers — 40% of a school in 24 hours, 60 messages/user — are founder-reported and are the ones people copy. Antoine Martin, unprompted, names tbh specifically as an example of reported numbers he believes are inflated (`knowledge/antoine-martin.md`). **Two Tier A founders disagree on whether tbh's headline seeding figures are real.** Neither has published the underlying data. Treat 40%-in-24-hours as an upper bound, not a target.

## Crisis management — the hoax response

In Oct 2022 a viral hoax claimed Gas was a front for human trafficking. Bier's survival rule: **the hoax's K-factor must be lower than your app's**, and you fight every vector simultaneously.

- **Dictate the headline** — got "Gas app is not for human trafficking" into the Washington Post.
- **Call superintendents and police chiefs** directly for public retractions.
- **Get Apple to remove review-bombs.**
- **Network to platform CEOs** to remove the viral videos at the source.
- **Intercept churn at the exit** — showed a debunking video on the account-deletion screen. **Daily deletions fell from 3% to 0.1%.** [Founder-reported]

**[Transferable]** That last one is the generalizable move: **instrument the moment of churn as a persuasion surface.** A 30× reduction in deletions came from addressing the objection at the exact instant it was acted on.

## Ethical considerations

Unusually, this is a case where the founder's constraints are the lesson rather than the failure.

- **Refusal to build anonymous free-text messaging.** Bier states it is reliably viral and reliably ends in bullying and tragedy, and he will not build it. Compare Fizz and Yik Yak, which did.
- **Constrain the input, not just the output.** tbh/Gas used authored, positive-only, multiple-choice polls, so the product structurally *could not* produce a cruel message. Moderation is unnecessary if the input space contains no bad outputs.
- **Boosting under-voted users.** Gas deliberately injected the names of students receiving few votes into polls so that everyone got some. A designed intervention against the natural popularity power law.
- **"The internet defends itself."** Never send invites from your server, never act on user data in the background. Compare Saturn's NY AG settlement, which cited exactly the behaviors Bier refuses — contact-book retention after revocation, undisclosed paid promoters. **[Interpretation]** Bier's Gaia framing reads as a moral flourish; the Saturn settlement is what it looks like as a legal outcome.
- **The Instagram follow-tactic is a grey zone.** Following minors' public accounts to build per-school reach was legal and not deceptive, but it is a company systematically enumerating a physical population of teenagers via a profile field. Reproducing it in 2026 deserves more thought than it got in 2017.

## Reproducibility in 2026

| Tactic | Still works? |
|---|---|
| Latent-demand detection via App Store anomalies | **Yes** — arguably better, charts are noisier and more legible |
| Synchronous single-school saturation | **Yes** |
| Instagram school-bio follow-farming | **Degraded** — bios are less consistently school-tagged, platform limits are tighter |
| Geo-targeted ads to one school | **Yes**, more expensive |
| Contact sync as friend-finding | **Largely dead.** Bier: post-iOS-18 selective contact access effectively kills it. Anything depending on full contact-book access needs a plan B now. |
| Geofenced staged rollout | **Yes** — underused |
| Push-notification curiosity loops | **Yes**, with much lower notification tolerance |

**[Interpretation]** The most important change is the contact-sync death. tbh and Gas both relied on rapid friend-graph construction from contacts to make night-one populated. A 2026 equivalent must construct the graph some other way — which is why Saturn's "infer the network from a schedule photo" and Partiful's "the host brings the guest list" matter more now than they did then.

## Transferable principles

1. **[Transferable] Two independent distorted processes make a demand signal.** A workaround inside another product *plus* an unlocalized foreign app charting on raw motivation.
2. **[Transferable] Saturate one network synchronously so night one is populated.** Nobody's first session should be empty.
3. **[Transferable] Three exposures, multiple channels, one geography.** Ads and owned social must hit the same physical population simultaneously.
4. **[Transferable] Seeding is a test, not a growth strategy.** It buys the first ~100 users and removes confounds. If you are still hand-seeding school 15, the product is not working.
5. **[Transferable] Pick the seed network on calendar, not quality, when time is the constraint.**
6. **[Transferable] Build the throttle before the accelerator.** Geofencing saved tbh from its own AWS bill.
7. **[Transferable] Constrain the input so the product cannot produce the bad outcome.** Cheaper and more reliable than moderating the output.
8. **[Transferable] Instrument the churn moment as a persuasion surface.** 3% → 0.1% daily deletions.
9. **[Transferable] Ask what regenerates the trigger.** A loop with no external clock and a closed network will exhaust. This is the diagnosis for both shutdowns and the most important line in the file.
10. **[Transferable] An acquisition is not proof of durability.**

## What Zimo can test

All **[Zimo hypothesis]**.

- **[Zimo hypothesis] Zimo's structural advantage over tbh is the external clock — protect it.** tbh died because a closed network ran out of novel social information. Zimo's trigger is regenerated by real life (dinners, rent, trips) forever, exactly like Venmo's. **Any feature that moves Zimo toward "novel social information" and away from "money that actually needs settling" is moving it toward tbh's failure mode.** Treat that as a design constraint, not a preference.
- **[Zimo hypothesis] Run the seeding operation as a test with a pre-registered kill criterion.** Pick one campus, saturate it synchronously, and write down beforehand what result means "the product has legs" (e.g. splits-per-group-per-week above X at day 30 with zero further ops). Then honour it. Bier's whole method is that the seed exists to remove the excuse "maybe the execution was bad."
- **[Zimo hypothesis] Find the 2026 equivalent of the school-in-the-bio hack.** The generalizable form: *a public, self-declared, machine-readable field that identifies membership in a dense physical network.* On campus today that may be Instagram class-year tags, GroupMe/Discord servers, club rosters, or intramural league signups. The tactic is not Instagram; it is finding the free roster.
- **[Zimo hypothesis] Build the geofence on day one.** A money product that goes viral without a throttle has a support, fraud and compliance exposure that a social app does not. Zimo needs the brake more than tbh did.
- **[Zimo hypothesis] Pick the seed campus by calendar.** Earliest term start, or the week before a high-spend event (formals, ski trips, spring break) when splitting frequency peaks.
- **[Zimo hypothesis] 24/7 in-app human chat from day one on the first campus.** Bier calls it the best user-research vehicle he ever had, and for a money product it doubles as the trust mechanism that makes strangers accept a payment request.
- **[Zimo hypothesis] Constrain the input.** Money between friends has its own cruelty vector — public shaming over unpaid debts. Design the request so the product cannot produce a humiliating outcome (no public shaming feeds, no visible delinquency).
- **[Zimo hypothesis] Never claim 40%-in-24-hours as a benchmark.** It is founder-reported and contested by a peer. Fizz's independently documented ~10% in week one is the number to plan against.

## Sources

**Primary (transcripts, `ingest/transcripts/`):**
- `bhnfZhJWCWY` — Nikita Bier, Lenny's Podcast, "How to consistently go viral" (1:38:21) — the Sarahah signal, Georgia seed school and earliest-start-date reasoning, 40%-in-24h, the Instagram school-bio follow tactic, three-exposure rule, geofenced state rollout, AWS bill, hoax response, the age/invitation curve
- `Rql6GZakVTI` — Nikita Bier, Greg Isenberg, "Where It Happens" (1:12:43) — Midnight Labs ran ~5 years before tbh; term sheet within 6 weeks of launch; views on Meta/TikTok. *Mostly off-topic for tbh/Gas mechanics; logged so it isn't re-pulled.*
- Also distilled in `knowledge/nikita-bier.md` (coach layer — how he thinks; this file is the machine).

**Secondary:**
- "Facebook acquires anonymous teen compliment app tbh, will let it run," TechCrunch, Oct 16 2017 — https://techcrunch.com/2017/10/16/facebook-acquires-anonymous-teen-compliment-app-tbh-will-let-it-run/
- "Hello. tbh, We're Moving On," Facebook Newsroom, Jul 2018 — https://about.fb.com/news/2018/07/hello-tbh-moving-on/ — the shutdown
- Bloomberg, "Facebook Buys TBH App Popular With Teens," Oct 16 2017
- Variety, Oct 2017; Washington Post, "What is TBH," Oct 17 2017
- "Discord acquires Gas, a compliments-based social media app for teens," TechCrunch, Jan 17 2023
- Appfigures, "Six Months and $7,000,000 Later, Discord Acquires Gas," Jan 20 2023 — installs, revenue, 30K/hour, App Store rank
- Wikipedia, *Gas (app)* — Nov 7 2023 shutdown date and stated reason
