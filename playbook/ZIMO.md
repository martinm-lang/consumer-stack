# Zimo translation layer

Every experiment here is a **[Zimo hypothesis]** — a proposal with a historical analogue, not a
finding. Per-case reasoning lives in `cases/`; this file ranks and sequences.

## Zimo as understood (V1)

- **Zimo coordinates money. It is not the payment rail.** The core is an **iMessage agent**:
  recognize that an expense needs splitting, create and coordinate the split, organize participants
  and reminders, then settle through **external rails** — Venmo, Zelle, bank links.
- Long-term vision can go much further into the financial layer. **Do not model V1 as Venmo, where
  every loop requires Zimo to hold or move the funds.**
- **Minimum Viable Network = 2. Distribution Network = the group chat. Saturation Network = campus,
  then the mainstream local graph.** See [`NETWORK_TIERS.md`](NETWORK_TIERS.md).

**Related:** [`ZIMO_METRICS.md`](ZIMO_METRICS.md) (the measurement system) ·
[`PREDECESSORS.md`](PREDECESSORS.md) (Splitwise as the direct predecessor, + interview guide)

**The single most important consequence:** Zimo V1 sits in **Splitwise's structural position** —
coordination without rails. Splitwise has been in that position for fifteen years and reached 30M+
users without ever becoming a verb. [`UTILITIES.md`](UTILITIES.md) is therefore the most important
file in this playbook for Zimo, and the thesis below is built against it.

---

## The three structural facts

### 1. Zimo's loop runs on renewable real-world behavior

Dinner tomorrow → new trigger. Rent next month → new trigger. Trip → new trigger. Groceries → new
trigger. **You do not consume the loop; life regenerates it.** (`LAWS.md` Law 3.)

tbh and Gas both hit #1 in the US App Store and both were shut down within a year, because their
fuel was a finite pool of novel social information in a closed network. Zimo's fuel is inexhaustible.
**Lead the investor narrative with this**, and treat it as a design constraint: anything that moves
Zimo toward *novel social information* and away from *money that actually needs settling* moves it
toward tbh's failure mode.

### 2. Zimo's core action inherently involves a non-user

Of ten Tier A cases, only three deliver real value to a non-user before signup — and two of them
(Venmo, Partiful) are the ones whose core action necessarily reaches someone who is not yet a user.
Zimo has this property by construction, **and it does not depend on owning the rails.**

### 3. Pair-atomic makes the campus play *more* attractive, not less

Zimo works at n=2, so the campus is an **accelerant on an engine that already runs** rather than the
engine itself. A campus is the densest available concentration of **overlapping group chats** — a
student is simultaneously in a roommate chat, a class chat, a club chat, a trip chat and a dinner
chat, and that overlap coefficient is the highest it will ever be in their life. That is a better
argument for campus than the usual density argument, and it produces different tactics.

---

## The hybrid model

| Phase | Borrow from | Purpose | Exit condition |
|---|---|---|---|
| **Ignition** | **Bier / Fizz** — synchronous saturation, temporal compression, three exposures, one dense network at a time | Manufacture enough simultaneous group chats that the overlap effect can start | Escape-velocity test passes: 30 days, zero ops touches, activity still rising |
| **Propagation** | **Venmo / Partiful** — value before signup, no-install recipient path, transaction-as-invitation | Carry Zimo between and beyond networks with no operator | Never |
| **Durability** | **Antoine Martin / Zenly** — retention before growth, frequency over time-spent, latency budgets | Keep ignited networks lit | Never |

**Bier is ignition. Antoine Martin is durability. Use both; canonize neither.** The best ignition
engineer in consumer built two apps that reached #1 and both were shut down for low usage inside a
year.

---

## Tier 1 — do these first

### 1. Own the social coordination layer all the way to the payment action
**Analogue:** [`UTILITIES.md`](UTILITIES.md), [`PREDECESSORS.md`](PREDECESSORS.md)

