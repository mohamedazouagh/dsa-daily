"""0055 - Move Zeroes (easy · two pointers, in-place stable compaction)

Given a list of numbers, move every 0 to the end while keeping the non-zero
values in their original order. Do it in place, without building a copy.
Example: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0].

Idea: keep a write pointer w = "next slot for a non-zero value". Scan with
a read pointer r; whenever nums[r] is non-zero, swap it into slot w and
advance w. Everything left of w is the non-zero values in order, everything
between w and r is zeros, so after the scan the zeros sit at the end.
Swapping (instead of copying and zero-filling afterwards) means each value
moves at most once, and a list without zeros does no real writes because
r == w the whole time.

`move_value` is the same routine for any value (e.g. move every None or
every "" to the end); it returns how many items stayed in front.

Time O(n) · Space O(1)
"""
from __future__ import annotations

from typing import Any


def move_zeroes(nums: list[int]) -> None:
    move_value(nums, 0)


def move_value(items: list[Any], value: Any) -> int:
    """Move every item equal to ``value`` to the end, in place and stable.

    Returns the number of items that are not ``value`` (the new front length).
    """
    w = 0
    for r in range(len(items)):
        if items[r] != value:
            if r != w:
                items[w], items[r] = items[r], items[w]
            w += 1
    return w
