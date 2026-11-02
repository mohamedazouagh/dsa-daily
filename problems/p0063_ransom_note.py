"""0063 - Ransom Note (easy · letter counting)

Given a note and a magazine, decide whether the note can be built by cutting
letters out of the magazine, where each letter in the magazine can be used
only once. Example: "aab" can be made from "baa" but not from "ab".

Idea: count what the magazine offers, then spend those counts on the note.
The moment a letter's count would go below zero, the note is impossible. A
quick length check up front rejects notes longer than the magazine.

`missing_letters` answers the follow-up question "what would I still need?"
as a dict of letter -> how many more copies, which is empty exactly when the
note can be built.

Time O(m + n) · Space O(k) for k distinct characters
"""
from __future__ import annotations

from collections import Counter


def can_construct(note: str, magazine: str) -> bool:
    if len(note) > len(magazine):
        return False
    available = Counter(magazine)
    for ch in note:
        available[ch] -= 1
        if available[ch] < 0:
            return False
    return True


def missing_letters(note: str, magazine: str) -> dict[str, int]:
    """Letters (and how many of each) the magazine is short of; {} if the note fits."""
    short = Counter(note) - Counter(magazine)  # Counter subtraction drops counts <= 0
    return dict(sorted(short.items()))
