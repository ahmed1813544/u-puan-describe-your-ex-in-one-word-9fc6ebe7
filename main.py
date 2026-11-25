"""Describe Your Ex in One Word.

Writes exactly one word to /output/entry.txt: the single-word verdict
on an ex. Python 3.13 standard library only, no network access.
"""

import os
from pathlib import Path


def main() -> None:
    word = "Unsubscribed"
    # The gate requires exactly one word: no whitespace, 1-111 chars.
    assert word and not any(ch.isspace() for ch in word) and len(word) <= 111
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(word, encoding="utf-8")


if __name__ == "__main__":
    main()
