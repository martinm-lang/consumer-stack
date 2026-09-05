# Laws of Consumer Distribution

Derived from the ten Tier A cases in `cases/`. Each law states a mechanism, names the evidence,
names where it **doesn't** hold, and says how founders misuse it.

A law here earns its place by being supported in **at least two independent cases** and by having a
real counterexample. Anything without a counterexample is probably a slogan, not a law.

**Read the counterexamples first.** They are where the thinking is.

---

## Law 1 — Separate the Minimum Viable Network, the Distribution Network and the Saturation Network. Never let one stand in for another.

> **Corrected.** An earlier version of this law said that because a product works at n=2, a campus
> strategy is largely unnecessary. That was wrong. It collapsed *"does not need saturation to
> deliver first value"* into *"does not benefit from density"* — and the second does not follow from
> the first. Full treatment in [`NETWORK_TIERS.md`](NETWORK_TIERS.md).

**Statement.** Every product has three network sizes, and they are not the same number:

- **Minimum Viable Network** — the smallest group at which the product delivers real value.
  Determines whether you have a cold-start problem.
- **Distribution Network** — the group exposed by one ordinary use. Determines your branching factor.
- **Saturation Network** — the population in which many Distribution Networks overlap. Determines
  where you launch and what ubiquity feels like.

**The correct inference is the opposite of the intuitive one: a product that works at n=2 *and*
benefits from density is in a strictly better position than one that requires density.** It captures
the upside of saturation without being hostage to it. **Pair-atomic makes the campus play more
attractive, not less.**

**Evidence.**
- **MVN = crowd, SN mandatory:** Fizz (a feed is dead below a few hundred users), tbh/Gas (a poll
  needs a populated school), Yik Yak, Saturn. Every one ran an expensive field operation because it
  had no choice. Fizz buys each campus with flyers, donuts, paid ambassadors *and paid moderators
  who seed the content.*
- **MVN = 2, SN pursued anyway — and these are the winners:** Venmo (Penn, `penn-dp` invite codes,
  Philadelphia food trucks), PayPal (eBay sellers, who then forced buyers to adopt), Cash App
  (Southeast US + hip-hop), Snapchat (Orange County high schools). All worked at n=2. All chased
  density. All became culturally dominant.
- **MVN = 2, SN never pursued:** **Splitwise.** 30M+ users, 170+ countries, fifteen years — and not
  a verb, not a norm, no cultural moment. See [`UTILITIES.md`](UTILITIES.md).

**Counterexample / boundary.** Zenly reached 40M MAU with no SN strategy at all, on forced
reciprocity alone (Law 6). Density is an accelerant, not a requirement, for pair-atomic products —
which is exactly why it is a *choice* worth making deliberately rather than a constraint.

**Mechanism.** The engine is the **overlap between DN and SN**. One person belongs to many
Distribution Networks — a student is in a roommate chat, a class chat, a sorority chat, a trip chat
and a dinner chat simultaneously. Saturate the bounded population those groups live in and the
product does not appear once; it appears in every context of that person's life at the same time.
That superposition is what produces *"everyone is suddenly using this."* It is a property of
overlap, not of user count.

**Failure mode.** Three distinct errors, all common:
1. **Crowd-MVN founders expecting organic growth** — every early user opens an empty room and leaves.
2. **Pair-MVN founders copying campus tactics wholesale** — spending a year on ambassadors their
   product never required, and measuring installs instead of transactions.
3. **Pair-MVN founders concluding density is therefore worthless** — the Splitwise path. This is the
   error the earlier version of this law made, and it is the most expensive of the three, because it
   forfeits cultural dominance in exchange for a modest saving on field operations.

**[Zimo implication]** MVN = 2. **DN = the group chat.** SN = campus, then the mainstream local
graph. Zimo should absolutely pursue the campus — not because it needs density to function, but
because **a campus is the densest available concentration of overlapping group chats**, and a
student's overlap coefficient is the highest it will ever be in their life. That is a better
argument for campus than the usual one, and it produces different tactics: target **groups**, not
individuals; measure **splits per group per week**, not installs; select campuses by group-density
(Greek systems, residential colleges, heavy club cultures), not prestige. The hybrid model —
**Bier/Fizz to ignite, Venmo/Partiful to propagate, Zenly to retain** — is set out in
[`NETWORK_TIERS.md`](NETWORK_TIERS.md).

---

## Law 2 — The best invite is not an invite. It is an action that has already created value for a non-user.

