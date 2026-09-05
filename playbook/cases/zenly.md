# Zenly

> **Era:** 2011–2023 | **Wedge:** "where are you?" between close friends | **Atomic network:** a friend group of ~5
> **Status:** **dead.** Acquired by Snap 2017; **shut down Feb 3 2023 while growing faster than ever.**
> **Sources:** 1 long founder interview transcript (Antoine Martin, high yield), 1 CTO/co-founder talk (Alexis Bonillo), The Pragmatic Engineer, Rest of World, TechCrunch, Sifted.

## TL;DR

Zenly is the corpus's best case of **retention-first company building** and its most painful ending. Antoine Martin's doctrine — *purpose → retention → engagement → growth, in that order, ignoring growth for roughly two years* — produced a product with elite frequency and a friend graph so durable that the app **grew from under 1M MAU at acquisition to over 40M MAU five years later, inside Snap, with ~70 people.**

Snap shut it down anyway, on Aug 31 2022, as part of a 20% workforce reduction. At the time it was the **10th most downloaded social app in the world** and its downloads were running at roughly **one-third of Snap's own global download volume.**

The reason is the most important strategic lesson here and it has nothing to do with product: **Zenly grew in markets Snap could not monetize — Japan, Vietnam, Indonesia, Russia — and overlapped with Snap Map.** Selling it would have created a competitor. Shutting it down wrote off the acquisition and removed the threat. Zenly's founder had left in April 2022, so the division had no internal advocate.

**Zenly did not fail. Zenly was closed.** Those are different, and the distinction matters for any founder thinking about an acquisition as an outcome.

## The machine

> "when are you coming home?" (wedge) → ~5 close friends (atomic network) → **contacts + phone verification; the graph already exists** (cold start) → word of mouth, no paid acquisition doctrine (distribution) → **weak explicit loop; visible daily use is the loop** → frequency of opens, emotional micro-delights (retention) → friend groups → whole countries via structural product fit → Snap → shutdown

## Timeline

| Date | Event |
|---|---|
| 2011 | Founded in France by **Antoine Martin** and **Alexis Bonillo**. Predecessor product: a family-safety/location app. [Confirmed] |
| 2011–2015 | Retention-first period. Growth explicitly ignored for ~2 years post-launch. [Founder-reported] |
| 2017 | **Acquired by Snap for ~$350M**, largely for social-mapping IP. MAU at acquisition: **under 1M** — one engineer's estimate is "a few hundred thousand." [Confirmed — Pragmatic Engineer] |
| 2017–2022 | Paris office runs as a **siloed, independent division**, ~70 people, and quietly compounds. |
| Mar 2022 | **10th most downloaded social app globally.** [Confirmed] |
| 2022 | Downloads reach **~1/3 of Snap's global app download volume** for several months. **40M+ MAU** (~8% of Snap's 500M). [Confirmed] |
| **Apr 2022** | **Antoine Martin leaves Snap.** The division loses its internal advocate. [Confirmed] |
| **Aug 31, 2022** | Snap announces 20% layoffs and the **shutdown of Zenly**. [Confirmed] |
| **Feb 3, 2023** | Zenly goes dark. [Confirmed — TechCrunch] |

## Initial conditions

**The wedge is a text message everyone has already sent.** Martin's framing:

> "Half of us have a text message from someone we live with asking when are you coming home — and that's true in Japan, that's true in Europe, that's true in the US." [l5dFuyyOY7A]

**[Interpretation]** This is latent demand in Bier's sense, and it is unusually strong because the distorted process is *universal and invisible*. Nobody experiences "asking where someone is" as a problem; it is simply how life works. That makes it a hard product to pitch and an easy one to retain, because the underlying behavior is already at maximum frequency.

**The second-degree job.** Martin insists social products are hired for something other than their literal function:

> Nobody opens Zenly to see a pin on a map; they open it because friends showed up at their club on a Saturday out of nowhere. [l5dFuyyOY7A]

**[Transferable]** The stated feature (location sharing) is the mechanism; the job (serendipitous presence, the feeling of being accompanied) is the product. Optimizing the mechanism without naming the job produces a utility nobody loves.

## Cold start

**Zenly has no cold-start problem at the network level, for the same structural reason as Venmo and Partiful: its atomic network is tiny and pre-existing.** Five close friends is enough. That group already exists offline and is already in your phone's contacts.

