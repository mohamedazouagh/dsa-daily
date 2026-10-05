"""0015 - Subsets (medium · backtracking)

Given a list of distinct integers, return every possible subset (the power
set), including the empty set and the full list. Order of the subsets does
not matter, but each subset keeps the input order of its elements.

Idea: walk the list once, and at every index branch on two choices: take the
element or skip it. A shared path list is extended before recursing and popped
afterwards (backtracking), and a copy is recorded at each leaf. With n
elements there are exactly 2**n leaves.

Time O(n · 2**n) (2**n subsets, each copied in O(n)) · Space O(n) recursion
depth besides the output
"""
from __future__ import annotations


def subsets(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    path: list[int] = []

    def walk(i: int) -> None:
        if i == len(nums):
            out.append(path.copy())
            return
        path.append(nums[i])  # take nums[i]
        walk(i + 1)
        path.pop()  # skip nums[i]
        walk(i + 1)

    walk(0)
    return out
