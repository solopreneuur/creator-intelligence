# Strategies

Each strategy is a named way of looking: a shape aimed at a pool, a source, a dig
site or a far field. They run side by side and compete on the scoreboard. Cards
name the strategy that found them (`strategy: S05`).

- **Active** strategies run every day.
- **Contestants** are on trial. Each gets slots on a rotation (at least three
  contestant slots a day) until it has a month of data.
- Nothing is cut until it has a month of data (28 days from `Started`).
- The weekly run retires weak ones, breeds variations of strong ones (`Parent:`),
  and records each change at the bottom under Changelog.

## Active

### S01 · Everyday oddity
- **Shape:** 1-hidden-reason · **Aimed at:** Marketing, Founders
- **How:** Pick a product or moment everyone uses. Search "why does [X] [odd specific detail]", "[X] designer explains", "[X] was designed that way because".
- **Started:** 2026-10-31

### S02 · Ex-insider explains
- **Shape:** 1-hidden-reason · **Aimed at:** Founders
- **How:** Former designers, engineers and PMs explaining a product decision outsiders find strange. Oral histories, launch retrospectives, "I worked on X" posts, conference talks.
- **Started:** 2026-10-31

### S03 · The lab number
- **Shape:** 2-shocking-number · **Aimed at:** Psychology
- **How:** Experiments with a one-line setup and a single striking number. Search SSRN, NBER, Behavioral Scientist, Choiceology and Hidden Brain episodes, and "study found only X% of people".
- **Started:** 2026-10-31

### S04 · Experiments companies ran
- **Shape:** 2-shocking-number · **Aimed at:** Marketing
- **How:** Field tests and A/B tests that companies, campaigns and governments ran on real customers, with the result as a number. Engineering blogs, case-study writeups, Nudge and Growth Unhinged.
- **Started:** 2026-10-31

### S05 · The call everyone hated
- **Shape:** 3-wrong-decision-worked · **Aimed at:** Founders
- **How:** "Analysts called it a mistake", "the board voted against", "critics said it would never work". Look for named decisions with what happened next. Founders, Acquired, How I Built This.
- **Started:** 2026-10-31

### S06 · The ad that broke the rules
- **Shape:** 3-wrong-decision-worked · **Aimed at:** Marketing
- **How:** Campaigns that insulted the product, told people not to buy, or apologised, and worked anyway. Ad-industry award archives, Everyone Hates Marketers, Marketing Against the Grain.
- **Started:** 2026-10-31

### S07 · One word, one button
- **Shape:** 4-tiny-change · **Aimed at:** Marketing
- **How:** Copy, layout, default or wording changes with a measured lift. Marketing Examples, Growth Unhinged, Nudge.
- **Started:** 2026-10-31

### S08 · Small nudge, big policy
- **Shape:** 4-tiny-change · **Aimed at:** Psychology
- **How:** Behavioural-insights interventions (letters, defaults, form order, reminders) and their measured effect. Behavioural Insights Team reports, government trials, The Decision Lab.
- **Started:** 2026-10-31

### S09 · Before it was famous
- **Shape:** 5-unknown-origin · **Aimed at:** Founders, Marketing
- **How:** "What [famous product or brand] started as". Old company histories, founder biographies, Cautionary Tales, Planet Money, 99% Invisible.
- **Started:** 2026-10-31

### S10 · Day-walk
- **Shape:** 6-day-walk · **Aimed at:** All three pools
- **How:** Walk one slice of an ordinary day (morning, commute, supermarket, office, evening) and ask of each object "why is it like this?" Rotate the slice daily. 99% Invisible and Planet Money are strong here.
- **Started:** 2026-10-31

### S11 · Far-field transplant
- **Shape:** 7-far-field · **Aimed at:** Far field (medicine, sport, military, aviation, biology, craft, AI)
- **How:** A practice from an unrelated field whose principle carries over to business, marketing or the mind. Radiolab, Cautionary Tales, the AI-perspective Substacks.
- **Started:** 2026-10-31

