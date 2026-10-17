"""0037 - Squares of a Sorted Array (easy · two pointers from both ends)

Given integers sorted in non-decreasing order (negatives allowed), return
the squares of every number, also sorted in non-decreasing order.
Example: [-4, -1, 0, 3, 10] -> [0, 1, 9, 16, 100].

Idea: squaring breaks the order only because of the negatives, and the
largest square is always at one of the two ends (the most negative or the
most positive number). Keep a pointer at each end, compare the absolute
values, write the bigger square into the last free slot of the result and
move that pointer inwards. Filling from the back avoids having to find the
"zero crossing" first, and no sort is needed.

Time O(n) · Space O(n) for the output (O(1) extra)
"""
from __future__ import annotations


def sorted_squares(nums: list[int]) -> list[int]:
    out = [0] * len(nums)
    lo, hi = 0, len(nums) - 1
    for slot in range(len(nums) - 1, -1, -1):
        if abs(nums[lo]) > abs(nums[hi]):
            out[slot] = nums[lo] * nums[lo]
            lo += 1
        else:
            out[slot] = nums[hi] * nums[hi]
            hi -= 1
    return out
