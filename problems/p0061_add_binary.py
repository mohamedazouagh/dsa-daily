"""0061 - Add Binary (easy · digit-by-digit addition with a carry)

Given two binary numbers as strings of '0' and '1', return their sum as a
binary string, without converting the whole thing to an int. Example:
"1011" + "111" -> "10010" (11 + 7 = 18). The inputs have no leading zeros
except for the number "0" itself, and the result follows the same rule.

Idea: the way you add on paper. Walk both strings from the right, add the two
digits (a missing digit on the shorter side counts as 0) plus the carry; the
new digit is total % 2 and the new carry is total // 2. When both strings run
out, a leftover carry becomes one extra leading '1'. Digits are collected
right to left and reversed once at the end, so no string is rebuilt per step.

`add_binary_many` folds the same routine over a list of numbers, which the
tests check against Python's int(..., 2) on random inputs.

Time O(max(m, n)) · Space O(max(m, n)) for the result
"""
from __future__ import annotations


def add_binary(a: str, b: str) -> str:
    for s in (a, b):
        if not s or set(s) - {"0", "1"}:
            raise ValueError(f"not a binary string: {s!r}")
    i, j, carry = len(a) - 1, len(b) - 1, 0
    digits: list[str] = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += a[i] == "1"
            i -= 1
        if j >= 0:
            total += b[j] == "1"
            j -= 1
        digits.append("1" if total % 2 else "0")
        carry = total // 2
    result = "".join(reversed(digits)).lstrip("0")
    return result or "0"


def add_binary_many(numbers: list[str]) -> str:
    total = "0"
    for n in numbers:
        total = add_binary(total, n)
    return total
