"""0042 - Word Break (medium · 1D dynamic programming over prefixes)

Given a string s and a list of dictionary words, decide whether s can be cut
into a sequence of one or more dictionary words (a word may be reused any
number of times). Also return one such segmentation when it exists.
Example: "applepenapple" with ["apple", "pen"] -> True ("apple pen apple");
"catsandog" with ["cats", "dog", "sand", "and", "cat"] -> False.

Idea: ok[i] says "the first i characters can be segmented". ok[0] is True
(the empty prefix). For every end position i, look back only as far as the
longest dictionary word: ok[i] is True if some j has ok[j] and s[j:i] is a
word. Remembering which j made ok[i] true lets us walk back from len(s) to
rebuild one segmentation. Greedy "take the longest word first" fails on
"aabc" with ["aab", "a", "abc"] (it takes "aab" and is stuck on "c"), which
is why we need the table.

Time O(n · L) slice checks, where L is the longest word length (each slice
costs O(L), so O(n · L²) character work) · Space O(n + size of dictionary)
"""
from __future__ import annotations


def word_break(s: str, words: list[str]) -> list[str] | None:
    """Return one segmentation of s into dictionary words, or None."""
    vocab = {w for w in words if w}
    if not s:
        return []
    if not vocab:
        return None
    longest = max(map(len, vocab))
    n = len(s)
    prev: list[int | None] = [None] * (n + 1)  # prev[i] = start of last word ending at i
    ok = [False] * (n + 1)
    ok[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - longest), i):
            if ok[j] and s[j:i] in vocab:
                ok[i], prev[i] = True, j
                break
    if not ok[n]:
        return None
    parts, i = [], n
    while i > 0:
        j = prev[i]
        parts.append(s[j:i])
        i = j
    return parts[::-1]


def can_break(s: str, words: list[str]) -> bool:
    return word_break(s, words) is not None
