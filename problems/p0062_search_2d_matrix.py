"""0062 - Search a 2D Matrix (medium · binary search over a virtual flat array)

A matrix has rows sorted left to right, and the first value of each row is
greater than the last value of the row above, so reading it row by row gives
one sorted sequence. Return whether a target value is in it. Example:
[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]] contains 3 but not 13.

Idea: treat the m x n matrix as a sorted array of length m * n without
building it. Flat index k maps to row k // n and column k % n, so an ordinary
binary search over 0 .. m*n - 1 works directly on the matrix.

`search_sorted_rows_cols` handles the weaker variant where every row and every
column is sorted but rows may overlap (e.g. [[1, 4], [2, 5]]). There a flat
binary search is wrong; instead start in the top-right corner and walk a
"staircase": if the value is too big, move left (the whole column below is
even bigger); if it is too small, move down (the rest of the row is smaller).

Time O(log(m*n)) for the strict matrix, O(m + n) for the staircase
Space O(1) for both
"""
from __future__ import annotations


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        value = matrix[mid // n][mid % n]
        if value == target:
            return True
        if value < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def search_sorted_rows_cols(matrix: list[list[int]], target: int) -> tuple[int, int] | None:
    """Position of ``target`` in a matrix whose rows and columns are each sorted, or None."""
    if not matrix or not matrix[0]:
        return None
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        value = matrix[row][col]
        if value == target:
            return row, col
        if value > target:
            col -= 1
        else:
            row += 1
    return None