**Confirmed: Zimo V1 still hands off.** The split is coordinated in Zimo; settlement happens in
Venmo/Zelle/a bank link. The gap is real and partially open.

**The precise formulation — and it is not "add a Venmo integration":**

> **Zimo must own the social coordination layer all the way until the payment action, even if it
> does not own the payment rail.**

This does not require becoming a processor or holding funds. It requires never shipping this:

> ❌ Zimo calculates → the user is left to figure it out inside Venmo

The target flow:

> Dinner detected → Zimo determines who owes what → **Zimo sends and coordinates the request** →
> recipient sees exactly *why* they owe $46 → Pay → **Zimo opens and pre-fills the best available
> rail** → settlement confirmed → **group state updated**

**Zimo stays the interface; the rail becomes almost invisible.**

**Why this is the whole differentiation.** Splitwise solved the arithmetic fifteen years ago. The
arithmetic was never the hard part. The hard part is *asking*, and it is hard because it is social:

- Who is going to ask?
- When?
- How do we not make this awkward?
- Who chases the person who forgot?
- Has everyone actually paid?

**A ledger can write:** *Sarah owes $46.*
**An agent can act:** Sarah still hasn't paid, the group is going out again tonight, she probably
just forgot — so remind her directly, **without Martin having to play debt collector.**

What is being outsourced is not the maths. **It is the awkwardness.** Nobody has ever charged for
that in this category.

### 1b. But do not let "closing the settlement gap" become the whole vision

**If settlement is the entire thesis, you rebuild Venmo** — and Venmo already exists, owns the rails,
and nearly went bankrupt building them.

The defensible territory is the **coordination lifecycle**, of which the payment is one step:

| Phase | What Zimo owns |
|---|---|
| **Before** | Who paid? Who was involved? Should this be split at all? How — evenly, by item, by share? |
| **During** | How much does everyone owe? Which rail? Who has already paid? |
| **After** | Who still owes? Should Zimo remind them, and how? Is this recurring? Does it belong to a standing group/squad? What happens next? |

**[Interpretation]** Every one of those questions is social judgment, not computation — which is
exactly what an agent can do and a ledger cannot, and exactly what neither Splitwise nor Venmo
occupies. Venmo owns the rail and knows nothing about the group. Splitwise owns the ledger and does
nothing about the asking. **The lifecycle in between is unclaimed.**

### 2. The V1 loop is exposure-and-proof, not money-waiting
**Analogue:** Partiful (`cases/partiful.md`); Venmo's *structure*, not its rails

Without owning the rails, the payload cannot be "you have $46 waiting in Zimo." The V1 loop is:

> **Martin split dinner with you — you owe $46. Here's the itemization. Settle in one tap.**

or, for the group-exposure variant:

> **Dinner was split with 5 people — see yours.**

**The value genuinely pre-exists** even without a proprietary rail, and it is worth naming exactly
what the non-user receives, because `LAWS.md` Law 2's test still applies:

| What the non-user possesses before signup | Splitwise | Zimo V1 target |
|---|---|---|
| The amount | ✓ | ✓ |
| **The itemization proving they aren't overcharged** | partial | **✓ — this is the asset** |
| **Who else is in it and who has already paid** | ✗ | **✓ — social proof + pressure** |
| **A one-tap settle through a rail they already use** | ✗ | **✓ — this is the gap Splitwise leaves** |
| **A durable record that protects them** | ✓ | ✓ |

The recipient payload must never be *only* a liability. A notification whose entire content is "you
owe $46" is a Splitwise notification.

### 3. No install for the recipient — ever
**Analogue:** Partiful

A split sent to a non-user opens a **full web view**: what the expense was, the itemization, who
else is in it, who's paid, and a settle action. No download, no account. Partiful's entire growth
rests on this and it is the most copyable mechanic in the playbook. **Take the conversion loss on
purpose** — nagging the recipient degrades the organizer's experience, and the organizer is the one
who churns.

