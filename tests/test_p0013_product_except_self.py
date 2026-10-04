import math
import random

import pytest

from problems.p0013_product_except_self import product_except_self


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),  # one zero
        ([0, 4, 0], [0, 0, 0]),  # two zeros
        ([5], [1]),  # empty product
        ([], []),
        ([2, -3], [-3, 2]),
    ],
)
def test_product_except_self(nums, expected):
    assert product_except_self(nums) == expected


def test_matches_brute_force():
    rng = random.Random(13)
    for _ in range(200):
        nums = [rng.randint(-5, 5) for _ in range(rng.randint(0, 8))]
        brute = [math.prod(nums[:i] + nums[i + 1 :]) for i in range(len(nums))]
        assert product_except_self(nums) == brute
