"""Convert measured word intervals to display frames on the final audio clock."""
import json
import math
import sys
from pathlib import Path

source, rate, length, destination = sys.argv[1:]
fps, total = int(rate), int(length)
rows = json.loads(Path(source).read_text())
if not rows or min(fps, total) <= 0:
    raise ValueError("Empty speech or invalid composition")
previous = 0
for row in rows:
    start, end = row["start"], row["end"]
    if not (row["word"].strip() and previous <= start < end <= total / fps):
        raise ValueError(f"Invalid measured interval: {row}")
    previous = end
    row["startFrame"] = math.floor(start * fps + 1e-8)
    row["endFrame"] = min(total, math.ceil(end * fps - 1e-8))
for left, right in zip(rows, rows[1:]):
    left["endFrame"] = min(left["endFrame"], right["startFrame"])
    if left["endFrame"] <= left["startFrame"]:
        raise ValueError("Two word onsets occupy one frame; group that cue or raise fps")
Path(destination).write_text(json.dumps(rows, ensure_ascii=False, indent=2))
