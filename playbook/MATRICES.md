# Cross-company matrices

Ten Tier A cases, compared. Sources per claim are in the individual `cases/` files.

---

## 0. Network-tier matrix

The framework in [`NETWORK_TIERS.md`](NETWORK_TIERS.md). **The right-hand column is the one to read
against outcomes.**

| Product | Minimum viable | Distribution network | Saturation network | Requires SN? | Outcome |
|---|---|---|---|---|---|
| **Fizz** | Hundreds | The campus | Campus | **Yes — fatal without** | Live, ops-heavy |
| **tbh / Gas** | Hundreds | The school | School → state | **Yes** | Both dead |
| **Saturn** | Dozens | A class / grade | School | **Yes** | Acquired |
| **Tinder** | Small, two-sided | Greek chapter → paired chapter | Campus → city | **Yes** | Live |
| **Venmo** | **2** | Transaction pair → friend group | Friend graph → campus → city | No — **pursued anyway** | Dominant |
| **PayPal** | **2** | An eBay listing | eBay marketplace | No — **pursued anyway** | Dominant |
| **Cash App** | **2** | Transaction pair | Region + cultural community | No — **bought culture** | Dominant |
| **Snapchat** | **2** | Friend group | High school → teens → all | No — **density accelerated** | Dominant |
| **Partiful** | Host + guests | The guest list | Urban social scene | No | Live |
| **Zenly** | **~5** | Friend group | Country | No | Closed by Snap |
| **Airbuds** | **2–3** | Friend group | School / country | No | Live |
| **Splitwise** | **2** | The group — **and it stops there** | **Never acquired one** | No — **and that's the problem** | 30M users, not a verb |
| **Zimo** | **2** | **The group chat** | **Campus → mainstream local graph** | No — **should pursue** | — |

**The pattern:** products that *require* an SN are expensive and fragile. Products that don't
require one but chase it anyway became culturally dominant. Products that don't require one and
never chase it plateau as useful tools — see [`UTILITIES.md`](UTILITIES.md).

---

## 1. Saturation matrix

| Company | Atomic network | Initial geography | Launch compression | Time to critical mass | Primary loop | Retention loop |
|---|---|---|---|---|---|---|
| **Fizz** | One campus (`.edu`-gated), hundreds of users | Stanford dorms | **Extreme** — 6 a.m. flyer drop, one morning, ~20 recruited friends | **~10% in week 1; ~95% took ~1 year** | *None product-borne* — paid ops + word of mouth | Anonymous local gossip; later marketplace |
| **tbh / Gas** | One high school | One Georgia school (**picked for earliest US start date**) | **Extreme** — synchronous school saturation | 40% of school in 24h [Founder-reported, contested] | Poll-result curiosity notification | *Failed* — stock exhausted; dead in ~12 months |
| **Saturn** | One high school | Staples HS, Westport CT | None — organic, founder built for himself | 30%→50%→80%→90% over ~1 school year | *Weak* — utility + co-location | **Daily calendar** + friend status |
| **Tinder** | One campus's dating pool | USC Greek system | High — download-to-enter parties, chapter meetings | <5K→15K on one trip | *Weak outward* — mutual match is inward | Chat + new matches |
| **Snapchat** | High-school friend group | Orange County high schools | **None** — a cousin showed classmates | 3K users in 2 months → 1M DAU in ~18 months | Addressed ephemeral message | **Streaks + Stories** |
| **Venmo** | **A pair** | Penn / Philadelphia | **None** — 3 years in beta | ~3 years to public launch | **Payment claim** | Real-world events (rent, dinners) |
| **Partiful** | **One guest list** | NYC | None | ~2 yrs building through COVID | **No-install guest page** | *Weak* — events are rare; expanding down-stakes |
| **Zenly** | **~5 close friends** | France → "the East" | None — growth ignored ~2 yrs by doctrine | ~6 yrs to 1M; 40M+ by yr 11 | **Forced reciprocity** (K≈1) | Frequency: opens/day, ~20s sessions |
| **Airbuds** | Friend group | US high school + college | None — one TikTok | ~3 yrs to 5M MAU | **Invite-gated unlock** + weekly recap artifact | Ambient widget + reactions |
| **Meerkat** | **Twitter's follower graph (rented)** | Twitter, then SXSW | High — SXSW moment | Weeks | **Borrowed** — Twitter's notifications | *Never established* |

