import random
from functools import lru_cache

import pytest

from problems.p0024_coin_change import coin_change


def brute_force(coins, amount):
    coins = tuple(c for c in set(coins) if c > 0)

    @lru_cache(maxsize=None)
    def fewest(a):
        if a == 0:
            return 0
        options = [fewest(a - c) for c in coins if c <= a]
        options = [o for o in options if o >= 0]
        return 1 + min(options) if options else -1

    return fewest(amount)


@pytest.mark.parametrize(
    "coins,amount,expected",
    [
        ([1, 2, 5], 11, 3),  # 5 + 5 + 1
        ([2], 3, -1),
        ([1], 0, 0),
        ([], 0, 0),
        ([], 7, -1),
        ([1, 3, 4], 6, 2),  # greedy would pick 4 + 1 + 1
        ([186, 419, 83, 408], 6249, 20),
        ([5, 5, 0, -2, 3], 9, 3),  # duplicates and non-positive coins are ignored
    ],
)
def test_examples(coins, amount, expected):
    assert coin_change(coins, amount) == expected


def test_negative_amount_rejected():
    with pytest.raises(ValueError):
        coin_change([1], -1)


def test_matches_brute_force():
    rng = random.Random(24)
    for _ in range(300):
        coins = [rng.randint(1, 12) for _ in range(rng.randint(0, 4))]
        amount = rng.randint(0, 40)
        assert coin_change(coins, amount) == brute_force(coins, amount)
