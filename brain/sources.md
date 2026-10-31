# Sources

Seeds, contestants and discovered sources. Seeds are a starting point, not a
boundary.

Every source was checked on 2026-10-31 from a home connection: feed fetched, latest
item dated, and a recent episode probed for a transcript. GitHub's runners have
not been tested yet. The first scheduled run is that test, and any source that
fails there is named at the top of that day's email.

**How to reach a source:**

- `Feed:` lines are read by `python3 .claude/scripts/feeds.py recent --days 7`. Keep the
  `- Feed: <url>` format exactly so the script finds them.
- **Transcripts** come in three tiers:
  - **feed**: a `podcast:transcript` file in the RSS item. Reliable from any
    machine. Read with `python3 .claude/scripts/feeds.py transcript <url>`.
  - **page**: the transcript is on the episode's web page. Use WebFetch.
  - **none**: use show notes, then web search for coverage or a YouTube
    transcript.
- **YouTube** often blocks transcript fetches from data-centre machines such as
  GitHub's. Treat YouTube as a place to confirm a clip and timestamp exists, not
  as a reliable transcript source.

Pools: far-field sources supply shape 7 material. Each card still gets one of the
three pools: the pool its principle carries into.

## Seeds

### Nudge (Phill Agnew)
- Type: Podcast · Pool: Marketing · Shapes: 2, 1
- Status: active (latest 2026-10-26)
- Feed: https://feeds.megaphone.fm/HS2038060283
- Transcripts: none in feed, no episode page link. Use show notes and web search.

### Everyone Hates Marketers (Louis Grenier)
- Type: Podcast · Pool: Marketing · Shapes: 3, 4
- Status: **slowing**: latest episode 2026-06-18, nothing in the four months since. Still worth digging for its archive.
- Feed: https://feeds.transistor.fm/everyone-hates-marketers
- Transcripts: feed (263 of 309 episodes ship a transcript file)

### Marketing Against the Grain
- Type: Podcast (HubSpot) · Pool: Marketing · Shapes: 4, 3
- Status: active (latest 2026-10-29)
- Feed: https://feeds.megaphone.fm/marketingagainstthegrain
- Transcripts: none in feed. Episodes are also on YouTube.

### Marketing Examples (Harry Dry)
- Type: Newsletter · Pool: Marketing · Shapes: 1, 4
- Status: active site (marketingexamples.com, 2026 content present)
- Feed: **none**. /rss and /feed return 404.
- Reach: WebFetch https://marketingexamples.com and its category pages, or web search `site:marketingexamples.com`.

### Rory Sutherland's talks
- Type: Talks (YouTube, conferences, podcast guest spots) · Pool: Marketing · Shapes: 1, 3, 8
- Status: active (2026 talks found: RESET keynote in August, Creativity4Better on 12 November, podcast guest spots in June and July)
- Feed: none, not a single channel
- Reach: web search "Rory Sutherland" + topic. His Knowledge Project episodes have fs.blog pages. For a shape 8 quote, confirm the clip and timestamp on the video or podcast page.

### Growth Unhinged (Kyle Poyar)
- Type: Newsletter · Pool: Marketing · Shapes: 4
- Status: active, but **moved** from Substack to beehiiv at www.growthunhinged.com. The old feed's last post (2026-01-12) is the move notice.
- Feed: none found on the new site (/feed, /rss and /rss.xml all 404)
- Reach: WebFetch https://www.growthunhinged.com/archive (lists /p/ posts)

### Choiceology (Katy Milkman)
- Type: Podcast (Charles Schwab) · Pool: Psychology · Shapes: 2, 3
- Status: active (latest 2026-10-19)
- Feed: https://feeds.schwab.com/choiceology
- Transcripts: page (schwab.com episode pages carry the transcript)

