# Minimum Viable Network / Distribution Network / Saturation Network

**The central question of this playbook:**

> **How do products that work at n=2 exploit dense networks to become culturally dominant?**

Everything else here is in service of that question.

---

## Why this framework exists — a correction

An earlier version of `LAWS.md` Law 1 argued that because Zimo is "pair-atomic," a campus strategy
was largely unnecessary. **That was wrong**, and the error is worth naming precisely because it is
easy to make.

The mistake was collapsing two different claims:

- ❌ *"This product does not need saturation to deliver its first unit of value."* — **True.**
- ❌ *"Therefore local density does not meaningfully improve its distribution."* — **False, and it
  does not follow.**

The correct inference runs the other way. **A product that works at n=2 and also benefits from
density is in a strictly better position than one that requires density**, because it gets the
upside of saturation without being hostage to it. Fizz *must* buy 500 users before anyone gets
value. Zimo does not — but Zimo still wants the campus, because the campus is where its
distribution unit repeats most often and overlaps most densely.

**Pair-atomic makes the Bier/Fizz campus play more attractive, not less.**

---

## The three tiers

Every consumer product has three different network sizes, and conflating them causes most
go-to-market errors.

### 1. Minimum Viable Network (MVN)
**The smallest group at which the product delivers real value.**
Determines: whether you have a cold-start problem at all, and whether an empty product is fatal.

### 2. Distribution Network (DN)
**The unit through which the product naturally propagates — the group that gets exposed by one
ordinary use.**
Determines: your branching factor, and what your loop should be designed around.

### 3. Saturation Network (SN)
**The larger population in which many Distribution Networks overlap, such that adoption becomes
self-reinforcing and eventually feels ambient.**
Determines: where you launch, and what "this is everywhere" looks like.

**The engine is the overlap between DN and SN.** Sarah is in her roommate chat, her sorority chat,
her class chat, her trip chat and her dinner chat. Those are five Distribution Networks sharing one
person. Saturate the campus and Sarah does not encounter the product once — she encounters it in
every context of her life simultaneously. That superposition is what produces the sensation that
*everyone is suddenly using this*, and it is a property of the SN, not of any single DN.

---

## Classification

| Product | Minimum viable | Distribution network | Saturation network | Does it *need* SN? |
|---|---|---|---|---|
| **Fizz** | **Hundreds** — a feed is dead below critical mass | The campus itself | Campus | **Yes — fatal without it** |
| **tbh / Gas** | **Hundreds** — a poll needs a populated school | The school | School → state | **Yes** |
| **Saturn** | **Dozens** — your classmates must be on it | A class / a grade | School | **Yes** |
| **Yik Yak** | **Hundreds** | Geographic radius | Campus | **Yes** |
| **Tinder** | **Small pool, but two-sided** | Greek chapter → paired chapter | Campus → city | **Yes** |
| **Venmo** | **2** | The transaction pair, then the friend group | Friend graph → campus → city → US | **No — but it won because of it** |
| **PayPal** | **2** (buyer + seller) | An eBay listing | eBay's whole marketplace | **No — but eBay made it default** |
| **Cash App** | **2** | The transaction pair | Regional + cultural community | **No — bought culture instead** |
| **Partiful** | **Host + guests** | The guest list | Urban social scene | **No** |
| **Zenly** | **~5 close friends** | The friend group | Country (Japan, Indonesia…) | **No** |
| **Airbuds** | **2–3 friends** | The friend group | School / country | **No** |
| **Snapchat** | **2** | The friend group | High school → teens → everyone | **No — density accelerated it** |
| **Splitwise** | **2** | **The group — but it stops there** | **Never achieved one** | **No — and that's the problem** |
| **Zimo** | **2** | **The group chat** | **Campus → mainstream local graph** | **No — but should pursue it** |

---

## What the table shows

**Reading the "needs SN" column against outcomes is the most useful thing in this playbook.**

**Products that require an SN are expensive and fragile.** Fizz buys every campus with flyers,
donuts, paid ambassadors and paid moderators. tbh/Gas saturated schools brilliantly and died anyway
when the loop ran out of fuel. Yik Yak collapsed. Requiring saturation means you must purchase each
network before you learn anything, and you can never stop.

**Products that don't require an SN but pursue one anyway are the winners.** Venmo, PayPal, Cash App
and Snapchat all worked at n=2 and *still* went after dense networks — Penn and Philadelphia food
trucks, eBay sellers, the Southeast US and hip-hop, Orange County high schools. That combination is
what produced cultural dominance.

