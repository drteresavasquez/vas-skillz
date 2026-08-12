#!/usr/bin/env python3
"""Example deterministic helper script for example-skill.

Skills should put executable logic like this here rather than describing it
in prose in SKILL.md — Claude can run the script without loading its source
into context.
"""

import sys


def main() -> int:
    args = sys.argv[1:]
    print(f"example-skill script ran with args: {args}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
