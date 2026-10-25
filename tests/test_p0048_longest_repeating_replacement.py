import random
from collections import Counter

import pytest

from problems.p0048_longest_repeating_replacement import (
    longest_replacement,
    longest_replacement_window,
)


def brute(s: str, k: int) -> int:
    best = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            window = s[i:j]
            if len(window) - max(Counter(window).values()) <= k:
                best = max(best, j - i)
    return best


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("", 3, 0),
        ("A", 0, 1),
        ("ABCDE", 0, 1),
        ("ABCDE", 10, 5),
        ("AAAA", 0, 4),
        ("BAAAB", 0, 3),
    ],
)
def test_examples(s, k, expected):
    assert longest_replacement(s, k) == expected


def test_returned_window_is_really_fixable():
    length, start = longest_replacement_window("AABABBA", 1)
    window = "AABABBA"[start : start + length]
    assert len(window) == 4
    assert len(window) - max(Counter(window).values()) <= 1


def test_matches_brute_force_on_random_strings():
    rng = random.Random(48)
    for _ in range(400):
        s = "".join(rng.choice("ABC") for _ in range(rng.randint(0, 14)))
        k = rng.randint(0, 4)
        length, start = longest_replacement_window(s, k)
        assert length == brute(s, k)
        if length:
            window = s[start : start + length]
            assert len(window) - max(Counter(window).values()) <= k


def test_rejects_negative_k():
    with pytest.raises(ValueError):
        longest_replacement("AB", -1)
