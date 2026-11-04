import random

import pytest

from problems.p0064_sort_colors import partition_three, sort_colors


def test_examples():
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
    nums = [2, 0, 1]
    sort_colors(nums)
    assert nums == [0, 1, 2]


def test_edge_cases():
    for case in ([], [0], [2], [1, 1, 1], [2, 2, 0, 0]):
        nums = list(case)
        sort_colors(nums)
        assert nums == sorted(case)


def test_rejects_other_values():
    with pytest.raises(ValueError):
        sort_colors([0, 3, 1])


def test_partition_three_returns_equal_block():
    nums = [5, 1, 5, 9, 3, 5, 7]
    low, high = partition_three(nums, 5)
    assert all(v < 5 for v in nums[:low])
    assert nums[low:high + 1] == [5, 5, 5]
    assert all(v > 5 for v in nums[high + 1:])
    assert sorted(nums) == [1, 3, 5, 5, 5, 7, 9]


def test_pivot_missing_gives_empty_block():
    nums = [4, 1, 6, 2]
    low, high = partition_three(nums, 3)
    assert high == low - 1
    assert sorted(nums[:low]) == [1, 2] and sorted(nums[low:]) == [4, 6]


def test_random_matches_sorted():
    rng = random.Random(64)
    for _ in range(500):
        case = [rng.randint(0, 2) for _ in range(rng.randint(0, 30))]
        nums = list(case)
        sort_colors(nums)
        assert nums == sorted(case)
        other = [rng.randint(-5, 5) for _ in range(rng.randint(0, 30))]
        pivot = rng.randint(-6, 6)
        low, high = partition_three(other, pivot)
        assert all(v < pivot for v in other[:low])
        assert all(v == pivot for v in other[low:high + 1])
        assert all(v > pivot for v in other[high + 1:])
