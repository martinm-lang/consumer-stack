# Viral Loop Library

Every loop documented in `cases/`, written out mechanically. Ranked roughly by strength.

**The one test that separates the top of this list from the bottom:**
**what does the non-user possess before they sign up?**
"Money" beats "a party they're going to" beats "information about a friend" beats "nothing."

---

## 1. Venmo — the payment claim

| Field | |
|---|---|
| **Name** | Payment claim / money-waiting |
| **Company** | Venmo |
| **Trigger** | A real debt between two people. Occurs naturally; the product never prompts it. |
| **Sender** | Someone settling up — **not** referring |
| **Receiver** | A specific person, by phone number or email |
| **Receiver value before signup** | **Money. Theirs. Already sent.** Payment sits in a Pending state; sender is already charged. |
| **Signup requirement** | Yes — sign up and verify the identifier the money was sent to, in order to claim |
| **Friction** | Verification only |
| **Incentive** | Cash, intrinsic to the transaction |
| **Intrinsic vs extrinsic** | **Fully intrinsic** — the loop *is* the product |
| **Online/offline** | Online, triggered by offline events |
| **Speed** | Minutes to hours |
| **Network type** | Pair, expanding to friend group |
| **Why it worked** | It never asks the recipient for a favour. There is no persuasion step — only a retrieval step. |
| **Risks** | Payments to mistyped identifiers are claimable by whoever controls them; loop costs money per turn and earns none |
| **Replicability 2026** | **High.** Unchanged and still the strongest pattern available. |
| **Zimo adaptation** | Direct. A split *must* reach a non-user by construction. Instrument the claim funnel as the primary growth metric. |

---

## 2. Partiful — the no-install guest page

| Field | |
|---|---|
| **Name** | Event invite / no-install guest path |
| **Company** | Partiful |
| **Trigger** | A real event that would exist without the product |
| **Sender** | The host, motivated by their own party succeeding |
| **Receiver** | Every guest, individually, **by SMS — deliberately never email** |
| **Receiver value before signup** | **Complete.** Party details, guest list, RSVP — all in a browser, no app, no account |
| **Signup requirement** | **None to be a guest.** Only to host. |
| **Friction** | Approximately zero — tap a link |
| **Incentive** | Intrinsic — it's your friend's party |
| **Speed** | Hours |
| **Fan-out** | **1 host → tens or hundreds of guests.** Highest branching factor in the library. |
| **Why it worked** | They take the guest-conversion loss on purpose. Nagging a guest degrades the host's event, and the host is the one who churns. |
| **Risks** | Guest→host conversion is a power law; most guests never host. 5M new users vs 500K MAU. |
| **Replicability 2026** | **High**, and under-copied. Most competitors still gate the guest list behind an account. |
| **Zimo adaptation** | **Non-negotiable.** A split sent to a non-user must open a full web view — what it was, what they owe, who else is in it, how to settle — with no download. |

---

## 3. Tinder — the pre-seeded opposite side

| Field | |
|---|---|
| **Name** | Two-sided sequencing / supernode seeding |
| **Company** | Tinder |
| **Trigger** | Offline: a sorority chapter meeting |
| **Sender** | A campus operator (Whitney Wolfe), not a user |
| **Receiver** | The paired fraternity, in a room, together |
| **Receiver value before signup** | **Verifiable inventory** — they open the app and see specific women they already know |
| **Friction** | Install, at a meeting where everyone else is installing |
| **Incentive** | Intrinsic and immediate |
| **Intrinsic vs extrinsic** | Product intrinsic; **distribution is purely operational** |
| **Online/offline** | **Offline → online** |
| **Speed** | One meeting |
| **Result** | <5,000 users → ~15,000 [Company-reported] |
| **Why it worked** | Converted the unanswerable pitch ("is anyone good on this?") into a ten-second demonstration |
| **Risks** | Requires paired institutions; ops capability lived in one person who left and built a competitor |
| **Replicability 2026** | **Medium-high on campus** — Greek chapters, clubs, teams still meet. Low elsewhere. |
| **Zimo adaptation** | Run it literally at chapter/club/team meetings, ending with the treasurer executing one real split. Seed **organizers**, not users. |

---

## 4. Airbuds — the honest invite gate

