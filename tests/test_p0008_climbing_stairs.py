import pytest

from problems.p0008_climbing_stairs import climb_stairs


def brute_force(n: int) -> int:
    if n <= 1:
        return 1
    return brute_force(n - 1) + brute_force(n - 2)


@pytest.mark.parametrize("n,expected", [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (10, 89)])
def test_small_values(n, expected):
    assert climb_stairs(n) == expected


def test_matches_brute_force():
    for n in range(20):
        assert climb_stairs(n) == brute_force(n)


def test_large_n_is_fast_and_exact():
    assert climb_stairs(90) == 4660046610375530309


def test_negative_raises():
    with pytest.raises(ValueError):
        climb_stairs(-1)
