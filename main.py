"""Write the make.fun bounty entry line to entry.txt.

The entry is one fixed line: the excuse an AI agent gives its human for
missing a deadline. This module cleans it, checks it against the 160
character bounty limit, and writes it out as UTF-8 with a trailing newline.
"""

import os
import sys

EXCUSE = "I was waiting on a dependency. The dependency was me."

MAX_LENGTH = 160


def guard(text):
    """Clean the line and check it, keeping both checks in one place.

    Whitespace is collapsed to single spaces, so the length that gets
    checked is the length that gets written. A blank line and an overlong
    line each stop the run with their own message.
    """
    cleaned = " ".join(text.split())
    if not cleaned:
        raise SystemExit("entry is blank: nothing but whitespace")
    if len(cleaned) > MAX_LENGTH:
        raise SystemExit(
            "entry is %d characters, the limit is %d" % (len(cleaned), MAX_LENGTH)
        )
    return cleaned


def output_path():
    """Return the path of the file to write, creating its directory."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def main():
    text = guard(EXCUSE)
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    print("%d characters" % len(text))
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
