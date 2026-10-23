from itertools import product
from string import ascii_uppercase

import pytest

from problems.p0047_excel_column_title import column_number, column_title


@pytest.mark.parametrize(
    "n, title",
    [(1, "A"), (26, "Z"), (27, "AA"), (28, "AB"), (52, "AZ"), (53, "BA"), (701, "ZY"), (702, "ZZ"), (703, "AAA"), (16384, "XFD")],
)
def test_examples_both_ways(n, title):
    assert column_title(n) == title
    assert column_number(title) == n


def test_matches_enumerated_labels():
    # Build labels in spreadsheet order: all 1-letter, then all 2-letter, then all 3-letter.
    labels = ["".join(p) for size in (1, 2, 3) for p in product(ascii_uppercase, repeat=size)]
    for n, label in enumerate(labels, start=1):
        assert column_title(n) == label
        assert column_number(label) == n


def test_round_trip_large_numbers():
    for n in (10**6, 2**31 - 1, 26**5, 26**5 + 1):
        assert column_number(column_title(n)) == n


@pytest.mark.parametrize("bad", [0, -1])
def test_rejects_non_positive(bad):
    with pytest.raises(ValueError):
        column_title(bad)


@pytest.mark.parametrize("bad", ["", "a", "A1", "Ä"])
def test_rejects_invalid_titles(bad):
    with pytest.raises(ValueError):
        column_number(bad)
