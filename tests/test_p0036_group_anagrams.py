import random
from collections import Counter

import pytest

from problems.p0036_group_anagrams import group_anagrams


def brute_force(words):
    groups = []
    for w in words:
        for g in groups:
            if Counter(g[0]) == Counter(w):
                g.append(w)
                break
        else:
            groups.append([w])
    return groups


@pytest.mark.parametrize("use_counts", [False, True])
@pytest.mark.parametrize(
    "words,expected",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["ab", "ba", "ab"], [["ab", "ba", "ab"]]),  # duplicates are kept
        (["abc", "abcc", "cab"], [["abc", "cab"], ["abcc"]]),  # same letters, different counts
        ([], []),
    ],
)
def test_examples(words, expected, use_counts):
    assert group_anagrams(words, use_counts=use_counts) == expected


def test_both_keys_match_brute_force_on_random_words():
    rng = random.Random(36)
    for _ in range(200):
        words = ["".join(rng.choice("abc") for _ in range(rng.randint(0, 4))) for _ in range(rng.randint(0, 12))]
        expected = brute_force(words)
        assert group_anagrams(words) == expected
        assert group_anagrams(words, use_counts=True) == expected


def test_count_key_rejects_non_lowercase():
    with pytest.raises(ValueError):
        group_anagrams(["Tea"], use_counts=True)
    assert group_anagrams(["Tea", "eaT"]) == [["Tea", "eaT"]]  # sorted key handles any characters
