"""0047 - Excel Sheet Column Title (easy · bijective base-26 conversion)

Spreadsheet columns are labelled A, B, ..., Z, AA, AB, ..., AZ, BA, ...,
ZZ, AAA, ... Convert a positive column number to its label and back.
Example: 1 -> "A", 26 -> "Z", 27 -> "AA", 28 -> "AB", 701 -> "ZY",
702 -> "ZZ", 703 -> "AAA".

Idea: this is base 26 without a zero digit ("bijective" base 26): the digits
run from 1 (A) to 26 (Z). Plain `n % 26` would give 0 for Z, so subtract 1
before each step: digit = (n - 1) % 26 maps to 'A'..'Z', then
n = (n - 1) // 26 moves to the next, more significant letter. Letters come
out least significant first, so reverse at the end.

The inverse is Horner's rule: n = n * 26 + (letter value 1..26) for each
letter from left to right.

Time O(log n) · Space O(log n) for the label
"""
from __future__ import annotations

from string import ascii_uppercase


def column_title(n: int) -> str:
    if n < 1:
        raise ValueError(f"column numbers start at 1, got {n}")
    letters: list[str] = []
    while n:
        n, digit = divmod(n - 1, 26)
        letters.append(ascii_uppercase[digit])
    return "".join(reversed(letters))


def column_number(title: str) -> int:
    if not title or not all("A" <= ch <= "Z" for ch in title):
        raise ValueError(f"expected letters A-Z, got {title!r}")
    n = 0
    for ch in title:
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n
