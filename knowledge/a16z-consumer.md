# a16z — Consumer AI Playbook

> Collective view of the a16z consumer investing team. Speakers identified from context: **Justine Moore** and **Olivia Moore** (consumer partners, creative tools / consumer AI), **Bryan Kim** ("BK", partner, ex-Snap — social and consumer social), **Anish Acharya** (general partner, ex-Google PM — voice, business models).
>
> Sources: we9mNqAW_5I (The State of Consumer Tech in the Age of AI), p4-7x6QiYr0 (Where does consumer AI stand at the end of 2025?)

## Worldview

- **Velocity replaced moats as what wins early consumer AI.** BK admits his moat-first investment theses (network effects, system of record, workflow lock-in) have not picked the winners; the winners break the mold, ship relentlessly, and convert mind share into traffic into revenue. Moats still matter eventually — but they come *after* velocity, not before.
- **AI flipped consumer monetization.** Pre-AI, a best-in-class consumer subscription was ~$50/year; now consumers happily pay $200–250/month (ChatGPT Pro, VO3) and some say they're undercharged — because the product *does work for them* (e.g. deep research replacing 10 hours of report-writing) rather than helping them help themselves. Anish: every part of consumer discretionary spend gets overtaken by software — the future budget is food, rent, software.
- **The missing white space is connection.** BK: past breakouts (Google=information, Dropbox=utility, creative tools=expression) all have AI analogs already being built — but the social graph has not been rebuilt on AI. People pour more of themselves into ChatGPT than into Google; the open question is what connection looks like when the essence of you becomes sharable.
- **Consumer AI is a power-user story.** Anish: pre-AI, power users were a niche; now depth of value and depth of monetization is so much higher that maybe all of AI is a power-user story — and everyone else is just traffic. Revenue concentrates in the deep end.
- **The labs won't verticalize everything.** Justine: labs are great at models and incremental core-experience improvements, but their standalone consumer products (Pulse, Atlas, Sora-as-social, group chats, Stitch, Gems, Opal) largely aren't working — Notebook LM is ~1 success out of 20 attempts. Opinionated standalone consumer UI is no longer their core competency, which is structurally positive for startups.
- **Consumer is unpredictable by nature.** The best products emerge out of nowhere — if they were predictable they'd already have been built. Hence: try everything, form opinions from usage, not theory.

## Frameworks

