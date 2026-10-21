"""Compress a Claude Code asciinema cast in time: spinner-only stretches go fast, real output keeps its pace.

Usage: python3 warp.py in.cast out.cast
"""
import json
import os
import re
import sys

ANSI = re.compile(r"\x1b\[[0-9;?<>=:]*[a-zA-Z~]|\x1b[78()=>]|\x1b\][^\x07]*\x07")
USER = os.environ.get("USER", "")
lines = open(sys.argv[1]).read().splitlines()
header, events = lines[0], [json.loads(line) for line in lines[1:] if line.startswith("[")]
# Start at the main UI's first full clear: skips the folder-trust dialog, which shows the absolute path.
first_clear = next(i for i, e in enumerate(events) if "\x1b[2J" in e[2])
events = [[0.0, *events[first_clear][1:]], *events[first_clear + 1:]]
out, clock, paused, started = [header], 0.0, False, False
for delay, kind, data in events:  # asciicast v3: the first field is the delay since the previous event
    if "/exit" in data:  # end on the finished answer, not on the exit screen
        break
    visible = re.sub(r"\s+", "", ANSI.sub("", data))
    spinner_only = len(visible) < 40  # spinner glyph, elapsed seconds, token counter
    if delay >= 12:  # the driver's quiet wait before a follow-up: give the reader time once
        delay = 0.8 if paused or not started else 6.0  # the first gap is the prompt being submitted
        paused, started = True, True
    else:
        paused = paused and len(visible) == 0
        delay = min(delay * (0.15 if spinner_only else 1.0), 0.4 if spinner_only else 2.5)
    data = data.replace("\u00a0", " ")  # agg's font fallback draws a no-break space as an icon
    if USER:  # hide the local username; same length, so cursor columns stay right
        data = data.replace(USER, ("demo" * 8)[: len(USER)])
    out.append(json.dumps([round(delay, 4), kind, data]))
    clock += delay
open(sys.argv[2], "w").write("\n".join(out) + "\n")
print(f"{sys.argv[2]}: {clock:.1f}s after warp")
