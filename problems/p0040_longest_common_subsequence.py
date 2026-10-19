"""0040 - Longest Common Subsequence (medium · 2D dynamic programming)

Given two strings a and b, return the length of their longest common
subsequence: the longest string that can be obtained from both by deleting
characters without changing the order of the rest. Also return one such
subsequence so the answer can be checked.
Example: a = "abcde", b = "ace" -> 3 ("ace"); a = "abc", b = "def" -> 0.

Idea: dp[i][j] is the LCS length of the prefixes a[:i] and b[:j]. If the
last characters match, they can both end the subsequence:
dp[i][j] = dp[i-1][j-1] + 1. Otherwise one of them is not used:
dp[i][j] = max(dp[i-1][j], dp[i][j-1]). For the length alone two rows are
enough; to rebuild an actual subsequence keep the full table and walk back
from dp[len(a)][len(b)], stepping diagonally on matches and otherwise towards
the larger neighbour.

Time O(n·m) · Space O(min(n, m)) for the length, O(n·m) to rebuild a subsequence
"""
from __future__ import annotations


def lcs_length(a: str, b: str) -> int:
    if len(b) > len(a):
        a, b = b, a  # keep the row as short as possible
    prev = [0] * (len(b) + 1)
    for ch in a:
        cur = [0] * (len(b) + 1)
        for j, other in enumerate(b, start=1):
            cur[j] = prev[j - 1] + 1 if ch == other else max(prev[j], cur[j - 1])
        prev = cur
    return prev[-1]


def lcs(a: str, b: str) -> str:
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    out: list[str] = []
    i, j = n, m
    while i and j:
        if a[i - 1] == b[j - 1]:
            out.append(a[i - 1])
            i, j = i - 1, j - 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(out))
