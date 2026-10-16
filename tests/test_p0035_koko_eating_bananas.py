import random

import pytest

from problems.p0035_koko_eating_bananas import hours_needed, min_eating_speed


def brute_force(piles, h):
    k = 1
    while hours_needed(piles, k) > h:
        k += 1
    return k


@pytest.mark.parametrize(
    "piles,h,expected",
    [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),  # one hour per pile -> speed = biggest pile
        ([30, 11, 23, 4, 20], 6, 23),
        ([1], 1, 1),
        ([1_000_000_000], 2, 500_000_000),
        ([5, 5, 5], 100, 1),  # lots of time -> slowest possible speed
    ],
)
def test_examples(piles, h, expected):
    assert min_eating_speed(piles, h) == expected


def test_matches_brute_force_on_random_inputs():
    rng = random.Random(35)
    for _ in range(300):
        piles = [rng.randint(1, 40) for _ in range(rng.randint(1, 8))]
        h = rng.randint(len(piles), 60)
        k = min_eating_speed(piles, h)
        assert k == brute_force(piles, h)
        assert hours_needed(piles, k) <= h
        assert k == 1 or hours_needed(piles, k - 1) > h


def test_impossible_or_empty_input_rejected():
    with pytest.raises(ValueError):
        min_eating_speed([3, 4, 5], 2)
    with pytest.raises(ValueError):
        min_eating_speed([], 3)
