"""0052 - Gas Station (medium · greedy, one pass with a running balance)

Stations sit on a circular road. At station i you can fill up gas[i] litres,
and driving from station i to station i + 1 (the last one wraps to 0) burns
cost[i] litres. The tank is unlimited and starts empty. Return the index of
the station you can start from to drive one full lap, or -1 if no start
works. (With strictly positive margins the start is unique; if several
legs net to zero more than one start may work, and any of them is valid.)
Example: gas [1,2,3,4,5], cost [3,4,5,1,2] -> 3 (tank after each leg:
4-1=3, 3+5-2=6, 6+1-3=4, 4+2-4=2, 2+3-5=0).

Idea: two facts make one pass enough.
1. If total gas < total cost, no start can work; otherwise one does.
2. If you start at s and the tank first goes negative after station j, then
   no station between s and j can be a start either: each of them would
   arrive at j with no more fuel than the run from s had (that run reached
   them with a tank >= 0). So jump the candidate to j + 1 and reset the tank.
The last candidate standing is the answer when the totals allow it.

`lap_fuel` replays the lap from a start and returns the tank after every
leg; the tests use it to check that the answer never runs dry.

Time O(n) · Space O(1)
"""
from __future__ import annotations


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if len(gas) != len(cost):
        raise ValueError("gas and cost must have the same length")
    if not gas:
        return -1
    total = tank = start = 0
    for i, (g, c) in enumerate(zip(gas, cost)):
        diff = g - c
        total += diff
        tank += diff
        if tank < 0:
            start, tank = i + 1, 0
    return start if total >= 0 else -1


def lap_fuel(gas: list[int], cost: list[int], start: int) -> list[int]:
    """Tank level after each of the n legs when starting at ``start``."""
    n, tank, levels = len(gas), 0, []
    for k in range(n):
        i = (start + k) % n
        tank += gas[i] - cost[i]
        levels.append(tank)
    return levels