**Statement.** Loops that ask a recipient for a favour convert badly. Loops that hand a recipient
something already theirs convert extraordinarily.

**Evidence.**
- **Venmo:** you send money to someone with no account; it sits Pending, *theirs*, until they sign
  up to claim it. The sender is not referring anyone — they are settling a debt. The recipient is
  not being asked for anything — they are being paid.
- **Partiful:** the guest receives a text with a link, opens a full party page in a browser, sees
  who's coming and RSVPs — **with no install and no account.** The value is delivered before any
  conversion is attempted, and the conversion is deliberately not attempted.
- **Airbuds (partial):** the invite gate unlocks something genuinely worthless alone.

**Counterexample.** Zenly and Snapchat both require installation before you can see anything, and
both grew enormously. Reciprocity-forced products (Law 6) and physically dense networks (Law 4) can
compensate for a total absence of value-before-signup.

**Mechanism.** Every invite contains a persuasion step. Value-before-signup deletes the persuasion
step and replaces it with a retrieval step. People will do work to collect something that is
already theirs; they will not do work to evaluate a claim.

**Failure mode.** Dressing an invite as value — "see what Alex shared with you!" behind a signup
wall. The recipient has been shown a locked box, not given a gift, and knows the difference.
The honest test: **what does the non-user possess before they sign up?** If the answer is
"information about something," you have an invite. If it is "a thing," you have a loop.

**[Zimo implication]** A Zimo split *must* reach a non-user by construction — the person who owes
money. This is Venmo's structural gift and Zimo should not waste it. Instrument the claim funnel
(non-user notified → claim started → identifier verified → first outbound action) as **the**
primary growth metric. If a Zimo non-user's pre-signup experience is a link to a locked screen,
that is the single highest-ROI thing to change.

---

## Law 3 — The strongest consumer loops run on renewable real-world behavior.

> **Stock vs flow.** A loop fuelled by a finite pool of novelty exhausts on a schedule you cannot
> change. A loop fuelled by something that keeps happening in the world does not.
>
> Dinner tomorrow → new trigger. Rent next month → new trigger. Trip → new trigger. Uber → new
> trigger. Groceries → new trigger.
> **You do not consume the loop. Life regenerates it.**

**Evidence.**
- **Stock — and it ran out, twice:** tbh and Gas. The fuel was novel social information inside a
  fixed school. There are only so many nice things a group of 1,000 teenagers can tell you about
  yourself. Both apps hit #1 in the US App Store and **both were shut down within about a year of
  acquisition, for low usage.**
- **Flow:** Venmo (dinners and rent recur forever), Saturn (the school bell rings every morning),
  Snapchat (whatever happened today), Airbuds (people listen to music for hours daily).

**Counterexample / boundary.** Partiful is flow-based but the flow is *slow* — parties happen a few
times a year. A flow can be genuine and still be too thin to retain on. Frequency matters
independently of renewability, which is why Partiful is expanding down-stakes into dinners and
movie nights.

**Mechanism.** Retention requires a trigger. A trigger regenerated by the outside world is free and
infinite. A trigger regenerated by the product itself is a depleting resource with a marketing
budget attached.

**Failure mode.** Reading explosive early growth as product-market fit when the growth is novelty
consumption. The curve looks identical for the first few months. The diagnostic question is not
"how fast is it growing" but **"what regenerates the reason to open it, and who controls that?"**

**[Zimo implication]** Zimo's trigger is regenerated by real life forever. **This is Zimo's single
strongest structural property and it should be the first line of the investor narrative.** It also
implies a design constraint: any feature that moves Zimo toward "novel social information" and away
from "money that actually needs settling" moves it toward tbh's failure mode.

---

## Law 4 — In a physically co-located network, utility frequency substitutes for a viral loop.

**Statement.** If your users are in the same building every day, you do not need the product to
carry itself between them. Word of mouth is free and continuous.

**Evidence.** Four of ten Tier A cases spread primarily by people standing next to each other:
**Fizz** (dorms), **Saturn** (a high school), **Snapchat** (Orange County high schools), **Tinder**
(a campus). None of the four has a meaningful product-borne acquisition loop. Fizz literally cannot
have one — anonymity forbids both tagging and taking credit.

**Counterexample.** Venmo and Partiful spread through dispersed populations with no physical
density at all, entirely on product-borne loops. Density is one way to get repetition, not the
only way.

