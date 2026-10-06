"""0017 - Missing Number (easy · bit manipulation)

A list holds n distinct integers taken from the range 0..n, so exactly one
number from that range is absent. Return the missing number.

Idea: x ^ x == 0 and x ^ 0 == x, and XOR is order-independent. XOR every
index 0..n together with every value in the list: each present number appears
twice and cancels out, leaving only the missing one. Unlike the sum formula
n * (n + 1) // 2 - sum(nums), this never builds a large intermediate value
(which matters in fixed-width languages).

Time O(n) · Space O(1)
"""
from __future__ import annotations


def missing_number(nums: list[int]) -> int:
    acc = len(nums)  # the index loop below stops at n - 1, so start with n
    for i, x in enumerate(nums):
        acc ^= i ^ x
    return acc
