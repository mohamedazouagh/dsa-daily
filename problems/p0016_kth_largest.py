"""0016 - Kth Largest Element in an Array (medium · heap)

Given a list of integers and k (1 <= k <= len(nums)), return the k-th largest
value in sorted order, counting duplicates separately: in [3, 3, 1] the 1st
and 2nd largest are both 3. Raise ValueError when k is out of range.

Idea: keep a min-heap of the k largest values seen so far. Push each value;
once the heap holds more than k items, pop the smallest. After the scan the
heap root is the smallest of the top k, i.e. the k-th largest. This avoids
sorting the whole list when k is small.

Time O(n log k) · Space O(k)
"""
from __future__ import annotations

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    if not 1 <= k <= len(nums):
        raise ValueError(f"k must be between 1 and {len(nums)}, got {k}")
    heap: list[int] = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