The engineering that made the cold start work was **onboarding infrastructure, not seeding**. Bonillo's talk is entirely about the unglamorous half: phone-number signup at global scale required partnering with many SMS vendors, maintaining credit on each platform, and handling deliverability country by country — eventually consolidated onto a single provider [BCOF9V7bQUo]. **[Interpretation]** For a product whose identity primitive is a phone number, SMS deliverability *is* the activation funnel. A verification code that fails in Indonesia is an unlaunched country.

**The MVP truth test**, in Martin's telling: he brought the first build to a birthday party and collected ten bug reports before he reached the birthday boy — from friends who were not supposed to have the app yet.

## Retention — the actual product

This is where Zenly is genuinely world-class, and the doctrine is unusually specific.

**Frequency, not time spent.** Zenly refused to optimize session length. With no ads, there is no reason to hold anyone:

> "If your session is 20 seconds long, we're doing an okay job; if your session is 40 seconds long, it's probably that we have an engineering problem." [l5dFuyyOY7A]

The KPI is **opens per day**. **[Interpretation]** This inverts the entire attention-economy metric stack, and it has a compounding distribution benefit Martin names directly: five *visible* opens during a conference makes the people around you ask what the app is. **High frequency plus public use is a distribution channel** — the phone screen is the billboard.

**Latency is retention, quantified.** Friend location must render in **~500ms**; at 2–3 seconds users lose the habit and revert to texting. Any infrastructure latency shows up as a usage flattening. **[Founder-reported]** **[Transferable]** This is the most concrete engineering-as-retention claim in the corpus: for a product competing with an existing free habit (texting), your latency budget is set by how long it takes the user to give up and do the old thing instead.

**Activation is the first two minutes.** ~80% of the retention job happens in the user's first few hours, and the required actions must complete within roughly two minutes. Users ride a **motivational wave** that peaks at download and decays within ~10 seconds. Mechanics: stack the required inputs early (location permission, first name, phone verify), **one required action per screen**, and use *more* screens with simpler steps rather than fewer dense ones.

**~5 active friends is the retention threshold** for a social product of this kind. [Endorsed on stage by Martin]

**McDonald's Wednesdays.** A weekly ritual: go to a fast-food restaurant full of students, buy a teenager's meal and stand in the queue for them, and in exchange they test the app for 15 minutes on camera. Deliberately done *there*, not in an office — during lunch the kid receives a snap every 20 seconds and switches between twenty apps, and the onboarding must survive that. Martin calls it "probably one of our most important secrets." When iOS made always-on location harder: "we just go more often to McDonald's."

## Geographic expansion — the best localization insight in the corpus

Zenly's strongest markets were **Japan, Vietnam, Indonesia and Russia**; hubs also in Brazil and Thailand. Internally: *"Growth comes from the East."* [Confirmed]

Martin's explanation is structural, not cultural, and it is excellent:

> "In Asia, especially Japan, the address system is very complicated. So being able to just see where your friend is on the map and follow your phone to him helps." [l5dFuyyOY7A]

Japanese addresses are block-based rather than street-sequential, which makes "meet me here" genuinely hard to express in text. **The product was more valuable in Japan because of a property of Japan, not because of anything Zenly did there.** Add Tokyo's density and the value compounds.

**And the anti-generalization discipline:**

> "Internally we don't generalize talking about Asian users, because when we look at the different countries there's very different behaviors… Japan versus South Korea versus Taiwan versus China have totally different cultures around privacy." [l5dFuyyOY7A]

**[Transferable] Find the country where a structural feature of daily life makes your product mechanically more useful, and expect propagation there without effort.** Then refuse to treat the region as one market. This is a far more actionable localization heuristic than "adapt to local culture."

## Viral loop

Zenly's explicit loop is weak; its implicit one is unusual and worth naming.

> A shares location with B → **B must install to see A** → B installs, shares back → B's other friends appear as friends-of-friends → B invites them

| Dimension | Zenly |
|---|---|
| Trigger | Wanting to see or be seen by a specific friend |
| Value before signup | **None.** You must install to see anything. |
| Reciprocity | **Structurally forced** — location sharing is only useful if mutual |
| Intrinsic? | Yes |
| **The real mechanism** | **Public, high-frequency use.** Opening it five times an hour in front of people |

