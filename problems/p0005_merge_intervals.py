"""0005 — Merge Intervals (medium · sorting)

Given a list of closed intervals [start, end], merge every group of
overlapping intervals and return the result sorted by start. Intervals that
only touch (e.g. [1, 4] and [4, 5]) count as overlapping.

Idea: sort by start. Walk through the intervals keeping the last merged one;
if the current interval starts at or before its end, stretch that end to
max(end, current end). Otherwise the gap means a new merged interval begins.
The input is not modified.

Time O(n log n) for the sort · Space O(n) for the output
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
