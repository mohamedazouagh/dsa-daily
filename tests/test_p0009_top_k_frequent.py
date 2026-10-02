import pytest

from problems.p0009_top_k_frequent import top_k_frequent


@pytest.mark.parametrize(
    "items,k,expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([], 3, []),
        ([4, 4, 5], 0, []),
        (["b", "a", "b", "a", "c"], 2, ["b", "a"]),  # tie: first seen wins
        ([3, 1, 2], 2, [3, 1]),  # all equal counts -> input order
        ([5, 6, 6, 7, 7, 7], 10, [7, 6, 5]),  # k larger than distinct values
    ],
)
def test_top_k_frequent(items, k, expected):
    assert top_k_frequent(items, k) == expected


def test_does_not_modify_input():
    items = [2, 1, 2]
    top_k_frequent(items, 1)
    assert items == [2, 1, 2]


def test_negative_k_raises():
    with pytest.raises(ValueError):
        top_k_frequent([1, 2], -1)
