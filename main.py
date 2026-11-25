#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true, single-line review of a boring everyday object
(a rubber band) to /output/entry.txt. Deterministic: no input, no network,
no randomness, no clock — the same bytes on every run.
"""

import os

ENTRY = (
    "Five stars. The rubber band held my cables together for two years, "
    "then snapped without warning and now lies on the floor as a tiny "
    "beige corpse nobody will pick up."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
