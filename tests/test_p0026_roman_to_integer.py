import pytest

from problems.p0026_roman_to_integer import int_to_roman, roman_to_int


@pytest.mark.parametrize(
    "s,expected",
    [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("MMXXVI", 2026),
        ("MMMCMXCIX", 3999),
        ("CDXLIV", 444),
    ],
)
def test_examples(s, expected):
    assert roman_to_int(s) == expected


@pytest.mark.parametrize("s", ["", "IIII", "IC", "VX", "IIV", "MMMM", "XM", "abc", "VV", "iv"])
def test_rejects_invalid(s):
    with pytest.raises(ValueError):
        roman_to_int(s)


def test_round_trip_all_values():
    for n in range(1, 4000):
        assert roman_to_int(int_to_roman(n)) == n


def test_int_to_roman_range():
    with pytest.raises(ValueError):
        int_to_roman(0)
    with pytest.raises(ValueError):
        int_to_roman(4000)
