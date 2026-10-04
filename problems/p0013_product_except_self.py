"""0013 - Product of Array Except Self (medium · prefix products)

Given a list of integers, return a list where position i holds the product of
every element except the one at i. Do it without division, so zeros are no
special case.

Idea: the answer at i is (product of everything left of i) times (product of
everything right of i). One pass left-to-right writes the running prefix
product into the output; a second pass right-to-left multiplies in a running
suffix product. No extra arrays are needed besides the output.

Time O(n) · Space O(1) extra (the output list does not count)
"""
from __future__ import annotations


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [1] * n
    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]
    return out