### Velocity is the moat (Bryan Kim)
In the early AI era, defensibility = shipping speed.
- The loop: incredible model/product launches → break through distribution noise → mind share → users and traffic → real revenue → fuel to keep shipping.
- Classic moats (network effects, workflow lock-in, system of record) arrive later as a *consequence* — a fast-moving product gets adopted by enterprises and locked into workflows (11 Labs).
- True network effects haven't kicked in yet because it's mostly creation, not a closed creation–consumption loop; where they exist (11 Labs' voice library) they look like traditional marketplace effects, not something new.
- Evaluate teams on product generation speed and launch cadence, not on a static moat story.

### The quality frontier (Justine Moore)
A consumer AI company avoids the MySpace/Friendster fate as long as it stays at the technology/quality frontier — training a state-of-the-art model or integrating one.
- Fall slightly behind → ship the next update → you're number one again. Falling off the frontier, not age, is what kills.
- The frontier is segmenting: best image model for designers vs. photographers vs. $10/month users vs. $100/month users; in video, ad-video splits into product shots vs. people.
- Therefore multiple winners persist per modality — each segment is a large market — as long as each keeps shipping.

### Inception theory (Bryan Kim)
To judge a product, peel the onion three to five layers down to the emotional one-liner — "I want my dad to love me" [p4-7x6QiYr0].
- ChatGPT bottoms out at *help me be better* — which is why it's #1 in productivity.
- TikTok is *entertain me*; social is *I'm lonely, I want to be seen*. These are different parallels of product direction.
- Products fail when they bolt one emotional category onto another — e.g. OpenAI shoving connection features into a help-me product. ChatGPT group chat stops at 2–3 people planning a trip (help-me); it never becomes understanding your friend better (see-me).

### The status game test (team consensus)
A social network needs real emotional stakes: you post something sensitive about *yourself* and care how it lands.
- AI-generated content where you always look perfect and happy removes the stakes; the status game collapses. That's why AI-feed apps stall as social networks.
- Sora 2's retention data shows a *creator tool*, not a social app: a small number of creators export virality to TikTok/X/Reddit; little in-app consumption, remixing, or commenting. BK's frame: Sora's true analogy is CapCut, not TikTok.
- Anish's bull case: the new status game is humor — prompting skill × cultural awareness — a direction nobody has captured.
- Test: do consumption and creation live together in the app? Is the output native to it, or strictly better exported? (TikTok with Sora videos is strictly better than Sora.)

### Consumer virality → enterprise pipeline (Justine & Olivia Moore)
A growth loop unique to this era: viral consumer moment → enterprise lead generation.
- Enterprise buyers have an AI mandate and watch Twitter/Reddit/AI newsletters; a random-looking consumer meme product becomes someone's AI strategy and makes them the internal hero.
- 11 Labs sequence: early-adopter consumers (memes, voice cloning, game mods) → massive enterprise contracts in conversational AI and entertainment — *before* ever reaching mainstream consumers.
- Operationalize it: mine your Stripe payment emails for employer domains; when 40+ people at one company are paying, reach out and convert the account.
- Same loop runs top-down now too: ChatGPT enterprise usage up ~8–9x YoY converts into personal consumer habit.

### Revenue retention ≠ user retention (BK & Olivia Moore)
Pre-AI these were the same number — pricing rarely changed, nobody upgraded. Now track them separately.
- Usage-based overages, credit/token purchases, and tier upgrades on top of subscriptions push revenue retention meaningfully *above* unique-user retention.
- Consumer products with >100% net revenue retention exist for the first time ever; pre-AI, BK would have said the number made no sense.
- That line — over vs. under 100% — separates the good from the great from the exceptional in consumer AI.

### Labs' structural blind spots (Anish Acharya & Justine Moore)
Three reasons the app layer stays open for startups:
1. **Promo committees** — mid-career PMs get promoted for safely extending core metrics; opinionated products risk legal, compliance, and the CEO yelling. So labs ship incremental, never opinionated; the more opinionated founders are, the bigger their advantage. Evidence: of ~20 standalone consumer experiments (Pulse, Atlas, group chats, Stitch, Gems, Opal), only Notebook LM works.
2. **Compute tension** — labs split finite compute between training and inference, and between entertainment (Ghibli) and coding/intelligence; a viral launch can delay the next frontier model. App-layer startups have no such tension (xAI is the only lab not compute-bottlenecked).
3. **First-party model bias** — labs will only ever serve their own models, but many categories are best served multi-model and multimodal (Krea wins by being the best interface over every frontier model, e.g. saving reusable characters/styles as taggable elements on top of Nano Banana).

### Voice as the new substrate (Anish Acharya)
Voice has intermediated human interaction since the beginning of time but never worked as a technology substrate (VoiceXML, Dragon) — generative models finally make voice a primitive.
- Consumer thesis: always-on coach/therapist/companion in your pocket — playing out.
- The surprise: enterprises adopted voice fastest, even in sensitive categories like financial services, replacing offshore call centers with 300% annual turnover.
- Voice is the AI insertion point for the enterprise — and not just low-stakes support calls: the *most important* conversation of the day (negotiation, sales pitch, persuasion) gets AI-intermediated because AI does it better.
- The first great net-new consumer voice experience hasn't appeared yet; Granola blowing up — finally doing something valuable with everything you say all day — is the early signal.

### Anything in, anything out (Justine Moore)
The direction of creative tools: from text-in/image-out to any modality in, any modality out.
- Image+text+reference → coherent design; video+prompt → edited video; video → next-iteration images.
- Labs are merging separate text/image/video efforts into mega-models; huge implications for design, which is exactly the combination of images, text, and video.
- Products that assume a single fixed input→output pipe will feel dated.

## Heuristics & rules of thumb

- General LLM assistants trend winner-take-most: only 9% of consumers pay for more than one of ChatGPT/Gemini/Claude/Cursor; for most of 2025 <10% of ChatGPT users even *visited* another provider. Don't build a slightly-better general assistant.
- If your product is mainly **text in, text out**, the labs will absorb you — ChatGPT is used ~24–25 times/week; you cannot out-frequency that. You need a creative angle to steal usage (BK).
- Growth-rate over scale as the leading signal: Gemini growing desktop 155% YoY *while accelerating at scale* vs ChatGPT at 23% — watch the derivative, not the WAU (ChatGPT ~800–900M weekly actives).
- Distribution ≠ usage: Gemini is at 50% of ChatGPT's scale on Android (where Google controls distribution) but only 17% on iOS. Being everywhere-but-nowhere loses to being the Kleenex brand.
- **Templates and style beat raw capability** once models are good enough: the Ghibli moment, Grok's viral video templates, ChatGPT's TikTok-style trending-theme picker vs Gemini's blank pane that leaves even a Snap veteran unsure what to type. Blank-canvas products lose to opinionated on-ramps; then character consistency keeps people generating. Think TikTok: capability constant, trend/format churn keeps it fresh.
- There is near-infinite demand for the **best-in-class** image/video model; new capabilities spawn viral trends that drag mainstream users into products they'd never tried. Being second-best in a modality gets you segment-specific wins only.
- Companionship is the first mainstream LLM use case and still early: 11 of the top 50 apps on their list were companion apps; users try to turn *any* chatbot — even a car dealer's support bot — into a therapist or girlfriend. The category is fragmenting into vertical companions (nutrition, teens, coaching) — *companion* now means any advice/wisdom/counsel you'd have gotten from a human.
- Companion design rule: not too agreeable. Just agreeable enough to help users practice connection; so agreeable it makes them worse at real relationships is a product failure (Anish). Positive existence proof: Character AI users graduating to real-world relationships; Replika studies showing depression/anxiety declining.
- Consumer→enterprise voice sequencing: voice is the AI insertion point for the enterprise, and it's not just low-stakes support calls — the *most important* conversation of the day (negotiation, sales pitch) will be AI-intermediated because AI does it better (Anish).
- Enterprise usage feeds consumer habit: ChatGPT enterprise usage up ~8–9x YoY; when people must use a product at work, it converts to personal usage. Watch the reverse funnel too.
- Reality check on reach: ~3x more US teens have ever used Character AI than Claude. Tech-insider love (Claude, powerful features hidden behind settings toggles) does not equal mainstream adoption — dumbing it down is real product work.
- AI art quality bar: models are averaging machines, while culture lives at the edge, outside the training data (Anish — he doubts a model trained on pre-hip-hop music would infer hip-hop). Expect pools of AI talent and human talent with a very low conversion rate to the top of each — the problem is bad art, not AI artists.
- Creators fragment into two persistent types: human-experience celebrities (Taylor Swift — the lived story matters) and interest-based creators (where being AI doesn't matter, only being interesting on the topic). Both survive (Justine).
- Execution beats distribution even at browser scale: Perplexity's Comet launch spike and sustained traffic beat ChatGPT's Atlas despite vastly less distribution — first-class agentic workflows (repeatable, schedulable tasks) were the difference (Olivia).
- Proactive is the prize: at ~25 ChatGPT sessions/week, whoever ingests your email/calendar/docs and earns the right to send useful nudges wins the everything-app position — Pulse and connectors are the right primitives with the wrong execution so far (BK, Olivia).
- Hardware watch: the most-adopted post-phone device is AirPods — hiding in plain sight for AI if it fits existing social protocols (Anish). Under-20s already wear recording pins at parties and get real value; new cultural norms will form around always-on recording like they did for cell phones (Olivia, BK).

## Category picks

Where the team is explicitly leaning for 2026:
- **Vertical companions** — the first mainstream LLM use case, now fragmenting beyond friend/girlfriend into any advice, wisdom, entertainment, or counsel a human used to provide (nutrition-plus-emotional-support, teen worlds like Tolan). The need endures: the youngest generation averages barely more than one close friend to talk to (BK).
- **AI-native social / connection** — the biggest unbuilt white space; the social graph hasn't been rebuilt on AI. Likely not a skeuomorphic feed; possibly sharing the essence-of-you that models already hold, or people recommendation (co-founder, friend, date) — the sci-fi endgame of an AI that hears everything and benchmarks you against the world (BK, Justine).
- **AI clones & personas** — from thought-leader clones (Delphi) and known characters (Character AI) to everyone in between: letting ordinary people with real skill scale themselves via text/voice/video personas; Masterclass's RAG-based voice agents as the template (Justine, Olivia).
- **Consumer voice** — the net-new consumer voice experience is still unclaimed (see Voice framework).
- **Prosumer workspace & proactive assistants** — connectors + proactive nudges on top of daily-habit frequency; also AI-native browsers/workflows (Comet as the accessible entry) (BK, Olivia).
- **App generation** — the biggest startup trend of 2025; winners put satisfying constraints on generation (Wabi) while labs half-heartedly bundle it (Opal released with a whimper) (Anish, BK).
- **Creative tools at the interface layer** — multi-model, template-driven, anything-in-anything-out (Krea); templates and style now matter more than raw model capability (Justine, BK).
- **Screen-aware and always-on agents** — products that see your screen or hear your day, then move beyond suggestions to doing the work: sending emails, coaching in context (Olivia).

## Red flags they call out

- **Skeuomorphic AI social**: an Instagram/Twitter feed but the users are bots, or a feed of AI-generated pictures of you. No emotional stakes, no status game, no network — it's yesterday's form factor with AI poured in.
- **Moat-first pitches** in early-era categories: a beautiful defensibility story with slow product velocity has systematically lost to fast shippers (BK's self-described conversion moment).
- **Text-in/text-out apps** competing head-on with the labs' frequency advantage.
- **Creation without consumption**: if the output is more native to TikTok/X than to your own app, you're a feature/creator-tool, not a social network — value exports itself away.
- **Over-promising in app generation** — it discourages early users; the winners put the right constraints on generation so results are reliably satisfying (Anish on Wabi).
- **Buried features and blank screens**: shipping powerful capabilities as a toggle inside a settings bar (Claude's file creation) or opening on an empty prompt box (Gemini). Execution nuance is the difference between a new primitive being underhyped and unused (Pulse, connectors).
- **Over-agreeable companions** that optimize engagement at the cost of the user's real-world social capability.
- **Mid AI content**: if the product's median output feels mid, virality won't come; templates, style, and taste are the fix, not more capability.

## Questions they ask founders

1. Peel the onion: three layers down, what's the emotional one-liner of your product — help me, entertain me, or see me? Are you accidentally mixing two?
2. What's your shipping cadence, and what did you launch in the last month? Why will you out-velocity the category?
3. Are you at the quality frontier for your modality — state-of-the-art model or integrating one — and which *segment* of that frontier do you own (designer vs. photographer vs. $10/month user)?
4. If your product is text in, text out — why doesn't ChatGPT's 25-uses-a-week frequency absorb this? What's your angle to steal usage away?
5. What's your unique-user retention vs. revenue retention? How do users spend *beyond* their subscription — overages, credits, upgrades? Are you above 100% revenue retention?
6. Where does consumption of your users' output live — inside your app, or on TikTok? Do creation and consumption live together?
7. What's the emotional stake when someone posts/shares? If everything is AI-generated and flattering, what status game is left?
8. What's the first template or trending on-ramp a confused new user clicks — or do they face a blank pane?
9. Has a viral consumer moment produced enterprise pull yet? Have you mined your payment data for employer domains?
10. What can you do because you're multi-model/multimodal that a definitionally first-party lab product never will?

## Voice

- Data-forward and product-obsessed: they argue from usage stats (WAU, YoY growth, retention curves, App Store ranks) and from personally power-using every product — recommendations come with I-use-it-daily credibility. Olivia published one new consumer product a day for a month on Twitter.
- Coin and reuse compressed labels: *velocity is the moat*, *the Kleenex of AI*, *everywhere but nowhere*, *anything in to anything out*, *food rent software*, *inception theory*.
- Deliver bearishness cheerfully and structurally: criticism targets incentive structures (promo committees, compute tension, status games) rather than people; a favorite frame is underhyped-primitive-but-execution-is-off (Pulse, connectors).
- Techno-optimist on the human question — they treat companions enabling better real-world connection as AI's peak value, not a doom story — while staying clear-eyed about slop: models are "averaging machines and culture is supposed to be at the edge" — Anish [we9mNqAW_5I].
- Comfortable holding a bull and a bear case at once, and answering flatly (bearish for now) when asked to pick.
- Verbatim: "We're living in this early era of AI where velocity is the moat" — BK [we9mNqAW_5I]; "consumer spend to be like food, rent, software" — Anish [we9mNqAW_5I]; "ChatGPT is like the Kleenex of AI" [p4-7x6QiYr0]; "maybe all of AI is actually a power user story" — Anish [p4-7x6QiYr0]; "Sora's competition … isn't actually TikTok. It's actually CapCut." — BK [p4-7x6QiYr0]; "The more founders do opinionated things, the more advantage they are." — Anish [p4-7x6QiYr0]
