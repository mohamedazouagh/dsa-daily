import random

import pytest

from problems.p0046_subarray_sum_equals_k import longest_subarray_with_sum, subarray_sum


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([], 0, 0),  # no non-empty subarrays
        ([0, 0, 0], 0, 6),  # every subarray of zeros
        ([1, -1, 1, -1], 0, 4),
        ([3, 4, -7, 1, 3, 3, 1, -4], 7, 4),
        ([5], 5, 1),
        ([5], 4, 0),
    ],
)
def test_examples(nums, k, expected):
    assert subarray_sum(nums, k) == expected


def _brute_count(nums, k):
    return sum(1 for i in range(len(nums)) for j in range(i + 1, len(nums) + 1) if sum(nums[i:j]) == k)


def _brute_longest(nums, k):
    return max(
        (j - i for i in range(len(nums)) for j in range(i + 1, len(nums) + 1) if sum(nums[i:j]) == k),
        default=0,
    )


def test_matches_brute_force_with_negatives():
    rng = random.Random(46)
    for _ in range(500):
        nums = [rng.randint(-3, 3) for _ in range(rng.randint(0, 12))]
        k = rng.randint(-4, 4)
        assert subarray_sum(nums, k) == _brute_count(nums, k)
        assert longest_subarray_with_sum(nums, k) == _brute_longest(nums, k)


def test_longest_examples():
    assert longest_subarray_with_sum([1, -1, 5, -2, 3], 3) == 4  # [1, -1, 5, -2]
    assert longest_subarray_with_sum([-2, -1, 2, 1], 1) == 2  # [-1, 2]
    assert longest_subarray_with_sum([1, 2, 3], 7) == 0


def test_does_not_mutate_input():
    nums = [2, -1, 3]
    subarray_sum(nums, 2)
    longest_subarray_with_sum(nums, 2)
    assert nums == [2, -1, 3]
