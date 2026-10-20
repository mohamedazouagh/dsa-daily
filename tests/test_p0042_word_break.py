import random
from functools import lru_cache

import pytest

from problems.p0042_word_break import can_break, word_break


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("", ["a"], True),
        ("a", [], False),
        ("aaaaaaab", ["a", "aa", "aaa"], False),
        ("aab", ["aa", "a", "b"], True),
    ],
)
def test_examples(s, words, expected):
    assert can_break(s, words) is expected


def test_segmentation_joins_back_and_uses_only_words():
    words = ["cats", "dog", "sand", "and", "cat"]
    parts = word_break("catsanddog", words)
    assert "".join(parts) == "catsanddog"
    assert all(p in words for p in parts)


def test_greedy_longest_first_would_fail_but_dp_does_not():
    # taking "aab" first leaves "a" + "c..." unmatched; "a" + "abc" works
    assert word_break("aabc", ["aab", "a", "abc"]) == ["a", "abc"]


def test_empty_words_are_ignored():
    assert word_break("ab", ["", "a", "b"]) == ["a", "b"]


def _brute(s, vocab):
    @lru_cache(maxsize=None)
    def go(i):
        return i == len(s) or any(s[i:j] in vocab and go(j) for j in range(i + 1, len(s) + 1))
    return go(0)


def test_matches_brute_force_on_random_inputs():
    rng = random.Random(42)
    for _ in range(400):
        vocab = {"".join(rng.choice("ab") for _ in range(rng.randint(1, 3))) for _ in range(rng.randint(1, 4))}
        s = "".join(rng.choice("ab") for _ in range(rng.randint(0, 12)))
        parts = word_break(s, sorted(vocab))
        assert (parts is not None) == _brute(s, frozenset(vocab))
        if parts is not None:
            assert "".join(parts) == s and all(p in vocab for p in parts)
