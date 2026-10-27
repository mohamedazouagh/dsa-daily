"""0053 - Single Number (easy · bit manipulation, XOR folding)

Every integer in a non-empty list appears exactly twice, except one that
appears once. Find that one, in linear time and without extra memory.
Example: [4, 1, 2, 1, 2] -> 4.

Idea: XOR is its own inverse (x ^ x == 0), has 0 as identity (x ^ 0 == x)
and is order-independent. XOR-ing the whole list cancels every pair and
leaves the lonely value. Python ints are arbitrary precision and XOR works
on their two's-complement form, so negative numbers are fine too.

Follow-up `two_singles`: exactly two values appear once, the rest twice.
XOR-ing everything gives a ^ b, which is non-zero because a != b. Pick any
set bit of it (the lowest: x & -x); a and b differ on that bit, so splitting
the list by it puts a and b in different halves, each half being a plain
"single number" problem.

Time O(n) · Space O(1)
"""
from __future__ import annotations

from functools import reduce
from operator import xor


def single_number(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")
    return reduce(xor, nums)


def two_singles(nums: list[int]) -> tuple[int, int]:
    """The two values that appear once (smaller first); all others appear twice."""
    both = reduce(xor, nums, 0)
    if both == 0:
        raise ValueError("expected exactly two values that appear once")
    bit = both & -both
    a = 0
    for x in nums:
        if x & bit:
            a ^= x
    b = both ^ a
    return (a, b) if a < b else (b, a)