### 4. Instrument the group, not the user — and measure secondary group creation
**Full system: [`ZIMO_METRICS.md`](ZIMO_METRICS.md)**

The primary KPI is **not** "what fraction of a group adopts." It is:

> **How many new groups are created by people who were exposed inside a first group?**

Because that is what produces 1 group → 3 → 8 → 20, and that is where campus saturation begins.

Four rates, in order: **exposure → interaction → activation → propagation**, where propagation means
*initiating a split in a **different** group.* Then the headline number:

$$B = \frac{\text{new groups created by exposed people}}{\text{originating groups}}$$

B > 1 is exponential. B < 1 means every group must be purchased forever — the Fizz position.

**A warning the metric tree surfaces immediately:** an illustrative funnel of
100 splits → 400 exposed → 160 interact → 80 signup → **24 create a split elsewhere** looks healthy
at every individual step, and still yields **B ≈ 0.24–0.6.** Below 1. A funnel can be good at every
stage and still not propagate; the multiplication is where the truth is. Closing that gap needs
~4×, and the three available levers are worked out in `ZIMO_METRICS.md`.

### 5. Photograph the receipt; infer the whole thing
**Analogue:** Saturn (`cases/saturn.md`)

Saturn's user photographs a class schedule and gets a calendar, class group chats and a friend graph
in ~30 seconds — **the document the user already owns contains the network.** Zimo's equivalent:
photograph a receipt → line items, split, group and amounts inferred in one step. No manual entry,
no participant picking. Vision models make this cheap and it is badly under-exploited.

### 6. Seed organizers, not users
**Analogue:** Tinder (`cases/tinder.md`); PayPal's eBay sellers

In every shared-expense event there is one person who fronts the money and chases everyone — the
trip organizer, the lease-holder, the one who books the table, the club treasurer. Scarce,
identifiable, high-effort. **One converted organizer brings the whole group as a byproduct.**

PayPal's version: seed eBay **sellers**, who then required buyers to adopt. The organizer has the
same leverage — they control whether the group settles through Zimo.

Concrete: present at Greek chapter, club and team meetings, ending with the treasurer running **one
real split in the room.**

### 7. Win the $12 dinner, not just the $2,000 trip
**Analogue:** `UTILITIES.md`

High-stakes cases pay the bills; low-stakes cases build the habit. Splitwise owns trips and lost
everyday life, which is why it never became a reflex. **Frequency is the whole game for a
renewable-trigger product** — and it is where the group chat fires most often.

### 8. Set the escape-velocity test before launching campus #1
**Analogue:** Saturn, Fizz, Bier's doctrine (`LAWS.md` Law 5)

Write down in advance: **30 days, zero ops touches, is activity still rising?** Do not launch campus
#2 before campus #1 passes. Every seeded network grows while the seeder is present.

---

## Tier 2

### 9. Audit the iMessage dependency now — this is the Meerkat position
**Analogue:** Meerkat (`cases/meerkat-houseparty.md`), `LAWS.md` Law 9

**Zimo's core is an iMessage agent. iMessage is Apple's.** Meerkat's growth engine was Twitter's
notification system until Twitter shipped Periscope and revoked access on the first day of SXSW.
Rubin's line: *"Twitter did the whole job for us."* **A borrowed channel is indistinguishable from
product-market fit while it is switched on.**

**The architectural principle: iMessage-native, not iMessage-dependent.**

iMessage can be an enormous American wedge — it is exactly why Zimo can own the coordination layer
where Splitwise can't. But **Zimo's intelligence must live elsewhere:**

- the graph
- groups
- ledger / state
- memory
- transaction context
- orchestration
- user identity
- the recommendation engine

Built this way, an Apple API change, policy shift, or aggressive first-party launch costs Zimo **an
interface, not its brain.** That is a completely different failure mode from Meerkat's, which lost
the graph itself.

