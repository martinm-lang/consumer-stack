# Why useful consumer utilities fail to become viral

The anti-case file. **This is the most important file in the playbook for Zimo**, because the
realistic danger is not failing to become Gas. It is succeeding at becoming a slightly better
Splitwise.

> The enemy question is not *"how do we become Gas?"*
> It is ***"how do we avoid becoming a marginally better Splitwise?"***

---

## The central anti-case: Splitwise

**Splitwise is not a failure.** Founded early 2011 by Jonathan Bittner, Marshall Weir and Ryan
Laughlin, after Bittner — then a Harvard grad student — got tired of the social friction of
splitting rent with housemates. Today: **30M+ users across 170+ countries**, $30M+ raised (Series A
led by Insight Partners), 50+ employees, 4.5+ App Store rating, freemium with a Pro tier, 20%
subscription-revenue growth in 2023. [Confirmed / Company-reported]

That is a real business, built on exactly Zimo's problem, with a fifteen-year head start.

**And yet.** Splitwise is not a verb. It did not change a norm. It has never had a cultural moment.
Nobody says "just Splitwise me." Most of its users would switch for a marginally better product
tomorrow. In the vocabulary of [`NETWORK_TIERS.md`](NETWORK_TIERS.md): it has an MVN of 2 and a DN of
the group, and it **never acquired a Saturation Network** — and, more damningly, its DN barely
propagates beyond the group it started in.

Fifteen years, 30M users, no ubiquity. **That is the trajectory to be afraid of.**

### The one-line diagnosis

> **Splitwise owns the ledger. The opening is to own the conversation.**

The problem in this category was never *"who owes what."* Arithmetic is the easy part and it was
solved in 2011. The actual problem is:

- **Who is going to ask?**
- **When?**
- **How do we not make this awkward?**
- **Who chases the person who forgot?**
- **Has everyone actually paid?**

That is **social coordination**, not accounting — and it is why a conversational agent is a
different product category rather than a better ledger.

**A ledger can write:** *Sarah owes $46.*

**An agent can act:** Sarah still hasn't paid; the group is going out again tonight; she probably
just forgot — so remind her directly, in the thread, **without the organizer having to play debt
collector.**

**[Interpretation]** The thing being outsourced is not the maths. **It is the awkwardness.** No
product in this category has ever charged for removing awkwardness, and Splitwise's fifteen-year
plateau is the evidence that a better ledger cannot get there. See
[`PREDECESSORS.md`](PREDECESSORS.md) for the interview that would turn this interpretation into
evidence.

---

## The five structural reasons

### 1. The ledger has no recipient event

> *"Splitwise is a ledger, Venmo is a wallet."*

Splitwise **records** who owes whom and does not transfer money. At settle-up it computes the net
amounts and **links out** to a payment app.

Compare the two recipient experiences:

| | Venmo | Splitwise |
|---|---|---|
| What arrives | **Money. Yours. Already sent.** | **A number saying you owe someone.** |
| Emotional valence | Gift | **Debt** |
| Action required | Claim it | Go do work in another app |
| Reason to hurry | It's yours | None |

**[Interpretation]** This is the whole difference and it is not a UI problem. Venmo's loop
terminates in an *asset*; Splitwise's terminates in a *liability*. A viral loop whose payload is an
obligation runs against human motivation at every turn. The recipient's optimal move is to
procrastinate — which is precisely what happens.

### 2. It stops at the hardest step

The most-cited criticism, and the most useful sentence found in this pass:

> **"The moment between 'calculating what everyone owes' and 'actually getting paid' is where most
> splits die."**

And the mechanic behind it:

> *"You're still doing the actual Venmo request manually — finding the person, entering the amount,
> writing the note. Splitwise doesn't send the request for you."*

**[Interpretation]** Splitwise solves arithmetic, which was never the hard part. The hard part is
**asking**, and it is hard because it is *social*, not computational. Splitwise hands the user back
control at the exact moment the emotional stakes peak, then asks them to re-key the entire
transaction into a second app.

**[Transferable] A utility that offloads its hardest step back onto the user has not removed the
friction — it has relocated it, and taken the credit for the easy half.** The willingness to pay,
the gratitude, and the word of mouth all attach to whoever closes the loop. For Splitwise, that is
Venmo.

### 3. Utilities optimize for accuracy; social products optimize for the moment

