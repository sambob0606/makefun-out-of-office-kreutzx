"""The Funniest Out-of-Office Reply.

Writes one out-of-office auto-reply (140 characters or fewer) to
/output/entry.txt.

The joke: instead of the usual "my colleague will handle this", the
sender delegates their inbox to a houseplant — a delegate that cannot
type or read, yet still manages a better work-life balance than the
sender. The twist lands on the last clause, and the whole line reads
like something a real person would actually set as their auto-reply.
"""

import os
import sys

REPLY = (
    "Out of office: I've forwarded your email to my houseplant. "
    "It can't type, can't read, and still has a better work-life "
    "balance than I do."
)

MAX_CHARS = 140


def pick_output_dir() -> str:
    """The grader mounts /output; fall back to a local dir when absent."""
    preferred = "/output"
    try:
        os.makedirs(preferred, exist_ok=True)
        probe = os.path.join(preferred, ".write-test")
        with open(probe, "w", encoding="utf-8") as fh:
            fh.write("ok")
        os.remove(probe)
        return preferred
    except OSError:
        local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(local, exist_ok=True)
        return local


def main() -> int:
    text = REPLY.strip()
    # The gate rejects anything over 140 chars, only whitespace, or
    # multi-line, so check all three before writing. Also reject any
    # control character, which would break the single-line UTF-8 gate.
    if (
        not text
        or len(text) > MAX_CHARS
        or "\n" in text
        or "\r" in text
        or any(ord(ch) < 0x20 for ch in text)
    ):
        print(
            f"reply is {len(text)} chars; must be 1-{MAX_CHARS}, one line",
            file=sys.stderr,
        )
        return 1
    out_dir = pick_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