**[Interpretation]** Reciprocity-forced products have a distinctive growth shape: they cannot be used alone, so every new user must bring at least one other. That is a floor of K≈1 by construction, and it is why Zenly compounded steadily for a decade rather than spiking. It also caps the speed — there is no way to acquire a user without acquiring their friend.

**Zenly is the strongest evidence in the corpus for "retention is the strongest form of distribution."** With no paid acquisition doctrine, no ambassador program, no launch operations and ~70 people, it went from a few hundred thousand to 40M MAU on frequency and word of mouth alone.

## Product philosophy worth transplanting

- **Never implement a user request literally.** *"I don't think we've ever implemented directly something coming from a user — if that happens we've been very bad, because it means it's obvious."* Feedback is a signal pointing at something else. Martin personally Google-translated Japanese tweets ~300 times a day to build conviction.
- **No product managers until ~50 people.** Nobody between engineers and designers, forcing the whole company to think in product terms. A designer hears something in the morning, designs before lunch, rebounds with an engineer, ships.
- **Freelancers before employees** — 100% of Zenly's leadership started as freelancers, including a VP Engineering courted for five years and converted over 6–8 months.
- **Data belongs to the user.** *"We've never sold user data, we'll never sell user data"* — stated as an internal engineering ground rule, not marketing.
- **DAU growth target: 6% per week** (against Paul Graham's 7% YC bar).

## Metrics

| Metric | Value | Label |
|---|---|---|
| MAU at Snap acquisition (2017) | **<1M**; engineer estimate "a few hundred thousand" | **[Confirmed]** — Pragmatic Engineer |
| MAU at shutdown (2022) | **40M+** (~8% of Snap's 500M) | **[Confirmed]** |
| Downloads, 2022 | ~1/3 of Snap's global download volume, several months running | **[Confirmed]** |
| Global rank, Mar 2022 | 10th most downloaded social app | **[Confirmed]** |
| Team size | ~70, mostly Paris | **[Confirmed]** |
| Target session length | ~20s good, 40s = a bug | [Founder-reported] |
| Location render latency budget | ~500ms; habit breaks at 2–3s | [Founder-reported] |
| Retention threshold | ~5 active friends | [Founder-reported] |
| Activation window | ~80% of retention decided in first few hours; actions inside 2 minutes | [Founder-reported] |
| Weekly DAU growth target | 6% | [Founder-reported] |

**Note the growth ratio: >40× MAU growth in five years, post-acquisition, with a small siloed team.** This is the second case in the corpus (with Venmo) where the famous growth happened *after* the company stopped being independent.

## Why it was shut down

Snap's stated and reported reasoning:

1. **Zenly's growth was concentrated in markets Snap could not monetize** — Japan, Vietnam, Indonesia, Russia — precisely the markets where Snap itself had minimal presence. Users without ad revenue are a cost.
2. **Feature overlap with Snap Map** (launched 2017, the year of the acquisition).
3. **Selling it would have created a competitor.** Shutting it down wrote off the acquisition cost *and* removed a future threat. Rest of World's reporting frames this as decisive.
4. **No internal advocate** after Antoine Martin's departure in April 2022.
5. Timing was set by Snap's own 20% workforce reduction, not by Zenly's performance.

**[Interpretation]** The uncomfortable synthesis: Zenly's greatest strength — organic growth in dense, under-monetized international markets — was the exact property that made it worthless to its owner. A metric that reads as excellent to a founder (40M engaged users) reads as a liability on an ad-supported P&L if those users cannot be sold to advertisers. **Product-market fit and product-market-*owner* fit are different things**, and an acquisition swaps which one determines your survival.

## Transferable principles

1. **[Transferable] Purpose → retention → engagement → growth, in that order.** Growth pursued out of order is the most common failure Martin sees.
2. **[Transferable] Optimize opens per day, not time spent** — and pick a KPI native to your category.
3. **[Transferable] Set a latency budget from the alternative behavior.** You are competing with what users did before; the habit breaks at the moment your product is slower than that.
4. **[Transferable] Activation is the first two minutes; one required action per screen; more screens, not fewer.**
5. **[Transferable] Test with real users in their real environment, weekly, on camera** — not in your office.
6. **[Transferable] Find the market where a structural fact of daily life makes your product mechanically more useful.** Then refuse to treat that region as one market.
7. **[Transferable] Reciprocity-forced products have K≈1 by construction** — slow, steady, and very hard to kill.
8. **[Transferable] High-frequency public use is itself a distribution channel.**
9. **[Transferable] Never implement a user request literally.** It is a signal, not a spec.
10. **[Transferable] An acquisition transfers the definition of success.** Ask what your users are worth on the *acquirer's* P&L, not yours.

## What Zimo can test

All **[Zimo hypothesis]**.

- **[Zimo hypothesis] Adopt the frequency KPI explicitly.** For Zimo the native metric is not DAU and not time-in-app — it is **splits per group per week** and **opens per day per active group**. Martin's point is that the wrong KPI for your category corrupts every downstream decision.
- **[Zimo hypothesis] Set the latency budget against cash and the group chat.** Zimo competes with "I'll Venmo you later" and with doing the arithmetic in iMessage. Time the incumbent behavior and make Zimo faster than it. If settling a split takes longer than typing a number into a group chat, the habit will not form.
- **[Zimo hypothesis] Establish Zimo's "5 active friends" equivalent.** Find the threshold — likely *n* active co-splitters, or *n* splits completed — beyond which retention steps up, then make onboarding drive at that number and nothing else.
- **[Zimo hypothesis] Run McDonald's Wednesdays on campus.** Buy a student lunch, film them using Zimo for 15 minutes in the dining hall — mid-conversation, notifications firing, bad wifi. Not a lab, not a Zoom call. Martin calls this his most important secret and it costs almost nothing.
- **[Zimo hypothesis] Look for Zimo's Japan.** Where is splitting structurally harder or more frequent for reasons that have nothing to do with the product — countries with weak instant-payment rails, high cash usage, large shared-housing norms, or strong group-dining culture? Zenly's lesson is that these markets adopt without marketing spend.
- **[Zimo hypothesis] Force reciprocity where it is honest.** A split is inherently mutual — both parties need the record. Design so a one-sided Zimo user gets meaningfully less than a reciprocal pair, and the K≈1 floor comes for free.
- **[Zimo hypothesis] Decide now what Zimo's users are worth to a potential acquirer.** Zenly's 40M engaged users were shut off because they lived where the owner could not monetize them. For a money product this is less acute — transactions monetize everywhere — but the question should be asked before, not after.

## Sources

**Primary (transcripts, `ingest/transcripts/`):**
- `l5dFuyyOY7A` — Antoine Martin, Startupfood, Paris (1:17:24) — the retention doctrine, frequency vs time-spent, the 500ms latency rule, first-two-minutes activation, McDonald's Wednesdays, the Japan address-system explanation, the anti-generalization rule on Asian markets, no-PMs, freelancers-first
- `BCOF9V7bQUo` — Alexis Bonillo, Telecom Application Development Summit (11:43) — cross-OS positioning vs Find My Friends, battery-impact algorithm, ghost mode, the billion-user ambition, and the SMS-vendor/phone-verification infrastructure problem
- Also distilled in `knowledge/antoine-martin.md` (coach layer).

**Secondary:**
- Orosz, G., "Inside the Shutdown of Zenly by Snap," **The Pragmatic Engineer** — https://blog.pragmaticengineer.com/zenly/ — MAU at acquisition vs shutdown, download share vs Snap, team size, "growth comes from the East," Martin's April 2022 departure
- "The Zenly implosion: Inside 6 months of tension, culture clash, and conflict," **Rest of World**, 2022 — https://restofworld.org/2022/fearing-competition-snap-decided-to-shut-down-zenly-rather-than-sell-it/ — the decision to shut down rather than sell
- "Zenly was the best social app and it will (sadly) shut down on February 3," **TechCrunch**, Dec 5 2022
- "Inside Snap's decision to shut down Zenly," **Sifted**

**Acquisition price:** ~$350M, per TechCrunch (Sept 2025), reported in coverage of Airbuds — whose co-founder Gawen Arab came from Zenly. See `cases/airbuds.md` for the lineage.

**Not established in this pass:** the "Taiwanese exchange class seeded a country" anecdote referenced in the coach playbook — the supporting passage was not recoverable from the transcript in this pass. Both logged in `RESEARCH_GAPS.md`.
