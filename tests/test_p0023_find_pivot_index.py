import random

import pytest

from problems.p0023_find_pivot_index import pivot_index


def brute_force(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1 :]):
            return i
    return -1


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),  # right side sums to 0, left side is empty
        ([5], 0),  # both sides empty
        ([], -1),
        ([0, 0, 0], 0),  # leftmost pivot wins
        ([-1, -1, 0, 1, 1, 0], 5),
    ],
)
def test_examples(nums, expected):
    assert pivot_index(nums) == expected


def test_matches_brute_force():
    rng = random.Random(23)
    for _ in range(500):
        nums = [rng.randint(-3, 3) for _ in range(rng.randint(0, 12))]
        assert pivot_index(nums) == brute_force(nums)
