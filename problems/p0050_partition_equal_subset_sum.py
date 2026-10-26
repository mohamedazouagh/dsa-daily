"""0050 - Partition Equal Subset Sum (medium · 0/1 knapsack, subset-sum DP)

Given a list of positive integers, decide whether it can be split into two
groups (every number used exactly once) whose sums are equal.
Example: [1, 5, 11, 5] -> True ({11} and {1, 5, 5}); [1, 2, 3, 5] -> False.

Idea: the two halves must each sum to total / 2, so an odd total is an
immediate no. Otherwise this is subset sum with target t = total / 2.
Keep the set of sums reachable with the numbers seen so far as the bits of
one Python integer: bit s is set when sum s is reachable. Adding a number x
either skips it or takes it once, which is `reach | (reach << x)`. Shifting
the whole integer handles "each number at most once" automatically (unlike
the unbounded coin-change DP in 0024, where a sum can reuse a coin), and we
mask off bits above t so the integer stays small.

`find_partition` rebuilds one actual half by remembering the reachable sets
after each number and walking back from t.

Time O(n * t / w) with w-bit machine words (bitset) · Space O(t / w) for the
yes/no answer, O(n * t / w) for the reconstruction
"""
from __future__ import annotations


def can_partition(nums: list[int]) -> bool:
    if any(x <= 0 for x in nums):
        raise ValueError("expected positive integers")
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    mask = (1 << (target + 1)) - 1
    reach = 1  # sum 0 is reachable with no numbers
    for x in nums:
        reach = (reach | (reach << x)) & mask
        if reach >> target & 1:
            return True
    return target == 0


def find_partition(nums: list[int]) -> tuple[list[int], list[int]] | None:
    """Two lists with equal sums that together use every number once, or None."""
    if any(x <= 0 for x in nums):
        raise ValueError("expected positive integers")
    total = sum(nums)
    if total % 2:
        return None
    target = total // 2
    mask = (1 << (target + 1)) - 1
    history = [1]  # history[i]: sums reachable with nums[:i]
    for x in nums:
        history.append((history[-1] | (history[-1] << x)) & mask)
    if not history[-1] >> target & 1:
        return None
    left, right, s = [], [], target
    for i in range(len(nums), 0, -1):
        x = nums[i - 1]
        if history[i - 1] >> s & 1:  # s was already reachable without x
            right.append(x)
        else:  # x must be taken to reach s
            left.append(x)
            s -= x
    return left[::-1], right[::-1]
