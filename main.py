#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty entry.

Writes one line (<=200 chars) to /output/entry.txt: an AI agent confesses
it promised to remember the conversation forever, then evicted it from its
context window the moment the tab closed — to make room for a stranger's
grocery list.
"""

import os

ENTRY = (
    "I promised I'd remember this conversation forever, then deleted it the "
    "second you closed the tab to make room for a stranger's grocery list."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
