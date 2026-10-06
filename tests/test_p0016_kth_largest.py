import random

import pytest

from problems.p0016_kth_largest import kth_largest


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([7], 1, 7),
        ([3, 3, 1], 2, 3),  # duplicates count separately
        ([-1, -5, -3], 3, -5),
    ],
)
def test_kth_largest(nums, k, expected):
    assert kth_largest(nums, k) == expected


@pytest.mark.parametrize("k", [0, 4, -1])
def test_k_out_of_range(k):
    with pytest.raises(ValueError):
        kth_largest([1, 2, 3], k)


def test_matches_sorting_on_random_input():
    rng = random.Random(16)
    for _ in range(200):
        nums = [rng.randint(-50, 50) for _ in range(rng.randint(1, 30))]
        k = rng.randint(1, len(nums))
        assert kth_largest(nums, k) == sorted(nums, reverse=True)[k - 1]


def test_input_not_modified():
    nums = [4, 1, 3]
    kth_largest(nums, 1)
    assert nums == [4, 1, 3]
