#!/usr/bin/env python3
"""PostToolUse hook: appends token usage snapshot to changelog/token-usage.md
Runs after Write/Edit in the playground. Throttled to once per hour."""
import sys, json, os, glob, re
from datetime import datetime

data = json.load(sys.stdin)
fp = data.get("tool_input", {}).get("file_path", "")
if "/Users/clark/playground/" not in fp:
    sys.exit(0)

log = "/Users/clark/playground/changelog/token-usage.md"
if os.path.exists(log):
    with open(log) as f:
        content = f.read()
    ts_list = re.findall(r"<!-- hook:(\d+) -->", content)
    if ts_list and (int(datetime.now().timestamp()) - int(ts_list[-1])) < 3600:
        sys.exit(0)

proj = [p for p in glob.glob(os.path.expanduser("~/.claude/projects/*")) if p.endswith("clark-playground")]
if not proj:
    sys.exit(0)
files = sorted(glob.glob(proj[0] + "/*.jsonl"), key=os.path.getmtime, reverse=True)
if not files:
    sys.exit(0)

ti = to = tcr = tcw = 0
with open(files[0]) as f:
    for line in f:
        try:
            u = json.loads(line).get("message", {}).get("usage", {})
            if u:
                ti  += u.get("input_tokens", 0)
                to  += u.get("output_tokens", 0)
                tcr += u.get("cache_read_input_tokens", 0)
                tcw += u.get("cache_creation_input_tokens", 0)
        except:
            pass

cost = ti/1e6*3 + to/1e6*15 + tcr/1e6*0.30 + tcw/1e6*3.75
now = datetime.now().strftime("%Y-%m-%d %H:%M")
ts = int(datetime.now().timestamp())
entry = f"| {now} | {ti:,} | {to:,} | {tcr:,} | ${cost:.4f} | auto-hook snapshot <!-- hook:{ts} -->\n"

with open(log, "a") as f:
    f.write(entry)
