"""0036 - Group Anagrams (medium · hash map with a canonical key)

Given a list of words, put words that are anagrams of each other (same
letters, same counts, any order) into the same group. Return the groups in
order of first appearance, each group keeping the input order of its words.
Example: ["eat", "tea", "tan", "ate", "nat", "bat"]
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]].

Idea: two words are anagrams exactly when they have the same letter
multiset, so map each word to a canonical key that only depends on that
multiset and bucket by key in a dict (dicts keep insertion order, which
gives "order of first appearance" for free). Two keys work:
- sorted letters: "".join(sorted(w)) - simple, O(L log L) per word;
- a 26-slot letter-count tuple - O(L) per word, lowercase a-z only.
Duplicates stay as separate entries in their group; "" is its own group.

Time O(n · L log L) with sorted keys, O(n · L) with counts · Space O(n · L)
"""
from __future__ import annotations


def _sorted_key(word: str) -> str:
    return "".join(sorted(word))


def _count_key(word: str) -> tuple[int, ...]:
    counts = [0] * 26
    for ch in word:
        i = ord(ch) - ord("a")
        if not 0 <= i < 26:
            raise ValueError(f"count key supports lowercase a-z only, got {ch!r}")
        counts[i] += 1
    return tuple(counts)


def group_anagrams(words: list[str], use_counts: bool = False) -> list[list[str]]:
    key = _count_key if use_counts else _sorted_key
    groups: dict = {}
    for w in words:
        groups.setdefault(key(w), []).append(w)
    return list(groups.values())
