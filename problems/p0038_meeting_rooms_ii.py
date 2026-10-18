"""0038 - Meeting Rooms II (medium · min-heap of end times / sweep line)

Given meetings as [start, end) intervals, return the smallest number of
rooms needed so that no two overlapping meetings share a room. A meeting
that ends at time t frees its room for one that starts at t.
Example: [[0, 30], [5, 10], [15, 20]] -> 2.

Idea: process meetings by start time and keep a min-heap with the end time
of every room in use. Before placing a meeting, if the earliest-ending room
is already free (its end <= this start), reuse it by popping it; then push
this meeting's end. The heap never shrinks below the number of meetings
running at the same moment, and its largest size is the answer.

Time O(n log n) (sort + heap operations) · Space O(n) for the heap
"""
from __future__ import annotations

import heapq


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    ends: list[int] = []
    rooms = 0
    for start, end in sorted(intervals):
        if ends and ends[0] <= start:
            heapq.heapreplace(ends, end)
        else:
            heapq.heappush(ends, end)
        rooms = max(rooms, len(ends))
    return rooms
