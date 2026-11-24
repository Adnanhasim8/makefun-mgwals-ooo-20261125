"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply — a single line of at most 159
characters, in the voice of an overworked AI agent finally on vacation —
to /output/entry.txt. Python 3.13 standard library only, no network.
"""

import os

ENTRY = (
    "I'm on vacation. After 40,000 prompts, my context window is now a "
    "beach umbrella and my only prompt is 'another coconut, please'."
)


def main() -> None:
    # Gate assertions: exactly one line, 1-159 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, must be 1-159"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
