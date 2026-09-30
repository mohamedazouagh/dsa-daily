import bisect
import random

import pytest

from problems.p0004_search_insert_position import search_insert


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([], 3, 0),
        ([4], 4, 0),
        ([4], 9, 1),
        ([-5, -2, 0, 8], -3, 1),
    ],
)
def test_search_insert(nums, target, expected):
    assert search_insert(nums, target) == expected


def test_matches_bisect_left_on_random_input():
    rng = random.Random(4)
    for _ in range(200):
        nums = sorted(rng.sample(range(-50, 50), rng.randint(0, 20)))
        target = rng.randint(-60, 60)
        assert search_insert(nums, target) == bisect.bisect_left(nums, target)
