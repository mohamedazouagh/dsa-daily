import random

import pytest

from problems.p0020_daily_temperatures import daily_temperatures


def brute_force(temps):
    out = []
    for i, t in enumerate(temps):
        wait = 0
        for j in range(i + 1, len(temps)):
            if temps[j] > t:
                wait = j - i
                break
        out.append(wait)
    return out


@pytest.mark.parametrize(
    "temps,expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([60, 50, 40], [0, 0, 0]),
        ([20, 20, 21], [2, 1, 0]),  # equal is not warmer
        ([], []),
        ([15.5], [0]),
    ],
)
def test_examples(temps, expected):
    assert daily_temperatures(temps) == expected


def test_matches_brute_force():
    rng = random.Random(20)
    for _ in range(300):
        temps = [rng.randint(0, 10) for _ in range(rng.randint(0, 30))]
        assert daily_temperatures(temps) == brute_force(temps)
