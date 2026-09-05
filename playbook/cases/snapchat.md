# Snapchat

> **Era:** 2011– | **Wedge:** Orange County high schools | **Atomic network:** a high school friend group
> **Status:** live, public company. The durable one.
> **Sources:** 4 founder interview transcripts already in corpus (`knowledge/evan-spiegel.md`), Fortune (2013), VatorNews chronology, TechCrunch.

## TL;DR

Snapchat's cold start is the least engineered in the corpus and the most instructive about **why** teen networks propagate. There was no ambassador program, no flyer drop, no paid seeding, no invite scarcity. Spiegel's **mother told his cousin**, the cousin showed classmates at an Orange County high school, and it spread through Southern California.

The structural fact that made it work is easy to miss: **those students had school-issued iPads on which Facebook was blocked.** A population with a device, an unmet social need, and their default social product administratively unavailable. Snapchat did not have to displace an incumbent — it walked into a vacuum the school had created.

Growth: 3,000 users in two months → ~100,000 by the April 2012 seed → **1M DAU by the end of 2012.** Word of mouth, first year, almost no marketing budget. [Confirmed]

Snapchat is also the corpus's only Tier A social product that **retained** — the black swan Bier says arrives about once a decade. The reason belongs in the retention section, not the growth section, and that is itself the lesson.

## The machine

> a photo you don't want kept (wedge) → one high school friend group (atomic network) → **a cousin shows classmates; Facebook is blocked on their school iPads** (cold start) → pure word of mouth (distribution) → the snap *is* the message; replying is the loop (viral loop) → streaks, Stories, notifications (retention) → SoCal high schools → US teens → global, multi-generational

## Timeline

| Date | Event |
|---|---|
| Apr 2011 | Reggie Brown brings the disappearing-photo idea to Stanford classmate Evan Spiegel; Bobby Murphy recruited to build it. [Confirmed] |
| Jul 2011 | Launched on iOS as **Picaboo**. [Confirmed] |
| Summer 2011 | **First users: Orange County high-schoolers**, via Spiegel's cousin, who heard about it from Spiegel's mother. Their school-issued iPads blocked Facebook. [Confirmed — Fortune] |
| Sep 2011 | Rebranded **Snapchat**. ~3,000 users within two months. [Confirmed] |
| End 2011 | >1,000 daily users. [Confirmed] |
| Apr 2012 | Seed round. ~100,000 users. [Confirmed] |
| End 2012 | **1M DAU.** [Confirmed] |
| 2013 | Turns down a reported ~$3B from Facebook. |
| 2013– | Stories, Snapcodes, Discover, Maps; IPO 2017. |

## Initial conditions — the policy vacuum

The specific mechanism deserves to be stated as a rule, because it recurs.

The Orange County students had:
1. **A capable device** (school-issued iPads),
2. **An unmet, urgent social need** (teenagers, constant communication),
3. **Their default product administratively blocked** (Facebook, by school IT).

**[Interpretation]** This is a **policy vacuum** — demand held artificially in place by an institutional restriction, with no supply. It is the single cheapest cold start available, because the incumbent has been removed by someone else and the population is captive and co-located. Snapchat did not out-compete Facebook among these students; it was simply the thing that worked.

**[Transferable] Look for populations whose default tool has been blocked, banned, deprecated or made unusable by an institution, not by a competitor.** School device policies, workplace IT restrictions, app-store removals, regional bans, and API shutdowns all create these. The demand is pre-qualified and the incumbent is absent by administrative fiat.

**The product wedge itself:** ephemerality. Every other photo product optimized for permanence and performance; Snapchat's constraint — the image is gone — removed the cost of posting. This is the same design logic as Fizz's anonymity (lower the cost of expression by removing the durable record) but without forfeiting identity, which is why Snapchat kept a friend graph and Fizz never had one.

## Viral loop

> A sends a snap to B → **B must open the app to view it** (it cannot be seen anywhere else) → the medium's grammar demands a reply → **B replies with a snap** → repeat

| Dimension | Snapchat |
|---|---|
| Trigger | Receiving a snap addressed to you personally |
| Value before signup | Moderate — a friend has sent you something *specific* and it expires |
| Reciprocity | **Conversational, not obligatory** — but socially near-mandatory between teens |
| Intrinsic? | Completely. The loop is the messaging. |
| Speed | Seconds |

**[Interpretation]** Snapchat's loop is a **messaging loop**, which is the strongest category of retention loop and the weakest category of acquisition loop — it circulates intensely inside an existing group and does almost nothing to reach outside it. The outward spread was physical: teenagers in the same school, showing each other. Combined with Fizz, Saturn and Tinder, that makes **four of the eight Tier A campus/school cases whose real distribution mechanism was people standing next to each other.**

**Later, product-borne distribution was added deliberately:**
- **Stories** — broadcast rather than addressed; created a reason to open with no incoming message.
- **Snapcodes** — a scannable identity artifact that collapses friend-adding to a camera point, avoiding the "10,000 taps versus one" username-exchange problem Bier describes.
- **Streaks** — see below.

## Retention — why this one survived

This is the section that matters, because Snapchat is the counterexample to tbh, Gas, Yik Yak, Clubhouse, Poparazzi and Meerkat.

