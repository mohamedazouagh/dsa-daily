"""0033 - Longest Increasing Subsequence (medium · DP + binary search)

Given a list of integers, return the length of the longest strictly
increasing subsequence (elements in their original order, not necessarily
adjacent). An empty list has length 0.
Example: [10, 9, 2, 5, 3, 7, 101, 18] -> 4 (e.g. 2, 3, 7, 18).

Idea ("patience sorting"): keep tails[k] = the smallest possible last value
of an increasing subsequence of length k + 1 seen so far. tails is always
sorted, so for each x binary-search the first tail >= x: replace it (x is a
cheaper ending for that length), or append if x is larger than every tail.
The answer is len(tails). Using bisect_left (first >= x) is what makes the
subsequence *strictly* increasing: an equal value replaces instead of
extending. tails itself is not a valid subsequence, only its length matters.

Time O(n log n) · Space O(n)   (the classic O(n^2) DP is kept as a reference)
"""
from __future__ import annotations

from bisect import bisect_left


def length_of_lis(nums: list[int]) -> int:
    tails: list[int] = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def length_of_lis_quadratic(nums: list[int]) -> int:
    """O(n^2) DP: best[i] = longest increasing subsequence ending at nums[i]."""
    best = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                best[i] = max(best[i], best[j] + 1)
    return max(best, default=0)
