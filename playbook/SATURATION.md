# The Saturation Playbook

How companies made a population feel *"everyone around me is suddenly using this"* — and how to
tell which stage a market is actually in.

---

## 1. The proposed formula, and why it needs replacing

The brief offers, as a hypothesis to test rather than accept:

> Saturation = Density × Frequency × Simultaneity × Social Proof × Product Propagation

Against the ten Tier A cases this does not hold up, for three reasons.

**It multiplies terms that are not independent.** Density *produces* frequency. On a residential
campus, co-location generates the repeat exposures for free — that is the entire finding of Law 4.
Treating them as separate multiplicands double-counts the same mechanism.

**Two of the terms only apply to some products.** Simultaneity is decisive for Fizz and tbh
(crowd-atomic) and **irrelevant** for Venmo, Partiful, Zenly and Airbuds, which never ran a
synchronized launch at all and saturated their networks anyway. A term that is meaningless for
half the corpus is not a factor in a general formula; it is a factor in one *class* of product.

**It has no threshold and no time.** Saturation is not a smooth product of inputs. Crowd-atomic
products have a **step function**: below a critical mass the product is worthless and nobody stays.
And every real case shows saturation happening in two distinct phases, months or years apart.

---

## 2. A better model: two questions, not one formula

Saturation of a single network decomposes cleanly into **a seed and an amplifier**, and they have
different economics.

```
Terminal penetration  ≈  Seed  ×  Amplifier ^ (time)
```

**Seed** — what one launch action buys. Empirically bounded:

- **~10%** of a residential campus, from a maximal launch-day operation (Fizz at Stanford: 700+
  users, ~10% of undergrads, within a week — the only *independently documented* number in the set)
- **40%** in 24 hours claimed for tbh's Georgia school — **founder-reported, and explicitly
  disputed by another Tier A founder.** Treat as an upper bound, not a target.
- Tinder: <5,000 → ~15,000 across one campus trip. [Company-reported]

**Plan against ~10%. Anything above it is a bonus, not a plan.**

**Amplifier** — what compounds the seed, and there are only two kinds:

| Amplifier | Mechanism | Cost per network | Cases |
|---|---|---|---|
| **Product-borne loop** | The product carries itself to non-users | **~Zero.** The last network gives you the next one. | Venmo, Partiful |
| **Co-location word of mouth** | People in the same building talk | **~Zero within a network, but does not travel.** Every new network must be bought again. | Fizz, Saturn, Snapchat, Tinder |

**This distinction is the whole strategic content of saturation.** Both amplifiers are free *inside*
a network. Only the first is free *between* networks. Fizz's ~250 campuses each cost an operation;
Venmo's expansion cost nothing per network because payments crossed the boundaries by themselves.

**The threshold condition, which sits underneath both:** if your atomic network is a crowd, none of
this matters until you clear critical mass, because below it the product is empty and retention is
zero. If your atomic network is a pair, there is no threshold and no seeding problem at all
(Law 1).

**And the durability condition:** an amplifier running on a *stock* of novelty will saturate a
network and then evacuate it. tbh saturated schools completely and was dead within a year (Law 3).
**Saturation is not the finish line — it is the point at which the retention question becomes
answerable.**

---

## 3. The state ladder

Six states, each with observable signals. Use this to answer "what stage is this campus actually
in" instead of guessing from a download count.

### Seeded
The launch action has happened.
- **Signal:** a burst of installs concentrated in hours; ~5–15% of the population registered.
- **Do not celebrate.** Fizz's own record shows many launch-day downloads went inactive or were
  deleted immediately; Tinder's download-to-enter parties produced installs under social pressure at
  a door. **Measure activations, not installs.**
- **Trap:** a founder reading a download spike as adoption. This is where nearly all campus-launch
  self-deception lives.

### Warming
Usage is growing without further launch effort — but the launch team is still present.
- **Signal:** DAU rising for 2–3 weeks post-launch with no new ops spend; the first content or
  transactions from people outside the founders' personal network.
- **Trap:** the founder and their friends are still in the building. **Everything looks like this
  while the seeder is present.** Not yet evidence of anything.

### Locally relevant
The product is referenced in the physical world by people who don't know you.
- **Signal:** overheard mentions; the product's name used as a verb or shorthand; non-users know
  what it is. For Saturn, students browsing each other's calendars all day — a behavior nobody
  designed. For Fizz, students talking about a post at lunch.
- **Metric proxy:** the share of new signups with **zero attribution to any launch channel** starts
  climbing.

### Saturated
Most of the network is on it, and non-participation now costs something.
- **Signal:** penetration in the 60–90%+ range; **the "completeness incentive" switches on** —
  staying off means missing information your peers have.
- **Fizz's ladder:** ~10% (week 1) → ~75% (~6 months) → ~95% (~1 year).
- **Saturn's ladder:** 30% → 50% → 80% → 90% of daily actives, across roughly one school year.
- **Note both took months to a year.** Nobody in this corpus saturated a network in a day, whatever
  the retellings say.

