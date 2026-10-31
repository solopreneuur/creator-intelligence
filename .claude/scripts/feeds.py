#!/usr/bin/env python3
"""Read the feeds listed in brain/sources.md. Standard library only.

Usage:
  python3 .claude/scripts/feeds.py recent --days 7
      Every source with a "- Feed: <url>" line, newest items first:
      source | date | title | link | transcript url (if the feed ships one)
      Sources that fail are listed at the end under FAILED.
  python3 .claude/scripts/feeds.py transcript <url>
      A transcript file (WebVTT, SRT or plain text) as "[hh:mm:ss] text" lines,
      so quotes can be checked and timestamped.
"""
import re, sys, urllib.request
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from xml.etree import ElementTree as ET

SOURCES = Path(__file__).resolve().parents[2] / "brain" / "sources.md"
UA = {"User-Agent": "Mozilla/5.0 (creator-intelligence feed reader)"}
PODCAST_NS = "{https://podcastindex.org/namespace/1.0}"
ATOM = "{http://www.w3.org/2005/Atom}"


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=30).read()


def sources():
    name = None
    for line in SOURCES.read_text().splitlines():
        if line.startswith("### "):
            name = line[4:].strip()
        m = re.match(r"^- Feed: (https?://\S+)", line)
        if m and name:
            yield name, m.group(1)


def parse_date(text):
    text = (text or "").strip()
    for parse in (parsedate_to_datetime, lambda t: datetime.fromisoformat(t.replace("Z", "+00:00"))):
        try:
            d = parse(text)
            return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
        except Exception:
            pass
    return None


def items(xml):
    root = ET.fromstring(xml)
    for it in root.iter("item"):
        tx = it.find(PODCAST_NS + "transcript")
        yield (
            parse_date(it.findtext("pubDate")),
            (it.findtext("title") or "").strip(),
            (it.findtext("link") or "").strip(),
            tx.get("url") if tx is not None else "",
        )
    for it in root.iter(ATOM + "entry"):
        link = it.find(ATOM + "link")
        yield (
            parse_date(it.findtext(ATOM + "published") or it.findtext(ATOM + "updated")),
            (it.findtext(ATOM + "title") or "").strip(),
            link.get("href", "") if link is not None else "",
            "",
        )


def recent(days):
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    rows, failed = [], []
    for name, url in sources():
        try:
            for date, title, link, tx in items(fetch(url)):
                if date and date >= cutoff:
                    rows.append((date, name, title, link, tx))
        except Exception as e:
            failed.append(f"{name} | {url} | {type(e).__name__}: {e}")
    for date, name, title, link, tx in sorted(rows, reverse=True):
        print(" | ".join([name, date.date().isoformat(), title, link] + ([tx] if tx else [])))
    if failed:
        print("\nFAILED")
        print("\n".join(failed))


def transcript(url):
    text = fetch(unescape(url)).decode("utf-8", "replace")
    stamp = None
    for line in text.splitlines():
        line = line.strip()
        m = re.match(r"^(\d{1,2}:)?(\d{2}):(\d{2})[.,]\d+\s+-->", line)
        if m:
            stamp = f"{(m.group(1) or '00:').rstrip(':').zfill(2)}:{m.group(2)}:{m.group(3)}"
            continue
        if not line or line.isdigit() or line == "WEBVTT" or line.startswith("NOTE"):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        print(f"[{stamp}] {line}" if stamp else line)


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "recent":
        days = int(sys.argv[sys.argv.index("--days") + 1]) if "--days" in sys.argv else 7
        recent(days)
    elif len(sys.argv) == 3 and sys.argv[1] == "transcript":
        transcript(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)
