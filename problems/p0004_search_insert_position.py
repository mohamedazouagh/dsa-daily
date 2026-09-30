"""0004 — Search Insert Position (easy · binary search)

Given a list of distinct integers sorted in ascending order and a target,
return the index of the target if it is present; otherwise return the index
where it would have to be inserted to keep the list sorted.

Idea: classic lower-bound binary search. Keep a half-open range [lo, hi) that
always contains the answer. If nums[mid] < target the answer is right of mid,
otherwise it is mid or to its left. When lo == hi, that is the first index
whose value is >= target, which is both the match and the insert position.

Time O(log n) · Space O(1)
"""


def search_insert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
