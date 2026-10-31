#!/usr/bin/env python3
"""Write the failure email body: what failed, the exit code, the run link and
the last 30 lines of the log. Reads the workflow's step outcomes from STEPS
(toJSON(steps)), plus CLAUDE_EXIT and RUN_URL, from the environment.
Usage: python3 failure_report.py "Daily run" > _run/failure.md
"""
import json, os, sys
from pathlib import Path

NAMES = {
    "check": "the already-done check",
    "brain": "checking out second-brain (check the SECOND_BRAIN_TOKEN secret)",
    "install": "installing Claude Code and the email library",
    "trust": "marking the workspace trusted",
    "save": "saving the reply and the issue",
    "run": "the Claude Code run",
    "commit": "committing and pushing the two repos",
    "deliver": "creating the issue or sending the email",
    "exitcheck": "the Claude Code run",
}

run_name = sys.argv[1] if len(sys.argv) > 1 else "Run"
steps = json.loads(os.environ.get("STEPS") or "{}")
failed = [k for k, v in steps.items() if v.get("outcome") == "failure"]
code = os.environ.get("CLAUDE_EXIT", "")

print(f"# {run_name} did not complete\n")
print("## What failed\n")
if code and code != "0":
    print(f"Claude Code exited with code {code}.")
elif code:
    print(f"Claude Code ran and exited with code {code}, but {NAMES.get(failed[0], failed[0]) if failed else 'a later step'} failed.")
else:
    where = NAMES.get(failed[0], failed[0]) if failed else "checkout or setup"
    print(f"Claude Code never started; {where} failed.")
if failed:
    print(f"\nFailed steps: {', '.join(failed)}")
print("\n## Full run on GitHub\n")
print(os.environ.get("RUN_URL", "(no run link)"))
print("\n## Last 30 lines of the log\n")
log = Path("_run/run.log")
lines = log.read_text(errors="replace").splitlines()[-30:] if log.exists() and log.stat().st_size else []
print("\n".join("    " + l for l in lines) if lines else "(no log was written)")
