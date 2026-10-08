import random

import pytest

from problems.p0021_contains_nearby_duplicate import contains_nearby_duplicate


def brute_force(nums, k):
    return any(
        nums[i] == nums[j]
        for i in range(len(nums))
        for j in range(i + 1, min(len(nums), i + k + 1))
    )


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        ([1, 2, 3, 1], 2, False),  # duplicate exists but too far apart
        ([], 5, False),
        ([7, 7], 0, False),  # k = 0 can never match two different positions
    ],
)
def test_examples(nums, k, expected):
    assert contains_nearby_duplicate(nums, k) is expected


def test_matches_brute_force():
    rng = random.Random(21)
    for _ in range(500):
        nums = [rng.randint(0, 6) for _ in range(rng.randint(0, 20))]
        k = rng.randint(0, 6)
        assert contains_nearby_duplicate(nums, k) == brute_force(nums, k)
