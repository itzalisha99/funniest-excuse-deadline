"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
"""

import os

EXCUSE = (
    "The API rate-limited me at 23:59, so I put the deadline in a retry "
    "queue with exponential backoff. Next attempt: Thursday."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char gate")
    text.encode("utf-8")


def main() -> None:
    validate(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
