"""0066 - Maximum Subarray (medium · Kadane's algorithm)

Given a non-empty list of integers (negatives allowed), find the largest sum
of any contiguous, non-empty slice. An all-negative list still has to pick a
slice, so the answer is then its largest single element, not 0.

Idea: scan once and keep `best_ending_here`, the best sum of a slice that ends
at the current index. That slice either extends the previous one or starts
fresh at the current element, whichever is larger:
best_ending_here = max(x, best_ending_here + x). The overall answer is the
largest value it ever takes. Starting fresh exactly when the running sum has
dropped below zero is the same rule, which also tells us where the best slice
begins.

`max_subarray_bounds` returns the slice itself as (sum, start, end) with an
inclusive end; on ties it keeps the first slice found.

Time O(n) · Space O(1)
"""
from __future__ import annotations


def max_subarray(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")
    best = here = nums[0]
    for x in nums[1:]:
        here = max(x, here + x)
        best = max(best, here)
    return best


def max_subarray_bounds(nums: list[int]) -> tuple[int, int, int]:
    if not nums:
        raise ValueError("nums must be non-empty")
    best, best_start, best_end = nums[0], 0, 0
    here, start = nums[0], 0
    for i in range(1, len(nums)):
        if here < 0:  # a negative prefix can only hurt: start over at i
            here, start = nums[i], i
        else:
            here += nums[i]
        if here > best:
            best, best_start, best_end = here, start, i
    return best, best_start, best_end