- **Streaks** convert a communication habit into a **jointly-owned asset with a loss condition**. Two people build a number neither can preserve alone. It is Nir Eyal's investment phase and a mutual sunk cost simultaneously — the strongest single retention mechanic documented in the corpus, and the reason Duolingo copied its logic.
- **Stories** supply content when no message has arrived, closing the gap that kills pure messaging apps.
- **The trigger is other people**, regenerated indefinitely. Compare tbh, whose trigger was novel social information in a closed network — a finite resource.
- **The friend graph is real and mutual**, so switching costs are collective, not individual.

**[Interpretation]** The precise difference between Snapchat and tbh: tbh's loop consumed a finite stock (the set of nice things a fixed group can say about you); Snapchat's loop consumes a renewable flow (whatever happened today). **Ask of any loop: is it drawing on a stock or a flow?** Stocks deplete on a schedule you cannot change. This is, in one line, why one of these companies is public and the other was shut down twice.

## Expansion — wedge to mainstream

Snapchat is the corpus's best example of **aging with a cohort while remaining open**. It never gated by school, `.edu`, or age, so:
- Its 2012 teenagers are its 2026 thirty-somethings and never had to leave.
- New teenagers kept arriving underneath them.
- Nothing structural had to change — unlike Fizz, which must expel every user within four years.

**[Transferable] A demographic wedge that is a *starting point* beats one that is a *boundary*.** Snapchat and Tinder both aged out of their wedge for free. Fizz cannot. The difference is whether the wedge is enforced in code.

## What the coach layer adds

`knowledge/evan-spiegel.md` (4 episodes) covers his thinking in depth — design-led invention, controlling only the differentiating layer, competing with giants, listening deeply then building something different. This file deliberately does not duplicate it. **For "how Spiegel thinks," read the coach file; for "how Snapchat spread," read this one.**

## Metrics

| Metric | Value | Label |
|---|---|---|
| Users, 2 months post-rebrand | ~3,000 | [Confirmed] |
| Daily users, end 2011 | >1,000 | [Confirmed] |
| Users at seed (Apr 2012) | ~100,000 | [Confirmed] |
| DAU, end 2012 | **1,000,000** | [Confirmed] |
| Marketing spend, year one | Effectively none; word of mouth | [Confirmed] |

## Transferable principles

1. **[Transferable] Hunt for policy vacuums.** A population whose default tool has been blocked by an institution is the cheapest cold start in consumer.
2. **[Transferable] Ask whether your loop draws on a stock or a flow.** Stock-based loops exhaust on a fixed schedule; flow-based loops don't.
3. **[Transferable] Streaks work because they are jointly owned.** A number two people built together and only one can break is far stronger than an individual streak.
4. **[Transferable] Add broadcast to messaging.** Pure messaging has nothing to show a user with no incoming message; Stories fixed that.
5. **[Transferable] Make identity scannable.** Snapcodes eliminate username exchange entirely.
6. **[Transferable] Don't enforce your wedge in code** if you ever want to leave it.

## What Zimo can test

All **[Zimo hypothesis]**.

- **[Zimo hypothesis] Zimo's loop is flow-based — say so and defend it.** Shared expenses regenerate forever. This is Zimo's structural advantage over every social-novelty app in this playbook, and it should be the first line of the investor narrative.
- **[Zimo hypothesis] Build a jointly-owned artifact with a loss condition.** The streak insight generalized: what does a Zimo *pair or group* build together that neither can maintain alone and would be sad to lose? A settled-up streak between roommates, a complete trip ledger, a household's unbroken monthly reconciliation. Not a personal badge — a shared one.
- **[Zimo hypothesis] Find the policy vacuum on campus.** Where has an institution blocked or failed to provide the default? Campuses where Venmo is awkward for club dues, where a treasurer is banned from using a personal account, where international students cannot get a US payment app. Blocked defaults are pre-qualified demand.
- **[Zimo hypothesis] Scannable identity for splits.** A Snapcode-equivalent — one QR at the table adds everyone to the split. This is the single highest-leverage taps-to-value fix available for an in-person group.
- **[Zimo hypothesis] Never gate by `.edu`.** Snapchat's refusal to enforce its wedge is why it still exists. Zimo's campus users must be able to graduate without leaving.

## Sources

**Primary (already in corpus, `ingest/transcripts/`):**
- `-7Yol5vX5xw` — Evan Spiegel, Lenny's Podcast, "How to win when software is not a moat"
- `Sr6n-9mzYnk` — Evan Spiegel, David Senra
- `0IYBJXS-1t8` — Evan Spiegel, Tiger Sisters
- `_uWmiVRDLoE` — Evan Spiegel, Great Company with Jamie Laing
- Distilled in `knowledge/evan-spiegel.md`

**Secondary:**
- "Countdown to the Snapchat revolution," **Fortune**, Dec 18 2013 — https://fortune.com/2013/12/18/countdown-to-the-snapchat-revolution/ — the Orange County origin, the blocked-Facebook iPads
- "When Snapchat was young: the early years," **VatorNews**, Mar 8 2016 — https://vator.tv/2016-03-08-when-snapchat-was-young-the-early-years/ — the user-count chronology
- TechCrunch, Crunchies 2013

**Note:** this file is deliberately shorter than the campus-ops cases. Snapchat's growth mechanism is genuinely simple — a policy vacuum plus word of mouth — and the interesting engineering is all in retention. Padding it would misrepresent the case. The deeper research target here is the **Stories/Snapcodes/streaks design history**, which is logged in `RESEARCH_GAPS.md`.
