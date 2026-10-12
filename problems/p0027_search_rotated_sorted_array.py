"""0027 - Search in Rotated Sorted Array (medium · modified binary search)

A sorted list of distinct integers was rotated at an unknown pivot, e.g.
[0, 1, 2, 4, 5, 6, 7] -> [4, 5, 6, 7, 0, 1, 2]. Return the index of a target
value, or -1 if it is not there, in O(log n).

Idea: binary search still works because at least one half around mid is
always sorted. Compare nums[lo] with nums[mid]: if nums[lo] <= nums[mid] the
left half is sorted, otherwise the right half is. If the target lies inside
the sorted half's value range, keep that half; otherwise keep the other one.
Each step halves the range just like a plain binary search.

Time O(log n) · Space O(1)
"""
from __future__ import annotations


def search_rotated(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half [lo..mid] is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half [mid..hi] is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
