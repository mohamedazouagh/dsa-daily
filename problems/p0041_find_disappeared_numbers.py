"""0041 - Find All Numbers Disappeared in an Array (easy · in-place index marking)

Given a list of n integers where every value is in the range 1..n (some
values appear twice, others not at all), return all numbers in 1..n that do
not appear, in increasing order, using no extra space besides the output.
Example: [4, 3, 2, 7, 8, 2, 3, 1] -> [5, 6]; [1, 1] -> [2].

Idea: the values themselves can serve as indexes. For every value v, flip
the number at position v - 1 to negative ("v was seen"), reading abs() so an
already-flipped slot still gives its original value. After one pass, every
position i that is still positive means i + 1 never occurred. A second pass
restores the signs so the caller's list is left as it was.

Time O(n) · Space O(1) extra (the input is modified temporarily)
"""
from __future__ import annotations


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n = len(nums)
    for v in nums:
        if not 1 <= v <= n:
            raise ValueError(f"value {v} outside 1..{n}")
    for v in nums:
        i = abs(v) - 1
        if nums[i] > 0:
            nums[i] = -nums[i]
    missing = [i + 1 for i, v in enumerate(nums) if v > 0]
    for i, v in enumerate(nums):
        nums[i] = abs(v)
    return missing
