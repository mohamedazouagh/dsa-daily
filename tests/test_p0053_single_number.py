import random
from collections import Counter

import pytest

from problems.p0053_single_number import single_number, two_singles


def test_examples():
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([2, 2, 1]) == 1
    assert single_number([7]) == 7


def test_negatives_and_zero():
    assert single_number([-3, 5, -3]) == 5
    assert single_number([0, -8, 0]) == -8
    assert single_number([5, 0, 5]) == 0


def test_against_counter():
    rng = random.Random(53)
    for _ in range(500):
        values = rng.sample(range(-1000, 1000), rng.randint(1, 20))
        lonely, pairs = values[0], values[1:]
        nums = [lonely] + pairs * 2
        rng.shuffle(nums)
        expected = next(v for v, c in Counter(nums).items() if c == 1)
        assert single_number(nums) == expected == lonely


def test_two_singles():
    assert two_singles([1, 2, 1, 3, 2, 5]) == (3, 5)
    assert two_singles([-1, 0]) == (-1, 0)
    rng = random.Random(530)
    for _ in range(500):
        values = rng.sample(range(-500, 500), rng.randint(2, 20))
        a, b, pairs = values[0], values[1], values[2:]
        nums = [a, b] + pairs * 2
        rng.shuffle(nums)
        assert two_singles(nums) == tuple(sorted((a, b)))


def test_errors():
    with pytest.raises(ValueError):
        single_number([])
    with pytest.raises(ValueError):
        two_singles([1, 1])
