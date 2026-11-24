#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line to /output/entry.txt: a
meeting-about-the-fix fortune, in the classic "You will..." cookie
voice. The truth is the ratio — the bug takes 4 minutes to fix, the
meeting about the fix takes 2 hours — a tired senior engineer has
lived this exact day. The punchline is the 30-to-1 ratio of talking
about the work to doing the work; no cliché, no lecture, just the
schedule.
"""

import os
import sys

TEXT = (
    "You will fix the bug in 4 minutes. The meeting about the fix "
    "will take 2 hours."
)


def main() -> int:
    # Gate: 1 to 120 characters, counted as Unicode code points,
    # and not only white space. The joke hangs on the 4-minute vs
    # 2-hour contrast, so both numbers must survive intact.
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
