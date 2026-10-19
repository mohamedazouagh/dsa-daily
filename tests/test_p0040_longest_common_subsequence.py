import random
from itertools import combinations

import pytest

from problems.p0040_longest_common_subsequence import lcs, lcs_length


def _is_subsequence(s: str, t: str) -> bool:
    it = iter(t)
    return all(ch in it for ch in s)


def _brute_force(a: str, b: str) -> int:
    for k in range(min(len(a), len(b)), 0, -1):
        if any(_is_subsequence("".join(c), b) for c in combinations(a, k)):
            return k
    return 0


@pytest.mark.parametrize(
    "a, b, expected",
    [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0), ("", "abc", 0), ("bl", "yby", 1)],
)
def test_examples(a, b, expected):
    assert lcs_length(a, b) == expected
    assert len(lcs(a, b)) == expected


def test_rebuilt_subsequence_is_common():
    s = lcs("AGGTAB", "GXTXAYB")
    assert s == "GTAB"
    assert _is_subsequence(s, "AGGTAB") and _is_subsequence(s, "GXTXAYB")


def test_symmetric_in_its_arguments():
    assert lcs_length("short", "a much longer string") == lcs_length("a much longer string", "short")


def test_matches_brute_force_on_random_strings():
    rng = random.Random(40)
    for _ in range(300):
        a = "".join(rng.choice("abc") for _ in range(rng.randint(0, 8)))
        b = "".join(rng.choice("abc") for _ in range(rng.randint(0, 8)))
        expected = _brute_force(a, b)
        assert lcs_length(a, b) == expected
        s = lcs(a, b)
        assert len(s) == expected
        assert _is_subsequence(s, a) and _is_subsequence(s, b)
