import pytest

from problems.p0049_happy_number import digit_square_sum, happy_trail, is_happy

# First happy numbers (OEIS A007770)
HAPPY_UP_TO_100 = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]


def test_digit_square_sum():
    assert digit_square_sum(19) == 82
    assert digit_square_sum(100) == 1
    assert digit_square_sum(0) == 0
    assert digit_square_sum(999) == 243


def test_matches_known_happy_numbers_up_to_100():
    assert [n for n in range(1, 101) if is_happy(n)] == HAPPY_UP_TO_100


def test_agrees_with_set_based_trail_on_a_wide_range():
    for n in list(range(1, 2000)) + [10**12 + 7, 2**40, 7 * 10**15]:
        assert is_happy(n) == (happy_trail(n)[-1] == 1)


def test_trails():
    assert happy_trail(19) == [19, 82, 68, 100, 1]
    assert happy_trail(1) == [1]
    assert happy_trail(2) == [2, 4, 16, 37, 58, 89, 145, 42, 20, 4]


@pytest.mark.parametrize("bad", [0, -7])
def test_rejects_non_positive(bad):
    with pytest.raises(ValueError):
        is_happy(bad)
    with pytest.raises(ValueError):
        happy_trail(bad)
