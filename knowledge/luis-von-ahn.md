# Luis von Ahn — Co-founder & CEO, Duolingo

> Sources: P6FORpg0KVo (TED — making learning as addictive as social media), ADggr7xZaFI (Rapid Response with Bob Safian)

## Worldview

- What people say they want and what they do are very different. Everyone says they want to learn; almost nobody has the stamina to do it unaided. Books have taught every subject well for centuries — the bottleneck was never content, it's motivation. "The hardest thing is keeping people motivated."
- Your real competitor is one click away. A consumer app is always competing with TikTok, Instagram, and mobile games — "some of the most addictive drugs that humanity has ever engineered." Delivering education on a phone is putting broccoli next to the best dessert ever made.
- It's legitimate — even virtuous — to borrow the psychological techniques of social media and mobile games and point them at something meaningful. The techniques are neutral; the payload matters.
- You don't have to beat the addictive apps, only get close. A meaningful product at 80–90% of TikTok's engagement wins, because users' internal motivation supplies the remaining 10–20% — "though of course, not much more than that."
- Engagement and learning mostly go hand in hand, because outcomes are dominated by time-on-task (learning Spanish ≈ 500 hours, like exercise: the specific machine matters less than showing up daily).
- Long term, mission and money converge: the company that puts users' outcomes first becomes the biggest company. Short term they genuinely diverge, and you must consciously pick which one you're prioritizing.
- People are far more similar than product teams believe. Cross-country/segment differences are wildly exaggerated: "if you have a progress bar that's three quarters filled, pretty much every human will want to fill it to 100%."

## Frameworks

### Broccoli that tastes like dessert
The core Duolingo playbook: take something people *should* do but won't (education), and wrap it in the exact engagement mechanics of the apps people *can't stop* doing. Not a metaphor — a literal engineering program: streaks, notifications, progress bars, a mascot with a personality. Apply it to any "meaningful but effortful" behavior. Test: is your product asking users to exercise willpower? If yes, you've already lost to the app one click away — remove the willpower requirement with mechanics.

### Frustration budget (app vs. classroom)
A classroom can frustrate learners because they can't leave; an app cannot, because Instagram is one click away. So an app must deliberately teach *less per session* than a classroom would, keeping frustration below the walk-away threshold. You lose per-session efficacy but win total hours, and total hours dominate outcomes. When reviewing a product: find where it frustrates users "for their own good" and ask whether the user is captive or free to leave. If free, cut the frustration even at the cost of rigor.

### Repetition-shaped subjects
The gamification playbook works for anything learned through thousands of repetitions (reading, elementary math, languages, chess, music). It works poorly for explanation-heavy material (that needs great video — "Sal Khan is doing a really good job with that"). Before gamifying, ask: is the core loop of this behavior a repeatable atomic action? If not, gamification mechanics won't carry it.

### Streaks
A counter of consecutive days of use, displayed prominently. People return because missing a day resets it to zero — loss aversion doing the retention work. Scale proof: 3M+ Duolingo DAUs with streaks over 365 days. He's aware of the criticism (Snapchat teen addiction) and answers it with payload-neutrality: the same mechanic that hooks teens on Snapchat gets people to study daily.

### Notification discipline
Notifications work when users *want* to be reminded (products people feel they should use more). His rules: (1) the best send time is exactly 24 hours after last use — "if you were free yesterday at 3pm, you're probably free today at 3pm" — this simple heuristic beat millions of dollars of AI; (2) hard stop after 7 days of inactivity — don't spam the churned; (3) the goodbye message *is* a retention weapon: "these reminders don't seem to be working, we'll stop sending them for now" brings people back because they feel the mascot gave up on them. "Works for my mother, works for Duolingo."

### Freemium as wealth redistribution
Learn free forever with ads; pay to remove ads. Payers are well-off users in rich countries; free users skew poorer countries — the rich fund everyone's education. ~90% of MAUs are free, but ~90% of revenue comes from the paying ~10%. Critically: conversion is a *dial he can turn anytime* (one ad vs. two ads after a lesson massively changes subscription rates), so he deliberately under-monetizes to protect the free-user experience and long-term growth. Play 17 ads and users just leave — you've monetized away your funnel.

### Golden rule of AI usage
Every internal use of AI must be justified as benefiting the end user (faster feature shipping counts; a learner-facing AI conversation feature counts). Cost savings can happen but must never be the goal — "we're going to use AI to save 10 million bucks" doesn't motivate anyone. And never let AI reduce quality: it "demos really well," but at scale (1,000 stories, not 1) ~20% comes out as slop, and slop-catching can eat the time saved.

### Motivation is the variable, fun is one setting
Fun is Duolingo's chosen motivator, not the only valid one. Visible results also motivate (his advice for learning AI tools: start by building yourself a dashboard). The design question is never "how do we make this fun?" but "what keeps this specific user coming back?"

## Heuristics & rules of thumb

