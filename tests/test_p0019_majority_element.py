import random
from collections import Counter

import pytest

from problems.p0019_majority_element import majority_element, majority_or_none


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([5], 5),
        ([1, 9, 9], 9),  # majority arrives late
        ([-4, -4, 0], -4),
    ],
)
def test_majority_element(nums, expected):
    assert majority_element(nums) == expected


def test_random_lists_with_a_majority():
    rng = random.Random(19)
    for _ in range(300):
        n = rng.randint(1, 40)
        winner = rng.randint(-5, 5)
        k = n // 2 + 1
        nums = [winner] * k + [rng.randint(-5, 5) for _ in range(n - k)]
        rng.shuffle(nums)
        expected = Counter(nums).most_common(1)[0][0]
        assert majority_element(nums) == expected


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([], None),
        ([1, 2], None),  # exactly half is not a majority
        ([1, 2, 3], None),
        ([1, 1, 2, 2, 3], None),
        ([4, 4, 1], 4),
    ],
)
def test_majority_or_none(nums, expected):
    assert majority_or_none(nums) == expected
