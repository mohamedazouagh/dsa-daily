import pytest

from problems.p0007_number_of_islands import num_islands


def grid(*rows: str) -> list[list[str]]:
    return [list(r) for r in rows]


@pytest.mark.parametrize(
    "g,expected",
    [
        ([], 0),
        (grid("0"), 0),
        (grid("1"), 1),
        (grid("11110", "11010", "11000", "00000"), 1),
        (grid("11000", "11000", "00100", "00011"), 3),
        (grid("101", "010", "101"), 5),  # diagonals don't connect
        (grid("111", "101", "111"), 1),  # ring around a lake
    ],
)
def test_num_islands(g, expected):
    assert num_islands(g) == expected


def test_grid_is_not_modified():
    g = grid("110", "011")
    before = [row[:] for row in g]
    num_islands(g)
    assert g == before


def test_large_single_island_has_no_recursion_issue():
    assert num_islands([["1"] * 300 for _ in range(300)]) == 1
