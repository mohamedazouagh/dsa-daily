"""0056 - Insert Interval (medium · interval sweep, three phases)

You get a list of closed intervals [start, end] that are sorted by start and
do not overlap, plus one new interval. Insert the new interval so the list
stays sorted and non-overlapping, merging wherever it touches or overlaps
existing ones. Intervals that only share an endpoint ([1, 2] and [2, 3])
count as overlapping. Example: [[1, 3], [6, 9]] + [2, 5] -> [[1, 5], [6, 9]].

Idea: because the input is already sorted and disjoint, one left-to-right
pass splits it into three groups:
  1. intervals that end before the new one starts  -> copy unchanged;
  2. intervals that overlap it (start <= new end)  -> widen the new interval
     to min(start) / max(end) and drop them;
  3. everything after                               -> copy unchanged.
The merged new interval goes between groups 1 and 3. No sorting is needed,
unlike the general Merge Intervals problem (0005).

`remove_interval` is the opposite operation: cut [a, b] out of the set,
splitting intervals that stick out on either side. With closed integer
intervals the leftovers are [s, a - 1] and [b + 1, e].

Time O(n) · Space O(n) for the output list
"""
from __future__ import annotations


def insert_interval(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    lo, hi = new
    if lo > hi:
        raise ValueError(f"invalid interval {new!r}: start > end")
    out: list[list[int]] = []
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < lo:  # 1. entirely before
        out.append(list(intervals[i]))
        i += 1
    while i < n and intervals[i][0] <= hi:  # 2. overlapping: absorb
        lo = min(lo, intervals[i][0])
        hi = max(hi, intervals[i][1])
        i += 1
    out.append([lo, hi])
    out.extend(list(iv) for iv in intervals[i:])  # 3. entirely after
    return out


def remove_interval(intervals: list[list[int]], cut: list[int]) -> list[list[int]]:
    """Remove the closed integer range ``cut`` from sorted disjoint ``intervals``."""
    a, b = cut
    if a > b:
        raise ValueError(f"invalid interval {cut!r}: start > end")
    out: list[list[int]] = []
    for s, e in intervals:
        if e < a or s > b:
            out.append([s, e])
            continue
        if s < a:
            out.append([s, a - 1])
        if e > b:
            out.append([b + 1, e])
    return out
