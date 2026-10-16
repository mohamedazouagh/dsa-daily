from math import comb

import pytest

from problems.p0034_pascals_triangle import generate, get_row


def test_example_five_rows():
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def test_zero_and_one_rows():
    assert generate(0) == []
    assert generate(1) == [[1]]


def test_rows_match_binomial_coefficients():
    for n, row in enumerate(generate(30)):
        assert row == [comb(n, k) for k in range(n + 1)]
        assert sum(row) == 2**n


def test_get_row_matches_generate():
    tri = generate(25)
    for n in range(25):
        assert get_row(n) == tri[n]


def test_negative_input_rejected():
    with pytest.raises(ValueError):
        generate(-1)
    with pytest.raises(ValueError):
        get_row(-2)
