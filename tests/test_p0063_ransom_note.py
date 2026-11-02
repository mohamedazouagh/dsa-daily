import random
import string

from problems.p0063_ransom_note import can_construct, missing_letters


def test_examples():
    assert can_construct("aab", "baa") is True
    assert can_construct("aab", "ab") is False
    assert can_construct("a", "b") is False


def test_empty_and_case_sensitive():
    assert can_construct("", "") is True
    assert can_construct("", "abc") is True
    assert can_construct("A", "a") is False
    assert can_construct("hi there", "the hire!") is True  # spaces are letters too


def test_missing_letters():
    assert missing_letters("aab", "baa") == {}
    assert missing_letters("hello", "hel") == {"l": 1, "o": 1}
    assert missing_letters("zzz", "") == {"z": 3}


def test_random_matches_brute_force_removal():
    rng = random.Random(63)
    for _ in range(500):
        note = "".join(rng.choices("abcde", k=rng.randint(0, 8)))
        magazine = "".join(rng.choices(string.ascii_lowercase[:6], k=rng.randint(0, 12)))
        pool = list(magazine)
        ok = True
        for ch in note:
            if ch in pool:
                pool.remove(ch)
            else:
                ok = False
                break
        assert can_construct(note, magazine) == ok
        assert (missing_letters(note, magazine) == {}) == ok
