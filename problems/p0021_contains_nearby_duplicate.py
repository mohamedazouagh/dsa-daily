"""0021 - Contains Duplicate II (easy · sliding window set)

Given a list of numbers and a distance k, report whether two different
positions i and j hold the same value with abs(i - j) <= k.

Idea: only the last k values can pair with the current one, so keep exactly
those in a set. For each new value, a hit in the set means a close duplicate;
otherwise add it and, once the window is longer than k, drop the value that
just slid out on the left. (A dict of "last index seen" works too.)

Time O(n) · Space O(min(n, k))
"""
from __future__ import annotations


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    if k <= 0:
        return False
    window: set[int] = set()
    for i, x in enumerate(nums):
        if x in window:
            return True
        window.add(x)
        if len(window) > k:
            window.remove(nums[i - k])
    return False
