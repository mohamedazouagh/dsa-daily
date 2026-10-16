"""0035 - Koko Eating Bananas (medium · binary search on the answer)

There are piles of bananas (positive integers) and h hours. Each hour Koko
picks one pile and eats up to k bananas from it; if the pile has fewer, she
finishes it and waits for the next hour. Return the smallest integer speed k
that lets her finish every pile within h hours. If h is smaller than the
number of piles it is impossible (one pile per hour at most): raise
ValueError.
Example: piles = [3, 6, 7, 11], h = 8 -> 4.

Idea: we are not searching the input but the range of possible answers.
hours(k) = sum(ceil(p / k)) only goes down as k goes up, so "can finish at
speed k" is monotone: False ... False True ... True. Binary-search the first
True in [1, max(piles)] (at max(piles) every pile takes exactly one hour, so
that speed always works when h >= len(piles)). ceil(p / k) is computed as
-(-p // k) to stay in exact integer arithmetic.

Time O(n log m) with m = max(piles) · Space O(1)
"""
from __future__ import annotations


def hours_needed(piles: list[int], k: int) -> int:
    return sum(-(-p // k) for p in piles)


def min_eating_speed(piles: list[int], h: int) -> int:
    if not piles:
        raise ValueError("need at least one pile")
    if h < len(piles):
        raise ValueError("h must be at least the number of piles")
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(piles, mid) <= h:
            hi = mid  # mid works; the answer is mid or smaller
        else:
            lo = mid + 1
    return lo
