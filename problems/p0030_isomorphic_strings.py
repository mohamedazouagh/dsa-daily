"""0030 - Isomorphic Strings (easy · two-way hash map)

Two strings s and t of equal length are isomorphic when the characters of s
can be replaced to get t, where every occurrence of a character maps to the
same character and no two different characters map to the same one (a
character may map to itself). Return whether s and t are isomorphic.
Example: "egg" / "add" -> True, "foo" / "bar" -> False, "badc" / "baba" -> False.

Idea: walk both strings together and keep two dicts, s->t and t->s. A pair
(a, b) is fine if neither side has a mapping yet or both already point at
each other. One dict alone misses "badc" / "baba": b->b and d->a both look
fine from the s side, but t's "a" would come from two characters.

Time O(n) · Space O(k), k = number of distinct characters
"""
from __future__ import annotations


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_to_t: dict[str, str] = {}
    t_to_s: dict[str, str] = {}
    for a, b in zip(s, t):
        if s_to_t.setdefault(a, b) != b or t_to_s.setdefault(b, a) != a:
            return False
    return True
