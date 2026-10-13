"""0028 - Counting Bits (easy · bit manipulation + dynamic programming)

For every integer i from 0 to n (inclusive), count how many 1-bits its binary
form has, and return those counts as a list of length n + 1.
Example: n = 5 -> [0, 1, 1, 2, 1, 2] (0, 1, 10, 11, 100, 101).

Idea: i >> 1 drops the lowest bit of i, and that smaller number is already
solved. So bits[i] = bits[i >> 1] + (i & 1): the count of the shifted number
plus 1 if the bit we dropped was a one. One pass, no per-number bit loop.

Time O(n) · Space O(n) for the output (O(1) extra)
"""
from __future__ import annotations


def count_bits(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n must be >= 0")
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits
