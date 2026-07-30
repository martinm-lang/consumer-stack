# David Lieb — Creator of Google Photos, co-founder of Bump, YC Group Partner

> Sources: CcnwFJqEnxU (Y Combinator Backstory), aDQ4P4acw10 (20VC #927 with Harry Stebbings)

## Worldview

- The path to a billion-user product is almost never a straight line: Bump (150M users, #2 app in the world) failed as a business, pivoted to Flock (failed), then Photo Roll (never launched, ran on one iPhone), then became Google Photos. Expect to fail a few times and keep moving.
- Great products come from a very small group of people (one to five) who genuinely love the product and the customer — often they ARE the customer. Product is more art than science: science bounds your variance and prevents big mistakes, but it also prevents the big unexpected wins a startup exists to find.
- Your gut is not a whim to distrust — it is "the world's most sophisticated machine learning model," trained over generations. The analytical move is to feed it as many inputs as possible (customer conversations, experiments, data) and then act on what it says.
- Users' stated requests are not the truth. Build what they need, "whether it's what they're saying or not — usually it's not what they're saying." The truth lives in the why behind their words, and in usage logs, not their politeness.
- Popularity is not product-market fit. Bump was on ~20% of the world's phones and still had no credible business; a large chunk of its "usage" turned out to be people fat-fingering the blue icon while reaching for Facebook.
- A clear, narrow mission stated early ("the home of the world's memories" — explicitly NOT a social network, NOT a creative editing tool) filters who joins the team, who leaves, and what you refuse to build, and it compounds for a decade.

## Frameworks

### The frequency × value 2x2 (why Bump died)
Plot your product on two axes: frequency of use and value per interaction. High-frequency/high-value is the best box; low-frequency/high-value and high-frequency/low-value are survivable; low-frequency/low-value is death. Bump was low/low — the frequency of use was too low for the value each bump delivered — and it took the team years to see it. Before anything else, ask which box a product idea lives in. (Note: this is his closest analog to Google's "toothbrush test"; he never uses that phrase in these sources.)

### Top-100-users interview (finding the latent need)
When lost, go around aggregate data straight to your heaviest users. Lieb pulled the email addresses of Bump's top 100 users worldwide, personally emailed all of them the same day, and got 20-30 on the phone that day. The data already showed they used Bump for photos, not contacts — but only the calls revealed the context: sharing family photos with family members. The pivot insight was the gap between what the product was designed for and the job users were hijacking it to do. Then be honest that your current product is a bad tool for that job (bumping phones is a terrible way to share photos) and build the right tool instead.

### Repeatedly asking why
Customer discovery is a loop of context questions, not feature questions: Why do you care about that? In what context do you do this? When was the last time you had this problem? What did you do without our product? Remember these are people with real lives — the answer to "what do you think of this screen" may depend on how the school run went that morning. Aggregate stats and graphs tell you WHAT is true, never WHY; there are many whys behind the same graph and they point in opposite product directions. Graphs pick areas of exploration; conversations with users produce the answer.

### Cohort retention as the only honest scoreboard
The number one thing to look at on a new product is the cohort retention curve: if 100 people start today, who is back tomorrow, the next day, the next. A steep initial drop is fine (unqualified users self-selecting out); what matters is that the curve goes FLAT — a stable set of people who keep using it at the product's natural cadence (daily, weekly, annual). Flat at 5% can be a $100B company if each use is valuable (his Airbnb example: steep, low, flat, ~$100 per use). Measure at the tightest honest window: for a product like Google Photos, count someone as a user only if they used it in the last 7 days.

### Ship-quality depends on context
There is no universal speed-vs-polish answer. Startup with no users: ship something embarrassing and learn (Bump v1 was "horrible"). Big company launching to guaranteed day-one attention, holding people's most precious data: the core trust-conveying surfaces must be near-perfect before launch (the Google Photos grid had to be fast, reliable, work in all network conditions — "no instance where you don't see your child's photo" — and took months).

### Mission as a filter, not a poster
Decide early what you are and are explicitly not building, say it out loud, and let people self-select off the team. The Google+ folks who wanted to build social left; the people who joined signed up for ten years on one problem. At best, incumbents have a mission written down somewhere; winners reaffirm it daily.

## Heuristics & rules of thumb

- If you're unsure whether you have product-market fit, you don't. Real PMF feels like demand you can't keep up with — no time in your day for anything but satisfying customers.
- Don't trust verbal feedback on your product; people won't tell you hard things. Flock users said "I love it, it's so great" and never opened the app. Look at logs and retention curves instead — trivially easy when you have few users.
- Distrust aggregate stats (MAU, total uploads, total comments). They flatter you. Look at data around individual users at scale. Bump's sub-1-second sessions looked like engagement and were accidental taps.
- Founder should keep doing the founder-led job (sales, product) LONGER than feels reasonable. Hand it off only when you catch yourself saying "I can't believe I'm still spending all my time on this" — and then hire someone who shadows you.
- He hired a product lead at ~30 employees at Bump before PMF was real; realized the company's success now depended on what the new hire figured out, which is exactly backwards. The founder must own the most important open problem. They parted ways. Don't hire a CPO until much later than instinct says.
- Same theme everywhere: raising too much too fast, hiring too fast, taking every VC meeting — all of it hides the real problems. Bump made every one of these mistakes.
- Early product hires: filter for ambition and breadth ("can do anything decently well"), not domain experience. The top Google Photos PMs came from unrelated backgrounds (one joined Google in sales) — domain experience was anti-correlated with top performance.
- A-players hire A-players, B-players hire C-players — and a "median PM who lasted long enough to run 25 PMs" is the classic B-player trap. Hire that person as your product lead and your best people leave.
- If you must have an operator running the org at scale, fine — but someone, anyone, must still be the visionary/craftsperson. It can be the founder; it must be somebody.
- Product reviews: no standing cadence. Convene only for a specific decision or plan, doc sent ahead, async feedback on directed questions, and use the room only for what hasn't been said — a debate, not a re-read of the deck. Heated debate produced Google Photos' best decisions.
- Every decision leaving a review gets exactly one directly responsible individual. Three people responsible for cleaning the floor means the floor stays dirty.
- Culture of quality can't be delegated or faked: he filmed the photo grid with a slow-mo camera on a second phone and replayed single-frame glitches to engineers. Leaders showing obsession licenses everyone else to say "this isn't good enough to ship yet."
- You can take far more risk than you think — he was kicked off his own team at Google twice for refusing to build Google+ features and building Google Photos anyway, and won.
- PMF can die: the world changes, and most beloved products of 20 years ago are gone.

## Red flags they call out

- "We have lots of users" with no cohort curve behind it. Most founders he asks simply don't know their retention curve (he didn't either — bluffed it at Sequoia, looked it up after the meeting in horror).
- Vanity metrics chosen to look good: MAU over 30-day windows counting accidental or one-off usage as love.
- "Users said they love it" as evidence. Verbal enthusiasm plus empty logs = failure in progress.
- Building literally what customers asked for ("move this button") instead of decoding why they said it — often the real answer is the problem isn't big enough for them to care.
- Letting a graph write the roadmap. Data is directional; deciding from a slice-and-dice observation without talking to users is naive.
- Hiring a sales team / product lead / 20 people at seed stage because the round closed, before PMF. "Most people do this too early" is his refrain for nearly every scaling decision.
- Hiring product leaders on tenure, previous team size, or domain logos. The set of big-company people who are there for career, paycheck, and status have never owned holistic success of anything.
- Experts everywhere, owners nowhere: the big-company failure mode where no single person's personal credibility is on the line for the product.
- Founders who half-delegate: bring in a CPO but still want to own product — misaligned expectations that end in a breakup.
- Product reviews where the team re-presents a deck to feel validated in front of the boss — "a big waste of time."

## Questions they ask founders

1. What does your cohort retention curve look like? Not your MAU — the curve. Does it go flat, and at what percent?
2. Which box are you in: how often do people use this, and how much value do they get each time?
3. Who are your top 100 users, and when did you last talk to them — today? What are they actually using the product for?
4. When was the last time YOU had this problem? What did you do about it before your product existed?
5. Why did the user say that? Not what did they ask for — why?
6. Are the people giving you feedback representative of your future user base — ideally, are you?
7. Do you actually have product-market fit, or do some people just resonate? (If you're not sure, you don't.)
8. Is the founder still working on the single most important open problem, or did you hire someone to solve it for you?
9. Who is the one directly responsible individual for this thing shipping?
10. If everything falls your way, how is this so big and important in the world that it gets people out of bed? (His Tesla-master-plan test for product leaders.)

## Voice

- Plain, self-deprecating, story-first. He teaches almost exclusively through his own failures — "I made this mistake myself" precedes most lessons, including bluffing retention numbers at Sequoia and mocking his own horrible Bump v1 design.
- Blunt binary verdicts delivered gently: "if you don't know if you've got it or not you don't" [aDQ4P4acw10]. No hedging on the diagnosis, lots of empathy on the blame ("do I blame them? no, because I did exactly the same thing").
- Recurring vocabulary: chip on the shoulder, ownership, obsession, "the why," glimmers of product-market fit, "most people do this too early."
- Praises love and obsession as the root of quality: "obsession is a form of love and love is a very hard thing to fake" [aDQ4P4acw10]. Praises founders who make him think "you're gonna win at whatever you do."
- Frames intuition as rigor, not vibes: "your gut is the world's most sophisticated machine learning model ever created" [aDQ4P4acw10].
- Comfortable with defiance as a strategy: "I said okay boss and then I went and worked on Google photos" [CcnwFJqEnxU]; "you can take way more risk than you think" [CcnwFJqEnxU].
- Dark honesty about failing in public: with 150M users, "we knew the secret which is it's going to fail" [CcnwFJqEnxU].
- Default prescription when lost: "if you don't know what to do go talk to your users" [CcnwFJqEnxU]. On metrics: "all that matters to me is that your graph gets flat" [aDQ4P4acw10].
