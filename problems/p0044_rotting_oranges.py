"""0044 - Rotting Oranges (medium · multi-source BFS on a grid)

A grid holds 0 (empty cell), 1 (fresh orange) or 2 (rotten orange). Every
minute, each fresh orange that shares an edge (up/down/left/right) with a
rotten one becomes rotten. Return how many minutes pass until no fresh orange
is left, or -1 if some fresh orange can never be reached.
Example: [[2,1,1],[1,1,0],[0,1,1]] -> 4; [[2,1,1],[0,1,1],[1,0,1]] -> -1
(the bottom-left orange is cut off); [[0,2]] -> 0 (nothing fresh to begin with).

Idea: start a BFS from *all* rotten oranges at once (multi-source BFS). The
queue then processes cells level by level, and level k is exactly the set of
oranges that rot at minute k, so the number of completed levels that rotted
something is the answer. Count fresh oranges up front and decrement as they
rot; if any remain when the queue empties, they are unreachable -> -1.
Running one BFS per rotten orange instead would revisit cells and cost
O((rows*cols)^2) in the worst case.

Time O(rows * cols) · Space O(rows * cols) for the queue
"""
from __future__ import annotations

from collections import deque

EMPTY, FRESH, ROTTEN = 0, 1, 2


def oranges_rotting(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    cells = [row[:] for row in grid]  # don't mutate the caller's grid
    queue: deque[tuple[int, int]] = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if cells[r][c] == ROTTEN:
                queue.append((r, c))
            elif cells[r][c] == FRESH:
                fresh += 1

    minutes = 0
    while queue and fresh:
        for _ in range(len(queue)):  # one BFS level = one minute
            r, c = queue.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and cells[nr][nc] == FRESH:
                    cells[nr][nc] = ROTTEN
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1
    return -1 if fresh else minutes
