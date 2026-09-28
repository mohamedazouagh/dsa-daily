import pytest

from problems.p0001_two_sum import two_sum


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
        ([-4, 10, 1, 8], 4, (0, 3)),
    ],
)
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected


def test_no_pair_raises():
    with pytest.raises(ValueError):
        two_sum([1, 2, 3], 100)
