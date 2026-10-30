"""0058 - Longest Palindromic Substring (medium · expand around centre)

Given a string s, return its longest contiguous substring that reads the
same forwards and backwards. If several have the maximum length, return the
one that starts first. Example: "babad" -> "bab" ("aba" is equally long but
starts later), "cbbd" -> "bb", "" -> "".

Idea: every palindrome is mirrored around a centre, and a string of length n
has 2n - 1 centres: each character (odd lengths) and each gap between two
neighbours (even lengths). From each centre, grow outwards while the two ends
match; the first mismatch ends that palindrome. Keep the longest seen, and
only replace it on a strictly longer one so ties keep the earliest start.
Centres are visited left to right, and a palindrome's centre position grows
with its start for a fixed length, so the earliest-starting one wins ties.

`count_palindromic_substrings` reuses the same expansion: every successful
step outwards is one more palindrome, so it counts all of them (with
repeats at different positions) in the same O(n^2) time.

Time O(n^2) worst case (e.g. "aaaa…"), O(n) for strings with few repeats ·
Space O(1) beyond the output
"""
from __future__ import annotations


def _expand(s: str, lo: int, hi: int) -> tuple[int, int]:
    """Grow [lo, hi] outwards while it stays a palindrome; return the last valid bounds (hi exclusive)."""
    while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
        lo -= 1
        hi += 1
    return lo + 1, hi


def longest_palindrome(s: str) -> str:
    best_lo, best_hi = 0, 0
    for centre in range(len(s)):
        for lo, hi in (_expand(s, centre, centre), _expand(s, centre, centre + 1)):
            if hi - lo > best_hi - best_lo:
                best_lo, best_hi = lo, hi
    return s[best_lo:best_hi]


def count_palindromic_substrings(s: str) -> int:
    total = 0
    for centre in range(len(s)):
        for lo, hi in ((centre, centre), (centre, centre + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                total += 1
                lo -= 1
                hi += 1
    return total