**The pattern to read off this table:** launch compression is **extreme** exactly where the atomic
network is a crowd (Fizz, tbh/Gas) and **absent** exactly where it is a pair or small group (Venmo,
Partiful, Zenly, Airbuds). That is Law 1, visible as a column.

---

## 2. Viral loop matrix

| Company | Action | Non-user exposed? | **Value before signup?** | Signup required to get value? | Intrinsic? | Speed |
|---|---|---|---|---|---|---|
| **Venmo** | Pay someone | **Yes, directly** | **Yes — money, theirs** | Yes, to claim | Fully | Minutes |
| **Partiful** | Create an event | **Yes, by SMS** | **Yes — the complete guest experience** | **No** | Fully | Hours |
| **Airbuds** | Unlock recap | Yes, invited | No | Yes | Mixed (honest gate) | Weekly |
| **Airbuds/Wrapped** | Post recap | **Yes, broadly** | Entertainment only | Yes | Extrinsic-ish | Weekly |
| **tbh / Gas** | Vote in a poll | Within school only | Yes — emotional | Yes | Fully | Minutes |
| **Snapchat** | Send a snap | Weakly | Moderate — addressed to you | Yes | Fully | Seconds |
| **Zenly** | Share location | No | **No** | Yes | Fully (reciprocity-forced) | — |
| **Tinder** | Swipe | **No** | No | Yes | Inward only | — |
| **Fizz** | Post anonymously | **No — structurally impossible** | No | Yes | **No loop** | — |
| **Saturn** | Use calendar | No | No | Yes | **No loop** | — |
| **Meerkat** | Stream to Twitter | Yes — **via Twitter's system, not Meerkat's** | Yes, the stream | Yes | **Borrowed** | Minutes |

**Only three of ten deliver real value to a non-user before signup: Venmo, Partiful, and (weakly)
Snapchat.** Two of those three are the two products in this set whose core action inherently
involves someone who isn't a user yet. Zimo's core action has the same property.

---

## 3. Campus / school matrix

| Company | School strategy | Ambassadors | Offline | Owned media | Product loop | Expansion |
|---|---|---|---|---|---|---|
| **Fizz** | `.edu`-gated, one campus at a time; **never through the administration** | **Yes, paid.** "Launch leaders" recruited by cold email, 3 Zoom trainings, tasked with recruiting other ambassadors | **Flyers under dorm doors at 6 a.m.**, donuts, branded hats | **Borrowed** — approached existing campus meme pages (Seattle U) | None | 13→25→80→250 campuses; retired manual launches; "Global Fizz" untested |
| **tbh / Gas** | One school, saturated synchronously | No | No | **Yes — a dedicated Instagram account per school**, built by following students whose bios contained the school code ("RHS") and accepting follow-backs | Poll notification | Geofenced **state-by-state** rollout |
| **Saturn** | Per-school **white-label apps**, then one app | Yes; **NY AG cited undisclosed compensation of student promoters** | School visits | No | Weak | 18,000 schools; **acquired by Snap** |
| **Tinder** | USC Greek system; **sorority first, then paired fraternity** | Yes — Whitney Wolfe, in person, at chapter meetings | **Download-to-enter parties**; ~300 personal texts pre-launch | No | Match | Campus→campus→mainstream (aged out free) |
| **Snapchat** | **None.** A cousin showed classmates. | No | No | No | Message | Teen→everyone (never gated) |
| **Venmo** | Penn; **invite-only with a campus code (`penn-dp`)** published in the student paper | One student marketer (Harish Venkatesan) | **Zero-fee acceptance at 4 Philadelphia food trucks** | No | Payment claim | Campus→city→national |
| **Partiful** | None | No | Parties themselves | No | Event invite | House parties→**a16z mandating it for NY Tech Week**→trips, weddings |
| **Airbuds** | Ambassadors program exists (scale unestablished) | Yes | No | **TikTok** — growth traced to one video by a team member | Invite gate | US students→UK, AU, BR, MX |

**Three campus-native companies used paid students (Fizz, Saturn, Tinder). Two drew criticism or
enforcement over it — and in both cases the issue was disclosure, not payment.** Fizz's ambassadors
handed out donuts openly and were criticized for the *moderators* who also seeded content; Saturn
was cited by the NY Attorney General specifically for **undisclosed** compensation.

---

## 4. Founder mental-model matrix

