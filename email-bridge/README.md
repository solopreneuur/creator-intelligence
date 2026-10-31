# Email bridge

Lets you reply to any Creator Intelligence email instead of commenting on the
GitHub issue. A Google Apps Script checks Gmail every 5 minutes and posts each
reply, as you, as a comment on the matching issue. The reply workflow then runs
as normal and emails you the result.

## How it finds the issue

Every email the workflows send has a Message-ID carrying its issue number
(`...ci-issue-12@creator-intelligence`), and your reply quotes that ID in its
headers. For emails sent before this existed, it matches the subject to the
issue title instead.

## What it accepts

Only replies from your own address (`REPLY_FROM`) that answer a Creator
Intelligence email. It skips the emails the workflows send, cuts everything from
the quoted part down ("On … wrote:", `>` lines, "Original Message") and a
trailing "Sent from my iPhone", and posts what's left. Each reply is posted once.

## Setup (about 5 minutes)

1. **Which Gmail account.** Replies go to the address the emails come from:
   the `GMAIL_USER` secret. Do these steps signed in to that account. If it's
   not the address you read and reply from, set `REPLY_FROM` (step 4) to the
   address you reply from.
2. **A GitHub token for the bridge.** Fine-grained token, resource owner
   `solopreneuur`, repository access **only creator-intelligence**, repository
   permission **Issues: Read and write**. The comment is posted as you, which is
   what lets the reply workflow accept it.
3. **The script.** Go to [script.google.com](https://script.google.com), click New
   project, name it "Creator Intelligence email bridge", replace the contents of
   `Code.gs` with this folder's `Code.gs`, and save.
4. **Script properties.** Project Settings (gear icon) > Script properties > Add:
   - `GITHUB_TOKEN`: the token from step 2
   - `REPO`: `solopreneuur/creator-intelligence`
   - `REPLY_FROM`: optional; the address you reply from, if it isn't this account
5. **Start it.** Back in the editor, pick `install` in the function dropdown and
   click Run. Approve the permissions (Gmail read, external requests, triggers).
   Google warns the app is unverified because it's your own script: Advanced >
   Go to project.
6. **Test it.** Pick `checkReplies` and click Run, then open Executions to see the
   log. Replies from the last 3 days are picked up on the first run.

To stop it, delete the trigger under Triggers (alarm-clock icon).
