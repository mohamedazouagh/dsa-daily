"""0019 - Majority Element (easy · Boyer-Moore voting)

A non-empty list is guaranteed to contain one value that appears more than
len(nums) // 2 times. Return that value.

Idea: Boyer-Moore majority vote. Keep a candidate and a counter. A matching
value adds a vote, any other value cancels one; when the counter hits zero the
next value becomes the new candidate. Every cancellation removes one majority
copy at most together with one non-majority copy, and the majority has more
copies than everything else combined, so it is the candidate left standing.
No hash map needed, unlike counting with a dict.

Without the guarantee, a second pass is required to confirm the candidate;
`majority_or_none` does that and returns None when nothing is a majority.

Time O(n) · Space O(1)
"""
from __future__ import annotations


def majority_element(nums: list[int]) -> int:
    candidate, votes = nums[0], 0
    for x in nums:
        if votes == 0:
            candidate = x
        votes += 1 if x == candidate else -1
    return candidate


def majority_or_none(nums: list[int]) -> int | None:
    if not nums:
        return None
    candidate = majority_element(nums)
    return candidate if nums.count(candidate) > len(nums) // 2 else None