Splitwise's stated value is *"clarity over time."* Multi-currency, itemization, receipt scanning,
advanced reporting, running balances.

Every one of those is a **deferred, abstract, individual** benefit. Venmo's note-and-emoji feed is
an **immediate, concrete, social** one. The Pro feature list reveals the theory of value: Splitwise
believes users want a better ledger. **[Interpretation]** Users want to stop feeling weird about
money with their friends. Those are different products, and only one of them gets talked about.

### 4. Symmetric burden, asymmetric value

For a shared ledger to be accurate, **everyone in the group must maintain it.** But a non-adopter
gets nothing from adopting except more bookkeeping. There is no moment where joining hands you
something.

Compare Partiful: the guest gets the complete experience — details, guest list, RSVP — with **no
install and no account**. Compare Venmo: the non-user gets money. Compare Splitwise: the non-user
gets a chore.

**[Transferable] If joining your network is a burden the joiner absorbs on behalf of the group, you
have a coordination tax, not a viral loop.** These products grow only as fast as groups can be
convinced to accept the tax collectively — which is slow, and which is why utilities spread by
persuasion rather than propagation.

### 5. The good-enough alternative is free and already installed

The real competitor is not another app. It is **a group chat plus mental arithmetic plus letting
small amounts slide.** That alternative costs nothing, requires no adoption, and is socially
frictionless for amounts under about $20.

**[Interpretation]** A utility must beat the incumbent behavior *by enough to justify a coordination
event across a whole group.* This is a much higher bar than beating it for one user, and it is why
utilities cluster at the high-stakes end (trips, rent) where the arithmetic genuinely hurts — and
lose the everyday cases, which are the frequent ones. **Losing the frequent cases is how you lose
the habit, and losing the habit is how you stay a tool.**

---

## Tricount, and the European mirror

Tricount (Belgium, later acquired by Belfius) is the same product with the same shape: a shared
expense ledger, strong in trip and holiday contexts, genuinely well-liked, and settlement handed off
to bank transfers. Same MVN, same DN, same absence of an SN, same outcome — a well-used utility that
never became a norm, and that ultimately found its home inside a bank rather than as a consumer
network.

**[Interpretation]** Two independent teams on two continents built the same product and hit the same
ceiling. That is evidence the ceiling is structural, not executional. Nobody out-executed Splitwise
into dominance because the category as designed does not produce dominance.

---

## The contrast cases: what money products did instead

| Product | The thing it did that a ledger cannot |
|---|---|
| **Venmo** | The loop terminates in **money the recipient owns**. And it hid the amount, turning a financial record into a postable social artifact. |
| **PayPal** | **Paid people $10 to join and $10 to refer** — $20 CAC, 7–10% *daily* growth, 1M users (Mar 2000) → 5M (Sep 2000). Thiel: advertising was "too ineffective to justify the cost." ~$60–70M spent, 5–6M active transactors. Then wedged into **eBay sellers**, who forced buyers to adopt. |
| **Cash App** | **Bought culture deliberately.** Targeted younger unbanked/underbanked users in the Southeast US — explicitly *not* the coastal-campus play — and went through hip-hop: Travis Scott, Cardi B, Snoop Dogg, Chance the Rapper. *"Cash App markets aspiration while Venmo markets belonging."* Then cross-sold P2P into a full banking product. |
| **Revolut** | **Waitlists with queue-climbing referrals**, ~$50–100 per successful signup, feature unlocks traded for referrals, ~65% of new customers organic or referred, minimal paid advertising until 2018. |

**[Interpretation]** Three of these four bought their way through the cold start with cash (PayPal,
Revolut) or culture (Cash App). Only Venmo got it free, and Venmo nearly went bankrupt doing it.
**The honest reading: in money products, distribution is usually purchased.** The question is with
what currency — dollars (PayPal, Revolut), cultural placement (Cash App), or product mechanics
(Venmo). Splitwise purchased none of them.

---

## The utility trap — a diagnostic

Score any product. Every "no" is a step toward Splitwise.

1. **Does one ordinary use expose a non-user to something they can act on?**
   Splitwise: a notification about a debt. Venmo: money.
2. **Does the loop terminate in an asset or a liability?**
   Liabilities do not propagate.
3. **Do you close the hardest step, or hand it back?**
   Whoever closes the loop gets the credit, the gratitude and the word of mouth.
