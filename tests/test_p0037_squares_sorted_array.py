import random

import pytest

from problems.p0037_squares_sorted_array import sorted_squares


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([-5, -3, -1], [1, 9, 25]),  # all negative -> reversed order
        ([1, 2, 3], [1, 4, 9]),  # all positive -> unchanged order
        ([-2, -2, 2, 2], [4, 4, 4, 4]),
        ([0], [0]),
        ([], []),
    ],
)
def test_examples(nums, expected):
    assert sorted_squares(nums) == expected


def test_matches_square_then_sort_on_random_inputs():
    rng = random.Random(37)
    for _ in range(500):
        nums = sorted(rng.randint(-50, 50) for _ in range(rng.randint(0, 20)))
        assert sorted_squares(nums) == sorted(x * x for x in nums)


def test_input_is_not_modified():
    nums = [-3, -1, 2]
    sorted_squares(nums)
    assert nums == [-3, -1, 2]
