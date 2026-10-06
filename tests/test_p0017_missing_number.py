import random

import pytest

from problems.p0017_missing_number import missing_number


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),  # missing the top of the range
        ([1], 0),  # missing zero
        ([], 0),  # n = 0: range is just {0}
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ],
)
def test_missing_number(nums, expected):
    assert missing_number(nums) == expected


def test_every_position_on_shuffled_ranges():
    rng = random.Random(17)
    for n in range(0, 40):
        for missing in range(n + 1):
            nums = [x for x in range(n + 1) if x != missing]
            rng.shuffle(nums)
            assert missing_number(nums) == missing
