import random

from problems.p0058_longest_palindromic_substring import count_palindromic_substrings, longest_palindrome


def _brute_longest(s: str) -> str:
    best = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub
    return best


def _brute_count(s: str) -> int:
    return sum(
        1 for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] == s[i:j][::-1]
    )


def test_examples():
    assert longest_palindrome("babad") == "bab"  # tie with "aba", earliest start wins
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("") == ""
    assert longest_palindrome("a") == "a"


def test_odd_and_even_centres_and_whole_string():
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("abcd") == "a"
    assert longest_palindrome("aaaa") == "aaaa"


def test_count_palindromic_substrings():
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6  # a, a, a, aa, aa, aaa
    assert count_palindromic_substrings("") == 0


def test_against_brute_force():
    rng = random.Random(58)
    for _ in range(400):
        s = "".join(rng.choice("abc") for _ in range(rng.randint(0, 14)))
        assert longest_palindrome(s) == _brute_longest(s)
        assert count_palindromic_substrings(s) == _brute_count(s)
