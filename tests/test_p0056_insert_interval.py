import random

import pytest

from problems.p0056_insert_interval import insert_interval, remove_interval


def covered(intervals):
    return {x for s, e in intervals for x in range(s, e + 1)}


def to_intervals(points):
    """Sorted disjoint intervals covering exactly ``points`` (touching ones merged)."""
    out = []
    for x in sorted(points):
        if out and x <= out[-1][1] + 1:
            out[-1][1] = x
        else:
            out.append([x, x])
    return out


def test_examples():
    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2], [3, 10], [12, 16]
    ]


def test_edge_cases():
    assert insert_interval([], [5, 7]) == [[5, 7]]
    assert insert_interval([[3, 4]], [1, 2]) == [[1, 2], [3, 4]]  # goes first
    assert insert_interval([[1, 2]], [5, 6]) == [[1, 2], [5, 6]]  # goes last
    assert insert_interval([[1, 2], [3, 4]], [2, 3]) == [[1, 4]]  # touching endpoints merge
    assert insert_interval([[1, 10]], [3, 4]) == [[1, 10]]  # fully inside
    assert insert_interval([[2, 3], [5, 6]], [0, 9]) == [[0, 9]]  # swallows everything
    with pytest.raises(ValueError):
        insert_interval([[1, 2]], [4, 3])


def test_input_not_mutated():
    data = [[1, 3], [6, 9]]
    result = insert_interval(data, [2, 5])
    assert data == [[1, 3], [6, 9]]
    result[-1][0] = 0
    assert data[1] == [6, 9]  # output does not share inner lists


def test_insert_against_point_sets():
    rng = random.Random(56)
    for _ in range(500):
        base = to_intervals(rng.sample(range(40), rng.randint(0, 20)))
        a = rng.randint(0, 39)
        b = rng.randint(a, 39)
        got = insert_interval(base, [a, b])
        # closed intervals sharing an endpoint merge, ones only adjacent (2 and 3) stay apart
        assert covered(got) == covered(base) | set(range(a, b + 1))
        assert all(got[i][1] < got[i + 1][0] for i in range(len(got) - 1))


def test_remove_interval():
    assert remove_interval([[0, 2], [3, 4], [5, 7]], [1, 6]) == [[0, 0], [7, 7]]
    assert remove_interval([[0, 5]], [2, 3]) == [[0, 1], [4, 5]]  # split in two
    assert remove_interval([[0, 5]], [0, 5]) == []
    assert remove_interval([[1, 2]], [5, 6]) == [[1, 2]]
    rng = random.Random(560)
    for _ in range(500):
        base = to_intervals(rng.sample(range(40), rng.randint(0, 20)))
        a = rng.randint(0, 39)
        b = rng.randint(a, 39)
        got = remove_interval(base, [a, b])
        assert covered(got) == covered(base) - set(range(a, b + 1))
    with pytest.raises(ValueError):
        remove_interval([[1, 2]], [3, 1])