### S12 · Credible voice, odd claim
- **Shape:** 8-unexpected-claim · **Aimed at:** Long-form interview podcasts (Diary of a CEO, Modern Wisdom, Huberman Lab, The Knowledge Project, Founders, How I Built This)
- **How:** Read transcripts of recent episodes for a credentialed or famous person saying something you'd not expect from them. Prefer feeds that ship transcripts. Quote only with a real clip and timestamp.
- **Started:** 2026-10-31

### S13 · Named idea hunt
- **Shape:** 9-unfamiliar-concept · **Aimed at:** Psychology
- **How:** Named effects, biases and ideas most people have never heard of that explain something familiar. The Decision Lab's reference guide, You Are Not So Smart, Hidden Brain, academic glossaries.
- **Started:** 2026-10-31

### S14 · Concept to finds
- **Shape:** Any · **Aimed at:** The concept library
- **How:** The formula done as research. Take a proven concept (from `concepts/`, or a well-known one like friction or loss aversion) and hunt for fresh, concrete evidence of it that hasn't been told everywhere.
- **Started:** 2026-10-31

### S15 · Fresh feed sweep
- **Shape:** Any · **Aimed at:** Seed and discovered sources
- **How:** Read the last 7 days of every source with a feed (`python3 .claude/scripts/feeds.py recent --days 7`) and pull anything rich and novel.
- **Started:** 2026-10-31

### S16 · Lead queue
- **Shape:** Any · **Aimed at:** `brain/leads.md`
- **How:** Dig into the oldest queued leads first, plus any lead you dropped in. Mark each one dug.
- **Started:** 2026-10-31

## Contestants

The unusual dig sites. They are tested, not debated.

### C01 · Court filings
- **Shape:** 1, 3, 5 · **Aimed at:** Founders, Marketing
- **How:** Lawsuits and trial exhibits that reveal how a company really works (internal emails, pricing memos). CourtListener, news coverage of exhibits.
- **Started:** 2026-10-31

### C02 · Patents
- **Shape:** 1, 5 · **Aimed at:** Founders, Marketing
- **How:** Patents behind everyday objects and odd product details. Google Patents, "patent reveals why".
- **Started:** 2026-10-31

### C03 · Old shareholder letters
- **Shape:** 3, 8 · **Aimed at:** Founders
- **How:** Letters from the 1960s to the 2000s with candid reasoning or a surprising admission. Avoid the over-quoted ones (Bezos 1997, Buffett's most famous lines).
- **Started:** 2026-10-31

### C04 · Trade magazines
- **Shape:** 1, 4, 6 · **Aimed at:** Marketing, Founders
- **How:** Industry press that consumers never read (packaging, grocery, hospitality, logistics) explaining why things are the way they are.
- **Started:** 2026-10-31

### C05 · Ex-employee forum threads
- **Shape:** 1, 3 · **Aimed at:** Founders
- **How:** Former staff explaining decisions on Hacker News, Quora, Reddit AMAs, Blind (reached through web search).
- **Started:** 2026-10-31

### C06 · Archived websites
- **Shape:** 5, 4 · **Aimed at:** Marketing, Founders
- **How:** The Wayback Machine for early homepages, first pitches and abandoned taglines of famous companies.
- **Started:** 2026-10-31

### C07 · Dead companies
- **Shape:** 3, 5 · **Aimed at:** Founders
- **How:** Postmortems and the ideas that were right too early. Founder postmortems, failory-style archives, Cautionary Tales. Avoid the over-told (Pets.com, Theranos, Blockbuster).
- **Started:** 2026-10-31

### C08 · Practices from other countries
- **Shape:** 1, 4, 7 · **Aimed at:** All three pools
- **How:** A habit, business practice or design choice that's normal in one country and strange elsewhere, and why it exists.
- **Started:** 2026-10-31

## Retired

<!-- The weekly run moves cut strategies here with the date and the reason. -->

## Changelog

<!-- One dated line per change: bred, retired, promoted. -->
