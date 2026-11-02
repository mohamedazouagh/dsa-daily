import random

from problems.p0062_search_2d_matrix import search_matrix, search_sorted_rows_cols

GRID = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]


def test_examples():
    assert search_matrix(GRID, 3) is True
    assert search_matrix(GRID, 13) is False


def test_every_value_and_the_gaps():
    values = [v for row in GRID for v in row]
    for v in values:
        assert search_matrix(GRID, v)
    for v in range(-2, 65):
        assert search_matrix(GRID, v) == (v in values)


def test_empty_and_single_shapes():
    assert search_matrix([], 1) is False
    assert search_matrix([[]], 1) is False
    assert search_matrix([[5]], 5) is True
    assert search_matrix([[1, 2, 3, 4]], 4) is True  # one row
    assert search_matrix([[1], [2], [3]], 0) is False  # one column


def test_random_strict_matrices_match_membership():
    rng = random.Random(62)
    for _ in range(200):
        m, n = rng.randint(1, 6), rng.randint(1, 6)
        flat = sorted(rng.sample(range(200), m * n))
        grid = [flat[r * n:(r + 1) * n] for r in range(m)]
        target = rng.randrange(-5, 205)
        assert search_matrix(grid, target) == (target in flat)


def test_staircase_on_overlapping_rows():
    grid = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
    assert search_sorted_rows_cols(grid, 5) == (1, 1)
    assert search_sorted_rows_cols(grid, 10) == (3, 0)
    assert search_sorted_rows_cols(grid, 15) is None
    assert search_sorted_rows_cols([], 1) is None
    assert search_matrix(grid, 2) is False  # the flat search assumes strict row order


def test_staircase_random_matches_brute_force():
    rng = random.Random(162)
    for _ in range(200):
        m, n = rng.randint(1, 5), rng.randint(1, 5)
        # rows and columns sorted: cumulative non-negative steps in both directions
        grid = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                above = grid[r - 1][c] if r else 0
                left = grid[r][c - 1] if c else 0
                grid[r][c] = max(above, left) + rng.randint(0, 3)
        target = rng.randint(0, 30)
        found = search_sorted_rows_cols(grid, target)
        present = any(target in row for row in grid)
        assert (found is not None) == present
        if found:
            assert grid[found[0]][found[1]] == target
