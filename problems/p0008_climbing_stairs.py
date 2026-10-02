"""0008 - Climbing Stairs (easy · dynamic programming)

A staircase has n steps. Each move climbs either 1 or 2 steps. Count how many
distinct sequences of moves reach the top. n = 0 counts as one way (do
nothing); negative n is invalid.

Idea: the last move onto step n came from step n-1 or step n-2, so
ways(n) = ways(n-1) + ways(n-2), with ways(0) = ways(1) = 1. That is the
Fibonacci recurrence. Only the previous two values are ever needed, so two
variables replace the whole DP table.

Time O(n) · Space O(1)
"""
from __future__ import annotations


def climb_stairs(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    prev, cur = 1, 1  # ways(0), ways(1)
    for _ in range(n - 1):
        prev, cur = cur, prev + cur
    return cur
