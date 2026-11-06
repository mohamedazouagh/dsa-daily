import random

import pytest

from problems.p0068_decode_ways import decode_all, num_decodings


def test_examples():
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert decode_all("226") == ["BBF", "BZ", "VF"]


def test_zeros():
    assert num_decodings("0") == 0
    assert num_decodings("06") == 0
    assert num_decodings("10") == 1  # only "J"
    assert num_decodings("100") == 0  # second 0 has nothing to pair with
    assert num_decodings("2101") == 1  # the 0 needs the 1 before it: 2 10 1 only
    assert decode_all("2101") == ["BJA"]
    assert num_decodings("30") == 0


def test_boundaries_26_and_27():
    assert num_decodings("26") == 2
    assert num_decodings("27") == 1


def test_long_input_is_fibonacci():
    # a run of n ones decodes in Fib(n + 1) ways
    assert num_decodings("1" * 40) == 165580141


def test_invalid_input():
    for bad in ("", "12a", "-1"):
        with pytest.raises(ValueError):
            num_decodings(bad)


def test_random_against_enumeration():
    rng = random.Random(68)
    for _ in range(500):
        s = "".join(rng.choice("0112223456789") for _ in range(rng.randint(1, 10)))
        assert num_decodings(s) == len(decode_all(s))
