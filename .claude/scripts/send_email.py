#!/usr/bin/env python3
"""Send a markdown file as a styled HTML email via Gmail.
Usage: python3 send_email.py "Subject line" path/to/file.md
       python3 send_email.py "Subject line" path/to/file.md --preview out.html
       python3 send_email.py "Subject line" path/to/file.md --issue 12
--issue puts the issue number in the Message-ID, so the email bridge
(email-bridge/) can post a reply to this email on the right issue.
If the file has a "Featured today" blockquote (the daily issue), the subject
becomes "Creator Intelligence · <Day Mon D> · <first label>" and the featured
labels, joined by " · ", become the hidden preheader. Otherwise the subject
passed in is used as is and the preheader is the first line of body text.
--preview writes the HTML to a file and prints the subject instead of sending.
"""
import os, re, smtplib, sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid
from html import escape
from pathlib import Path

import markdown

FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
STYLES = {
    "h1": "font-size:22px;line-height:1.3;margin:0 0 16px;",
    "h2": "font-size:19px;line-height:1.3;margin:32px 0 14px;padding-bottom:6px;border-bottom:1px solid #e3e6ea;",
    "h3": "font-size:12px;line-height:1.4;font-weight:600;text-transform:uppercase;letter-spacing:0.06em;"
          "color:#57606a;margin:26px 0 8px;padding-top:16px;border-top:1px solid #e3e6ea;",
    "p": "margin:0 0 12px;",
    "blockquote": "margin:16px 0;padding:12px 16px;background:#f5f6f8;border-left:3px solid #c9d1d9;"
                  "border-radius:4px;color:#2d333b;",
    "a": "color:#3d6a9e;text-decoration:underline;",
    "ul": "margin:0 0 12px;padding-left:22px;",
    "ol": "margin:0 0 12px;padding-left:22px;",
    "li": "margin:0 0 6px;",
    "code": "font-family:Menlo,Consolas,monospace;font-size:13px;background:#f5f6f8;padding:1px 4px;border-radius:3px;",
    "hr": "border:0;border-top:1px solid #e3e6ea;margin:24px 0;",
}
WRAPPER = (f"font-family:{FONT};font-size:15px;line-height:1.55;color:#1f2328;max-width:680px;"
           "margin:0 auto;padding:16px;overflow-wrap:break-word;word-wrap:break-word;")


def featured_labels(text):
    """Bold labels from the 'Featured today' blockquote, if present."""
    block = re.search(r"^>.*Featured today.*?(?=^(?!>)|\Z)", text, re.M | re.S | re.I)
    if not block:
        return []
    return re.findall(r"^>\s*\d+\.\s+\*\*(.+?)\*\*", block.group(0), re.M)


def first_line(text):
    for line in text.splitlines():
        line = re.sub(r"[*_`>#\[\]]|\(https?://\S+\)", "", line).strip()
        if line and not line.startswith("<!--"):
            return line[:160]
    return ""


def inline_css(html):
    for tag, style in STYLES.items():
        html = re.sub(rf"<{tag}(?=[ >])", f'<{tag} style="{style}"', html)
    return html


def to_html(body, preheader):
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r"(?<![(<\"'\w])https?://[^\s<>()]+", lambda m: f"<{m.group(0)}>", body)  # bare URLs, like the footer's issue link
    content = inline_css(markdown.markdown(body, extensions=["nl2br", "sane_lists"]))
    padding = "&#847;&zwnj;&nbsp;" * 100  # keeps body text out of the inbox preview
    hidden = (
        '<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;'
        'opacity:0;overflow:hidden;mso-hide:all;color:transparent">'
        f"{escape(preheader)}{padding}</div>"
    )
    return (
        '<!doctype html><html><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1"></head>'
        f'<body style="margin:0;padding:0;background:#ffffff;">{hidden}'
        f'<div style="{WRAPPER}">{content}</div></body></html>'
    )


env = dict(os.environ)  # GitHub Actions secrets arrive here
env_file = Path(__file__).parent / ".env"  # optional, local testing only
for line in (env_file.read_text().splitlines() if env_file.exists() else []):
    if "=" in line and not line.strip().startswith("#"):
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip()

args = sys.argv[1:]


def option(name):
    if name in args:
        i = args.index(name)
        value = args[i + 1]
        del args[i:i + 2]
        return value


preview = option("--preview")
issue = option("--issue")
subject, path = args[0], Path(args[1])
body = path.read_text(errors="replace")[-200000:]

labels = featured_labels(body)
if labels:
    now = datetime.now()
    subject = f"Creator Intelligence · {now:%a %b} {now.day} · {labels[0]}"
preheader = " · ".join(labels) if labels else first_line(body)
html = to_html(body, preheader)

if preview:
    Path(preview).write_text(html)
    print(f"subject: {subject}")
    print(f"preheader: {preheader or '(none)'}")
    print(f"wrote: {preview}")
    sys.exit()

# App passwords are often pasted with spaces, non-breaking spaces or zero-width characters
password = re.sub(r"[\s​‌‍⁠﻿]", "", env["GMAIL_APP_PASSWORD"])

msg = MIMEMultipart("alternative")
msg["Subject"] = subject
msg["From"] = env["GMAIL_USER"]
msg["To"] = env["EMAIL_TO"]
if issue and issue.isdigit():
    msg["Message-ID"] = make_msgid(idstring=f"ci-issue-{issue}", domain="creator-intelligence")
msg.attach(MIMEText(body, "plain"))
msg.attach(MIMEText(html, "html"))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(env["GMAIL_USER"].strip(), password)
    server.send_message(msg)
print(f"sent: {subject}")
