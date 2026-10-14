import copy

import pytest

from problems.p0031_rotate_image import rotate


def rotated_copy(m):
    # Reference: new row i is old column i read bottom-up.
    return [list(col) for col in zip(*m[::-1])]


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ([[5]], [[5]]),
        ([], []),
    ],
)
def test_examples(matrix, expected):
    assert rotate(matrix) is None  # works in place
    assert matrix == expected


def test_matches_reference_for_several_sizes():
    for n in range(1, 8):
        m = [[i * n + j for j in range(n)] for i in range(n)]
        expected = rotated_copy(m)
        rotate(m)
        assert m == expected


def test_four_rotations_restore_original_and_keep_row_objects():
    m = [[i * 4 + j for j in range(4)] for i in range(4)]
    original = copy.deepcopy(m)
    rows = [id(r) for r in m]
    for _ in range(4):
        rotate(m)
    assert m == original
    assert [id(r) for r in m] == rows


def test_non_square_rejected():
    with pytest.raises(ValueError):
        rotate([[1, 2, 3], [4, 5, 6]])
