"""0003 — Longest Substring Without Repeating Characters (medium · sliding window)

Given a string, return the length of the longest contiguous substring in which
no character appears twice.

Idea: keep a window [left, i] with no repeats and remember the last index of
every character. When s[i] was already seen inside the window, jump `left`
to just after that earlier position. The answer is the widest window seen.

Time O(n) · Space O(k) where k is the number of distinct characters
"""


def length_of_longest_substring(s: str) -> int:
    last: dict[str, int] = {}
    left = best = 0
    for i, ch in enumerate(s):
        if last.get(ch, -1) >= left:
            left = last[ch] + 1
        last[ch] = i
        best = max(best, i - left + 1)
    return best
