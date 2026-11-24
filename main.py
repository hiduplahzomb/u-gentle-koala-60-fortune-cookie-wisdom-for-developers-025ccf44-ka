#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line to /output/entry.txt: a
Friday-afternoon deploy fortune, in the classic "You will..." cookie
voice. The truth is the timing — Friday 4:59 PM ships, Monday 9:03 AM
is when the bug introduces itself — a tired senior engineer has lived
this exact week. Two concrete times carry the joke; no cliché, no
lecture, just the schedule.
"""

import os
import sys

TEXT = (
    "You will ship on Friday at 4:59 PM. The bug will introduce "
    "itself Monday at 9:03 AM."
)


def main() -> int:
    # Gate: 1 to 120 characters, counted as Unicode code points,
    # and not only white space.
    if not (1 <= len(TEXT) <= 120) or not TEXT.strip():
        print("entry text fails the 1-120 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # the program claims to have written.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
