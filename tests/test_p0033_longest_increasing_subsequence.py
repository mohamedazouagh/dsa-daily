import random

import pytest

from problems.p0033_longest_increasing_subsequence import length_of_lis, length_of_lis_quadratic


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7], 1),  # strictly increasing: equal values do not chain
        ([5, 4, 3, 2, 1], 1),
        ([1, 2, 3, 4, 5], 5),
        ([42], 1),
        ([], 0),
        ([-3, -1, -2, 0], 3),
    ],
)
def test_examples(nums, expected):
    assert length_of_lis(nums) == expected
    assert length_of_lis_quadratic(nums) == expected


def test_matches_quadratic_reference_on_random_lists():
    rng = random.Random(33)
    for _ in range(300):
        nums = [rng.randint(-20, 20) for _ in range(rng.randint(0, 40))]
        assert length_of_lis(nums) == length_of_lis_quadratic(nums)


def test_does_not_modify_input():
    nums = [3, 1, 2]
    length_of_lis(nums)
    assert nums == [3, 1, 2]
