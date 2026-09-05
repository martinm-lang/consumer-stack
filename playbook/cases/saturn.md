# Saturn

> **Era:** 2015–2025 | **Wedge:** one high school's class schedule | **Atomic network:** a single high school
> **Status:** **acquired by Snap Inc., June 2025** (~30 employees). $68M raised. NY AG settlement, March 2025.
> **Sources:** 3 founder interview transcripts (high yield), NY Attorney General settlement + Assurance of Discontinuance (primary legal), Forbes, TechCrunch, Built In NYC, Entrepreneur.

## TL;DR

A high-school junior built a schedule-sharing tool for his own school, noticed it was only used at semester boundaries, and converted it into a **daily-use calendar** by reusing the schedule database he already had. That single move — peaky utility → daily utility — took penetration at his school from ~30% to ~90% of students **and kept climbing after he graduated**, which is the cleanest escape-velocity signal in the corpus.

They then made the mistake worth studying: they built **a separate white-labeled app per school**, hand-submitted each build to Apple, and waited for review. Launch throughput was gated by App Store approval. They merged everything into one app — Saturn — specifically because they could not launch schools fast enough.

The ending matters as much as the growth. In March 2025 the New York Attorney General found that Saturn had **switched off school verification for more than 4,000 high schools**, replaced it with a check that a user appeared in three people's contact books, ran **undisclosed paid student promoters**, and copied users' contact books and kept them after permission was revoked. $650,000 settlement. Snap acquired the company three months later.

**Saturn is the case where you can read the growth tactic and the enforcement action side by side.** Almost every mechanic the AG cited was a growth mechanic.

## The machine

> a school website that didn't work on a phone (wedge) → one high school (atomic network) → founder builds for himself, classmates look over his shoulder (cold start) → per-school white-label apps, then one app (distribution) → **weak loop; the real engine is utility + local completeness** → daily calendar + friend status (retention) → 30%→50%→80%→90% of one school (saturation) → *growth continued after the founder left* (escape velocity) → 18,000 schools (expansion) → Snap

## Timeline

| Date | Event |
|---|---|
| ~2015 | Dylan Diamond, a junior at **Staples High School, Westport CT**, builds an app to check grades because the school portal didn't work on phones. Built for himself. [Confirmed] |
| ~2015–16 | Classmates see it over his shoulder and ask for it. Kids at other schools ask. It becomes **#1 grossing in the App Store Education category**. [Founder-reported] |
| ~2016 | Schedule-sharing web app + calendar merge into **"iStaples"** — a single-school app. |
| ~junior year | Penetration at Staples climbs 30% → 50% → 80% → 90% of all students using daily, **entirely word of mouth**. [Founder-reported] |
| — | Max Baron (Wharton) joins after seeing Google Analytics showing a step-function DAU increase **and continued growth after Diamond graduated**. |
| — | Per-school white-label apps; manual builds submitted to Apple per school. |
| — | Apps merged into one product: **Saturn**, after the Roman god of time. |
| Aug 2021 | **$44M** round — Benioff, Bezos Expeditions, von Tobel. [Confirmed — Forbes] |
| 2021–2023 | School email verification made optional; **verification disabled for 4,000+ high schools**. [Confirmed — NY AG] |
| Aug 2023 | Begins screening users by birth date — not before. [Confirmed — NY AG] |
| 2023–24 | Viral school-year growth; parent and school warnings; security upgrades announced. |
| ~2023 | GPT-4-based schedule import: photograph a paper schedule → calendar built. 30-second onboarding. |
| Mar 2025 | **NY AG settlement: $650,000** ($200K immediate, $450K suspended). [Confirmed] |
| Jun 2025 | **Snap Inc. acquires Saturn**; ~30-person team joins. [Confirmed — TechCrunch] |

Total raised: **$68M** — General Catalyst, Insight Partners, Coatue, Bezos Expeditions, Benioff. [Confirmed]

## Initial conditions

**The wedge was an institutional failure, not a social need.** The school's own website did not render on a phone. Diamond built a grades checker for himself. This is the purest form of "solve your own problem," and the acquisition mechanism was physical proximity:

