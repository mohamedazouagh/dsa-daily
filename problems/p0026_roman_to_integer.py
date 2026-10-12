"""0026 - Roman to Integer (easy · string parsing)

Convert a Roman numeral (I=1, V=5, X=10, L=50, C=100, D=500, M=1000) to an
integer. A smaller symbol written before a larger one is subtracted instead
of added (IV = 4, XC = 90, CM = 900). Only the six standard subtractive
pairs are valid: IV, IX, XL, XC, CD, CM.

Idea: scan left to right and look one symbol ahead. If the next symbol is
larger, the current one is subtracted, otherwise added. That handles every
subtractive pair without listing them. To reject malformed input ("IIII",
"IC", "VX"), convert back with the greedy integer->Roman algorithm and
require the round trip to give the same string: every valid numeral has
exactly one canonical spelling.

Time O(n) · Space O(1) (the round-trip check is O(n) too)
"""
from __future__ import annotations

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
_CANONICAL = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
    (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def int_to_roman(n: int) -> str:
    if not 1 <= n <= 3999:
        raise ValueError("Roman numerals cover 1..3999")
    out = []
    for value, symbol in _CANONICAL:
        count, n = divmod(n, value)
        out.append(symbol * count)
    return "".join(out)


def roman_to_int(s: str) -> int:
    if not s or any(ch not in VALUES for ch in s):
        raise ValueError(f"not a Roman numeral: {s!r}")
    total = 0
    for i, ch in enumerate(s):
        v = VALUES[ch]
        if i + 1 < len(s) and VALUES[s[i + 1]] > v:
            total -= v
        else:
            total += v
    if not 1 <= total <= 3999 or int_to_roman(total) != s:
        raise ValueError(f"not a canonical Roman numeral: {s!r}")
    return total
