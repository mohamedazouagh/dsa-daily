import random

import pytest

from problems.p0038_meeting_rooms_ii import min_meeting_rooms


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [5, 10]], 1),  # back-to-back meetings share a room
        ([[1, 10], [2, 9], [3, 8], [4, 7]], 4),  # all nested
        ([[1, 3], [1, 3], [1, 3]], 3),
        ([], 0),
    ],
)
def test_examples(intervals, expected):
    assert min_meeting_rooms(intervals) == expected


def _brute_force(intervals):
    """Peak number of meetings running at any integer time point."""
    points = {s for s, _ in intervals}
    return max((sum(1 for s, e in intervals if s <= t < e) for t in points), default=0)


def test_matches_peak_overlap_on_random_inputs():
    rng = random.Random(38)
    for _ in range(500):
        intervals = []
        for _ in range(rng.randint(0, 12)):
            s = rng.randint(0, 30)
            intervals.append([s, s + rng.randint(1, 10)])
        assert min_meeting_rooms(intervals) == _brute_force(intervals)


def test_input_is_not_modified():
    intervals = [[5, 10], [0, 30]]
    min_meeting_rooms(intervals)
    assert intervals == [[5, 10], [0, 30]]