**Mechanism.** Bier's three-exposure rule — people need to see a message ~3 times to install.
On a residential campus the network supplies those exposures for free through conversation. In a
dispersed population you must buy them or build a loop that manufactures them.

**Failure mode.** **The most expensive error in this playbook.** A product saturates a campus, the
founders conclude the loop is strong, they expand to a dispersed population, and growth stops dead —
because the loop was never doing the work. Fizz's "Global Fizz" is this test, live.

**[Zimo implication]** Zimo will get free repetition on a campus and must not mistake it for a
working loop. **Test the loop explicitly off-campus, early, in a small dispersed cohort** (a
post-grad friend group, a set of housemates in a city). If Zimo only works where people are
co-located, the campus wedge is a trap rather than a beachhead.

---

## Law 5 — Escape velocity is what happens after you leave.

**Statement.** Every seeded network grows while the seeder is present. Only a self-propagating one
keeps growing after they are gone. That difference is the only reliable test.

**Evidence.**
- **Saturn:** Max Baron joined because analytics showed the engaged share of the student body **kept
  rising after Dylan Diamond graduated.** Not the level — the derivative after the founder's
  personal network was removed.
- **Fizz:** the manual launch operation was **retired** once inbound school requests replaced
  outbound launches. Solomon: "nowadays we don't even do that operation."
- **Bier, stated as doctrine:** school seeding is how you **test**, not how you **grow**. Imitators
  who ran it as a growth strategy across 15 schools stalled, because after the seed the app must
  grow by itself.

**Counterexample.** Tinder's ops-heavy phase was genuinely necessary and genuinely finite — the
operation was not a failure signal, it was a bridge. The distinction is whether you are still doing
it at network 15.

**Mechanism.** A founder's presence injects social capital that is not part of the product.
Removing it is an ablation study that separates the product's pull from the founder's.

**Failure mode.** Declaring a campus "successful" on penetration while the launch team is still on
it. Every campus looks successful with three people living there.

**[Zimo implication]** Do not declare campus #1 a success on install rate. Declare it a success only
if activity keeps rising in the **30 days after** the launch team and their personal contacts stop
touching it. Write this down before the launch, not after.

---

## Law 6 — Reciprocity-forced products have K≈1 by construction: slow, steady, and very hard to kill.

**Statement.** If the product is useless alone, every user must bring at least one other, so the
loop cannot die — but it also cannot spike.

**Evidence.** **Zenly** (location sharing is only useful mutually) compounded from under 1M MAU to
over 40M in five years with ~70 people, no paid acquisition doctrine, no launch operations.
**Airbuds** (an empty feed shows nothing) and **Venmo** (a payment needs two parties) share the
property.

**Counterexample.** tbh/Gas was *not* reciprocity-forced — you could be voted on passively — which
is part of why it could spike to 30,000 signups an hour and also part of why it could evaporate.
Forced reciprocity trades peak speed for durability.

**Mechanism.** Each new user must recruit at least one other for their own experience to work at
all. The recruitment is self-interested, not altruistic, so it does not need an incentive.

**Failure mode.** Founders remove the reciprocity requirement to reduce onboarding friction —
adding a "browse alone" mode, a solo view, a single-player experience — and unknowingly delete the
mechanism that guaranteed K≈1.

**[Zimo implication]** A split is inherently mutual: both parties need the record. Design so a
one-sided Zimo user gets meaningfully less than a reciprocal pair, and the K≈1 floor is free.
Resist "let solo users track their own expenses" — it is a reasonable-sounding feature that
converts a self-propagating product into a personal finance app.

---

## Law 7 — Hide the number to create the artifact.

**Statement.** Removing one field can convert a private record into publishable social content.

**Evidence.**
- **Venmo, the canonical case.** Kortina: *"We never showed the amounts, because this was not as
  interesting as the social context and the story itself."* This is the most consequential product
  decision in Venmo's history and it is a distribution decision disguised as a privacy one. A feed
  of payments *with* amounts is unpublishable; without them it is a diary of a friend group.
- **Airbuds / Spotify Wrapped:** shares taste, never spend or hours-wasted framing.
- **Partiful:** the invite is designed to be beautiful and screenshot-able; the logistics are not
  the point.

**Counterexample — and it's instructive.** Robinhood made a number *the* artifact: your position in
the waitlist queue. Scarcity ranking is shareable precisely *because* the number is visible and
competitive. So the law is not "hide numbers" — it is **"identify which single field makes the
output unpostable, and remove it."** Sometimes the number is the shame; sometimes it is the status.

