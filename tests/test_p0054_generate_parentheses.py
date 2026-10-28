from itertools import product

import pytest

from problems.p0054_generate_parentheses import catalan, generate_parentheses


def is_balanced(s: str) -> bool:
    depth = 0
    for ch in s:
        depth += 1 if ch == "(" else -1
        if depth < 0:
            return False
    return depth == 0


def test_example():
    assert generate_parentheses(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


def test_small_n():
    assert generate_parentheses(0) == [""]
    assert generate_parentheses(1) == ["()"]
    assert generate_parentheses(2) == ["(())", "()()"]


def test_against_brute_force():
    for n in range(0, 7):
        expected = sorted(
            "".join(p) for p in product("()", repeat=2 * n) if is_balanced("".join(p))
        )
        assert generate_parentheses(n) == expected  # same set, already sorted


def test_counts_are_catalan_and_unique():
    assert [catalan(n) for n in range(8)] == [1, 1, 2, 5, 14, 42, 132, 429]
    for n in range(9):
        got = generate_parentheses(n)
        assert len(got) == catalan(n) == len(set(got))
        assert all(len(s) == 2 * n and is_balanced(s) for s in got)


def test_rejects_negative():
    with pytest.raises(ValueError):
        generate_parentheses(-1)
