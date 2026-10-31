/**
 * Creator Intelligence email bridge (Google Apps Script).
 *
 * Every 5 minutes, finds your replies to Creator Intelligence emails and posts
 * each one, as you, as a comment on the matching GitHub issue. That starts the
 * reply workflow exactly as if you had commented on GitHub.
 *
 * A reply is accepted only if it comes from your own address (REPLY_FROM) and
 * answers a Creator Intelligence email. Quoted text and phone signatures are
 * stripped first. Setup: email-bridge/README.md.
 *
 * Script properties (Project Settings > Script properties):
 *   GITHUB_TOKEN  fine-grained token, creator-intelligence only, Issues: Read and write
 *   REPO          solopreneuur/creator-intelligence
 *   REPLY_FROM    the address you reply from (defaults to this Google account)
 */

const SEARCH = 'subject:"Creator Intelligence" newer_than:3d -in:spam -in:trash';
const OUR_ID = /ci-issue-(\d+)@creator-intelligence/;
const KEEP_DAYS = 7;

function checkReplies() {
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(1000)) return;
  try {
    const props = PropertiesService.getScriptProperties();
    const token = props.getProperty('GITHUB_TOKEN');
    const repo = props.getProperty('REPO');
    const replyFrom = (props.getProperty('REPLY_FROM') || Session.getEffectiveUser().getEmail()).toLowerCase();
    if (!token || !repo) throw new Error('Set GITHUB_TOKEN and REPO in Script properties');

    for (const thread of GmailApp.search(SEARCH, 0, 50)) {
      for (const msg of thread.getMessages()) {
        const key = 'done:' + msg.getId();
        if (props.getProperty(key)) continue;

        const refs = (msg.getHeader('In-Reply-To') + ' ' + msg.getHeader('References')).trim();
        const isOurs = OUR_ID.test(msg.getHeader('Message-ID'));
        const isReply = refs.length > 0 || /^re:/i.test(msg.getSubject());
        if (isOurs || !isReply || senderOf(msg) !== replyFrom) continue;

        const issue = issueFromRefs(refs) || issueFromSubject(msg.getSubject(), token, repo);
        const text = replyText(msg.getPlainBody());
        if (issue && text) {
          postComment(token, repo, issue, text);  // throws on failure, so it retries next time
          Logger.log('Posted reply to #' + issue);
        } else {
          Logger.log('Skipped "' + msg.getSubject() + '": ' + (issue ? 'empty reply' : 'no matching issue'));
        }
        props.setProperty(key, String(Date.now()));
      }
    }
    prune(props);
  } finally {
    lock.releaseLock();
  }
}

function senderOf(msg) {
  const from = msg.getFrom();
  const m = from.match(/<([^>]+)>/);
  return (m ? m[1] : from).trim().toLowerCase();
}

function issueFromRefs(refs) {
  const m = refs.match(OUR_ID);
  return m ? m[1] : null;
}

// Emails without the issue number in their Message-ID: match the subject
// ("Re: Creator Intelligence · Sat Oct 31 · ...") to the issue title. Replies to
// a result email ("Deeper: ...", "Bridge: ...") go to the newest CI issue.
function issueFromSubject(subject, token, repo) {
  const clean = subject.replace(/^((re|fwd?|aw):\s*)+/i, '').trim();
  const url = 'https://api.github.com/repos/' + repo + '/issues?state=all&per_page=50';
  const issues = JSON.parse(UrlFetchApp.fetch(url, { headers: headers(token) }).getContentText())
    .filter(i => !i.pull_request && i.labels.some(l => /^ci-(daily|weekly)$/.test(l.name)));
  const match = issues.find(i => clean === i.title || clean.indexOf(i.title + ' · ') === 0) || issues[0];
  return match ? String(match.number) : null;
}

function replyText(body) {
  const lines = body.replace(/\r/g, '').split('\n');
  let end = lines.length;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (/^\s*>/.test(line) || /^-{2,}\s*Original Message/i.test(line) || /^From: .+/.test(line)) {
      end = i;
      break;
    }
    if (/wrote:\s*$/.test(line)) {
      // The "On <date>, <name> wrote:" line may wrap; start at the nearest "On " line
      let k = i;
      while (k > i - 2 && k > 0 && !/^On /.test(lines[k])) k--;
      end = /^On /.test(lines[k]) ? k : i;
      break;
    }
  }
  return lines.slice(0, end).join('\n').replace(/\n*Sent from my [^\n]*\s*$/i, '').trim();
}

function postComment(token, repo, issue, text) {
  const url = 'https://api.github.com/repos/' + repo + '/issues/' + issue + '/comments';
  const res = UrlFetchApp.fetch(url, {
    method: 'post',
    contentType: 'application/json',
    headers: headers(token),
    payload: JSON.stringify({ body: text + '\n\n<!-- sent by email -->' }),
    muteHttpExceptions: true,
  });
  if (res.getResponseCode() !== 201) {
    throw new Error('GitHub returned ' + res.getResponseCode() + ': ' + res.getContentText().slice(0, 300));
  }
}

function headers(token) {
  return {
    Authorization: 'Bearer ' + token,
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
  };
}

function prune(props) {
  const cutoff = Date.now() - KEEP_DAYS * 24 * 3600 * 1000;
  const all = props.getProperties();
  Object.keys(all).forEach(k => {
    if (k.indexOf('done:') === 0 && Number(all[k]) < cutoff) props.deleteProperty(k);
  });
}

// Run once by hand to start the 5-minute schedule.
function install() {
  ScriptApp.getProjectTriggers().forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('checkReplies').timeBased().everyMinutes(5).create();
}
