"""0011 - Course Schedule (medium · topological sort)

There are n courses labelled 0..n-1 and a list of prerequisite pairs
(course, required): `required` must be taken before `course`. Return an order
in which all courses can be taken, or None if that is impossible because the
prerequisites contain a cycle. When several courses are available at once the
lowest label goes first, so the answer is deterministic.

Idea: Kahn's algorithm. Count incoming edges (unmet prerequisites) for every
course; repeatedly take a course with none left and "release" the courses
that depend on it. If we run out of available courses before taking all n,
the remaining ones sit on a cycle. A min-heap of available courses gives the
lowest-label tie-break.

Time O(n log n + e) for e prerequisite pairs · Space O(n + e)
"""
from __future__ import annotations

import heapq


def course_order(n: int, prerequisites: list[tuple[int, int]]) -> list[int] | None:
    if n < 0:
        raise ValueError("n must be non-negative")
    unlocks: list[list[int]] = [[] for _ in range(n)]
    pending = [0] * n
    for course, required in prerequisites:
        if not (0 <= course < n and 0 <= required < n):
            raise ValueError(f"course label out of range: {(course, required)}")
        unlocks[required].append(course)
        pending[course] += 1

    ready = [c for c in range(n) if pending[c] == 0]
    heapq.heapify(ready)
    order: list[int] = []
    while ready:
        c = heapq.heappop(ready)
        order.append(c)
        for nxt in unlocks[c]:
            pending[nxt] -= 1
            if pending[nxt] == 0:
                heapq.heappush(ready, nxt)
    return order if len(order) == n else None


def can_finish(n: int, prerequisites: list[tuple[int, int]]) -> bool:
    return course_order(n, prerequisites) is not None
