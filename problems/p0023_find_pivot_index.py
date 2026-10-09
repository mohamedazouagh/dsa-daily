"""0023 - Find Pivot Index (easy · prefix sums)

Given a list of integers, find the leftmost index whose left-side sum (all
values before it) equals its right-side sum (all values after it). The value
at the index itself belongs to neither side; an empty side sums to 0.
Return -1 if no such index exists.

Idea: compute the total once, then walk left to right keeping a running sum
of the values already passed. At index i the right side is
total - left - nums[i], so each position is checked in O(1).

Time O(n) · Space O(1)
"""
from __future__ import annotations


def pivot_index(nums: list[int]) -> int:
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1
