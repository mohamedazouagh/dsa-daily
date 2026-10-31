"""0060 - Container With Most Water (medium · two pointers, discard the shorter wall)

You get a list of non-negative wall heights standing at positions 0..n-1. Pick
two walls; together with the floor they hold water up to the shorter wall, so
the amount is min(h[i], h[j]) * (j - i). Return the largest amount any pair can
hold. Example: [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49 (walls 8 at index 1 and 7 at
index 8: 7 * 7). Fewer than two walls hold nothing.

Idea: start with the widest pair, the two outer walls. Every other pair is
narrower, so it can only win with a taller shorter wall. Keeping the shorter
wall of the current pair and moving the other one inwards can never help: the
width shrinks and the water level stays capped by that same short wall. So the
shorter wall can be dropped for good; step its pointer inwards and repeat
until the pointers meet. With equal heights either side can go, since neither
can be part of a better pair with anything between them.

`best_pair` returns the indices too (the first best pair found), which the
tests compare with a brute-force scan over all pairs.

Time O(n) · Space O(1)
"""
from __future__ import annotations


def best_pair(heights: list[int]) -> tuple[int, int, int]:
    """(area, i, j) of the best pair, or (0, -1, -1) for fewer than two walls."""
    best = (0, -1, -1)
    i, j = 0, len(heights) - 1
    while i < j:
        area = min(heights[i], heights[j]) * (j - i)
        if area > best[0] or best[1] == -1:
            best = (area, i, j)
        if heights[i] <= heights[j]:
            i += 1
        else:
            j -= 1
    return best


def max_area(heights: list[int]) -> int:
    return best_pair(heights)[0]