### Self-propagating — **the state that actually matters**
Growth continues after you remove yourself.
- **The test (Law 5): take the founder, the launch team and their personal contacts out, and see
  whether penetration still rises.**
- **Saturn's is the cleanest instance in the corpus:** the engaged share of the student body kept
  increasing *after Dylan Diamond graduated.* That single fact is why his co-founder joined.
  Graduation runs this ablation study for you every June.
- **Fizz's institutional version:** inbound school requests replaced outbound launches, and the
  manual operation was retired.
- **Metric:** week-over-week growth on a network with zero ops touches for 30 days.

### Dominant
The alternative has become socially awkward.
- **Signal:** the product's name becomes a verb; the previous behavior reads as a small social
  failure. **Venmo is the corpus's only clean example** — asking for cash now carries mild
  embarrassment.
- **[Interpretation]** This is the strongest moat in consumer, and it is a *norm*, not a network
  effect. Norms outlast graphs — which is why Venmo survived a decade of well-funded competitors and
  Zenly's 40M-user graph evaporated the moment its owner switched it off.
- **Leading indicator:** track whether anyone uses your product's name as a verb, unprompted, in
  the wild.

---

## 4. What to measure at each stage

| Stage | The one number | Not this number |
|---|---|---|
| Seeded | Activations (reached first value) | Downloads |
| Warming | Signups with no launch-channel attribution | Total DAU |
| Locally relevant | Organic share of new users | Press mentions |
| Saturated | Penetration of *daily actives*, not registrations | Cumulative installs |
| Self-propagating | WoW growth with **zero ops touches for 30 days** | Anything measured while you're on campus |
| Dominant | Unprompted verb usage | NPS |

**Cross-check every threshold against `knowledge/_synthesis.md`'s metrics cheat-sheet before
quoting it to anyone.**

---

## 5. Choosing the next network

Observed selection criteria, in the order the cases actually used them:

1. **Calendar, when time is the constraint.** tbh chose a Georgia school **because it had the
   earliest start date in the United States** and the company was nearly out of money. An adequate
   network that starts Monday beats a perfect one that starts in six weeks.
2. **Proximity, early.** Fizz's second and third campuses were Pepperdine and Chapman — both
   drivable from Palo Alto. Not prestige; driving distance.
3. **Structural product fit, for geographic expansion.** Zenly's best market was Japan because
   **Japanese addresses are block-based rather than street-sequential**, making "meet me here" hard
   to express in text. The product was mechanically more useful there because of a fact about the
   country. **Look for where a structural feature of daily life makes your product more valuable,
   and expect propagation without spend.**
4. **Inbound demand, once you have it.** Fizz's endgame: tens of thousands of school requests
   replaced outbound launches entirely.
5. **Institutional calendars, for borrowed distribution.** a16z mandating Partiful for all NY Tech
   Week events took it from house parties to 1,000-person conferences in a week. Find who already
   owns a calendar full of your users.

**Do not select networks by multiplying independent success probabilities.** Fizz's founder
estimated per-school odds for a dozen launches, multiplied them, got ~8%, and hit essentially all
of them. Repeating one playbook on structurally identical networks is **one correlated experiment**,
not twelve independent ones. The error is always in the same direction.

---

## 6. Zimo's saturation model

All **[Zimo hypothesis]**.

**Zimo is pair-atomic, so it has no threshold problem — and therefore should not run a
crowd-atomic saturation playbook.** Two roommates alone get the whole product. This is the single
most important strategic implication in this file, because it means the Fizz/tbh campus machine is
*optional* for Zimo, and expensive.

The defensible reason to use a campus anyway is **frequency, not density**: students split costs
more often than any other population. So:

| Standard campus metric | Zimo's replacement |
|---|---|
| % of campus installed | **Splits per group per week** |
| Downloads on launch day | **Groups that completed a real split** |
| DAU/MAU | **Non-user claim conversion rate** |
| Campuses launched | **Networks where activity rose with zero ops touches for 30 days** |

**Proposed state ladder for one campus:**

- **Seeded:** 10+ organizer-led groups have completed one real split. (Not 10% of campus installed.)
- **Warming:** splits appearing from groups with no connection to the launch team.
- **Locally relevant:** someone says "just Zimo me" without being taught the phrase.
- **Saturated:** the majority of a bounded sub-network — a Greek chapter, a dorm floor, a club —
  settles its shared costs through Zimo by default.
- **Self-propagating:** **30 days, zero ops touches, activity still rising.** Do not launch campus
  #2 before campus #1 passes this. This is the discipline that separates Bier's "seeding is a test"
  from the imitators who stalled at 15 schools.
- **Dominant:** asking a friend for cash, or doing the arithmetic in a group chat, feels like the
  worse option.

**And the cross-check that matters most:** because Zimo will get free repetition from co-location,
it must **test the loop off-campus early** — a post-grad friend group, a set of housemates in a
city — to find out whether the amplifier is the product or the campus. If Zimo only saturates where
people live together, the campus is a trap rather than a beachhead (Law 4).
