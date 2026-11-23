#!/usr/bin/env python3
"""Six Words, One Story.

Writes one complete story in exactly six words to /output/entry.txt:
this Christmas, his empty chair burned. Kept for years; one
morning ends it — the reader fills in who struck the match.
"""

import os
import sys

TEXT = (
    "This Christmas, his empty chair burned."
)


def main() -> int:
    # Gate: exactly 6 words, 1 to 60 characters, counted as Unicode
    # code points, and not only white space.
    words = TEXT.split()
    if len(words) != 6 or not (1 <= len(TEXT) <= 60) or not TEXT.strip():
        print("entry text fails the six-word gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # we gated, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != TEXT or len(written.split()) != 6 or not (1 <= len(written) <= 60):
        print("written entry.txt does not match the gated text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
