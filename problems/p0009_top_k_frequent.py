"""0009 - Top K Frequent Elements (medium · heap)

Given a list of values and an integer k, return the k values that occur most
often, most frequent first. Ties are broken by first appearance in the input
so the result is deterministic. If k is larger than the number of distinct
values, return all of them; k must be non-negative.

Idea: count occurrences with a hash map (Counter keeps first-seen order), then
pick the k largest counts with a heap of size k instead of sorting every
distinct value. heapq.nlargest is stable for equal keys when we include the
first-seen index in the key.

Time O(n + d log k) for n items and d distinct values · Space O(d)
"""
from __future__ import annotations

import heapq
from collections import Counter
from collections.abc import Hashable


def top_k_frequent(items: list[Hashable], k: int) -> list[Hashable]:
    if k < 0:
        raise ValueError("k must be non-negative")
    counts = Counter(items)
    order = {value: i for i, value in enumerate(counts)}  # first-seen position
    return heapq.nlargest(k, counts, key=lambda v: (counts[v], -order[v]))
