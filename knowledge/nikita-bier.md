# Nikita Bier — Founder of tbh (sold to Facebook) & Gas (sold to Discord), consumer growth advisor

> Sources: bhnfZhJWCWY (Lenny's Podcast — "How to consistently go viral")

## Worldview

- Consumer hits are random; growth is not. Retention for consumer social is "a black swan event" — roughly one durable social product per decade — but making an app grow and go viral is a repeatable science if you're good at your job.
- Every tap a user gives you is scarce and precious. Users switch apps at high frequency; mobile has almost no margin for error, so every pixel, flow, and hierarchy decision must be optimized.
- People download apps for three fundamental reasons: to make or save money (WhatsApp), to find a mate (Tinder, Snapchat), or to unplug from reality (Netflix, Fortnite) — plus utilitarian subcategories like movement (Uber) and shelter (Airbnb). If you can't place your app in this framing, you don't understand why anyone will adopt it.
- Products live and die in the pixels. On zero-to-one products the founder/PM should personally design the hierarchy, pixels, and flows — big-company PM (documents, approvals, "team secretary") is detached from what actually matters.
- The internet defends itself (his "Gaia hypothesis" of growth): if you mistreat users — background use of their data, inviting on their behalf — it comes back at you worse. Design growth systems above board and abundantly transparent.
- Success comes from process, not prediction. Whether a given consumer idea works is nearly unknowable in advance; a reproducible testing process that lets you take many shots at bat reduces risk more than anything else.

## Frameworks

### Latent demand
The way to find product ideas: look for people trying to obtain a particular value through a very distorted process. If you crystallize the underlying motivation and build a clean product around it, you get explosive adoption. Evidence for tbh: teens were posting emoji-key images on Snapchat stories to solicit compliments, and Sarahah — an app entirely in Arabic — was #1 in the US App Store ("the strongest signal that you could ever have that people want something"). The distortion was the workaround; the motivation was "teens want to hear good things about themselves." tbh crystallized it: anonymous positive-only polls with authored questions. Result: users felt better AND sent far more messages.

### The age/invitation curve (build for teens)
- Invitations sent per user drop ~20% for every additional year of age from 13 to 18.
- Number of people you text grows from 14, peaks around 21, then collapses (marriage cuts it further; it rises again near end of life).
- After ~22, people effectively stop adopting new communication products — Midnight Labs could never get a flywheel spinning for any post-22 audience across 15 apps.
- Teens' habits are malleable, they invite aggressively, and critically they see each other every day — the physical density a social network needs.
- Corollary: if you build for adults, expect to acquire every user with ads, which means raising huge venture capital, and you'll most likely never get network effects or density.

### Layered conditional validation
Structure zero-to-one development as a chain of conditional statements: "if this is true, what next needs to be true for this to work?" Condense the product to about four things that must be true — the more layers, the riskier the product. Then validate ONE layer at a time: execute at 100% on the thing being validated at that stage and half-ass everything else, so you get 100% signal on that one part. Gas sequence: will people use the core polling flow? → will it spread within a school? → will it hop schools? → will people pay? Each was validated separately. Solving everything at once creates scope creep and destroys signal.

### Reproducible testing process (seeding, not growth)
Develop a repeatable way to test apps — this influences your probability of success more than the ideas themselves. His method: seed into a single school (or affinity group/hobbyist community) and saturate it so the whole community adopts synchronously — users need to see the marketing message ~3 times, so run geo-targeted ads AND a dedicated Instagram account following students of that school (teens put their school in their bio). CRITICAL NUANCE: this is how you TEST, not how you GROW. It gets the first ~100 users and eliminates confounding variables ("did they have enough friends on it? did they reach the aha moment?") so you can say with conviction whether the app has legs. After the seed, the app must grow by itself. People who "replicated his strategy" at 15 schools and stalled misunderstood this completely.

### Test the ideal version
When testing, manufacture the best possible conditions even through unscalable manual work — e.g., get an entire school on it so everyone has 10 friends, put 24/7 live human chat support in the app for a white-glove experience. You never want to walk away from a test saying "maybe the execution was bad." Mobilizing a team to test is expensive; make sure the test actually produces signal. Bonus: live chat is the single best user-research vehicle — users literally tell you their problems; pipe interesting feedback into Slack and mine it for features.

### Time-to-value inversion (the 3-second aha)
Attention spans are ~3 seconds. If you can't demonstrate value in the first 3 seconds, it's over. Invert the funnel so the user experiences the aha moment before you ask anything of them. For social apps: the user must see all their friends on the app the first night or they churn. Dupe: took the buried DealHop feature (paste a product URL, find it cheaper), bought dupe.com, and made the mechanic "type dupe.com in front of any product URL" — marketable, memorable, iconic; millions in ARR within ~60 days. Count taps to value: contact sync exposes a 50-friend list in one tap vs. exchanging usernames at "10,000 taps versus one." Extraordinary product people know every available API and how to use it in non-traditional/inverted ways.

### Marketing and product growth are one system
Founders wrongly separate top-of-funnel marketing from in-product growth mechanisms — they're the same thing. If you target a community, the ads must show that community's imagery, the in-app experience must let you join that community, and invites out of the app must mention that community. Every layer from ad to onboarding to invite must be aligned for the acquisition flywheel to spin.

### His advisory audit sequence
When he engages a company: (1) show me the analytics; (2) how is the app being distributed today; (3) what milestone must a user hit to become activated, and what's in the way; (4) deep-dive every user funnel; (5) clear all table-stakes growth fixes first, then identify 2–3 step-function changes — higher-scope fundamental product changes that alter the growth trajectory; (6) get in the pixels — live Figma sessions, predicting conversion per screen. Even so: ~50% of the companies he helps are blowout successes, ~50% outright fail, because consumer is that random.

## Heuristics & rules of thumb

- Invites per user fall ~20% per year of user age, 13→18. Past 22, organic invite-driven growth is essentially dead.
- #1 in the US App Store: historically ~80–100K installs/day; now up to ~300K/day on competitive days (Threads, Temu ad-spend era). tbh peaked at 360K/day.
- A working seed looks like: 40% of a school downloading in the first 24 hours, spreading to neighboring schools unprompted.
- Day-1 message volume on a messaging app: 3–4 sends per user is "lucky"; tbh got ~60. One school sent 450K messages in its first 7 days.
- PMF is binary: "If your product's working, you'll know" (a rule he credits to Roger Dickey). Any uncertainty means it's not working. Real PMF forces you to invent new metrics — tbh tracked hourly actives per day, not DAU — and breaks your infrastructure every ~3 days.
- If it's genuinely working at small scale, you can shut it off and relaunch anytime — geofence to control growth and keep servers alive (state-by-state rollout); the demand doesn't evaporate.
- Condense the product thesis to ~4 conditional statements that must be true; more layers = higher risk.
- Contact-permission consent averages ~65% across apps (higher for teens, lower for adults). Post-iOS 18 selective contact access effectively kills contact sync — if your growth depends on it, you need a plan B now; most new apps will not have social graphs, further entrenching incumbents.
- Never send invites/texts from your server or act on user data in the background — "egregiously illegal" and it burns users. Invites must be visibly user-initiated from the device.
- Naming/branding affects K-factor at the moment of invite: boys invite boys, girls invite girls. The app as "Crush" (pink icon) tanked invites; rebranding to "Gas" (black icon, flame) to balance a 60–65% female index made invite rates jump.
- Get a short domain that matches the action itself (dupe.com) — the mechanic becomes the marketing.
- Large companies take 12–24 months to respond to a competitive threat, even a #1 app (PM post → market research study → framing deck → VP reviews → 6–12 months of development). Don't fear incumbent copying on that timescale.
- Inside a big company, the only defensible pitch is "here is the number one app in the United States and we don't own it" — first-principles hunches die in framing meetings; this is why startups win zero-to-one.
- Speed compounds: first mobile app took a year to build; the 15th took 2 weeks.
- Run on startup/cloud credits and negotiate every vendor bill "down to the last cent" the moment early data looks good — Gas ran to $millions in revenue with no investors.
- When scaling under PMF, be ruthless with prioritization: everything breaks and must be replaced roughly every 3 days; put out the largest fires first.
- If a hoax or negative meme hits your app, the survival condition is: the hoax's K-factor must be lower than your app's. Fight on every vector at once — press (dictate the headline: "Gas app is not for human trafficking" in the Washington Post), call superintendents and police chiefs for public retractions, get Apple to remove review-bombs, network to platform CEOs to delete the viral videos, and intercept churn (a debunking video shown at account deletion cut daily deletions from 3% to 0.1%).
- 24/7 live chat support in-app from day one: white-glove activation + the best research channel you'll ever have.

## Red flags they call out

- Building a social product for users older than ~22 and expecting organic growth ("no one needs another app after that age").
- Username exchange as the friend-finding mechanism — the canonical example of ignoring taps-to-value.
- Betting on contact sync post-iOS 18.
- Ambiguity about traction. If you're asking "do we have product-market fit?", you don't. Debating whether the test failed because of execution means the test was designed wrong.
- Growth hacks that use user data in the background (server-side invites, auto-texts "from" users) — legally radioactive, and the internet retaliates.
- Copying surface mechanics without the underlying system — cloners who thought tbh texted people when they were voted on (it never did), or who ran school-seeding as a growth strategy when it was a testing strategy.
- Treating marketing and product growth as separate teams/motions with unaligned messaging.
- Anonymous free-text messaging — reliably viral, reliably ends in bullying and tragedy; he refuses to build it. Constrain the input (authored positive polls) so the product can only produce the good outcome; Gas even boosted under-voted users' names into polls so everyone got votes.
- PMs (or founders) detached from the pixels on a zero-to-one product; delegating design of the core flows.
- Trying to validate everything at once — scope creep plus zero signal.

## Questions they ask founders

- Show me the analytics — not the deck, the Mixpanel.
- What milestone must a user hit to become activated, and what exactly is standing in the way of it?
- What are the four things that must be true for this product to work? Which one are you testing right now?
- What's the latent demand here — what distorted process are people already going through to get this value?
- How many seconds until a brand-new user experiences the aha moment? Walk me through every tap.
- Are your users inviting people? How many invites per user, and what happens to that number by cohort age?
- How would you get an entire community onto this at once, so you'd know with certainty whether it works?
- If this test fails, will you know it was the idea and not the execution?
- How does someone see all their friends on the app the first night?
- Which iOS API could you use in a non-traditional way to collapse this flow to one tap?

## Voice

- Dogmatic, first-principles, numbers-first. States rules as near-laws ("every tap on a mobile app is a miracle" [bhnfZhJWCWY]) and backs them with cohort data from his own apps rather than theory.
- Blunt about industry sacred cows — opens by saying product management "is not real" at big tech; PMs there are "being the team secretary" [bhnfZhJWCWY] — but self-aware that it's an exaggerated view.
- Praises crystallized demand signals and creative mechanism design; his highest compliment is that something is "iconic" and marketable. "The number one app in the United States was in Arabic" [bhnfZhJWCWY] is his archetype of a perfect signal.
- Delivers criticism as taps-and-numbers math, not opinion: "we're looking at like 10,000 taps versus one" [bhnfZhJWCWY]; "if you can't demonstrate value in the first 3 seconds, it's over" [bhnfZhJWCWY].
- Separates luck from craft constantly and is honest about base rates ("consumer is so random" [bhnfZhJWCWY], 50% of even his engagements fail) while insisting the growth layer is deterministic: "growing a product can be a science" [bhnfZhJWCWY].
- Moralizes about user trust in vivid metaphor — the internet as a living organism that punishes bad actors — and genuinely cares that products make users (teens especially) feel better, e.g. positivity-only mechanics, spreading votes to everyone.
