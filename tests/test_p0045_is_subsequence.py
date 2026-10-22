import random
from itertools import combinations

import pytest

from problems.p0045_is_subsequence import SubsequenceIndex, is_subsequence


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "", True),
        ("", "abc", True),
        ("a", "", False),
        ("aaa", "aa", False),
        ("aaa", "baaab", True),
        ("acb", "abc", False),  # order matters
        ("abc", "abc", True),
    ],
)
def test_examples(s, t, expected):
    assert is_subsequence(s, t) is expected
    assert SubsequenceIndex(t).contains(s) is expected


def _brute_force(s, t):
    return any("".join(c) == s for c in combinations(t, len(s)))


def test_matches_brute_force_on_random_strings():
    rng = random.Random(45)
    for _ in range(600):
        t = "".join(rng.choice("abc") for _ in range(rng.randint(0, 8)))
        s = "".join(rng.choice("abc") for _ in range(rng.randint(0, 4)))
        expected = _brute_force(s, t)
        assert is_subsequence(s, t) is expected
        assert SubsequenceIndex(t).contains(s) is expected


def test_index_reused_for_many_queries():
    t = "ab" * 50_000
    idx = SubsequenceIndex(t)
    assert idx.contains("ba" * 1000)
    assert idx.contains("a" * 50_000)
    assert not idx.contains("a" * 50_001)
    assert not idx.contains("abc")
