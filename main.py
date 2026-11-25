"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of exactly 100 words to /output/entry.txt.

The speaker is a specific villain, lord of the Hollow Throne for three
hundred years, with a scheme (the burning of the hero's village, booked
for Thursday, no, Friday) and a history (a ledger of grudges, a crown
that pinches, a dragon who quit). His tiredness is never announced: it
lives in his knees, his feet, his mixing up of days, and in the small
deflections -- take a number, sit, the menacing can wait.
"""

import os

MONOLOGUE = (
    "Come closer. No, stay there. I had the steps built steep so "
    "petitioners would arrive breathless, and now my knees complain. "
    "Three hundred years I have kept the Hollow Throne, and what do I "
    "have to show for it? A ledger of grudges, a crown that pinches, "
    "and a dragon who quit before I did. You came to slay me, yes? "
    "Take a number. The last hero still waits in the other room, "
    "sharpening his sword. Sign here. Your village burns Thursday, "
    "no, Friday. I keep mixing them up. Sit. We will do the menacing "
    "once my feet stop humming."
)


def main() -> None:
    text = MONOLOGUE.strip()
    words = text.split()
    assert len(words) == 100, f"expected 100 words, got {len(words)}"
    assert 1 <= len(text) <= 600, f"gate: 1-600 chars, got {len(text)}"
    # Judge criterion 2: the tiredness must be felt, never announced.
    lowered = text.lower()
    for banned in ("tired", "weary", "exhausted", "sleepy"):
        assert banned not in lowered, f"announced tiredness: {banned}"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # One trailing newline is the file's line ending, not part of the text.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8",
              newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(words)} words, {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
