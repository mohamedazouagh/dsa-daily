import pytest

from problems.p0003_longest_unique_substring import length_of_longest_substring


@pytest.mark.parametrize(
    "s,expected",
    [
        ("", 0),
        ("a", 1),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abba", 2),
        ("dvdf", 3),
        ("abcdef", 6),
    ],
)
def test_length_of_longest_substring(s, expected):
    assert length_of_longest_substring(s) == expected
