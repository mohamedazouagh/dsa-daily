import pytest

from problems.p0030_isomorphic_strings import is_isomorphic


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),  # needs the reverse map to catch
        ("ab", "aa", False),
        ("", "", True),
        ("a", "a", True),
        ("abc", "abcd", False),
    ],
)
def test_examples(s, t, expected):
    assert is_isomorphic(s, t) is expected


def test_relation_is_symmetric():
    pairs = [("egg", "add"), ("badc", "baba"), ("paper", "title"), ("abab", "cdcd"), ("abba", "abab")]
    for s, t in pairs:
        assert is_isomorphic(s, t) == is_isomorphic(t, s)


def test_matches_pattern_signature():
    # Two strings are isomorphic exactly when their "first index of each char" patterns match.
    def signature(x):
        return [x.index(c) for c in x]

    words = ["egg", "add", "foo", "bar", "abba", "cddc", "xyzx", "aaaa", "abcd"]
    for s in words:
        for t in words:
            if len(s) == len(t):
                assert is_isomorphic(s, t) == (signature(s) == signature(t))
