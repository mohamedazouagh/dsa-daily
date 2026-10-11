"""0024 - Coin Change (medium · dynamic programming)

Given coin denominations (unlimited supply of each) and a target amount,
return the fewest coins that add up exactly to the amount, or -1 if the
amount cannot be made. An amount of 0 needs 0 coins.

Idea: bottom-up DP over amounts. best[a] is the fewest coins for amount a;
best[0] = 0, and for every a, best[a] = 1 + min(best[a - c]) over coins
c <= a whose sub-amount is reachable. Greedy (always take the biggest coin)
is wrong in general: coins [1, 3, 4] and amount 6 -> greedy 4+1+1, optimum 3+3.

Time O(amount * len(coins)) · Space O(amount)
"""
from __future__ import annotations


def coin_change(coins: list[int], amount: int) -> int:
    if amount < 0:
        raise ValueError("amount must be >= 0")
    usable = sorted({c for c in coins if c > 0})
    unreachable = amount + 1  # more coins than any real answer can need
    best = [0] + [unreachable] * amount
    for a in range(1, amount + 1):
        for c in usable:
            if c > a:
                break
            if best[a - c] + 1 < best[a]:
                best[a] = best[a - c] + 1
    return best[amount] if best[amount] != unreachable else -1
