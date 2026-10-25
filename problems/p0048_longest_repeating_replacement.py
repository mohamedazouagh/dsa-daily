"""0048 - Longest Repeating Character Replacement (medium · sliding window + counts)

Given a string of uppercase letters and an integer k, you may change at most
k characters to any other letter. Return the length of the longest substring
that can be made of a single repeated letter.
Example: s = "AABABBA", k = 1 -> 4 ("AABA" -> "AAAA", or "ABBA" -> "BBBB").

Idea: a window s[left:right+1] can be made uniform when
(window length - count of its most common letter) <= k, i.e. the letters we
would have to change fit in the budget. Grow the window one letter at a time,
keep letter counts and the best "most common count" seen so far. When the
window becomes invalid, slide it (move left by one) instead of shrinking it:
the window never gets smaller, so its size at the end is the answer.

`max_count` is never decreased when the left edge moves. That is safe: a
stale, too-high max_count can only keep a window of the current size alive,
and the answer only grows once a real count exceeds the old maximum.

Also returns the start of one best window so the result can be checked.

Time O(n) · Space O(alphabet) (26 counters)
"""
from __future__ import annotations

from collections import Counter


def longest_replacement(s: str, k: int) -> int:
    return longest_replacement_window(s, k)[0]


def longest_replacement_window(s: str, k: int) -> tuple[int, int]:
    """Return (length, start index) of a longest fixable window."""
    if k < 0:
        raise ValueError(f"k must be non-negative, got {k}")
    counts: Counter[str] = Counter()
    left = max_count = 0
    best_len, best_start = 0, 0
    for right, ch in enumerate(s):
        counts[ch] += 1
        max_count = max(max_count, counts[ch])
        if right - left + 1 - max_count > k:
            counts[s[left]] -= 1
            left += 1
        if right - left + 1 > best_len:
            best_len, best_start = right - left + 1, left
    return best_len, best_start
