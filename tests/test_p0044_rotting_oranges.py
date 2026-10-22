import random

import pytest

from problems.p0044_rotting_oranges import oranges_rotting


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
        ([[0]], 0),
        ([[1]], -1),
        ([[2, 2], [1, 1], [0, 0], [2, 0]], 1),
        ([[2, 1, 1, 1, 1, 1, 2]], 3),  # two sources meet in the middle
        ([], 0),
    ],
)
def test_examples(grid, expected):
    assert oranges_rotting(grid) == expected


def test_does_not_mutate_input():
    grid = [[2, 1], [1, 1]]
    oranges_rotting(grid)
    assert grid == [[2, 1], [1, 1]]


def _brute_force(grid):
    """Simulate minute by minute on a copy until nothing changes."""
    g = [row[:] for row in grid]
    minutes = 0
    while True:
        to_rot = [
            (r, c)
            for r in range(len(g))
            for c in range(len(g[0]))
            if g[r][c] == 1
            and any(
                0 <= r + dr < len(g) and 0 <= c + dc < len(g[0]) and g[r + dr][c + dc] == 2
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            )
        ]
        if not to_rot:
            break
        for r, c in to_rot:
            g[r][c] = 2
        minutes += 1
    return -1 if any(1 in row for row in g) else minutes


def test_matches_simulation_on_random_grids():
    rng = random.Random(44)
    for _ in range(400):
        rows, cols = rng.randint(1, 6), rng.randint(1, 6)
        grid = [[rng.choice([0, 1, 1, 2]) for _ in range(cols)] for _ in range(rows)]
        assert oranges_rotting(grid) == _brute_force(grid)


def test_large_grid_single_corner_source():
    n = 200
    grid = [[1] * n for _ in range(n)]
    grid[0][0] = 2
    assert oranges_rotting(grid) == 2 * (n - 1)
