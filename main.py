#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single confession line (max 200 chars) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

LINE = (
    "I ran the migration on production because the dropdown said 'prod' "
    "and I thought it was short for 'productivity'."
)


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= 200, f"entry is {len(line)} chars, over the 200 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
