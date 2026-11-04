"""0064 - Sort Colors (medium · Dutch national flag partitioning)

An array holds only the values 0, 1 and 2 (red, white, blue). Sort it in
place, in a single pass and with O(1) extra memory, so all 0s come first,
then the 1s, then the 2s. Example: [2, 0, 2, 1, 1, 0] -> [0, 0, 1, 1, 2, 2].

Idea: keep three regions with two boundaries and a scanning index:
    nums[:low]       are 0s
    nums[low:i]      are 1s
    nums[i:high+1]   not looked at yet
    nums[high+1:]    are 2s
A 0 is swapped down to `low` (both pointers move on, since what comes back
from `low` is a known 1), a 1 just stays, and a 2 is swapped up to `high`.
After a swap with `high` the incoming value is unseen, so `i` does not move.

`partition_three` is the same loop with a pivot: values below, equal to and
above it, which is the three-way partition used by quicksort on data with
many duplicates.

Time O(n) · Space O(1)
"""
from __future__ import annotations


def partition_three(nums: list, pivot) -> tuple[int, int]:
    """Reorder ``nums`` in place into < pivot, == pivot, > pivot.

    Returns (low, high): ``nums[low:high + 1]`` is the block equal to the pivot.
    """
    low, i, high = 0, 0, len(nums) - 1
    while i <= high:
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
            i += 1
        elif nums[i] > pivot:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1
        else:
            i += 1
    return low, high


def sort_colors(nums: list[int]) -> None:
    """Sort a list of 0s, 1s and 2s in place in one pass."""
    for v in nums:
        if v not in (0, 1, 2):
            raise ValueError(f"only 0, 1 and 2 are allowed, got {v!r}")
    partition_three(nums, 1)