### Hidden Brain
- Type: Podcast · Pool: Psychology · Shapes: 2, 9
- Status: active (latest 2026-10-26)
- Feed: https://feeds.simplecast.com/kwWc0lhf
- Transcripts: none in feed, and the feed links only to the homepage. Search hiddenbrain.org for the episode page.

### You Are Not So Smart (David McRaney)
- Type: Podcast · Pool: Psychology · Shapes: 2, 9
- Status: active (latest 2026-10-26)
- Feed: https://feeds.simplecast.com/N5eKDxJI
- Transcripts: page (youarenotsosmart.com posts often include them)

### Modern Wisdom (Chris Williamson)
- Type: Podcast · Pool: Psychology · Shapes: 8, 9
- Status: active (latest 2026-10-31)
- Feed: https://feeds.megaphone.fm/SIXMSB5088139739
- Transcripts: none. YouTube for clips and timestamps.

### Huberman Lab
- Type: Podcast · Pool: Psychology · Shapes: 2, 8, 9
- Status: active (latest 2026-10-29)
- Feed: https://feeds.megaphone.fm/hubermanlab
- Transcripts: page (hubermanlab.com episode pages, with timestamps in show notes)

### Behavioral Scientist
- Type: Publication · Pool: Psychology · Shapes: 2, 9
- Status: active (latest 2026-10-15)
- Feed: https://behavioralscientist.org/feed/

### The Decision Lab
- Type: Publication · Pool: Psychology · Shapes: 9, 2
- Status: active (sitemap updated 2026-10-29; more than 500 reference-guide pages, about 120 bias pages)
- Feed: **none** (/feed and /rss.xml return 404)
- Reach: WebFetch https://thedecisionlab.com/biases and /reference-guide, or web search `site:thedecisionlab.com`.

### SSRN and NBER working papers
- Type: Research archives, searched rather than followed · Pool: Psychology, Founders · Shapes: 2
- Status: NBER active. SSRN blocks direct automated requests (403).
- Feed: https://www.nber.org/rss/new.xml
- Reach: web search `site:ssrn.com` or `site:nber.org` + topic. Read SSRN abstracts through search results, not direct fetches.

### Founders (David Senra)
- Type: Podcast · Pool: Founders · Shapes: 3, 5, 8
- Status: active (latest 2026-10-26)
- Feed: https://feeds.megaphone.fm/DSLLC6297708582
- Transcripts: none in feed. Show notes name the book, so go to the book for the facts.

### Acquired
- Type: Podcast · Pool: Founders · Shapes: 3, 5
- Status: active (latest 2026-10-23)
- Feed: https://feeds.transistor.fm/acquired
- Transcripts: page (acquired.fm episode pages carry full transcripts). Some feed items ship transcripts too.

### How I Built This (Guy Raz)
- Type: Podcast (now Vox Media) · Pool: Founders · Shapes: 3, 5, 8
- Status: active (latest 2026-10-29)
- Feed: https://feeds.megaphone.fm/VMP2035168248
- Transcripts: none in feed. Older NPR-era episodes have transcripts on npr.org.

### The Diary of a CEO (Steven Bartlett)
- Type: Podcast · Pool: Founders, Psychology · Shapes: 8
- Status: active (latest 2026-10-30)
- Feed: https://rss2.flightcast.com/xmsftuzjjykcmqwolaqn6mdn
- Transcripts: feed (WebVTT with timestamps on 658 of 904 items). Best source for shape 8.

### The Knowledge Project (Shane Parrish)
- Type: Podcast · Pool: All three · Shapes: 8
- Status: active (latest 2026-10-27)
- Feed: https://feeds.megaphone.fm/FSMI7575968096
- Transcripts: page, partly. fs.blog episode pages. Full transcripts may be for members only.

### Erik Torenberg
- Type: Substack · Pool: Founders · Shapes: 3
- Status: active (latest 2026-10-02)
- Feed: https://eriktorenberg.substack.com/feed

