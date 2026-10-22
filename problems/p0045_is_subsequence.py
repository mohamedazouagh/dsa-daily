"""0045 - Is Subsequence (easy · greedy two pointers, + binary search for many queries)

Given strings s and t, decide whether s is a subsequence of t: can s be made
by deleting zero or more characters of t without reordering the rest?
Example: "abc" in "ahbgdc" -> True; "axc" in "ahbgdc" -> False; "" is a
subsequence of every string.

Idea: walk through t once with a pointer into s. Whenever the current
character of t equals the next needed character of s, advance the s pointer.
Matching greedily as early as possible is safe: taking an earlier match never
leaves fewer options for the remaining characters. s is a subsequence iff the
pointer reaches the end of s.

Follow-up (many s against one long t): precompute, for every character, the
sorted list of positions where it appears in t. For each character of s,
`bisect` finds the first position after the previous match; if there is none,
the answer is False. Each query then costs O(len(s) * log len(t)) instead of
O(len(t)).

Time O(len(t)) per check · Space O(1); index build O(len(t)) time and space
"""
from __future__ import annotations

from bisect import bisect_left
from collections import defaultdict


def is_subsequence(s: str, t: str) -> bool:
    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
    return i == len(s)


class SubsequenceIndex:
    """Answer many "is s a subsequence of t?" queries against one fixed t."""

    def __init__(self, t: str) -> None:
        self._positions: dict[str, list[int]] = defaultdict(list)
        for i, ch in enumerate(t):
            self._positions[ch].append(i)  # appended in order, so already sorted

    def contains(self, s: str) -> bool:
        pos = -1  # index in t of the previous match
        for ch in s:
            spots = self._positions.get(ch)
            if not spots:
                return False
            k = bisect_left(spots, pos + 1)
            if k == len(spots):
                return False
            pos = spots[k]
        return True
