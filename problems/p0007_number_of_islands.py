"""0007 — Number of Islands (medium · graph BFS)

Given a grid of "1" (land) and "0" (water), count the islands. An island is a
group of land cells connected horizontally or vertically (not diagonally).
The grid may be empty; otherwise all rows have the same length.

Idea: scan every cell. When we hit land we haven't seen, that's a new island:
count it and flood-fill all land reachable from it with a breadth-first
search, marking cells as seen so they are never counted again. A deque-based
BFS avoids recursion limits on big islands, and a `seen` set keeps the input
grid unchanged.

Time O(rows · cols) · Space O(rows · cols) for the seen set and queue
"""
from __future__ import annotations

from collections import deque


def num_islands(grid: list[list[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    seen: set[tuple[int, int]] = set()
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            islands += 1
            seen.add((r, c))
            queue = deque([(r, c)])
            while queue:
                cr, cc = queue.popleft()
                for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc))
    return islands