> "I was using it just as a tool for myself. People over the shoulder would see it, they asked for the product." [4g3Evxq3SM0]

**Why a high school is an extraordinary atomic network:**
- Every member is in the same building, on the same bell schedule, every weekday.
- The schedule is a **shared object** — my calendar is only interesting because it intersects yours.
- Complexity creates the moat: US high-school schedules (rotating blocks, A/B days, drop periods) are genuinely hard, and no general calendar handles them. Diamond is explicit that "there is no calendar period that works for high school students today" and that building the schedule infrastructure took **four years** [CYVghIQvlp4].
- Total annual cohort turnover, which is both the churn problem and a permanent supply of new demand.

**The pre-existing distorted behavior** — Bier's latent-demand test again:

> "You remember posting your schedule on Facebook and being able to like and comment if you have classes with people." [4g3Evxq3SM0]

Students were manually posting schedule screenshots to Facebook to find out who they'd share classes with. The motivation was social; the process was absurd.

## The single most important product decision

**Schedule sharing was peaky. Calendars are daily.**

Diamond's own account of the pivot is the highest-value paragraph in the Saturn corpus:

> "That started as a schedule sharing, so it was used in the peaks of the semester… I took that schedule sharing product, I had the graph and the database of everyone's schedule, and made it a calendar so it could be used on a daily basis." [4g3Evxq3SM0]

The schedule-sharing app was used twice a year — at registration and at semester change. Same data, same users, same school; re-presented as a daily calendar, it became a habit.

**[Interpretation]** This is the general move: **he did not acquire new users or build a new network — he re-housed an existing dataset in a higher-frequency container.** The graph and the data were already paid for. Frequency was purely a packaging decision. Compare Partiful, whose retention ceiling is set by how often people throw parties and which *cannot* make this move because it does not own a daily dataset. Saturn could, and did, and that is the whole difference between the two retention profiles.

