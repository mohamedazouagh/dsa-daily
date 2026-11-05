"""0067 - Merge Sorted Array (easy · two pointers from the back)

nums1 holds m sorted values followed by n spare slots (their contents don't
matter); nums2 holds n sorted values. Merge nums2 into nums1 in place so the
first m + n slots end up sorted. Nothing is returned.

Idea: filling from the front would overwrite values of nums1 that haven't been
compared yet. Filling from the back can't: write position k = i + j + 1 is
always past i, the last unread nums1 value, because j >= 0 while nums2 still
has values. So compare the two largest unread values, write the bigger one at
k and step left. When nums2 runs out, the rest of nums1 is already in place;
when nums1 runs out first, copy what's left of nums2. Taking nums1's value on
ties (`>`) keeps the merge stable.

Time O(m + n) · Space O(1)
"""
from __future__ import annotations


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    if len(nums1) < m + n or len(nums2) < n:
        raise ValueError("nums1 needs m + n slots and nums2 at least n values")
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
