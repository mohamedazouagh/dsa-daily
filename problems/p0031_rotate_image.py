"""0031 - Rotate Image (medium · in-place matrix manipulation)

Given an n x n matrix, rotate it 90 degrees clockwise in place: change the
input list of lists itself instead of building a new matrix.
Example: [[1, 2, 3],      [[7, 4, 1],
          [4, 5, 6],  ->   [8, 5, 2],
          [7, 8, 9]]       [9, 6, 3]]

Idea: a clockwise rotation is a transpose (swap m[i][j] with m[j][i]) followed
by reversing every row. Both steps are simple swaps, so no second matrix is
needed. (Counter-clockwise would be transpose + reverse the row order.)

Time O(n^2) · Space O(1) extra
"""
from __future__ import annotations


def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