| Founder | Core belief | Best tactic | Biggest mistake | Most relevant Zimo lesson |
|---|---|---|---|---|
| **Nikita Bier** (tbh, Gas) | Growth is a repeatable science; retention is a black swan | Synchronous single-school saturation as a **test**, not a growth strategy | Built two loops with **no external clock** — both apps died within a year of acquisition | Ask what regenerates the trigger. Zimo's regenerates forever; protect that. |
| **Antoine Martin** (Zenly) | *"If you have retention you will have growth"* — purpose→retention→engagement→growth, in that order | **McDonald's Wednesdays**: test with real teens in a real fast-food restaurant, on camera, weekly | Sold into an owner who could not monetize his best markets and closed a product with 40M MAU | Pick a KPI native to your category — for Zimo, splits per group per week, not DAU |
| **Teddy Solomon** (Fizz) | Build for "the 99% of life not on Instagram and TikTok" | The 6 a.m. flyer swarm; going through students, never administrations | Publicly targeted 1,000 campuses by end of 2023; reached ~80. Retrospectively reframed as restraint. | A launch day buys ~10%, not a campus |
| **Dylan Diamond** (Saturn) | "Come for the utility, stay for the social" | **Re-housing peaky schedule data in a daily calendar** — same users, same data, higher frequency | Per-school binaries put Apple's review queue inside the launch loop; later weakened verification for growth and was cited by the NY AG | Apply the peaky→daily test to Zimo. Settling up is peaky; what's the daily container? |
| **Andrew Kortina / Iqram Magdon-Ismail** (Venmo) | Money between friends is a social act, not a financial one | **Hiding the amount** — turned an unpublishable record into a publishable artifact | Ran a world-class loop with no monetization; got ~2 weeks from bankruptcy | Cost one loop iteration *before* optimizing the loop |
| **Shreya Murthy** (Partiful) | Adult friend groups shrink; parties are how you meet friends-of-friends | **No install for guests**; SMS never email | Retention capped by an exogenous variable (how often people throw parties) | The no-install guest path is the most copyable thing in the playbook |
| **Whitney Wolfe Herd** (Tinder) | Solve the two-sided cold start by sequencing, not by acquiring both sides | Sorority chapter → **paired** fraternity, so side B recognizes side A instantly | The capability was a person, not an institution; she left under litigation and built Bumble | Seed **organizers**, not users |
| **Evan Spiegel** (Snapchat) | Control only the differentiating layer; listen deeply then build something different | Ephemerality as a constraint that lowers the cost of posting | — (the durable one) | Never enforce your wedge in code if you want to leave it |
| **Ben Rubin** (Meerkat, Houseparty) | Clear sense of purpose is what lets you be lucky | Honest diagnosis: *"the everyday person doesn't go live every day"* | Built the entire growth engine on Twitter's notification system | Audit every growth input for who owns the switch |
| **Gilles Poupardin / Gawen Arab** (Airbuds) | *"The app only really works if you add your friends"* | Invite gates on features that are **genuinely worthless alone**; weekly Wrapped | Total dependency on Spotify/Apple APIs — the Meerkat position | Gate only multiplayer features; ship a widget |

---

## 5. Outcome matrix — the base rates nobody puts in a growth deck

| Company | Peak | Outcome | Cause |
|---|---|---|---|
| **tbh** | 2.5M DAU, 5M downloads in 9 weeks | **Dead** Jul 2018 | Loop exhausted; Facebook shut it for low usage |
| **Gas** | #1 US App Store, 30K signups/hour | **Dead** Nov 2023 | Same failure mode, 5 years later |
| **Zenly** | 40M+ MAU, 10th most-downloaded social app | **Dead** Feb 2023 | Closed by Snap — unmonetizable markets, feature overlap, competitor risk |
| **Houseparty** | COVID-era spike | **Dead** 2021 | Closed by Epic |
| **Meerkat** | SXSW 2015 | **Effectively dead** Mar 2015 | Twitter revoked the graph |
| **Venmo** | ~$59M/quarter independent | **Survived via acquisition** | Sold at $26.2M, ~2 weeks from bankruptcy; all real growth came after |
| **Saturn** | 18,000 schools | **Acquired** by Snap, Jun 2025 | Preceded by a $650K NY AG settlement, Mar 2025 |
| **Fizz** | ~250 campuses | **Live** | — |
| **Partiful** | ~500K MAU | **Live** | — |
| **Airbuds** | 5M MAU | **Live** | — |
| **Snapchat** | Public company | **Live** | The black swan |

**Six of eleven products here are dead. Four were killed by an acquirer while functioning.**
One survived *because* of an acquisition. **Any plan that treats "get acquired" as the happy ending
should read this column first** — see `LAWS.md` Law 12.