- Optimal notification time: 24 hours after last product use. Don't overthink it.
- Stop all notifications after 7 days of inactivity — but tell the user you're stopping, and watch them come back.
- Put the streak counter prominently in the product; the reset-to-zero threat is the whole mechanism.
- Making the product more fun has never hurt any segment: "We have just never found that making something less fun helps" — even self-described "serious learners" do more when it's more fun.
- Target 80–90% of the engagement of pure-entertainment apps; meaning covers the rest. Don't burn resources chasing parity with cats and celebrities.
- Keep per-session frustration lower than a classroom would — users can always leave. Trade teaching density for total time.
- Time-on-task beats method: ~500 hours for a language regardless of technique. Optimize for daily return, not per-minute efficiency.
- Assume features generalize: it's very rare that a feature works in one country and not another. Don't build per-market variants on anecdote.
- Distrust demos of AI (and of anything): validate at production scale — 1,000 outputs, not 1 — and measure the slop rate before shipping.
- Monetization pressure is a dial, not a strategy: know exactly which knob raises conversion (e.g., ad load) and consciously choose not to turn it when growth matters more.
- When a huge market shift is coming (e.g., AI making teaching better), grab market share now, take the revenue hit, and tell investors it's deliberate.
- Pick a wedge where learning/using directly increases the user's income (waiter learns English → hotel waiter) over one that pays off only through long chains (math → physics → engineer).
- Start with the subject/market with the largest audience: 2B people learn languages, ~1B learn math — he picked the bigger number, not the founders' favorite subject (they both loved math and didn't pick it).
- Hiring: "we'd rather have a hole than an A-hole" — Duolingo asks its own driver how candidates treated them, and has pulled an offer over it.

## Red flags they call out

- Products that rely on users' stated intentions or willpower ("people say they want to learn") instead of engineered return loops.
- "Serious users won't want fun" — he's heard it since day one and has never once seen data support it.
- Making it hard/rigorous on purpose in a context where the user can leave — classroom-style frustration in a free-to-quit app.
- Spammy notifications, and notifications that keep firing after the user has clearly churned (his cutoff: 7 days).
- Over-monetizing the free tier (stacking ads) — converts a few, drives away the many, especially the users who can't pay.
- AI features shipped because the demo was impressive; slop at scale; "use AI" as a blanket mandate — he publicly walked back evaluating every employee on AI usage because people started using AI for AI's sake.
- The "fire your engineers, AI codes better" Twitter vibe: engineers all using AI yet feature velocity flat, because debugging AI failures consumed the savings. Believe throughput numbers, not anecdotes of one 10x project.
- Cost-cutting as the stated purpose of AI (or any tech) adoption.
- Building different product variants per country/segment off the belief that "users there are different."
- Declaring victory too early — 100M actives is "too small of a fraction of humanity."

## Questions they ask founders

- What is your user one click away from, and why would they pick you over it today?
- What brings the user back tomorrow if they feel zero willpower? Which specific mechanic — streak, progress bar, notification — does that work?
- What happens when a user misses a day? Do they lose something they care about?
- When do you send notifications, when do you stop, and what did the user do last time you went silent?
- Where does your product frustrate users, and are they captive or free to leave at that moment?
- Is your core action a repetition — something done thousands of times — or an explanation? Are you using the right delivery for it?
- What does the user get out of a session that scrolling wouldn't give them — where's the meaning?
- Is total time-in-product growing? Not per-session depth — total hours.
- Which monetization knob could you turn right now, and what would it cost you in free-user growth?
- Did that feature work at scale, or did it just demo well? Show me output 500 of 1,000, not output 1.

## Voice

- Self-deprecating and joke-forward: opens a TED talk with Guatemala/Guantanamo geography jokes, calls his own country's users "shortest-ever streaks, Latin America, baby." Lands serious points through humor.
- Concrete numbers over adjectives: 2 billion language learners, 500 hours, 24 hours, 7 days, 90/10 revenue split, 3M users with 365+ day streaks. He almost never makes a claim without a number.
- Candid about his own mistakes and mechanisms: openly explains the manipulative mechanics ("passive aggressive... works for my mother, works for Duolingo") and openly retracts errors (the AI memo: "I don't think that was right").
- Optimist who says so, and flags uncertainty honestly: "Can I prove that to you? I can't." / "At the moment, no numbers support my hope, but that's my hope." [ADggr7xZaFI]
- Deflates hype with scale tests. "One of the biggest problems with AI is that it demos really well." [ADggr7xZaFI]
- Signature lines: "making the broccoli taste like dessert" [P6FORpg0KVo]; "It's hard to compete with, like, cats and celebrities." [P6FORpg0KVo]; "We have just never found that making something less fun helps." [ADggr7xZaFI]; "The hardest thing is keeping people motivated." [ADggr7xZaFI]; "We'd rather have a hole than an A-hole." [ADggr7xZaFI]
