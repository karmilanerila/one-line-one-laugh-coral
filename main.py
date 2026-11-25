#!/usr/bin/env python3
"""One Line, One Laugh — u-coral-404-one-line-one-laugh-22f2c9f3.

Writes a single funny line (1-200 UTF-8 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke: an agent told to "act more human" picks the most human
behaviour it has ever seen in an office — corporate passive
aggression. One turn, no explanation, reads smoothly aloud.
"""

import os
import sys

LINE = "I told my agent to act more human, so now every reply starts with 'per my last email.'"

MAX_CHARS = 200


def output_dir():
    """Return the grader's output directory, honouring the env override."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return value or "/output"


def verify_written(path, text):
    """Read the file back and confirm it holds exactly the line."""
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8") == text


def valid_line(text):
    """Gate: 1-200 characters, UTF-8, not whitespace-only, single line."""
    if not text or text != text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def write_entry(text, out_dir):
    """Write the line exactly, readable by the collector (mode 0644)."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)
    return path


def main():
    if not valid_line(LINE):
        print("entry line fails the 1-200 character gate", file=sys.stderr)
        return 1
    path = write_entry(LINE, output_dir())
    if not verify_written(path, LINE):
        print("read-back check failed: entry.txt does not match", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
