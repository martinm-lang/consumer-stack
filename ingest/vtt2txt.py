#!/usr/bin/env python3
"""Convert YouTube auto-sub VTT files to clean plain-text transcripts.

YouTube auto-subs repeat lines as rolling captions; we dedupe consecutive
duplicates and strip inline timing tags.
"""
import re
import sys
from pathlib import Path

TAG = re.compile(r"<[^>]+>")
TS_LINE = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3} --> ")


def vtt_to_text(path: Path) -> str:
    lines = []
    last = None
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if (not line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE"))
                or TS_LINE.match(line) or line.isdigit()):
            continue
        line = TAG.sub("", line).strip()
        if not line or line == last:
            continue
        lines.append(line)
        last = line
    # collapse the rolling-window duplication: drop a line if it equals the previous
    out = []
    for line in lines:
        if out and (line in out[-1] or out[-1] in line):
            out[-1] = line if len(line) >= len(out[-1]) else out[-1]
            continue
        out.append(line)
    return "\n".join(out)


def main() -> None:
    subs_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("subs")
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("transcripts")
    out_dir.mkdir(exist_ok=True)
    for vtt in sorted(subs_dir.glob("*.vtt")):
        video_id = vtt.name.split(".")[0]
        txt = out_dir / f"{video_id}.txt"
        txt.write_text(vtt_to_text(vtt), encoding="utf-8")
        print(f"{video_id}: {txt.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
