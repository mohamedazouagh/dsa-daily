import pytest

from problems.p0005_merge_intervals import merge_intervals


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([], []),
        ([[5, 7]], [[5, 7]]),
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[8, 10], [1, 3], [2, 6]], [[1, 6], [8, 10]]),
        ([[1, 10], [2, 3], [4, 5]], [[1, 10]]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ],
)
def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected


def test_input_is_not_modified():
    intervals = [[2, 6], [1, 3]]
    merge_intervals(intervals)
    assert intervals == [[2, 6], [1, 3]]
