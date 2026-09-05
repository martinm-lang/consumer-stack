# Consumer Distribution Playbook

Reconstructed growth machines of consumer companies — what they actually did, sourced and labeled.

This is the **case layer**. It is not the coach layer. `knowledge/` holds one file per *person* and
answers *how they think*; `playbook/` holds one file per *company* and answers *what they did*. The
two have different sourcing rules and must not be mixed — see [`RULES.md`](RULES.md).

## Start here

**The central research question of this playbook:**
> **How do products that work at n=2 exploit dense networks to become culturally dominant?**

| If you want | Read |
|---|---|
| **The core framework** | **[`NETWORK_TIERS.md`](NETWORK_TIERS.md) — Minimum Viable / Distribution / Saturation Network** |
| **The anti-case that matters most for Zimo** | **[`UTILITIES.md`](UTILITIES.md) — why useful utilities fail to go viral (Splitwise)** |
| **The company that already spent 15 years on your problem** | **[`PREDECESSORS.md`](PREDECESSORS.md) — direct predecessors & failed-to-expand analogues, + the Splitwise interview guide** |
| The cross-company principles | [`LAWS.md`](LAWS.md) — 12 laws, each with a counterexample |
| Every viral loop, mechanically | [`LOOPS.md`](LOOPS.md) |
| How to tell what stage a market is in | [`SATURATION.md`](SATURATION.md) |
| Companies side by side | [`MATRICES.md`](MATRICES.md) |
| What to actually do about Zimo | [`ZIMO.md`](ZIMO.md) |
| How to measure whether it's working | [`ZIMO_METRICS.md`](ZIMO_METRICS.md) — the group branching factor |
| One company in depth | [`cases/`](cases/) |
| What we don't know | [`RESEARCH_GAPS.md`](RESEARCH_GAPS.md) |
| Where it all came from | [`SOURCES.md`](SOURCES.md) |

## Cases — Tier A complete (10/10)

| Case | Wedge | Atomic network | Outcome |
|---|---|---|---|
| [Fizz](cases/fizz.md) | Stanford dorms | One `.edu` campus | Live, ~250 campuses |
| [Venmo](cases/venmo.md) | Two roommates settling up | **A pair** | Survived via acquisition |
| [Partiful](cases/partiful.md) | House parties | One guest list | Live |
| [Saturn](cases/saturn.md) | A class schedule | One high school | Acquired by Snap 2025 |
| [tbh & Gas](cases/tbh-gas.md) | One high school | One high school | **Both dead** |
| [Tinder](cases/tinder.md) | USC Greek life | One campus's dating pool | Live |
| [Zenly](cases/zenly.md) | "Where are you?" | ~5 close friends | **Closed by Snap while growing** |
| [Snapchat](cases/snapchat.md) | Orange County high schools | A friend group | Live — the durable one |
| [Meerkat & Houseparty](cases/meerkat-houseparty.md) | Live video on Twitter | A **rented** graph | **Both dead** |
| [Airbuds](cases/airbuds.md) | A music widget | A friend group | Live |

## The six findings that changed the most

1. **Separate the Minimum Viable Network, the Distribution Network and the Saturation Network**
   ([`NETWORK_TIERS.md`](NETWORK_TIERS.md)). Products that *require* saturation (Fizz, tbh/Gas, Yik
   Yak) are expensive and fragile. Products that work at n=2 but chase density anyway (Venmo, PayPal,
   Cash App, Snapchat) became culturally dominant. Products that work at n=2 and never chase density
   (**Splitwise: 30M users, fifteen years, still not a verb**) plateau as useful tools.
   **Working at n=2 makes the campus play more attractive, not less** — you capture saturation's
   upside without being hostage to it.

2. **The strongest consumer loops run on renewable real-world behavior** (`LAWS.md` Law 3). Dinner
   tomorrow, rent next month, the trip, the groceries — you don't consume the loop, life regenerates
   it. tbh and Gas both hit #1 in the US App Store and both were shut down within a year, because a
   closed network contains a finite amount of novel social information.

3. **A campus launch day buys ~10%, not a campus.** Fizz's founder says the whole school signed up
   that morning; the Stanford Daily's contemporaneous report says 700 users — about 10% of undergrads
   — after a week, and 95% took roughly a year. Founder launch anecdotes compress time, attaching the
   terminal number to the day-one memory.

4. **Interview your predecessor before you interview your heroes** ([`PREDECESSORS.md`](PREDECESSORS.md)).
   The heroes tell you what worked in a different market ten years ago. The company that spent
   fifteen years on *your* problem and plateaued tells you where the ceiling is. For a shared-expense
   product that is Splitwise; for social music it was Last.fm; for events, Evite. This category was
   missing from the playbook and is now first-class.

5. **A utility that hands back its hardest step gets none of the credit.** Splitwise solves the
   arithmetic and then makes you re-key the request into Venmo — *"the moment between calculating
   what everyone owes and actually getting paid is where most splits die."* Whoever closes the loop
   gets the gratitude and the word of mouth.

6. **Six of eleven products in this playbook are dead, and four were killed by an acquirer while
   working** (`MATRICES.md` §5). Venmo is the one case where acquisition was the rescue. Any plan
   treating "get acquired" as the happy ending should read that column first.

## Evidence labels

Every claim carries one, and they are never blended:

**[Confirmed]** independently reported or corroborated · **[Founder-reported]** / **[Company-reported]**
originates with the company, unverified · **[Interpretation]** our explanation of why it worked ·
**[Transferable]** the extracted principle · **[Zimo hypothesis]** a proposed experiment, never a
finding · **[Unverified lore]** widely repeated, traced to no credible origin

## Status

**Tier A: complete (10/10).**

**Second wave: money-product sweep done as synthesis, not yet as case files.** Splitwise, Tricount,
PayPal, Cash App and Revolut are researched and written up in [`UTILITIES.md`](UTILITIES.md) —
because the question they answer together (*why do useful utilities fail to go viral?*) matters more
to Zimo than any of them does individually. Standalone case files for Cash App, PayPal and Revolut
are the next build.

**Still unresearched:** Facebook (how they removed the school gate), Dropbox (the canonical extrinsic
referral loop), BeReal, Yik Yak, Robinhood, Locket, Musical.ly/TikTok, Poparazzi, Clubhouse, Wise,
Instagram, Discord, Airbnb, Pinterest. Prioritized in [`RESEARCH_GAPS.md`](RESEARCH_GAPS.md).

Corpus: 69 episodes (20 added for this pass). Reproduce via [`../ingest/README.md`](../ingest/README.md).
