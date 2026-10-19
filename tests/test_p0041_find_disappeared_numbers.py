import random

import pytest

from problems.p0041_find_disappeared_numbers import find_disappeared_numbers


@pytest.mark.parametrize(
    "nums, expected",
    [([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]), ([1, 1], [2]), ([1], []), ([], []), ([2, 2, 2], [1, 3])],
)
def test_examples(nums, expected):
    assert find_disappeared_numbers(nums) == expected


def test_input_is_restored():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    find_disappeared_numbers(nums)
    assert nums == [4, 3, 2, 7, 8, 2, 3, 1]


@pytest.mark.parametrize("nums", [[0, 1], [1, 3], [-1, 1]])
def test_out_of_range_values_raise(nums):
    with pytest.raises(ValueError):
        find_disappeared_numbers(nums)


def test_matches_set_difference_on_random_inputs():
    rng = random.Random(41)
    for _ in range(500):
        n = rng.randint(1, 30)
        nums = [rng.randint(1, n) for _ in range(n)]
        expected = sorted(set(range(1, n + 1)) - set(nums))
        original = list(nums)
        assert find_disappeared_numbers(nums) == expected
        assert nums == original