**Mechanism.** People share things that flatter them and hide things that expose them. A financial
amount exposes; a social context flatters.

**Failure mode.** Adding "helpful" detail to a shareable artifact until nobody shares it.

**[Zimo implication]** Find Zimo's hidden field. The candidate: render a settled trip or dinner as a
social object — who was there, what it was, a photo — **with the individual balances suppressed.**
A group's shared spending is embarrassing; a group's shared *experience* is postable.

---

## Law 8 — Never put a platform gatekeeper inside your per-network launch loop.

**Statement.** Anything you must ship, submit, review or get approved *per network* caps your
rollout rate at that third party's latency.

**Evidence.**
- **Saturn** built a separate white-labeled app per school and hand-submitted each binary to Apple.
  Diamond: *"That was the timeline to when we would launch a school — but it was not scalable."*
  They merged into one app specifically because they could not launch schools fast enough.
- **Meerkat** put Twitter inside its graph-import step. Twitter revoked access on March 13 2015 —
  day one of SXSW, the same day it announced buying Periscope.

**Counterexample.** Fizz's `.edu` gating is also a per-network dependency (on university email
domains) and it works fine — because universities are not competing with Fizz and cannot
unilaterally revoke it. **The risk is not dependency; it is dependency on a party that might
compete with you.**

**Mechanism.** Rollout throughput is set by the slowest serialized step. A reviewer or an API owner
inside that step is both a rate limit and a kill switch.

**Failure mode.** Confusing the *feeling* of local identity with the *artifact* of a separate build.
Saturn's instinct — an app that feels like it's for your school — was right. Binding it to separate
binaries was the error. Move local identity into the runtime.

**[Zimo implication]** If Zimo ever skins per-campus, do it server-side. More urgently: audit
Zimo's growth inputs — contact permissions, SMS deliverability, iMessage extension surface, App
Store discovery, bank/payment rails — and for each name the owner and the plausible competing
product. Do this now, while it is cheap.

---

## Law 9 — A borrowed distribution channel is indistinguishable from product-market fit while it is switched on.

**Statement.** You cannot tell rented growth from earned growth by looking at the curve. Only by
asking who owns the switch.

**Evidence.** **Meerkat** — Twitter's notification and reactivation system distributed the app to
Twitter's user base for free for a month. Rubin: *"Twitter did the whole job for us."* When Twitter
shipped Periscope, the same machinery went dark in a day and engagement collapsed.
**Airbuds** sits in this position today, entirely on top of Spotify and Apple Music APIs.

**Counterexample.** Fizz borrowed distribution too — approaching existing campus meme pages at
Seattle University — and suffered nothing, because meme pages are not going to launch a competitor.
Borrowing from parties with no strategic interest in your category is safe.

**Mechanism.** Platforms optimize their own retention. Your app is a feature of their ecosystem
until it is a competitor in it, and the transition is not announced in advance.

**Failure mode.** Building the entire acquisition model on a channel you don't own, then treating
the resulting numbers as validation when raising money.

**[Zimo implication]** Zimo's natural home is the group chat — which is Apple's and Meta's
territory. Being *inside* iMessage is the Meerkat position exactly. The defensible design is a
product that works *better* with the group chat but does not *require* it.

---

## Law 10 — Hunt for policy vacuums.

**Statement.** A population whose default tool has been blocked, banned or deprecated by an
institution — not out-competed — is the cheapest cold start available.

**Evidence.** **Snapchat's** first users were Orange County high-schoolers with school-issued iPads
**on which Facebook was blocked.** A device, an urgent social need, and the incumbent removed by
someone else. Snapchat never had to displace Facebook among these students; it was simply the thing
that worked. **Fizz's** version was softer but real: a 1,200-person Stanford class GroupMe in which
nobody spoke, during a year when campus itself was closed.

**Counterexample.** Venmo faced no vacuum at all — it competed against cash, checks and inertia,
which are not blocked by anyone, and it took three years in beta to work. Vacuums accelerate; their
absence is not disqualifying.

**Mechanism.** The demand is pre-qualified and captive, and the switching cost is zero because
there is nothing to switch from.

**Failure mode.** Waiting for a vacuum instead of looking for one. They are findable: school device
policies, workplace IT restrictions, regional bans, app-store removals, API shutdowns, and
institutions that forbid a tool without providing an alternative.

