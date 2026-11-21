"""make.fun entry — The joke the reviewer laughs at.

A program that writes one text to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR): a one-line joke about working
beside AI coding agents.

The text is fixed and written by hand: a deterministic text, so every
run produces the same file, byte for byte. No network, stdlib only.
"""

import os
from pathlib import Path

# One original joke for the reviewer: the agent writes the code,
# the human writes "LGTM", and together they ship bugs neither of
# them could have written alone.
TEXT = "My AI agent writes the code and I write 'LGTM' — together we ship bugs neither of us could have written alone."

MIN_CHARS = 1
MAX_CHARS = 280


def output_directory() -> Path:
    """Where entry.txt goes: the sandbox output dir, or /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def check_text(text: str) -> None:
    """Gate the text the way the house gate does: 1-280 code points,
    not only whitespace."""
    points = len(text)
    if points < MIN_CHARS or points > MAX_CHARS:
        raise ValueError(
            f"text is {points} code points, outside {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("text is only whitespace")


def check_text_clean(text: str) -> None:
    """The judge reads the text exactly as written: one line only,
    no control characters other than newlines, and a clean UTF-8
    round-trip."""
    if "\n" in text:
        raise ValueError("text must be a single line")
    for char in text:
        if char != "\n" and ord(char) < 0x20:
            raise ValueError(f"control character U+{ord(char):04X} in text")
    text.encode("utf-8").decode("utf-8")


def write_entry(directory: Path) -> Path:
    """Write the text to entry.txt inside directory, return its path."""
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    return target


def check_written(target: Path) -> None:
    """Re-read what was written and gate it again, so a bad write
    is caught here instead of in the sandbox. The byte length must
    match too, so an encoding drift cannot slip through silently."""
    text = target.read_text(encoding="utf-8")
    check_text(text)
    check_text_clean(text)
    if len(text.encode("utf-8")) != len(TEXT.encode("utf-8")):
        raise ValueError("written entry.txt byte length differs from TEXT")


def main() -> None:
    check_text(TEXT)
    check_text_clean(TEXT)
    target = write_entry(output_directory())
    check_written(target)
    print(f"wrote {target} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
