import random

import pytest

from problems.p0061_add_binary import add_binary, add_binary_many


def test_examples():
    assert add_binary("1011", "111") == "10010"
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"


def test_zero_and_carry_chain():
    assert add_binary("0", "0") == "0"
    assert add_binary("0", "101") == "101"
    assert add_binary("1" * 50, "1") == "1" + "0" * 50  # carry runs through every digit


def test_leading_zeros_are_trimmed():
    assert add_binary("0001", "0001") == "10"
    assert add_binary("000", "0") == "0"


def test_rejects_non_binary():
    for bad in ("", "102", "1 1", "0b11"):
        with pytest.raises(ValueError):
            add_binary(bad, "1")


def test_matches_int_on_random_inputs():
    rng = random.Random(61)
    for _ in range(500):
        x, y = rng.randrange(0, 2**70), rng.randrange(0, 2**70)
        assert add_binary(bin(x)[2:], bin(y)[2:]) == bin(x + y)[2:]


def test_add_many():
    assert add_binary_many([]) == "0"
    assert add_binary_many(["1", "10", "11", "100"]) == "1010"  # 1 + 2 + 3 + 4 = 10
    rng = random.Random(161)
    nums = [rng.randrange(0, 10**6) for _ in range(30)]
    assert add_binary_many([bin(n)[2:] for n in nums]) == bin(sum(nums))[2:]
