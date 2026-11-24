#!/usr/bin/env python3
"""One Word From Your Ex.

Writes exactly one word to /output/entry.txt: the word an ex would use
to describe the author. The program is deterministic and stdlib-only.

The word is "forgettable". It is the most painfully honest one-word
self-portrait an ex could offer: not an insult thrown in anger, but the
quiet verdict that you never quite registered at all. It stings because
it is true, it lands instantly, and anyone who has ever been on either
side of a fading relationship recognises it at once.
"""

import os

WORD = "forgettable"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify: the entry must be exactly one word, no newline.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD, f"entry mismatch: {written!r} != {WORD!r}"
    assert written.strip() == written and len(written.split()) == 1


if __name__ == "__main__":
    main()
