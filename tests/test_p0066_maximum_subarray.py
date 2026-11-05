import random

import pytest

from problems.p0066_maximum_subarray import max_subarray, max_subarray_bounds


def _brute(nums: list[int]) -> int:
    return max(sum(nums[i : j + 1]) for i in range(len(nums)) for j in range(i, len(nums)))


def test_example():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray(nums) == 6
    assert max_subarray_bounds(nums) == (6, 3, 6)  # [4, -1, 2, 1]


def test_all_negative_picks_largest_element():
    assert max_subarray([-3, -1, -2]) == -1
    assert max_subarray_bounds([-3, -1, -2]) == (-1, 1, 1)


def test_single_and_all_positive():
    assert max_subarray([7]) == 7
    assert max_subarray_bounds([7]) == (7, 0, 0)
    assert max_subarray_bounds([1, 2, 3]) == (6, 0, 2)


def test_ties_keep_first_slice():
    assert max_subarray_bounds([3, -5, 3]) == (3, 0, 0)


def test_empty_raises():
    with pytest.raises(ValueError):
        max_subarray([])
    with pytest.raises(ValueError):
        max_subarray_bounds([])


def test_random_against_brute_force():
    rng = random.Random(66)
    for _ in range(500):
        nums = [rng.randint(-10, 10) for _ in range(rng.randint(1, 12))]
        expected = _brute(nums)
        assert max_subarray(nums) == expected
        best, i, j = max_subarray_bounds(nums)
        assert best == expected == sum(nums[i : j + 1])
        assert 0 <= i <= j < len(nums)
