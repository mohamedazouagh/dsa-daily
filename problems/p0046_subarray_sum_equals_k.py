"""0046 - Subarray Sum Equals K (medium · prefix sums + hash map of counts)

Given a list of integers nums (negatives and zeros allowed) and an integer k,
count the contiguous, non-empty subarrays whose elements add up to exactly k.
Example: nums = [1, 1, 1], k = 2 -> 2 ([1, 1] twice); nums = [1, 2, 3],
k = 3 -> 2 ([1, 2] and [3]).

Idea: let prefix(j) be the sum of the first j elements. The subarray
nums[i:j] sums to k exactly when prefix(j) - prefix(i) == k, i.e. when an
earlier prefix equals prefix(j) - k. Walk through nums keeping a running sum
and a Counter of how often each prefix sum has appeared so far (seeded with
{0: 1} for the empty prefix). At each step, add the number of earlier prefixes
equal to running - k, then record the current prefix.

A sliding window does not work here: with negative numbers, growing the
window can make the sum smaller, so there is no monotonic rule for moving the
edges. The hash map handles any sign.

`longest_subarray_with_sum` reuses the same idea, but stores only the first
index where each prefix sum appears, so the earliest start gives the longest
subarray ending at each position.

Time O(n) · Space O(n)
"""
from __future__ import annotations

from collections import Counter


def subarray_sum(nums: list[int], k: int) -> int:
    seen: Counter[int] = Counter({0: 1})
    running = 0
    count = 0
    for x in nums:
        running += x
        count += seen[running - k]  # Counter returns 0 for missing keys
        seen[running] += 1
    return count


def longest_subarray_with_sum(nums: list[int], k: int) -> int:
    """Length of the longest contiguous subarray summing to k (0 if none)."""
    first: dict[int, int] = {0: -1}  # prefix sum -> earliest end index
    running = 0
    best = 0
    for j, x in enumerate(nums):
        running += x
        i = first.get(running - k)
        if i is not None:
            best = max(best, j - i)
        first.setdefault(running, j)  # keep the earliest index only
    return best