**Products that don't require an SN and never pursue one plateau as useful tools.** Splitwise has
**30M+ users across 170+ countries** and is a real business — and it is not a verb, it did not
change a norm, and most of its users would switch for a marginally better product. That is the
anti-case, and it is the one closest to Zimo. See [`UTILITIES.md`](UTILITIES.md).

---

## The hybrid model

Fizz's sequence:

> marketing → **many users** → *then* the product becomes useful

Zimo's available sequence:

> marketing → **first user** → **a real split happens** → **the other participants are exposed** →
> some become users → **they bring their other groups** → repeat

The difference is where value appears. Fizz cannot deliver any value until the crowd arrives, so
every campus is a standing start. Zimo delivers value on transaction one, so the campus operation
is an **accelerant on an engine that already runs** rather than the engine itself.

**Therefore: use Bier/Fizz to ignite, and Venmo/Partiful to propagate without you.**

| Phase | Borrow from | What it does | When to stop |
|---|---|---|---|
| **Ignition** | **Nikita Bier / Fizz** — synchronous saturation, temporal compression, three exposures, one dense network at a time | Manufactures enough simultaneous Distribution Networks that the overlap effect can start | When the escape-velocity test passes (30 days, zero ops touches, activity still rising) |
| **Propagation** | **Venmo / Partiful** — value before signup, no-install recipient path, transaction-as-invitation | Carries the product between and beyond networks with no operator | Never |
| **Durability** | **Antoine Martin / Zenly** — retention before growth, frequency over time-spent, latency budgets, ~5-active-friends thresholds | Ensures ignited networks stay lit | Never |

**Bier is ignition. Antoine Martin is durability. You need both, and neither is the whole answer.**

tbh and Gas are the proof: the best ignition engineer in consumer built two apps that reached #1 in
the US App Store and both were shut down for low usage within a year of acquisition. Ignition
without durability is a spike. Zenly is the mirror image — world-class durability, 40M MAU, and it
took eleven years and an acquirer's balance sheet to get there.

---

## The diagnostic questions

For any product, in order:

1. **What is the MVN?** If it is a crowd, you have a cold-start problem and a mandatory field
   operation. If it is a pair, you do not — and any plan that assumes you do is overspending.
2. **What is the DN, and how often does it fire?** Not how big it is. A guest list of 100 that fires
   twice a year (Partiful) is worth less than a roommate group of 4 that fires weekly.
3. **How many DNs does one person belong to?** This is the overlap coefficient, and it is what makes
   an SN worth pursuing. A student belongs to 5+; a suburban parent belongs to 2.
4. **Do those DNs overlap inside a bounded population?** If yes, you have a real SN and saturation
   will feel like ubiquity. If no, saturation is just a large number of users.
5. **Does the DN survive when the person leaves the SN?** Fizz's does not — `.edu` gating expels
   every user within four years. Venmo's does — your friends move cities with you.

**Question 5 is the wedge-versus-boundary test, and it decides whether your saturation network is a
beachhead or a trap.**

---

## Zimo, tier by tier

**MVN = 2.** Two roommates splitting rent get the complete product. No cold start, no empty state,
no mandatory seeding.

**DN = the group chat.** This is the unit to design every mechanic around. One dinner for 6 exposes
5 non-payers. A roommate group fires monthly on rent and weekly on groceries. **The DN is where the
branching happens, and it is the tier Zimo has under-exploited if the product is currently designed
around individuals or pairs.**

**SN = the campus, then the mainstream local graph.** Justified not by density requirements but by
two things:
- **Frequency** — students split more often than any other population.
- **Overlap** — a student belongs to more simultaneous group chats than anyone else in adult life.
  Roommate, class, club, sorority, intramural, trip, dinner. That overlap coefficient is the highest
  it will ever be in a human's life, and it is exactly what converts many DNs into a felt SN.

**So the campus is worth pursuing — not because Zimo needs it to work, but because a campus is the
densest available concentration of overlapping group chats.** That is a different and much better
argument than the one usually made for campus launches, and it produces different tactics: target
*groups*, not individuals; measure *splits per group per week*, not installs; pick campuses by
group-density (Greek systems, residential colleges, heavy club cultures), not by prestige.

---

## Related

- [`LAWS.md`](LAWS.md) Law 1 — restated in terms of these three tiers
- [`UTILITIES.md`](UTILITIES.md) — what happens when a pair-atomic product never pursues an SN
- [`SATURATION.md`](SATURATION.md) — the six-state ladder for measuring SN progress
- [`ZIMO.md`](ZIMO.md) — the experiments