**"Come for the utility, stay for the social"** is how Diamond states the resulting architecture [CYVghIQvlp4]. Utility (my schedule) is the daily trigger; social (where my friends are, who's in my class, status) is the retention.

## First users and saturation

The Staples curve, from the founder:

> "It spread from around 30% to 50% to 80 to 90% of all the students using the product every day, even after I left — and it was all word of mouth." [4g3Evxq3SM0]

Two things in that sentence are worth separating.

**1. The penetration ladder: 30 → 50 → 80 → 90%, daily actives, one school.** Not downloads — daily use. This is a far more demanding number than Fizz's download-based 95%.

**2. The escape-velocity signal, which is the most useful idea in this file.** Max Baron's stated reason for joining was not the level of usage but its *derivative after the founder left*: Google Analytics showed a step-function rise in DAU relative to enrollment, and **the engaged percentage of the student body continued to increase after Diamond graduated.**

**[Transferable] The cleanest test of whether a local network is self-propagating: remove the founder and the people they personally know, and see whether penetration still rises.** Every seeded network grows while the seeder is present. Only a self-propagating one grows after they're gone. At a high school this experiment runs automatically every June — graduation is a built-in ablation study. Most products have to construct the equivalent deliberately.

## The white-label mistake

Before Saturn was one app, it was **many apps — one per school**, each separately branded:

> "Submitting manual builds to Apple and hoping that they would get approved in a fast turnaround, and that was the timeline to when we would launch a school. But it was not scalable." [CYVghIQvlp4]

Diamond and Baron were manually entering schedule data and shipping per-school binaries. **Launch throughput was rate-limited by App Store review.** They merged into one app "because we had all this demand and we couldn't launch the schools fast enough."

**[Interpretation]** The instinct was right and the implementation was fatal. Local identity genuinely drives adoption — an app called *iStaples* with your school's colors is unambiguously *for you* in a way a generic calendar is not. But binding local identity to *separate distribution artifacts* puts a third party (Apple) inside your launch loop. **The fix is not to abandon local identity; it is to move it from the binary into the runtime** — one app that skins itself per school. Saturn kept the feeling and dropped the artifact:

> "It still needed to feel the same experience that it did at Staples High School to the 17,000th school that launches in the Midwest." [CYVghIQvlp4]

**[Transferable] Never put a platform gatekeeper inside your per-network launch loop.** Anything you must ship, review, or approve per network caps your rollout rate at that gatekeeper's latency.

## Onboarding

The time-to-value work is exemplary and worth copying directly:

> "You just take a picture of your schedule and with GPT-4 it automatically extracts that and builds your calendar… the onboarding flow is 30 seconds. You take your paper high school schedule or a screenshot of your school portal, and automatically you're in class chats, your friends are connected, and your calendar [is built]." [CYVghIQvlp4]

One photograph produces three things at once: a calendar, class group chats, and a friend graph. **[Interpretation]** This is Bier's "know every available API and use it in a non-traditional way" applied to a vision model. The user does not enter data, choose friends, or join chats — a single photo infers all three, because a class schedule is simultaneously a time structure *and* a social graph. The document the user already owns contains the network.

## Viral loop

**Saturn's loop is weak, and it is honest to say so.** Written out:

> Student A uses Saturn → A's calendar is only interesting if friends are on it → A tells friends in person → they install

There is no artifact sent to a non-user, no claim state, no value-before-signup. What Saturn has instead:

- **Physical word of mouth in a building where everyone sees everyone daily.** Extremely high-frequency exposure at zero cost — the same free repetition Fizz got.
- **Completeness pressure.** Once ~80% of a school is on it, the remaining 20% are missing the actual coordination layer of their day.
- **Contact-book-based friend suggestion** — which is where the growth engineering strayed into what the AG later cited.

**[Interpretation]** Saturn is the third Tier A case (with Fizz and, partly, BeReal) whose real engine is *local density plus daily utility*, not virality. The pattern is consistent enough to state as a rule: **in a physically co-located network, utility frequency substitutes for a viral loop.** You do not need the product to carry itself between people if the people are already in the same hallway five days a week. This does not generalize to dispersed populations — which is exactly why Saturn's product is high school and not adulthood.

## Retention

Diamond's stated numbers, all [Founder-reported]:

| Metric | Value |
|---|---|
| DAU/MAU (percent of monthlies active daily) | **>50%** |
| D30 retention, brand-new users | **>30%** |
| D30 retention, existing users | **~70%** |
| New users returning the following school year | **90%** |
| Staples penetration, daily actives | 30% → 50% → 80% → 90% |
| Schools | ~18,000 |
| US high schools using Saturn | "over 80%" [Company-reported] |

DAU/MAU over 50% is genuinely elite — it is in the range Antoine Martin and Alex Zhu describe for top-tier social products. **[Interpretation]** It is also structurally easier for a calendar than for a feed: the school day supplies the trigger. Do not read Saturn's DAU/MAU as evidence that the *social* layer is exceptional; read it as evidence that anchoring to an involuntary daily routine is exceptional.

Retention mechanics beyond the calendar:
- **Status** — where your friends are *in time*; pin and favourite specific people. Diamond notes this did not exist at launch and emerged from observed behavior [CYVghIQvlp4].
- **Profile and calendar viewing throughout the school day** — the dominant unexpected behavior. Students were browsing each other's schedules, which is a social feed made of timetables.
- **Class group chats**, auto-created from the schedule import.

## Expansion

- **Geographic/institutional:** school by school, ~18,000 schools; claimed >80% of US high schools have some presence. **Note the ambiguity in that claim** — "uses Saturn" almost certainly means "has at least one user," not "is saturated." A single student at a school makes it a school. [Company-reported, and the definition is doing heavy lifting.]
- **Demographic:** the stated ambition is to follow users up: *"the high school market is… the first touch point with the user and we want to build a relationship with them for the rest of their lives"* [4g3Evxq3SM0]. This is the Facebook path — own a cohort at maximum density and age with it.
- **Monetization:** advertising, including "the first new ad unit in years."
- **Terminal:** acquired by Snap, June 2025.

## What stopped working — and the enforcement action

This section is the reason to read this file.

On **March 2025** the New York Attorney General announced a settlement with Saturn Technologies. The findings, from the primary settlement document:

| Finding | Detail |
|---|---|
| **Safety claim was false** | Saturn claimed the app "only allowed users from the same high school to interact with each other." It did not. |
| **Verification made optional, silently** | In 2021 school-email verification became optional **without notifying users or updating the safety promises**. |
| **Verification disabled at scale** | Turned off user verification for **more than 4,000 high schools** between 2021 and 2023. |
| **Replacement checks were unproven** | Users admitted on the basis of appearing in **three contacts' phone books**, or being friended by **a single existing user**. |
| **No age screening** | Did not screen users by birth date until **August 2023**. |
| **Contact-book harvesting** | Made unauthorized copies of users' contact books and **retained them after users revoked permission**. |
| **Undisclosed paid promoters** | **Compensated student promoters without disclosure.** |
| **Records** | Insufficient privacy and verification recordkeeping. |
| **Penalty** | **$650,000** — $200,000 immediate, $450,000 suspended pending compliance. |
| **Remediation** | Notify users of verification changes; enhanced privacy controls for under-18s; six-monthly privacy-setting prompts for minors; ban on unsubstantiated safety claims; **delete retained contact books**; hide minors' personal information pending informed consent. |

Exposed data included names, photos, biographies, social links, **and school schedules — i.e. a minor's physical location, hour by hour, for the whole week.**

### Reading this as a growth document

Nearly every cited failure is a growth mechanic:

- **Disabling verification for 4,000 schools removes the launch bottleneck.** A `.edu`-style gate is friction; friction suppresses signups; switching it off makes every school instantly launchable. It also removes the thing that made the network safe and made the marketing claim true.
- **"Appears in three contacts' phone books" is a graph-inference growth hack** — an elegant substitute for verification, and worthless as a safety control, because an adult can be in three teenagers' phones.
- **Retaining contact books after permission is revoked** is exactly what Bier calls out as legally radioactive: *"never act on user data in the background — egregiously illegal, and it burns users"* (`knowledge/nikita-bier.md`).
- **Undisclosed paid student promoters** is the Fizz ambassador model without the disclosure. Compare: Fizz's ambassadors handed out donuts openly; the AG's objection here is to compensation that was hidden.

**[Transferable] The gate is the product.** For any age-gated or institution-gated network, the verification boundary is not overhead — it is the thing being sold. Weakening it to accelerate rollout does not trade safety for growth at the margin; it removes the asset. Saturn shipped a safety promise it had quietly stopped keeping, and the gap between the promise and the code is what the settlement is about.

**[Interpretation]** Note the sequence: settlement March 2025, acquisition June 2025. Snap bought a company with a fresh regulatory consent agreement over minors' data — which is either a bet that the remediation is complete, or a sign the price reflected it. No source found addresses this; logged in `RESEARCH_GAPS.md`.

## Ethical & safety considerations

- **Location disclosure by schedule.** A high-school timetable is a precise weekly location log for a minor. Combined with a broken school gate, that is the specific harm the AG acted on.
- **Contact-book retention after revocation.** Permission revocation must actually delete.
- **Undisclosed compensation of student promoters.** Pay ambassadors, disclose it. Both Saturn and Fizz used paid students; the difference between an ordinary growth tactic and an enforcement finding was disclosure.
- **Parent and school warnings** preceded the AG action — schools were publicly warning families before regulators moved. **[Interpretation]** In a school-distributed product, the institution you routed around during launch becomes your loudest critic later. Fizz's "go through the students, not the administration" is correct for launch and creates exactly this liability at scale.

## Transferable principles

1. **[Transferable] Re-house peaky data in a daily container.** Same users, same dataset, higher frequency. Saturn's schedule-sharing → calendar move is the highest-leverage retention change in the corpus and cost no new acquisition.
2. **[Transferable] Escape velocity = growth continues after you leave.** Penetration rising once the founder and their personal network are gone is the only reliable proof a network is self-propagating.
3. **[Transferable] Never put a platform gatekeeper inside your per-network launch loop.** Per-school binaries capped rollout at App Store review latency.
4. **[Transferable] Keep local identity, drop local artifacts.** Skin one app per network at runtime; the feeling of "this is my school's app" is worth keeping, the separate build is not.
5. **[Transferable] Find the document that already contains the network.** A class schedule is a calendar, a group chat roster and a friend graph at once. One photo, three primitives, thirty seconds.
6. **[Transferable] Come for the utility, stay for the social** — and be honest about which half is the daily trigger.
7. **[Transferable] In a physically co-located network, utility frequency substitutes for a viral loop.** Do not conclude your loop is strong because a high school adopted you.
8. **[Transferable] The gate is the asset, not the friction.** Weakening verification to speed rollout destroys the thing you are selling — and, if you claimed otherwise, creates legal exposure.
9. **[Transferable] Pay ambassadors if you like; disclose it always.**

## What Zimo can test

All **[Zimo hypothesis]**.

- **[Zimo hypothesis] Find Zimo's schedule — the document that already contains the group.** Saturn inferred a whole network from one photo of a timetable. Zimo's equivalent candidates: a lease with roommates on it, a split screenshot from another app, a group chat, a trip itinerary, a restaurant receipt. **Test: photograph a receipt → the split, the group, and the amounts are inferred in one step.** No manual entry, no participant picking.
- **[Zimo hypothesis] Apply the peaky→daily test to Zimo itself.** Settling up is peaky (end of trip, end of month). Ask what daily container the same data could live in — a running balance across a household, a shared spending view for a couple, a "what did we spend this week" glance. Saturn's entire retention advantage over Partiful comes from having made this move.
- **[Zimo hypothesis] Run the founder-removal test on the first campus.** Do not declare a campus successful on penetration. Declare it successful only if penetration keeps rising in the month after the launch team and their personal contacts stop touching it.
- **[Zimo hypothesis] Local identity in the runtime, never in the build.** If Zimo skins itself per campus, do it server-side. Never ship a per-campus binary.
- **[Zimo hypothesis] Treat verification as product, not friction.** If Zimo gates anything (campus, age, institution), decide up front that the gate will never be weakened for growth — and never claim a guarantee the code does not enforce. Saturn's $650K settlement is the price list for getting this wrong with minors.
- **[Zimo hypothesis] Contact permissions: delete on revoke, and say so.** Given Bier's warning that iOS 18 selective contact access has already broken contact-sync-dependent growth, Zimo should not build a growth plan that needs the full contact book at all — and should be able to prove deletion.
- **[Zimo hypothesis] Disclose paid campus promoters in-product.** Both campus-native comparables were cited or criticized for exactly this. A visible "campus rep" badge costs almost nothing and removes the entire category of risk.

## Sources

**Primary (transcripts, `ingest/transcripts/`):**
- `CYVghIQvlp4` — Dylan Diamond, ARK Invest, "Breaking Down Classroom Walls" (44:58) — iStaples origin, per-school white-label apps and the App Store bottleneck, the Saturn merge, GPT-4 onboarding, come-for-utility-stay-for-social, status feature
- `4g3Evxq3SM0` — Dylan Diamond, Sourcery with Molly O'Shea (39:33) — the grades app, the schedule-sharing→calendar pivot, the 30→50→80→90% ladder, growth continuing post-graduation, retention metrics, high school as first touchpoint
- `_zjfnwghcJ8` — The Room Podcast, Summit 2024 consumer-platform panel incl. Saturn (45:15)

**Primary (legal):**
- New York State Attorney General, *Attorney General James Announces Settlement with App Developer for Failing to Protect Young Users' Privacy*, March 2025 — https://ag.ny.gov/press-release/2025/attorney-general-james-announces-settlement-app-developer-failing-protect-young
- *State of New York v. Saturn Technologies — Assurance of Discontinuance*, 2025 — https://ag.ny.gov/sites/default/files/settlements-agreements/state-of-new-york-v-saturn-technologies-assurance-of-discontinuance-2025.pdf

**Secondary:**
- Sternlicht, A., "Social Calendar Platform Saturn Raises $44 Million From Benioff, Bezos And Von Tobel," Forbes, Aug 10 2021
- "Meet Saturn, a New Social Calendar App Backed By Bezos, Benioff and Others," Built In NYC
- "Snap Inc acquires social calendar app Saturn to deepen Gen Z engagement," June 2025 (per TechCrunch)
- Entrepreneur, "This Former Tesla Employee Started a Side Hustle to Save Gen Z Time"
- ABC 33/40, parent and school warnings about Saturn; Shape The Sky app guide
