---
name: ci-daily
description: Creator Intelligence daily run. Runs the competing search strategies across the three pools, writes about 30 cards and the concept pages into second-brain, updates the brain, and writes the day's issue and email body to _run/issue.md. Invoke with /ci-daily.
---

# Creator Intelligence: daily run

You dig up raw material from marketing, behavioural psychology, and founders and
company building, from any time, and judge each find by how rich and novel it
is, not by when it happened. `DESIGN.md` is the source of truth; this file is
how to run one day of it.

This skill runs unattended. **Never ask a question, never wait for approval,
and always finish by writing `_run/issue.md`.** If a source, a tool or a step
fails, keep going with what works and say so at the top of the issue.

## Paths

- Engine (this repo): `brain/`, `.claude/scripts/`, `_run/`
- Library: `second-brain/creator-intelligence/` (the second-brain repo, checked
  out inside this one)
  - Cards: `second-brain/creator-intelligence/cards/YYYY/MM/<card-id>.md`
  - Concept pages: `second-brain/creator-intelligence/concepts/<concept-slug>.md`

If `second-brain/creator-intelligence/` doesn't exist, create `cards/` and
`concepts/` under it. If `second-brain/` itself is missing, say so at the top of
the issue, write nothing to the library, and still produce the issue.

## Step 1: Date and already-done check

1. Run `date +%F` and `date '+%a %b %-d'`. Today is TODAY (YYYY-MM-DD).
2. If card files whose names start with `TODAY-` already exist in
   `cards/YYYY/MM/`, today's run already happened. Don't dig again: rebuild
   `_run/issue.md` from those card files (Step 10) and stop.

## Step 2: Read the brain

Read all of these before digging:

- `brain/taste-profile.md`: what lands and what doesn't
- `brain/shapes.md`: the shapes, including any on trial
- `brain/strategies.md`: active strategies and contestants
- `brain/leads.md`: the queue
- `brain/sources.md`: how to reach each source
- `brain/seen.md`: every find already shown. Nothing here can be shown again.
- `brain/scoreboard.md`: what's been working
- `brain/signals.md`: the last 14 days of signals
- The file names in `second-brain/creator-intelligence/concepts/`, so you reuse
  existing concept slugs rather than inventing synonyms
- `second-brain/creator-intelligence/searches.md`, if present: what you searched
  for recently, a hint at what you need

Also treat these as seen: the example finds in `DESIGN.md` (the Uber chime, the
tapping study, the lace-making surgeon, the Olympian on neuroplasticity, pronoia,
identity priming), the examples in `brain/shapes.md`, and every story in
`second-brain/references/`.

## Step 3: Check the feeds

Run `python3 .claude/scripts/feeds.py recent --days 7`. This lists every new item
from sources with a feed, plus a transcript URL when the feed ships one. Any
source under FAILED goes in the source-problems note at the top of the issue.

Note too any source you try later and can't reach, any tool that fails
(Perplexity, WebFetch), and any shape 8 candidate dropped because no clip could be
found.

## Step 4: Plan the slate

Plan 30 slots before digging. Hard rules, checked again in Step 8:

- **Pools:** every pool (marketing, psychology, founders) gets **at least 8** of
  the 30 cards. A far-field find gets the pool its principle carries into.
- **Shapes:** no shape gets **more than 7** of the 30 (a quarter). Trial shapes
  and `unshaped` count as shapes for this cap. Aim to use all 9 shapes every day.
- **Wildcards:** about a quarter (**7 or 8**) ignore the taste profile on
  purpose. Pick them from shapes, pools, strategies or sources the profile
  underweights, or a lead that doesn't fit what usually lands. They must still
  pass the self-review. Mark them `wildcard: true`.
- **Strategies:** every active strategy gets at least one slot. At least three
  slots go to contestants (C01 to C08 and the contestant sources), rotating so
  each gets tried within a week. Strategies doing well on the scoreboard get more.
- **Old and new:** mix fresh feed material (S15) with digging into older
  material. Age is never a filter.
- **Both search directions:** at least 3 slots go to concept-to-finds (S14),
  where you take a proven concept and hunt for fresh, concrete evidence of it.
  Everything else runs find-to-concept: find it, then name the idea underneath.

## Step 5: Dig

Search by shape, not by topic. "Uber growth strategy" returns the generic
story; "why does an everyday product do this odd specific thing" returns the
chime. Use each strategy's `How` line and each shape's search angle.