### 99% Invisible
- Type: Podcast · Pool: Far-field · Shapes: 1, 6
- Status: active (latest 2026-10-30)
- Feed: https://feeds.simplecast.com/BqbsxVfO
- Transcripts: page (99percentinvisible.org episode pages)

### Cautionary Tales (Tim Harford)
- Type: Podcast (Pushkin) · Pool: Far-field · Shapes: 3, 5
- Status: active (latest 2026-10-30)
- Feed: https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/c0ae8c6e-22f0-4e9b-ac1c-ae390037ac53/7f5a4714-6b10-4ccf-a424-ae390037ac70/podcast.rss
- Transcripts: feed (SRT and WebVTT with timestamps)

### Planet Money
- Type: Podcast (NPR) · Pool: Far-field · Shapes: 1, 5
- Status: active (latest 2026-10-31)
- Feed: https://feeds.npr.org/510289/podcast.xml
- Transcripts: page (npr.org story pages link a transcript)

### Radiolab
- Type: Podcast (WNYC) · Pool: Far-field · Shapes: 7
- Status: active (latest 2026-10-30)
- Feed: https://feeds.simplecast.com/EmVW7VGp
- Transcripts: none in feed, and items link only to the homepage. Search radiolab.org for the episode page.

### r/todayilearned
- Type: Community · Pool: All three · Shapes: 5, 1
- Status: active
- Feed: none (deliberately left out). The RSS worked from a home connection, but Reddit blocks most automated access from data centres.
- Reach: web search `site:reddit.com/r/todayilearned` + topic. Always follow the TIL to its own source link and cite that, not the thread.

### The Algorithmic Bridge
- Type: Substack · Pool: Far-field, AI perspective · Shapes: 9, 8
- Status: active (latest 2026-10-29)
- Feed: https://www.thealgorithmicbridge.com/feed

### Gary Marcus
- Type: Substack · Pool: Far-field, AI perspective · Shapes: 8
- Status: active (latest 2026-10-31)
- Feed: https://garymarcus.substack.com/feed

### Digital Minds
- Type: Substack · Pool: Far-field, AI perspective · Shapes: 9
- Status: active but **low volume** (latest 2026-09-17; only 4 posts in the feed)
- Feed: https://www.digitalminds.news/feed

## Contestants

### The Joe Rogan Experience
- Type: Podcast · Pool: All three · Shapes: 8
- Status: active (latest 2026-10-31). Contestant: long episodes with a low useful-to-unrelated ratio, but rich in quotes.
- Feed: https://feeds.megaphone.fm/GLT1412515089
- Transcripts: none. Confirm clips and timestamps on YouTube.

### Dostoevsky's Blog
- Type: Substack · Pool: Psychology · Shapes: 9
- Status: **dormant**: latest post 2025-11-02, almost a year ago. Claims may come without sources (written with AI), so verify every one.
- Feed: https://dostoevskysblog.substack.com/feed

### exponent (Toni Witt)
- Type: Substack · Pool: Far-field · Shapes: 7, 9
- Status: active (latest 2026-09-12)
- Feed: https://toniwitt.substack.com/feed

### The Substack Post
- Type: Substack (Substack's official blog) · Pool: Marketing · Shapes: 4
- Status: active (latest 2026-10-31)
- Feed: https://post.substack.com/feed

### Propel Earth
- Type: Substack · Pool: Founders · Shapes: 3
- Status: **nearly empty**: one post in the feed, dated 2026-03-05. Likely to produce nothing.
- Feed: https://propelearth1.substack.com/feed

### The unusual dig sites
- Court filings, patents, old shareholder letters, trade magazines, ex-employee forum threads, archived websites, dead companies, practices from other countries.
- Reached through web search. Each is a strategy contestant in `strategies.md` (C01 to C08), scored there.

## Discovered

<!-- The daily run notes candidate sources on the scoreboard. The weekly run
promotes ones that keep producing kept cards. Format as above, plus:
- Discovered: YYYY-MM-DD, from card <id>
-->
