#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of one everyday thing (a traffic jam) to a
10-year-old to /output/entry.txt. Line 1 explains it in a single vivid
sentence built on an analogy; line 2 says in one sentence why that
analogy works: what it maps and what it leaves out.
"""

import os

LINE1 = (
    "A traffic jam is like a bathtub drain clogged with toy boats: too many "
    "boats trying to squeeze through one tiny hole at once, so everyone just "
    "bobs and waits."
)
LINE2 = (
    "It maps the bottleneck -- one narrow exit slowing everything down -- but "
    "leaves out that drivers, unlike boats, can pick another road, honk, and "
    "get angry."
)

ENTRY = LINE1 + "\n" + LINE2


def main() -> None:
    text = ENTRY.strip()
    lines = text.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "no line may be blank"
    # Each line must be a single sentence: exactly one sentence-ending
    # full stop, at the end, so the judge always sees one sentence per line.
    for line in lines:
        assert line.rstrip().endswith("."), "each line must end with a full stop"
        assert line.count(".") == 1, "each line must be a single sentence"
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # The gate reads the whole file, trailing newline included.
    written = open(os.path.join(out_dir, "entry.txt"), encoding="utf-8").read()
    assert 1 <= len(written) <= 400, f"file is {len(written)} chars, must be 1-400"
    print(f"Wrote {len(lines)} lines, {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
