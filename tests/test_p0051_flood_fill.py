import random

import pytest

from problems.p0051_flood_fill import flood_fill, region_size


def recursive_fill(grid, r, c, colour):
    out = [row[:] for row in grid]
    old = out[r][c]
    if old == colour:
        return out

    def go(i, j):
        if 0 <= i < len(out) and 0 <= j < len(out[i]) and out[i][j] == old:
            out[i][j] = colour
            go(i - 1, j), go(i + 1, j), go(i, j - 1), go(i, j + 1)

    go(r, c)
    return out


def test_example_ignores_diagonals():
    grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert flood_fill(grid, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert grid == [[1, 1, 1], [1, 1, 0], [1, 0, 1]]  # input not modified


def test_same_colour_returns_copy_without_looping():
    grid = [[0, 0], [0, 0]]
    out = flood_fill(grid, 0, 0, 0)
    assert out == grid and out is not grid


def test_single_cell_and_ragged_rows():
    assert flood_fill([[5]], 0, 0, 9) == [[9]]
    assert flood_fill([[1, 1, 1], [1], [1, 1]], 0, 2, 3) == [[3, 3, 3], [3], [3, 3]]


def test_large_region_does_not_hit_recursion_limit():
    grid = [[0] * 300 for _ in range(300)]
    out = flood_fill(grid, 150, 150, 1)
    assert all(cell == 1 for row in out for cell in row)
    assert region_size(grid, 0, 0) == 90_000


def test_against_recursive_reference():
    rng = random.Random(51)
    for _ in range(300):
        h, w = rng.randint(1, 8), rng.randint(1, 8)
        grid = [[rng.randint(0, 2) for _ in range(w)] for _ in range(h)]
        r, c, colour = rng.randrange(h), rng.randrange(w), rng.randint(0, 3)
        assert flood_fill(grid, r, c, colour) == recursive_fill(grid, r, c, colour)


def test_region_size():
    grid = [[1, 1, 0], [0, 1, 0], [1, 0, 0]]
    assert region_size(grid, 0, 0) == 3
    assert region_size(grid, 0, 2) == 4
    assert region_size(grid, 2, 0) == 1


@pytest.mark.parametrize("r, c", [(-1, 0), (0, 3), (3, 0)])
def test_rejects_start_outside_grid(r, c):
    with pytest.raises(IndexError):
        flood_fill([[1, 2, 3], [4, 5, 6], [7, 8, 9]], r, c, 0)
