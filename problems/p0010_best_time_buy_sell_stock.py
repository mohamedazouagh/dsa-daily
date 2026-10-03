"""0010 - Best Time to Buy and Sell Stock (easy · greedy)

Given daily prices, choose one day to buy and a later day to sell. Return the
largest profit possible from a single trade, or 0 if no trade makes money
(prices only fall, or there are fewer than two days).

Idea: scan once and keep the cheapest price seen so far. Selling today can
only be best if we bought at that running minimum, so the answer is the
largest (price - running minimum) over all days.

Time O(n) · Space O(1)
"""
from __future__ import annotations


def max_profit(prices: list[float]) -> float:
    best = 0
    cheapest = None
    for price in prices:
        if cheapest is None or price < cheapest:
            cheapest = price
        elif price - cheapest > best:
            best = price - cheapest
    return best
