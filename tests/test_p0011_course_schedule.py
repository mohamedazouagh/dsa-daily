import pytest

from problems.p0011_course_schedule import can_finish, course_order


@pytest.mark.parametrize(
    "n,prereqs,expected",
    [
        (2, [(1, 0)], [0, 1]),
        (4, [(1, 0), (2, 0), (3, 1), (3, 2)], [0, 1, 2, 3]),
        (3, [], [0, 1, 2]),  # no constraints: label order
        (3, [(0, 2)], [1, 2, 0]),  # 1 is free before 2 unlocks 0
        (0, [], []),
        (2, [(1, 0), (1, 0)], [0, 1]),  # duplicate edge counted consistently
    ],
)
def test_course_order(n, prereqs, expected):
    assert course_order(n, prereqs) == expected


@pytest.mark.parametrize(
    "n,prereqs",
    [
        (2, [(1, 0), (0, 1)]),  # two-course cycle
        (3, [(1, 0), (2, 1), (0, 2)]),  # longer cycle
        (1, [(0, 0)]),  # self-loop
    ],
)
def test_cycle_returns_none(n, prereqs):
    assert course_order(n, prereqs) is None
    assert can_finish(n, prereqs) is False


def test_order_respects_every_prerequisite():
    prereqs = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    order = course_order(6, prereqs)
    pos = {c: i for i, c in enumerate(order)}
    assert sorted(order) == list(range(6))
    assert all(pos[req] < pos[course] for course, req in prereqs)


def test_out_of_range_label_raises():
    with pytest.raises(ValueError):
        course_order(2, [(2, 0)])
