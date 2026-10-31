---
name: ci-weekly
description: Creator Intelligence Sunday run. Asks what was used or liked, rewrites the taste profile, scores and breeds strategies, trials new shapes, refills leads, promotes sources, and writes the Sunday issue and email body to _run/weekly.md. Invoke with /ci-weekly.
---

# Creator Intelligence: weekly run

Sundays, five things and one email. This runs unattended: never ask a
question, never wait for approval, and always finish by writing
`_run/weekly.md`. If a step fails, keep going and say so at the top.

## Inputs

- Run `date +%F` and `date +%u`. The week reviewed is the 7 days ending today.
  WEEK_START is the Monday of the current ISO week (today minus (`%u` − 1) days).
- `brain/signals.md`: every signal. This week's lines drive the run, and older
  lines give the month of data that cuts need.
- `second-brain/creator-intelligence/searches.md`: pull-mode searches. A search
  is a signal for what you need when you sit down to make something.
- The week's cards: every file in `second-brain/creator-intelligence/cards/`
  dated in the window (read the frontmatter: shape, pool, concept, strategy,
  featured, wildcard, status).
- `brain/scoreboard.md`, `brain/strategies.md`, `brain/shapes.md`,
  `brain/leads.md`, `brain/sources.md`, `brain/taste-profile.md`.

Silence is neutral. Weeks without replies penalise nothing, so with no signals
the run still reports the spread and refills leads, but doesn't rewrite taste or
cut anything on silence alone.

## 1. The one question

Ask: **What did you use or like this week?** The answer arrives later as a reply
and is handled by ci-reply.

To jog memory, list only the week's **featured cards** plus anything **deepened
or bridged** this week. Never list every card. Number the list 1 to N. Each line:
`N. **<title>** · <Mon D> #<card number> · featured | deepened | bridged`.

## 2. Rewrite the taste profile

Rewrite `brain/taste-profile.md` from the week's signals and the earlier ones:
which concepts look like big topics (used, deepened, searched), which shapes
land, which pools, and how you like to land an idea (bridge picks). Keep it in
plain English, keep the sections, update `Last rewritten`, and summarise the
signals under `Signals so far`. Track "used" at two levels: **concepts** (big
topics) and **shapes** (finds that land).

Taste is one input, not the only one. Never write the profile so narrowly that
it excludes a pool or a shape. Breadth comes from the balance rules and the
wildcards.

## 3. Score the strategies

From the scoreboard tallies and the signals, judge each strategy and contestant
on raw counts: cards kept versus tried, featured, deepened, bridged, used,
searched for. **No blended score or formula.** Read the numbers and decide.

- **Retire** only strategies and contestants with at least a month of data (28
  days since `Started`) that produce few kept cards and draw no signals. Move
  them to `## Retired` with the date and reason.
- **Breed** variations of strong strategies (ones whose cards get deepened,
  bridged or used). A variation narrows or shifts the angle: a different pool,
  source, era or sub-angle. Give it the next id, `Parent: <id>`, and `Started:
  today`. Breed at most 3 a week.
- Note each change in `## Changelog`.
- **Watch the used rate.** Compare deepened and used counts over the last three
  weeks. If deepening is plenty and using is near zero for three weeks running,
  say so in plain words: the finder works and the constraint is elsewhere.

Append a `### Week of WEEK_START` block under `## Weekly summaries` in the
scoreboard, including featured hits (featured and used) and misses (deepened but
not featured).

## 4. Trial new shapes

Look at `unshaped` cards you engaged with (deepened, bridged, used, liked, or
matched by a search). When two or more share a way of looking that no shape
covers, add a trial shape to `## On trial` in `brain/shapes.md` automatically,
with no approval needed. Use the format in that file: name, search angle, the
card ids that clustered, and the date. Promote a trial shape to Active after a
month of engaged finds; retire it after a month without. Report any change.

## 5. Refill leads, promote sources

- **Leads:** top `brain/leads.md` back up to at least 40 queued, balanced across
  the three pools. Draw on names this week's cards threw off, concepts and
  themes from searches.md, and gaps in the spread.
- **Sources:** promote a domain from the scoreboard's candidate discovered
  sources to `## Discovered` in `brain/sources.md` when it produced kept cards
  on two or more days, recording how to reach it (feed URL if it has one, in the
  `- Feed:` format). Cut a contestant source only after a month of data with no
  cards you used. Mark seed sources that failed every day this week.

## Output

Write `_run/weekly.md`:

```markdown
<!-- ci-week: 2026-10-26..2026-11-01 -->
<!-- ci-list: 1=<card id>, 2=<card id>, ... -->

## What did you use or like this week?

Answer in plain words ("the Haier one, the lace-making one"). Skipping it is fine.

1. **Haier's CEO smashed 76 fridges** · Oct 27 #3 · featured
2. ...

## What changed

- **Strategies cut:** none, or names and why
- **Strategies bred:** S17 from S05: <angle>
- **Shapes on trial:** none, or the new one and the cards behind it
- **Sources added:** none, or names
- **Taste profile:** one line on what moved
- **Used rate:** used N · deepened N · bridged N · searches N (and the
  three-week warning, if it applies)

## This week's spread

- Cards: 210 · featured 42 · wildcards 53
- Pools: marketing 70 · psychology 70 · founders 70
- Shapes: 1 Hidden reason 24 · 2 Shocking number 23 · ... · Unshaped 6

---

To reply, answer this email or comment on this week's issue: {{ISSUE_URL}}
Say what you used or liked this week, in your own words.
```

- `ci-list` maps each number in the list to its card id, so ci-reply can match
  "the second one" and "deeper 2".
- Count the spread from the card files' frontmatter, not from memory.
- End with the footer exactly as shown, including the literal `{{ISSUE_URL}}`,
  which the workflow replaces with the issue's link.