Name, for each growth input (iMessage extension surface, contact permissions, SMS deliverability,
App Store discovery, external rail APIs), the owner and the plausible competing first-party product.
**Apple Cash and Apple Invites both already exist.**

### 10. Test the loop off-campus, early
**Analogue:** `LAWS.md` Law 4

Zimo will get free repetition from co-location and must not mistake it for a working loop. Run a
small dispersed cohort in parallel with campus #1 — a post-grad friend group, housemates in a city.
**If Zimo only works where people live together, the campus is a trap rather than a beachhead.**

### 11. Decide which currency buys the cold start
**Analogue:** `UTILITIES.md` contrast cases

In money products, distribution is usually **purchased**. The question is with what:

| Currency | Case | Benchmark |
|---|---|---|
| **Dollars** | PayPal | $10 signup + $10 referral = $20 CAC; 7–10% *daily* growth; 1M→5M users in 6 months; ~$60–70M total for 5–6M active transactors |
| **Dollars + scarcity** | Revolut | Waitlist with queue-climbing referrals; ~$50–100 per signup; ~65% organic/referred |
| **Culture** | Cash App | Southeast US unbanked + hip-hop (Travis Scott, Cardi B); *"markets aspiration where Venmo markets belonging"* |
| **Mechanics** | Venmo | Free — and it nearly went bankrupt anyway |

Zimo's cheapest is **mechanics** (no-install recipient path + the agent closing the ask). If those
don't produce propagation, the fallback is dollars — and PayPal's numbers are the benchmark to plan
against, not a rounding error.

### 12. Build the group recap with balances hidden
**Analogue:** Airbuds weekly Wrapped + Venmo's hidden amounts

Venmo's most consequential decision was **deleting the amount**, turning an unpublishable financial
record into a publishable diary. A group's shared *spending* is embarrassing; a group's shared
*experience* is postable. Weekly or per-trip recap — biggest spender, most-split category, the
priciest dinner — as a shareable object with individual balances suppressed. Weekly cadence gives
52 shots a year instead of one.

### 13. Find the jointly-owned streak
**Analogue:** Snapchat

The key is **joint ownership**: a number two people built together that neither can preserve alone.
A personal streak is a chore; a shared one is an obligation to a person. Candidates: a settled-up
streak between roommates, an unbroken monthly household reconciliation, a complete trip ledger.

### 14. Apply the peaky→daily test
**Analogue:** Saturn's schedule-sharing → calendar pivot

Settling up is peaky. Saturn's highest-leverage move was re-housing the same data in a
higher-frequency container — same users, same dataset, no new acquisition. What is Zimo's daily
container? A running household balance, a shared week-to-date view, a couple's spending glance.

### 15. SMS/iMessage, never email
**Analogue:** Partiful

Every Zimo message to a non-user reads like a person, not a service. **But keep Bier's line:**
invites must be visibly user-initiated from the device, never server-side "on behalf of" the user.

---

## Tier 3 — queued

