"""0068 - Decode Ways (medium · 1D dynamic programming over prefixes)

Letters are encoded as numbers: A -> "1", B -> "2", ..., Z -> "26". Given a
string of digits, count how many different letter strings it could have come
from. "12" is 2 ("AB" or "L"), "226" is 3 ("BZ", "VF", "BBF"). A piece can
never start with 0, so "06" is not "F", and "0" or "30" decode to nothing:
the answer is 0.

Idea: let ways(i) be the number of decodings of the first i digits. The last
piece of a decoding is either one digit or two. Taking one digit s[i-1] is
allowed when it isn't "0", and adds ways(i-1). Taking two digits s[i-2:i] is
allowed when they form 10..26 (so no leading zero), and adds ways(i-2). With
ways(0) = 1 (the empty prefix has one decoding), only the last two values are
ever needed, so two variables replace the table. Once both options fail at
some position, every later count is 0 too, so the loop can stop early.

`decode_all` lists the actual decodings for small inputs, which is how the
tests check the count without trusting the recurrence.

Time O(n) · Space O(1) for the count (decode_all is exponential by nature)
"""
from __future__ import annotations


def num_decodings(s: str) -> int:
    if not s.isdigit():
        raise ValueError("s must be a non-empty string of digits")
    prev2, prev1 = 1, 1  # ways(i-2), ways(i-1); prev1 starts as ways(0), prev2 is first read at i = 2
    for i in range(1, len(s) + 1):
        cur = prev1 if s[i - 1] != "0" else 0
        if i >= 2 and "10" <= s[i - 2:i] <= "26":
            cur += prev2
        if cur == 0:
            return 0
        prev2, prev1 = prev1, cur
    return prev1


def decode_all(s: str) -> list[str]:
    """Every letter string that encodes to ``s``, in lexicographic order."""
    out: list[str] = []

    def walk(i: int, acc: list[str]) -> None:
        if i == len(s):
            out.append("".join(acc))
            return
        for width in (1, 2):
            piece = s[i:i + width]
            if len(piece) == width and piece[0] != "0" and 1 <= int(piece) <= 26:
                acc.append(chr(ord("A") + int(piece) - 1))
                walk(i + width, acc)
                acc.pop()

    walk(0, [])
    return sorted(out)
