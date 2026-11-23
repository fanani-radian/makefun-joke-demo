#!/usr/bin/env python3
"""Entry program for make.fun competition the-joke-about-the-demo-20261123-0112.

Writes one line — a joke about working beside AI coding agents — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: no randomness, no network, no clock. The same bytes every run.
"""

import os
import sys

JOKE = (
    "Working beside an AI coding agent is like pair programming with a genius "
    "who never sleeps, types at 200 wpm, and is absolutely certain about the "
    "one function it got completely wrong."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # One line, no trailing newline: exactly the joke, 182 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
