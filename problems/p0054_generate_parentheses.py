"""0054 - Generate Parentheses (medium · backtracking with open/close counts)

Given n, list every string of n pairs of parentheses that is balanced: read
left to right, the number of ")" never exceeds the number of "(" so far, and
both end at n. Example: n = 3 -> ["((()))", "(()())", "(())()", "()(())",
"()()()"].

Idea: build the string one character at a time and only ever make a move
that can still lead to a valid answer.
- "(" is allowed while fewer than n have been used.
- ")" is allowed only while it closes something, i.e. close < open.
Because no branch is ever a dead end, every leaf at length 2n is an answer,
so the work is proportional to the output. Trying "(" before ")" yields the
strings in lexicographic order ("(" < ")" in ASCII).

The number of answers is the n-th Catalan number C(2n, n) / (n + 1);
`catalan` computes it so the tests can check the count.

Time O(4^n / sqrt(n)) (Catalan(n) strings of length 2n) · Space O(n) for
the stack, plus the output
"""
from __future__ import annotations

from math import comb


def generate_parentheses(n: int) -> list[str]:
    if n < 0:
        raise ValueError("n must be >= 0")
    out: list[str] = []
    buf: list[str] = []

    def walk(open_: int, close: int) -> None:
        if close == n:
            out.append("".join(buf))
            return
        if open_ < n:
            buf.append("(")
            walk(open_ + 1, close)
            buf.pop()
        if close < open_:
            buf.append(")")
            walk(open_, close + 1)
            buf.pop()

    walk(0, 0)
    return out


def catalan(n: int) -> int:
    """Number of balanced strings with n pairs."""
    return comb(2 * n, n) // (n + 1)
