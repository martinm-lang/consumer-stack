# Zimo metric tree

**The primary KPI is not "what fraction of a group adopts."**
It is:

> **How many new groups are created by people who were exposed inside a first group?**

Because that is what produces **1 group → 3 groups → 8 groups → 20 groups**, and that is where campus
saturation actually begins ([`NETWORK_TIERS.md`](NETWORK_TIERS.md)).

Group adoption tells you the product is useful. **Secondary group creation tells you it propagates.**

---

## The four rates

A Zimo user creates a split with 5 people who are not yet users. Measure, in order:

| # | Rate | Definition | Denominator |
|---|---|---|---|
| 1 | **Exposure** | How many of the 5 actually *see* the split | non-user participants |
| 2 | **Interaction** | How many open it / act on it | exposed |
| 3 | **Activation** | How many become Zimo users | interacted |
| 4 | **Propagation** | Of those who activate, how many **initiate their own split in a different group** | activated |

Rate 4 is the one that turns a useful tool into a loop. Rates 1–3 are diagnostics for *why* rate 4
is what it is.

**Instrumentation notes**
- **Exposure ≠ delivery.** A message sent is not a message seen. If Zimo can't distinguish these,
  rate 1 is unmeasurable and every downstream rate is contaminated. Fix this first.
- **"A different group" is load-bearing in rate 4.** Someone settling a second dinner with the *same*
  five people has not propagated — they have retained. Both matter; they are different numbers, and
  conflating them is the most likely way this tree gets read wrong.
- **Rate 3 must not require an install.** If activation is gated behind a download, you are measuring
  your install friction, not your product's pull (`LAWS.md` Law 2).

---

## The headline number: group branching factor

$$B = \frac{\text{new groups created by exposed people}}{\text{originating groups}}$$

| B | Meaning | Consequence |
|---|---|---|
| **B > 1** | Each group produces more than one new group | **Exponential. You stop buying networks.** |
| **B = 1** | Steady state | Linear growth; ops cost never goes away |
| **B < 1** | Each group produces less than one | **Decay. Every group must be purchased, forever — the Fizz position.** |

**This is a group-level K-factor, and it is the right unit for Zimo** because the coordination tax is
paid collectively (`UTILITIES.md`). A per-user K-factor will look healthier than reality and will
mislead you.

---

## The worked example — and what it actually says

Taking the illustrative funnel:

```
100 splits
 → 400 non-users exposed        (4 per split)
 → 160 interact                  40% of exposed
 →  80 sign up                   50% of interactors  |  20% of exposed
 →  24 create a split elsewhere  30% of activated    |   6% of exposed
```

Those rates look healthy. **They are, individually.** 40% interaction and 50% activation would be
strong numbers for almost any consumer product.

**But run the branching factor.** If those 100 splits came from 100 distinct originating groups:

$$B = \frac{24}{100} = 0.24$$

Even if the 100 splits came from only 40 groups, **B ≈ 0.6.** Still below 1. Still decay. **Zimo
would still have to buy every campus, forever.**

**[Interpretation]** This is the value of the tree: a funnel that looks good at every individual step
can still not propagate, and you cannot see it from the step-level numbers. The multiplication is
where the truth is.

### What B = 1 requires

With ~4 non-users exposed per split, reaching B = 1 needs roughly **25% of exposed non-users to go on
and start a split in a new group.** The example gives 6%. That is a **~4× gap**, and there are only
three places to close it:

| Lever | From → to | Difficulty | Where the corpus says to look |
|---|---|---|---|
| **Exposure per split** (4 → 8+) | Bigger groups | **Easiest** | Target *group chats*, not pairs. Partiful's fan-out is 1 host → 100 guests |
| **Interaction × activation** (20% → 40% of exposed) | Better recipient path | Moderate | No-install web view; itemization; who's already paid (`LAWS.md` Law 2) |
| **Propagation** (30% → 60% of activated) | **The hard one** | **Hardest and most valuable** | This is entirely about whether a new user has a *second group* where splitting is a live problem |

**[Interpretation]** The third lever is where campus selection actually pays off. A student belongs to
five or more simultaneous group chats; a suburban adult belongs to two. **The overlap coefficient
is the propagation rate's ceiling.** That is the real, non-hand-wavy argument for launching on
campus — not density, not vibes: *propagation rate is bounded by how many other groups your new user
is already in.*

---

## The reporting dashboard

Five numbers, weekly. Nothing else on the front page.

| Metric | Why it's here |
|---|---|
| **B — group branching factor** | The only number that says whether Zimo propagates |
| **Splits per group per week** | Frequency; the renewable-trigger check (`LAWS.md` Law 3) |
| **Non-user → settled conversion** | The settlement gap, quantified |
| **Median split amount** | **Drift upward = becoming Splitwise** (winning trips, losing dinners) |
| **Groups active with zero ops touches, 30d** | The escape-velocity test (`LAWS.md` Law 5) |

### Two warning indicators, tracked separately

- **Accuracy-request ratio** — the share of user requests about multi-currency, itemization depth and
  reporting versus settlement and social features. Rising = Zimo is being hired as a ledger, and the
  saturation ambition is quietly dying (`UTILITIES.md`).
- **Second-group latency** — median time between a user activating and creating a split in a
  *different* group. If this is long or infinite, propagation is structurally blocked no matter what
  the funnel says.

---

## What this replaces

| Don't report | Report instead |
|---|---|
| Downloads | Groups that completed a real split |
| DAU / MAU | Splits per group per week |
| Total users | **B** |
| % of campus installed | Secondary groups created per originating group |
| Total volume | Median split amount (watching for drift) |
| Signups | Non-user → settled conversion |

**Rationale:** every metric in the left column is one Splitwise could have reported healthily for
fifteen years while never becoming a verb.

---

## Campus launch, restated in these terms

A campus is worth launching on **if and only if it raises B**, and the mechanism by which it does so
is the overlap coefficient — students belong to more simultaneous group chats than any other
population.

So the campus success criteria become:

- **Seeded:** 10+ organizer-led groups completed one real split
- **Warming:** splits appearing in groups with no connection to the launch team
- **Propagating:** **B > 1 measured within the campus**
- **Self-propagating:** B > 1 sustained for 30 days with zero ops touches
- **Do not launch campus #2 until campus #1 holds B > 1 unattended.**

**[Interpretation]** This is a much harder bar than "10% installed," and it is the right one. Fizz
could hit 95% penetration with B ≈ 0 because it bought every campus. Zimo's whole thesis is that it
does not have to.

---

*All metrics here are **[Zimo hypothesis]** — a proposed measurement system, not observed data. The
worked example uses the illustrative funnel provided, not measured values.*
