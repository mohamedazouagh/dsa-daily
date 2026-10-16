"""0034 - Pascal's Triangle (easy · row-by-row DP / combinatorics)

Return the first ``num_rows`` rows of Pascal's triangle. Every row starts and
ends with 1, and every inner value is the sum of the two values diagonally
above it. num_rows = 0 gives an empty list; negative input is an error.
Example: 5 -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]].

Idea: build each row from the previous one. Padding the previous row with a
0 on both sides and summing neighbouring pairs gives the next row in one
pass, edges included, without special-casing the 1s. Row n holds the
binomial coefficients C(n, 0..n), which the tests use as an independent check
(and which gives a single row in O(n) without the triangle above it).

Time O(n^2) · Space O(n^2) for the output (n = num_rows)
"""
from __future__ import annotations


def generate(num_rows: int) -> list[list[int]]:
    if num_rows < 0:
        raise ValueError("num_rows must be >= 0")
    rows: list[list[int]] = []
    row = [1]
    for _ in range(num_rows):
        rows.append(row)
        padded = [0, *row, 0]
        row = [a + b for a, b in zip(padded, padded[1:])]
    return rows


def get_row(n: int) -> list[int]:
    """Row ``n`` (0-based) on its own, via C(n, k) = C(n, k-1) * (n-k+1) / k."""
    if n < 0:
        raise ValueError("n must be >= 0")
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row