| Field | |
|---|---|
| **Name** | Invite-gated feature unlock |
| **Company** | Airbuds |
| **Trigger** | Weekly Recap generation |
| **Sender** | A user who wants to see past their top 3 artists |
| **Receiver** | Friends |
| **Receiver value before signup** | Low — must install |
| **Incentive** | **Extrinsic (unlock) layered on intrinsic (the feature needs friends to mean anything)** |
| **Is the gate honest?** | **Yes.** A comparative music recap is genuinely worthless alone. Poupardin: *"the app only really works if you add your friends."* |
| **Speed** | Weekly cadence |
| **Why it worked** | Gates a feature that cannot exist without friends, rather than taxing one that could |
| **Risks** | Gates that start honest drift extractive as growth targets rise |
| **Replicability 2026** | **High** — but only if the gated feature passes the honesty test |
| **Zimo adaptation** | Gate only genuinely multiplayer features (group balance, trip ledger, household comparison). **Never** gate something a solo user could use, like history or export. |

**The test, stated generally:** if the gated feature would work fine for a solo user, your gate is a
tax and users will resent it. If it would not, the gate is honest.

---

## 5. Airbuds / Spotify Wrapped — the recap artifact

| Field | |
|---|---|
| **Name** | Periodic recap artifact |
| **Company** | Airbuds (weekly); Spotify Wrapped (annual) is the ancestor |
| **Trigger** | Scheduled — every week |
| **Sender** | The user, posting to Stories/TikTok voluntarily |
| **Receiver** | The sender's whole audience, including non-users |
| **Receiver value** | Entertainment + curiosity about their own version |
| **Why it worked** | The artifact flatters the poster. People distribute things that say something good about them. |
| **Key innovation** | **Weekly instead of annual — 52 distribution events a year instead of 1** |
| **Risks** | Novelty decay. Whether weekly sustains its share rate over a year is **unmeasured** — the key open question about Airbuds. |
| **Zimo adaptation** | A weekly or per-trip group recap — biggest spender, most-split category, priciest dinner — **with individual balances hidden** (see Loop 6). |

---

## 6. Venmo — the amount-less feed

| Field | |
|---|---|
| **Name** | Social feed with the number removed |
| **Company** | Venmo (`#p` from 2009; in-app feed shipped **June 2012**) |
| **Trigger** | Any payment with a note |
| **Receiver** | Friends of both parties |
| **Mechanism** | **Amounts never shown.** Kortina: *"this was not as interesting as the social context and the story itself."* |
| **Why it worked** | Deleting one field converts an unpublishable financial record into a publishable diary of a friend group |
| **Risks** | Public-by-default relationship data; a decade of privacy walk-backs |
| **Important correction** | The feed is routinely credited with growth **that predates it by three years.** It shipped 3 months after public launch and 2 months before the company sold. |
| **Zimo adaptation** | Find Zimo's hidden field. Render the *experience* (trip, dinner, house) socially; suppress the balances. |

---

## 7. tbh / Gas — the curiosity notification

| Field | |
|---|---|
| **Name** | Poll-result curiosity loop |
| **Company** | tbh, Gas |
| **Trigger** | Someone votes for you in a poll |
| **Receiver value before signup** | High and purely emotional — someone said something nice about you |
| **Friction** | Low, but the poll only exists if your school is on the app |
| **Intrinsic?** | Yes |
| **Speed** | Minutes. Peak: **30,000 new users per hour** (Gas, Oct 2022) |
| **Why it worked** | Flattery plus curiosity plus a withheld name |
| **Why it died** | **Stock, not flow** (LAWS Law 3). Finite novelty in a closed school network; no new content supply, no accumulating asset, no external utility, no outside world. |
| **Outcome** | tbh shut down ~8 months post-acquisition; Gas ~10 months. |
| **Replicability 2026** | The loop still works; **the durability problem is structural and unfixed.** |
| **Zimo adaptation** | **Cautionary only.** Any Zimo feature drifting toward "novel social information" inherits this failure mode. |

---

## 8. Snapchat — the addressed ephemeral message

