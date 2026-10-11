import random

from problems.p0025_implement_trie import Trie


def test_word_vs_prefix():
    t = Trie()
    t.insert("apple")
    assert t.search("apple")
    assert not t.search("app")  # only a prefix so far
    assert t.starts_with("app")
    t.insert("app")
    assert t.search("app")
    assert not t.starts_with("apz")
    assert not t.search("apples")


def test_empty_trie_and_empty_strings():
    t = Trie()
    assert not t.starts_with("")
    assert not t.search("")
    t.insert("a")
    assert t.starts_with("")
    assert not t.search("")
    t.insert("")
    assert t.search("")


def test_duplicate_inserts_and_unicode():
    t = Trie()
    t.insert("café")
    t.insert("café")
    assert t.search("café")
    assert not t.search("cafe")
    assert t.starts_with("caf")


def test_matches_set_model():
    rng = random.Random(25)
    for _ in range(100):
        words = {"".join(rng.choice("abc") for _ in range(rng.randint(0, 5))) for _ in range(rng.randint(0, 8))}
        t = Trie()
        for w in words:
            t.insert(w)
        for _ in range(30):
            q = "".join(rng.choice("abc") for _ in range(rng.randint(0, 5)))
            assert t.search(q) == (q in words)
            assert t.starts_with(q) == any(w.startswith(q) for w in words)
