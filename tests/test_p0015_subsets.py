from itertools import combinations

import pytest

from problems.p0015_subsets import subsets


def _norm(sets):
    return sorted(tuple(s) for s in sets)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([], [[]]),
        ([7], [[], [7]]),
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ([3, -1], [[], [3], [-1], [3, -1]]),  # input order kept inside subsets
    ],
)
def test_subsets(nums, expected):
    assert _norm(subsets(nums)) == _norm(expected)


@pytest.mark.parametrize("n", range(0, 9))
def test_matches_itertools_and_count(n):
    nums = list(range(10, 10 + n))
    result = subsets(nums)
    assert len(result) == 2**n
    expected = [list(c) for k in range(n + 1) for c in combinations(nums, k)]
    assert _norm(result) == _norm(expected)


def test_returned_subsets_are_independent_copies():
    result = subsets([1, 2])
    result[0].append(99)
    assert all(99 not in s for s in result[1:])