| Field | |
|---|---|
| **Name** | Messaging loop |
| **Company** | Snapchat |
| **Trigger** | Receiving a snap addressed to you |
| **Receiver value before signup** | Moderate — a friend sent *you* something specific and it expires |
| **Reciprocity** | Conversational; socially near-mandatory between teens |
| **Speed** | Seconds |
| **Why it worked** | Strongest possible **retention** loop; ephemerality removes the cost of posting |
| **Limitation** | **Weakest possible acquisition loop** — circulates intensely inside a group, reaches nobody outside it. Snapchat's outward spread was physical word of mouth. |
| **Later additions** | Stories (broadcast, so there's something to open with no incoming message); Snapcodes (scannable identity, eliminating username exchange); Streaks |
| **Zimo adaptation** | Scannable identity: one QR at the table adds everyone to the split. Highest-leverage taps-to-value fix for an in-person group. |

---

## 9. Snapchat — streaks (a retention loop worth listing here)

| Field | |
|---|---|
| **Name** | Jointly-owned streak |
| **Mechanism** | Two people build a number **neither can preserve alone**; either can destroy it |
| **Why it's strong** | Investment phase + mutual sunk cost + loss aversion, simultaneously. The strongest single retention mechanic in the corpus; Duolingo copied its logic. |
| **Key distinction** | **Joint ownership.** A personal streak is a chore. A shared one is an obligation to a person. |
| **Zimo adaptation** | What does a Zimo *pair or group* build together that neither can maintain alone? A settled-up streak between roommates; an unbroken monthly household reconciliation; a complete trip ledger. **Not a personal badge — a shared one.** |

---

## 10. Zenly — forced reciprocity

| Field | |
|---|---|
| **Name** | Mutual-visibility requirement |
| **Company** | Zenly (also Airbuds) |
| **Receiver value before signup** | **None** — you must install to see anything |
| **Mechanism** | Location sharing is only useful mutually, so every user must bring at least one other |
| **Effect** | **K≈1 by construction.** Slow, steady, extremely hard to kill: <1M → 40M+ MAU in five years, ~70 people, no paid acquisition. |
| **Real distribution mechanism** | **High-frequency public use.** Opening it repeatedly in front of people is the channel — the phone screen is the billboard. |
| **Trade-off** | Durability bought with peak speed. Cannot spike the way tbh did. |
| **Zimo adaptation** | Make a one-sided Zimo user get meaningfully less than a reciprocal pair. Resist adding a solo expense-tracking mode — it deletes the mechanism. |

---

## 11. Fizz — the operational "loop" that isn't one

| Field | |
|---|---|
| **Name** | *(no product-borne loop)* |
| **Company** | Fizz |
| **Written out** | A posts anonymously → B reads it **inside the app** → B was already a user → **nothing leaves the network** |
| **Why there's no loop** | Anonymity forbids the two things that carry social products outward: **you cannot tag anyone and you cannot take credit.** A Fizz post cannot be screenshotted into a group chat as *yours*. |
| **What spreads it instead** | Physical word of mouth; paid ambassadors; flyers; donuts; paid moderators who also seed content |
| **Consequence** | Growth is operationally expensive — Fizz *buys* each network. A loop-borne product is *given* the next one by the last. |
| **What it has instead** | **Completeness pressure**: at 95% penetration, non-participation costs you information. This is utility lock-in, and it only switches on *after* saturation — which is why the first 10% must be bought. |
| **Zimo lesson** | If Zimo ever needs to hire content seeders, the loop is broken. Treat that as a diagnostic. |

---

## 12. Meerkat — the borrowed loop

| Field | |
|---|---|
| **Name** | Rented platform graph + rented notifications |
| **Company** | Meerkat |
| **Mechanism** | Twitter auto-connected new Meerkat users to people they already followed, pushed notifications about friends' streams, and included Meerkat activity in reactivation emails |
| **In the founder's words** | *"For the first month Twitter did the whole job for us in distributing Meerkat to their user base."* |
| **Why it worked** | It solved the hardest problem in social — a populated night one — with an API call |
| **How it ended** | **March 13, 2015.** Twitter announced the Periscope acquisition and revoked social-graph access **the same day**, day one of SXSW. Engagement collapsed. |
| **Replicability 2026** | **Lower and more dangerous.** APIs are more locked down and every platform has a competing first-party product. |
| **Zimo lesson** | A borrowed channel is indistinguishable from PMF while it's on. Audit every growth input for who owns the switch. |

---

## 13. Saturn — inference as onboarding

| Field | |
|---|---|
| **Name** | Document-inferred network |
| **Company** | Saturn |
| **Mechanism** | Photograph a paper class schedule or school-portal screenshot → GPT-4 extracts it → **calendar, class group chats and friend graph are all built at once.** ~30 seconds. |
| **Why it matters** | The user enters no data, picks no friends and joins no chats. A class schedule is simultaneously a time structure *and* a social graph — **the document the user already owns contains the network.** |
| **Replicability 2026** | **Higher than ever.** Vision models make this cheap and it is badly under-exploited. |
| **Zimo adaptation** | **The highest-value single experiment in this library for Zimo.** Photograph a receipt → the split, the group and the amounts are inferred in one step. No manual entry, no participant picking. |

---

## Loops named in the brief but not yet researched

From the second wave, not covered in this pass — see `RESEARCH_GAPS.md`:
Dropbox storage referral · BeReal synchronized notification · Locket widget invite ·
TikTok/Musical.ly watermark · Instagram cross-post · Robinhood waitlist ranking ·
Facebook school gating · Yik Yak hyperlocal feed · Clubhouse invite scarcity ·
Poparazzi contact-graph reconstruction
