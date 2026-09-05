# Direct predecessors & failed-to-expand analogues

A category this playbook was missing.

> **The most valuable company to study is not always the one that won.
> Sometimes it is the company that spent fifteen years on your exact problem and never became the
> product you are trying to build.**

Nikita Bier and Antoine Martin teach you how ignition and durability work *in general*. A direct
predecessor teaches you what happens **to your specific problem** when it is attacked with the
obvious solution, by competent people, for a decade. That is a far more targeted signal, and almost
nobody studies it, because predecessors are unglamorous and their founders are not on podcasts.

## Why this category is different from a failure case

| | Failure case | Direct predecessor |
|---|---|---|
| Example | Clubhouse, Meerkat, Gas | Splitwise, Last.fm, Evite |
| What happened | Grew explosively, then collapsed | Never collapsed — **plateaued** |
| What it teaches | How growth dies | **Where the ceiling of your category is** |
| Founder availability | Often talks openly post-mortem | Still operating; rarely interviewed |
| Danger it represents | You flame out | **You succeed modestly and never notice** |

The second danger is worse, because it does not feel like failure while it is happening.

---

## The pairs

| Your product | Direct predecessor | Years spent on the problem | Where it plateaued |
|---|---|---|---|
| **Zimo** | **Splitwise** | 2011– (15 yrs) | 30M+ users, never a verb, settlement handed to Venmo |
| Zimo (EU mirror) | **Tricount** | 2010s– | Well-liked utility; ended up inside a bank (Belfius) |
| Airbuds | **Last.fm** | 2002– | Owned social music for two decades; never became a network teens lived in |
| Partiful | **Evite / Paperless Post** | 1998– | Email-native, aesthetically corporate, invisible to Gen Z |
| Fizz | **Yik Yak** | 2013–2017 | Anonymous campus feed; collapsed on moderation |
| Zenly | **Google Latitude / Find My Friends** | 2009– | Platform-owned, utility-framed, no emotional layer |
| Tinder | **Hot or Not / OkCupid** | 2000s | Desktop-era matching; never solved density per campus |

**[Interpretation]** Every one of these predecessors was *correct about the problem*. None was wrong
about what users needed. They plateaued on **how the product related the users to each other**, not
on whether the need existed. That is the pattern: the predecessor validates your market and shows
you the exact wall.

---

## Case #1 — Splitwise

**The most important company in this playbook for Zimo**, and the one most likely to be skipped
because it is neither a rocket nor a wreck.

Full analysis in [`UTILITIES.md`](UTILITIES.md). The compressed version:

> **Splitwise owns the ledger. Zimo should own the conversation.**

The problem was never *"who owes what."* Arithmetic is the easy part, and Splitwise solved it
fifteen years ago. The problem is:

- **Who is going to ask?**
- **When?**
- **How do we not make this awkward?**
- **Who chases the person who forgot?**
- **Has everyone actually paid?**

That is **social coordination**, not accounting. And it explains why a conversational agent is
potentially differentiating in a way a better ledger never could be.

**A ledger can write:**
> *Sarah owes $46.*

**An agent can act:**
> Sarah still hasn't paid. The group is going out again tonight. She probably just forgot — so remind
> her directly, in the thread, **without Martin having to play debt collector.**

**[Interpretation]** That is not a feature difference. It is a different product category. The
ledger's output is *information*; the agent's output is *a social action performed on someone's
behalf that they were reluctant to perform themselves.* The thing being outsourced is not the maths —
it is the awkwardness. **Nobody has ever charged for removing awkwardness in this category, and that
is the actual opening.**

---

## The Splitwise interview guide

The single highest-value hour available. Frame it as a **fifteen-year post-mortem of user
behavior**, not as competitive research — Bittner, Weir and Laughlin have watched shared-expense
behavior at a scale nobody else has.

**Where the funnel breaks**
1. Where do users drop off after a split is calculated?
2. What percentage of balances actually get settled?
3. Did you ever try sending payment requests automatically? What happened?

**The social layer**
4. Did users dislike automated reminders?
5. What makes debt collection socially awkward?

**Which groups are real**
6. What types of groups retain best — roommates, couples, trips, dinners?
7. Why do some groups use Splitwise for years while others stop after one trip?

**What was tried and failed**
8. Did you ever try making the product more social or conversational?
9. What growth loops did you test that failed?
10. Why do you think Splitwise never became synonymous with paying friends the way Venmo did?

**Forward-looking**
11. If you rebuilt Splitwise today with AI agents, what would you do differently?
12. What is the biggest misconception founders have about shared expenses?

**Why these questions and not others.** Q1–3 locate the wall. Q4–5 test whether the awkwardness
thesis is real or a founder's fantasy — **if Splitwise tried automated reminders and users hated
them, that is the single most important negative result available to Zimo, and it is currently
unknown.** Q6–7 would replace guesswork about which Distribution Networks actually retain
(`NETWORK_TIERS.md`). Q9 is a free list of dead ends. Q10 is the whole playbook in one question.

**[Interpretation]** Answers to Q1, Q2 and Q3 could plausibly save months of iteration, and Q3 in
particular could invalidate or confirm Zimo's core thesis in a single sentence. Everything in
`UTILITIES.md` about why utilities plateau is currently **[Interpretation]**; this interview would
convert it into evidence.

---

## How to use this category generally

For any product, ask:

1. **Who has spent the longest on this exact problem without becoming dominant?** Not the biggest
   competitor — the most *persistent* one.
2. **What is their ceiling, in numbers?** Splitwise's is 30M users and no verb status.
3. **What did they try that failed?** This is the cheapest possible experiment list, and it is
   usually obtainable by asking.
4. **What structural thing about their product shape caused the ceiling?** For Splitwise: the loop
   terminates in a liability, and the hardest step is handed back to the user.
5. **Is your difference structural or cosmetic?** A better-designed ledger is cosmetic. Owning the
   conversation is structural. **If you cannot name the structural difference in one sentence, you
   are building a marginally better predecessor.**

**[Transferable] Interview your predecessor before you interview your heroes.** The heroes will tell
you what worked in a different market ten years ago. The predecessor will tell you what fails in
yours.

---

## Research status

- **Splitwise** — synthesized in `UTILITIES.md` from secondary and competitor-run sources. **No
  primary founder interview located.** Interview guide above. Highest-priority target.
- **Tricount** — barely researched; treated as corroboration that the ceiling is structural.
- **Last.fm, Evite/Paperless Post, Google Latitude, Yik Yak, Hot or Not** — named here as pairs, not
  yet researched. **Yik Yak** is the highest-value of these for the campus question and is already
  queued in `RESEARCH_GAPS.md`.
