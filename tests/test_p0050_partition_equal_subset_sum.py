import random
from itertools import combinations

import pytest

from problems.p0050_partition_equal_subset_sum import can_partition, find_partition


def brute(nums):
    total = sum(nums)
    return total % 2 == 0 and any(
        sum(c) * 2 == total for r in range(len(nums) + 1) for c in combinations(nums, r)
    )


def check_split(nums, split):
    left, right = split
    assert sum(left) == sum(right)
    assert sorted(left + right) == sorted(nums)


def test_examples():
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    check_split([1, 5, 11, 5], find_partition([1, 5, 11, 5]))
    assert find_partition([1, 2, 3, 5]) is None


def test_edge_cases():
    assert can_partition([]) is True  # two empty halves
    assert find_partition([]) == ([], [])
    assert can_partition([7]) is False
    assert can_partition([4, 4]) is True
    assert can_partition([2, 2, 3]) is False  # odd total
    assert can_partition([1, 1, 4]) is False  # even total, but 4 > 3 can't be matched


def test_each_number_used_once_not_reused():
    # target 4 is reachable as 2+2 only if 2 could be reused; it can't
    assert can_partition([2, 6]) is False


def test_against_brute_force():
    rng = random.Random(50)
    for _ in range(400):
        nums = [rng.randint(1, 20) for _ in range(rng.randint(0, 10))]
        expected = brute(nums)
        assert can_partition(nums) is expected
        split = find_partition(nums)
        if expected:
            check_split(nums, split)
        else:
            assert split is None


def test_large_input_is_fast():
    nums = [100] * 100 + [1, 1]
    assert can_partition(nums) is True
    check_split(nums, find_partition(nums))


@pytest.mark.parametrize("bad", [[0, 2], [3, -3]])
def test_rejects_non_positive(bad):
    with pytest.raises(ValueError):
        can_partition(bad)
    with pytest.raises(ValueError):
        find_partition(bad)