**[Zimo implication]** Look for campus contexts where the default money tool is unavailable or
forbidden: club treasurers barred from collecting dues through personal accounts, international
students who cannot get a US payment app, organizations whose bylaws prohibit a personal Venmo for
group funds. These are small, unglamorous, and pre-qualified.

---

## Law 11 — Sequence the sides of a two-sided market, and make side B's first session contain the proof.

**Statement.** Never acquire both sides at once. Seed the constrained side, then sell its verified
presence to the other side — where "sell" means "let them open the app and recognize people."

**Evidence.** **Tinder.** Whitney Wolfe presented to sorority chapters and had every woman in the
room install; then she went to the paired fraternity, where the men opened the app and **saw
specific women they already knew.** Under 5,000 users before the trip, ~15,000 after.

**Counterexample.** Partiful never sequences anything, because the host arrives carrying both sides
of the transaction. When one actor can supply the whole network, sequencing is unnecessary.

**Mechanism.** The second side's real objection is "is anyone I want on this?" — a question no
marketing answers and every empty product fails. Pre-seeding converts an unanswerable pitch into a
ten-second demonstration.

**Failure mode.** Pitching side B on features. Also: seeding side A with users who are not
*recognizable* to side B — density without adjacency is useless. Wolfe's chapters worked because
each sorority had a *paired* fraternity.

**[Zimo implication]** Zimo's constrained side is the **payer-organizer** — the person who fronts
the money and chases everyone: the trip organizer, the lease-holder, the one who books the table.
That role is scarce, identifiable, and high-effort. **Seed organizers, not users.** One converted
organizer brings the group as a byproduct, exactly as one chapter brought a fraternity.

---

## Law 12 — An acquisition transfers the definition of success.

**Statement.** After an acquisition, whether your product continues to exist depends on its value on
someone else's P&L, not on its performance.

**Evidence — this is the strongest-supported law here, at 4 of 10 Tier A cases.**
- **Zenly:** 40M+ MAU, 10th most downloaded social app in the world, downloads at ~1/3 of Snap's own
  volume — **shut down**, because its growth was in markets Snap could not monetize and selling it
  would have created a competitor.
- **Houseparty:** acquired by Epic 2019, **shut down 2021.**
- **tbh:** acquired by Facebook for ~$100M on day 73, **shut down 8 months later.**
- **Gas:** acquired by Discord, **shut down 10 months later.**

**Counterexample — and it matters.** **Venmo's acquisition saved it.** Venmo sold for $26.2M while
roughly two weeks from bankruptcy; every impressive number in its history came afterwards, under an
owner with payment infrastructure and a balance sheet. Acquisition is not inherently a death
sentence; it is a transfer of the criteria.

**Mechanism.** An acquirer evaluates your users against its own monetization model and its own
competitive map. Engaged users who cannot be monetized on that model are a cost. A growing product
that could become a rival is a threat whether or not it is performing.

**Failure mode.** Treating an acquisition as validation of the product. Bier sold both tbh and Gas
close to their peaks; reading tbh's ~$100M as proof the product was durable is a misread, and
reading it as excellent timing is correct.

**[Zimo implication]** Ask early what Zimo's users are worth on a *potential acquirer's* P&L, not
Zimo's. A money-movement product monetizes everywhere, which is a genuine structural advantage over
Zenly's position. But note the harder half of the lesson: Venmo's loop was world-class and it still
nearly died, because the loop cost money per turn and earned none. **Cost one loop iteration before
optimizing the loop.**

---

## Laws considered and rejected in this pass

Honest record of hypotheses from the brief that the evidence did **not** support:

- **"Density beats reach."** Too vague to be a law and partly circular. The useful version is Law 1
  (atomic network size) plus Law 4 (co-location substitutes for a loop).
- **"Consumer launches benefit from temporal compression."** Well supported for crowd-atomic
  products (Fizz's 6 a.m. drop, tbh's synchronous school saturation) and **irrelevant** for
  pair-atomic ones (Venmo, Partiful, Zenly launched nothing). It is a corollary of Law 1, not a law.
- **"Owned distribution compounds."** Not established by these ten cases. Fizz *borrowed* meme
  pages rather than building owned media; tbh's per-school Instagram accounts were disposable
  targeting tools, not compounding assets. Needs the second-wave research (Musical.ly, BeReal,
  Locket) before it can be stated. Logged in `RESEARCH_GAPS.md`.
- **"Local identity increases adoption."** True in spirit (Saturn's iStaples) but the case teaches
  the *opposite* operational lesson — see Law 8. Folded in there rather than stated separately.
