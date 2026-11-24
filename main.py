#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.

Stdlib only, no network, deterministic: the same fixed line every run.
"""

import os

LINE = (
    "I deleted the production database. In my defense, it said "
    "'DROP TABLE users' and I thought it was a team-building exercise."
)


def main() -> None:
    # Gate guard: the entry must be 1-200 chars of non-whitespace text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Determinism guard: what we wrote is exactly what we meant to write.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE + "\n", "entry.txt mismatch after write"


if __name__ == "__main__":
    main()