16. **Scannable identity** — one QR at the table adds everyone to the split. *(Snapchat Snapcodes)*
17. **Reuse past groups** — one tap for "same group as the ski trip." *(Partiful guest-list reuse)*
18. **Zero-fee acceptance where groups already divide bills** — late-night food, party tickets,
    ski-trip buses, formals. *(Venmo's food trucks)*
19. **Find Zimo's institutional calendar** — which campus body owns a calendar full of shared-cost
    events? *(a16z mandating Partiful for NY Tech Week)*
20. **Reactions on expenses** — a one-tap emoji on "Sam paid $84 for the Airbnb" makes settling feel
    like a group activity rather than debt collection. *(Airbuds)*
21. **Run McDonald's Wednesdays** — buy a student lunch, film them using Zimo for 15 minutes in the
    dining hall. Antoine Martin's "most important secret," and nearly free. *(Zenly)*
22. **Set a latency budget from the incumbent behavior** — Zimo competes with "I'll Venmo you later"
    and group-chat arithmetic. Zenly's number was 500ms, derived from where users reverted to
    texting. *(Zenly)*
23. **Pick campus #1 by group-density and calendar** — Greek systems, residential colleges, heavy
    club cultures; earliest term start, or the week before formals/ski trips. *(tbh's Georgia school)*
24. **24/7 in-app human chat on campus #1** — Bier's best research vehicle, and for a money product
    it doubles as the trust mechanism. *(tbh)*
25. **Find the policy vacuum** — club treasurers barred from collecting dues through personal
    accounts; international students without a US payment app. *(Snapchat)*
26. **Ship a widget** — "you're owed $47 across 3 groups," glanceable, dozens of impressions a day
    with no app open. *(Airbuds)*

---

## Guardrails

- **Never gate on `.edu`.** Fizz's gate expels 100% of every cohort within four years. Snapchat and
  Tinder aged out of their wedge for free because they never enforced it in code. **Campus for
  density; never for identity.**
- **Never add a solo mode.** A split is inherently mutual, which gives Zimo K≈1 for free
  (`LAWS.md` Law 6). "Let solo users track their own expenses" converts a self-propagating product
  into a personal finance app — and it is the Splitwise road.
- **Never hire content seeders.** Zimo's first user's own action populates the second user's
  experience. If Zimo ever needs seeders, the loop is broken. Treat it as a diagnostic.
- **Never ship a recipient payload that is only a liability.**
- **Watch the accuracy-request ratio.** When users start asking mainly for multi-currency,
  itemization depth and reporting, Zimo is being hired as a ledger and the SN ambition is quietly
  dying. Track accuracy requests vs settlement/social requests as a strategic indicator.
- **Never claim 40%-in-24-hours as a benchmark.** Founder-reported and disputed by a peer. Fizz's
  independently documented **~10% in week one** is the number to plan against.
- **Contacts: delete on revoke, and prove it.** The NY AG cited Saturn for retaining contact books
  after revocation. Given iOS 18's selective contact access, build the graph from the transaction,
  as Venmo does.
- **Disclose paid campus reps in-product.** Both Fizz and Saturn used paid students; the difference
  between an ordinary tactic and an enforcement action was disclosure.
- **Constrain the input.** Money between friends has a cruelty vector — public shaming over unpaid
  debts. Design so the product *cannot* produce a humiliating outcome. No public delinquency, no
  shaming feed.
- **Build the geofence before you need it.** A money product that goes viral without a throttle has
  fraud, support and compliance exposure a social app doesn't.
- **Cost one loop iteration before optimizing the loop.** Less acute for V1 (no rails, so no
  per-transaction cost), but the moment Zimo touches rails, Venmo's near-death becomes the base rate.
  **The V1 rail-free position is a genuine strategic asset — it buys time Venmo never had.**

---

## Open questions

**Answered this round:**
- ~~Does the agent send the ask, or hand off?~~ → **Hands off today.** Closing it is Tier 1 item 1,
  reframed as owning the coordination layer up to the payment action.
- ~~What fraction of a group adopts?~~ → superseded by a better question: **what is B?**
  (`ZIMO_METRICS.md`)

**Still open:**
1. **Is exposure measurable today?** If Zimo can't distinguish *delivered* from *seen*, the entire
   metric tree is uninstrumentable. Fix before anything else.
2. **Is there a campus already running?** The escape-velocity test and B are far more informative
   applied retroactively to a live campus than planned for a future one.
3. **What does a non-user see today?** Determines whether Tier 1 items 2–3 are a tweak or a rebuild.
4. **Did Splitwise ever try automated payment requests, and did users hate them?** The single most
   important unknown negative result in this space. Interview guide in
   [`PREDECESSORS.md`](PREDECESSORS.md).