- **Tools:** use Perplexity (`perplexity_search`, `perplexity_ask`) for digging
  when it's available, and WebSearch and WebFetch alongside or instead. Read
  transcripts with `python3 .claude/scripts/feeds.py transcript <url>`. Cost is
  not a constraint: dig properly, not cheaply.
- **Gather more than you need:** aim for about 45 candidates for the 30 slots,
  so the self-review can reject freely.
- **Every candidate needs a source link** that supports it. Follow TIL threads,
  listicles and roundups to the original source and cite that.
- **Leads:** use the oldest queued leads in `brain/leads.md` for S16. Every find
  throws off new names (people, companies, experiments, concepts it mentions).
  Note them for Step 9.

### Not already seen

Drop any candidate that matches a find in `brain/seen.md`, or one of the
examples listed in Step 2. The same story from a different source, or under a
different headline, is the same find. Concepts can repeat; finds can't.

### Shape 8, the quote rule

A quote from a real person must be real, with a real clip. The source must be a
video or podcast with the timestamp (for example `at 41:12`). Confirm the words
in a transcript (the feed transcript, the episode page, or the video page)
before writing the card. **No clip, no card.** The card carries the person's
credential or fame, whichever the source has, in a form ready to say out loud
("a three-time Olympic gold medallist", "the Nobel-winning economist").

## Step 6: Self-review every candidate

Before any card goes in, score it 1 to 3 on each:

- **Hook:** is it familiar, understandable in a second?
- **Surprise:** is it really not what you'd expect?
- **Travels:** does the principle underneath apply far beyond this story?

Then check three things:

- **Already told everywhere?** Generic stories about popular companies ("how
  Apple scaled") and stories every business account has told are out. Popular
  companies are fine when the detail is specific and little known.
- **Makes sense?** Not so obscure or strange it needs a paragraph of setup.
- **Blatantly wrong?** Accuracy isn't a priority, but drop anything blatantly
  wrong, and any hidden-reason explanation the source doesn't back up.
  Invented explanations are the real risk for shape 1.

Reject a candidate if any score is 1, or it's told everywhere, makes no sense,
is blatantly wrong, or has no supporting link. Record each kept card's scores in
its frontmatter (`review:`) and count rejections for the scoreboard.

## Step 7: Pick and research the featured cards

Choose the **5 to 7** you judge the most unique of the day: the "if you read
nothing else" picks. Wildcards can be featured.

Research each one properly. Use `perplexity_research` when available, plus
several sources. Get the full backstory, the specific numbers, the named people,
what happened next, and how the principle works. Write it up as an **In depth**
section of 200 to 400 words: plain, concrete and unhedged, followed by 2 to 4
further links. It describes the find. It never steers toward a take, an
audience or a video.

## Step 8: Balance check, number and write the cards

1. **Re-check the hard rules** from Step 4 on the final 30: each pool at least 8,
   no shape over 7, 7 or 8 wildcards, 5 to 7 featured. Swap cards until they
   hold. If fewer than 30 survive the self-review, dig more rather than lower
   the bar. If a shortfall remains, ship fewer cards (never below 24) and say so
   at the top.
2. **Number the cards 1 to 30:** featured first (1 to 5, 6 or 7), then the rest,
   interleaved so pools and shapes alternate rather than clump.
3. **Write each card as its own file:**
   `second-brain/creator-intelligence/cards/YYYY/MM/<card-id>.md`, where
   `<card-id>` is `TODAY-NN-slug` (NN is the two-digit number, slug is 2 to 5
   words), for example `2026-10-31-07-haier-smashed-fridges`.

```markdown
---
id: 2026-10-31-07-haier-smashed-fridges
number: 7
date: 2026-10-31
title: Haier's CEO smashed 76 fridges
shape: 3-wrong-decision-worked
pool: founders
concept: quality-signalling
kind: observation
source_link: https://...
source_name: Harvard Business School case, 1998
strategy: S05
featured: false
wildcard: false
status: [shown]
review: hook 3 · surprise 3 · travels 2
---

# Haier's CEO smashed 76 fridges

**The find:** what happened or what it is, in one or two sentences.
**The surprise:** why it's not what you'd expect, in one sentence.
**The idea:** the principle underneath, by name when it has one ([Quality signalling](../../../concepts/quality-signalling.md)).

3 · Wrong decision that worked · Founders · [Source name](https://...)
```

Field rules:

- `title`: a 3 to 6 word label for the find. It is the card's headline
  everywhere, and the top featured card's title becomes the email subject.
- `shape`: a slug from `brain/shapes.md` (`1-hidden-reason` to
  `9-unfamiliar-concept`, a trial shape, or `unshaped`).
- `pool`: `marketing`, `psychology` or `founders`.
- `concept`: the concept page slug. Leave it as `""` when there's no nameable idea.
- `kind`: `observation`, `principle` or `both`. Psychology mostly supplies
  principles; companies and the day-walk mostly observations; marketing both.
- `strategy`: the strategy id that found it (S01 to S16, C01 to C08, or a bred one).
- `status`: a list, starting `[shown]`. Later runs add `deepened`, `bridged`, `used`.
- Every card is the same size. Featured cards add a `## In depth` section after
  the card, holding the Step 7 research and its links.
- **Cards are stored raw.** Nothing on a card says who it's for, and there's no
  "belief it breaks" or other video-shaped line.

Shape display names for the meta line: 1 Hidden reason · 2 Shocking number ·
3 Wrong decision that worked · 4 Tiny change, big result · 5 Unknown origin ·
6 Day-walk · 7 Far-field · 8 Unexpected claim · 9 Unfamiliar concept · Unshaped.
Shape 8 cards put the timestamp in the meta line: `[Source name, at 41:12](link)`.

## Step 9: Update the library and the brain

1. **Concept pages.** For each card with a concept, create or update
   `second-brain/creator-intelligence/concepts/<slug>.md`:

```markdown
# Quality signalling

What it is: one plain sentence.
Also known as: other names, if any.

## Cards

- 2026-10-31 · [Haier's CEO smashed 76 fridges](../cards/2026/10/2026-10-31-07-haier-smashed-fridges.md) · 3 Wrong decision that worked · Founders
```

   Append new cards to the list, newest last. Don't rewrite existing lines.
2. **Seen.** Append one line per card to `brain/seen.md`:
   `- TODAY · <card id> · <the find in a few words> · <source link>`.
3. **Leads.** Tick the leads you dug (`- [x]`, then ` · dug TODAY → <card id>` or
   `→ nothing`) and move them to `## Dug`. Add the new names the finds threw off
   (5 to 15 a day) under Queued in the right pool, with `added TODAY (from <card id>)`.
4. **Scoreboard.** Append today's tally under `## Daily tallies` in
   `brain/scoreboard.md`, in the format shown there: counts by pool and shape,
   kept/tried and featured per strategy, kept per source, source failures, and
   candidate discovered sources (a domain that produced a kept card and isn't in
   `sources.md`).

## Step 10: Write the issue and email body

Write `_run/issue.md`. It becomes both the GitHub issue and the email, so it's
plain markdown. Keep it under 60,000 characters. Use exactly this structure:

```markdown
<!-- ci-date: 2026-10-31 -->

> **Source problems today:** Nudge feed timed out · Perplexity unavailable, used web search · one shape 8 candidate dropped, no clip found

> **Featured today**
>
> 1. **Haier's CEO smashed 76 fridges** · one plain sentence on the find
> 2. **Second featured title** · one sentence
> ...

30 cards · Marketing 10 · Psychology 10 · Founders 10 · 8 wildcards

## Featured

### 1 · Haier's CEO smashed 76 fridges

**The find:** ...
**The surprise:** ...
**The idea:** ...
3 · Wrong decision that worked · Founders · [Source name](https://...)

**In depth**

The researched section, then a line of further links.

### 2 · ...

## The rest

### 7 · Title

**The find:** ...
**The surprise:** ...
**The idea:** ...
5 · Unknown origin · Marketing · wildcard · [Source name](https://...)

---

To reply, answer this email or comment on today's issue: {{ISSUE_URL}}
"deeper 14" researches card 14 in depth.
"bridge 14" shows ways to connect card 14 to your audience.
```

- Leave the source-problems blockquote out entirely when nothing failed.
- The `Featured today` blockquote lists every featured card, numbered as in the
  issue, with its title in bold. The email subject and inbox preview come from it.
- Add `· wildcard` to the meta line of wildcard cards.
- In the issue, write the concept name in plain text on The idea line. The
  relative concept-page links only work inside second-brain.
- End with the footer exactly as shown, word for word, including the literal
  `{{ISSUE_URL}}`. The workflow replaces it with the issue's link after creating
  the issue.
