import pytest

from problems.p0028_counting_bits import count_bits


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, [0]),
        (1, [0, 1]),
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
    ],
)
def test_examples(n, expected):
    assert count_bits(n) == expected


def test_matches_bin_count_for_larger_n():
    assert count_bits(1024) == [bin(i).count("1") for i in range(1025)]


def test_powers_of_two_have_one_bit():
    bits = count_bits(4096)
    assert all(bits[1 << k] == 1 for k in range(13))
    assert all(bits[(1 << k) - 1] == k for k in range(13))


def test_negative_n_rejected():
    with pytest.raises(ValueError):
        count_bits(-1)