4. **Does joining give the joiner something, or give the *group* something at the joiner's expense?**
   The second is a coordination tax.
5. **Does the product produce an artifact anyone would voluntarily show someone?**
   Ledgers produce spreadsheets. Nobody posts a spreadsheet.
6. **Does it win the frequent low-stakes case, or only the rare high-stakes one?**
   Rare high-stakes wins revenue; frequent low-stakes wins the habit.
7. **Is the name usable as a verb?**
   If not, you are competing on features, permanently.

**Splitwise scores 0–1 out of 7. Venmo scores 6–7.** Both solve splitting money between friends.

---

## What Zimo can test

All **[Zimo hypothesis]**. Zimo's V1 **coordinates money without owning the rails — structurally the
same position as Splitwise.** That is the reason this file matters more than any other.

- **[Zimo hypothesis] The thesis must be: close the settlement gap that Splitwise leaves open.**
  Splitwise stops at "here is what you owe" and makes the user re-key the request into Venmo.
  **Zimo's iMessage agent can actually send the request, chase it, and remind — inside the
  conversation where the debt was incurred.** That is not a better ledger; it is a different
  product, and it is the only defensible answer to "why not Splitwise?" Everything else is features.
- **[Zimo hypothesis] Never ship a feature whose recipient payload is only a liability.** If a Zimo
  notification's entire content is "you owe $46," it is a Splitwise notification. Add what the
  recipient *gets*: the itemization proving they are not being overcharged, the one-tap settle, the
  record that protects them, the fact that everyone else has already paid.
- **[Zimo hypothesis] Win the $12 dinner, not just the $2,000 trip.** High-stakes cases pay the
  bills; low-stakes cases build the habit. Splitwise owns trips and lost everyday life — which is
  why it never became a reflex. Measure the median split amount; if it drifts upward, Zimo is
  becoming Splitwise.
- **[Zimo hypothesis] Test "does the group adopt?" not "does the user adopt?"** The coordination tax
  is paid collectively. The unit of conversion is the group chat, and the metric is what fraction of
  a group is active after the first split.
- **[Zimo hypothesis] Decide which currency buys Zimo's cold start.** The four contrast cases each
  bought distribution with dollars, culture or mechanics. Zimo's cheapest is **mechanics** — the
  no-install recipient path plus the agent closing the ask. If those do not produce propagation,
  the fallback is dollars, and PayPal's numbers ($20 CAC, ~$12/active transactor at scale) are the
  benchmark to plan against — not a rounding error.
- **[Zimo hypothesis] Watch the Splitwise tell: feature requests about accuracy.** When users start
  asking for multi-currency, itemization depth and reporting, the product is being hired as a ledger.
  That is the moment the SN ambition quietly dies. Track the ratio of accuracy requests to
  social/settlement requests as a strategic indicator.

---

## Sources

- Splitwise history and scale — Crunchbase; businessmodelcanvastemplate.com company profiles
  (30M+ users, 170+ countries, $30M+ raised, Insight Partners Series A, 50+ employees, Pro tier,
  20% subscription revenue growth 2023). **All company-reported or aggregator-sourced; no primary
  founder interview located this pass** — logged in `RESEARCH_GAPS.md`.
- The ledger-vs-wallet framing and the settlement-gap criticism — comparison analyses at
  splittyapp.com, gettidyflow.com, supasplit.app, splitmyexpenses.com. **These are competitor-run
  content sites and are therefore interested parties**; used only for the mechanical description of
  the handoff, which is uncontested and directly observable in the product.
- PayPal referral economics — Thiel's stated figures via multiple secondary retellings
  (ReferralCandy, GrowSurf, Extole, Aakash Gupta); PayPal S-1/424B1 filings, SEC EDGAR, for the
  corporate record. **The $10/$10 mechanic and 7–10% daily growth are widely repeated and trace to
  Thiel; treat as [Founder-reported].**
- Cash App strategy — Alex Johnson, "Cash App is Culture," Fintech Takes; Rex Woodbury, Digital
  Native; ARK Invest, "Cash App vs. Venmo" white paper; First 1000.
- Revolut referral mechanics — Viral Loops case study; Growthcurve; buyapowa.
- **No case files yet exist for Cash App, PayPal, Revolut, Wise or Tricount.** This file is the
  synthesis; the individual machines are the next research target.
