import random

import pytest

from problems.p0027_search_rotated_sorted_array import search_rotated


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([4, 5, 6, 7, 0, 1, 2], 7, 3),
        ([1], 0, -1),
        ([1], 1, 0),
        ([], 5, -1),
        ([3, 1], 1, 1),
        ([5, 1, 3], 5, 0),
        ([1, 2, 3, 4, 5], 4, 3),  # rotation by 0 is a plain sorted list
    ],
)
def test_examples(nums, target, expected):
    assert search_rotated(nums, target) == expected


def test_every_rotation_and_target():
    rng = random.Random(27)
    for _ in range(200):
        base = sorted(rng.sample(range(-50, 50), rng.randint(1, 15)))
        k = rng.randrange(len(base))
        nums = base[k:] + base[:k]
        for i, v in enumerate(nums):
            assert search_rotated(nums, v) == i
        for missing in set(range(-52, 52)) - set(nums):
            assert search_rotated(nums, missing) == -1
