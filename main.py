# SPDX-License-Identifier: MIT
"""Pigeon Pitch, One Line — a make.fun program/v1 entry.

A city pigeon delivers its elevator pitch to a room full of investors.
One line, one bird, one very confident ask for seed money.
"""

# The pitch itself: a breadcrumb-subscription startup, told in the
# pigeon's own voice — equal parts streetwise and shamelessly optimistic.
ENTRY = (
    "Coo. My startup delivers premium breadcrumbs to every rooftop in "
    "the city \u2014 we\u2019re pre-seed, pre-revenue, and already pecking "
    "at a total addressable market of one billion park benches."
)

# The competition allows a single line of at most two hundred characters.
# Anything longer, or anything that spills onto a second line, is a
# broken pitch — investors walk out, and so does the judge.
MAX_LENGTH = 200

# Why this line: the joke lands in three beats. First the "coo" plants
# the bird in the room. Then the startup jargon (pre-seed, pre-revenue,
# total addressable market) collides with the pigeon's actual business —
# crumbs on rooftops. The punchline quietly admits the whole market is
# just park benches, which is exactly the kind of confident overreach
# a real founder would deliver with a straight face.


def validate(entry: str) -> None:
    """Refuse anything that is not exactly one short line."""
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_LENGTH:
        raise ValueError(f"entry is {len(entry)} chars, over the 200 limit")
    if not entry.strip():
        raise ValueError("entry must not be empty")


def write_entry(entry: str, path: str = "/output/entry.txt") -> None:
    """Validate the pitch, then write it out for the grader to read."""
    validate(entry)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")


def main() -> None:
    write_entry(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
