import pytest

from problems.p0010_best_time_buy_sell_stock import max_profit


@pytest.mark.parametrize(
    "prices,expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),  # buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),  # only falling: no trade
        ([], 0),
        ([5], 0),
        ([2, 4, 1], 2),  # later minimum must not be paired with an earlier peak
        ([3, 3, 3], 0),
        ([1, 2, 3, 4, 5], 4),
        ([2, 9, 1, 8], 7),  # tie between two trades
    ],
)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected


def test_float_prices():
    assert max_profit([1.5, 1.25, 2.0]) == pytest.approx(0.75)
