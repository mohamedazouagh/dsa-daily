import random

import pytest

from problems.p0067_merge_sorted_array import merge


def test_example():
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_empty_sides():
    nums1 = [1]
    merge(nums1, 1, [], 0)
    assert nums1 == [1]
    nums1 = [0]
    merge(nums1, 0, [1], 1)  # spare slot overwritten
    assert nums1 == [1]


def test_nums2_all_smaller_and_negatives():
    nums1 = [4, 5, 6, 9, 9, 9]
    merge(nums1, 3, [-3, -1, 0], 3)
    assert nums1 == [-3, -1, 0, 4, 5, 6]


class _Item:
    """Compares by key only, so equal keys can still be told apart by tag."""

    def __init__(self, key: int, tag: str):
        self.key, self.tag = key, tag

    def __gt__(self, other: "_Item") -> bool:
        return self.key > other.key


def test_ties_keep_nums1_values_first():
    nums1 = [_Item(1, "a1"), _Item(2, "a2"), None, None]
    merge(nums1, 2, [_Item(1, "b1"), _Item(2, "b2")], 2)
    assert [x.tag for x in nums1] == ["a1", "b1", "a2", "b2"]


def test_too_short_raises():
    with pytest.raises(ValueError):
        merge([1, 2], 2, [3], 1)


def test_random_against_sorted():
    rng = random.Random(67)
    for _ in range(500):
        m, n = rng.randint(0, 8), rng.randint(0, 8)
        a = sorted(rng.randint(-5, 5) for _ in range(m))
        b = sorted(rng.randint(-5, 5) for _ in range(n))
        nums1 = a + [rng.randint(-99, 99) for _ in range(n)]  # junk in spare slots
        merge(nums1, m, b, n)
        assert nums1 == sorted(a + b)
