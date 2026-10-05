import random

import pytest

from problems.p0014_valid_palindrome import is_palindrome


@pytest.mark.parametrize(
    "s,expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),  # nothing left after cleaning
        (".,", True),
        ("0P", False),  # digits count, and '0' != 'p'
        ("No 'x' in Nixon", True),
        ("ab_a", True),  # underscore is ignored
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected


def test_matches_cleaned_reverse():
    rng = random.Random(14)
    alphabet = "abAB1 ,!"
    for _ in range(300):
        s = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 10)))
        cleaned = [c.casefold() for c in s if c.isalnum()]
        assert is_palindrome(s) == (cleaned == cleaned[::-1])
