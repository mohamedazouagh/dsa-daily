"""0051 - Flood Fill (easy · grid DFS with an explicit stack)

Given a grid of colours, a start cell (row, col) and a new colour, repaint
the start cell and every cell connected to it up, down, left or right
through cells of the same original colour. Return the repainted grid.
Example: [[1,1,1],[1,1,0],[1,0,1]], start (1, 1), colour 2 ->
[[2,2,2],[2,2,0],[2,0,1]] (the bottom-right 1 is only touching diagonally).

Idea: depth-first search from the start cell, using a list as a stack so a
large region can't hit Python's recursion limit. Painting a cell as soon as
it is pushed doubles as the "visited" mark, so no separate set is needed.
One trap: if the new colour equals the old one, painting marks nothing as
visited and the search would loop forever, so return early. The input grid
is left untouched; the function works on a copy.

`region_size` reuses the same walk to count the cells that would change.

Time O(R * C) in the worst case (every cell visited once) · Space O(R * C)
for the stack and the copy
"""
from __future__ import annotations


def flood_fill(grid: list[list[int]], row: int, col: int, colour: int) -> list[list[int]]:
    out = [r[:] for r in grid]
    if not (0 <= row < len(out) and 0 <= col < len(out[row])):
        raise IndexError(f"start cell ({row}, {col}) is outside the grid")
    old = out[row][col]
    if old == colour:
        return out
    out[row][col] = colour
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < len(out) and 0 <= nc < len(out[nr]) and out[nr][nc] == old:
                out[nr][nc] = colour
                stack.append((nr, nc))
    return out


def region_size(grid: list[list[int]], row: int, col: int) -> int:
    """Number of cells connected to (row, col) that share its colour (itself included)."""
    marker = object()  # a "colour" that can't be in the grid
    filled = flood_fill(grid, row, col, marker)  # type: ignore[arg-type]
    return sum(cell is marker for line in filled for cell in line)
