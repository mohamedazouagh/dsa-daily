import random

import pytest

from problems.p0052_gas_station import can_complete_circuit, lap_fuel


def brute_force(gas, cost):
    for s in range(len(gas)):
        if all(level >= 0 for level in lap_fuel(gas, cost, s)):
            return s
    return -1


def test_example():
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert lap_fuel([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3) == [3, 6, 4, 2, 0]


def test_not_enough_gas_overall():
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1


def test_single_station_and_empty():
    assert can_complete_circuit([5], [5]) == 0
    assert can_complete_circuit([4], [5]) == -1
    assert can_complete_circuit([], []) == -1


def test_start_after_a_dip_at_the_end():
    # first case never dips; second dips twice, so the candidate moves to the last station
    assert can_complete_circuit([3, 1, 1], [1, 2, 2]) == 0
    assert can_complete_circuit([1, 1, 3], [2, 2, 1]) == 2


def test_against_brute_force():
    rng = random.Random(52)
    for _ in range(1000):
        n = rng.randint(1, 9)
        gas = [rng.randint(0, 6) for _ in range(n)]
        cost = [rng.randint(0, 6) for _ in range(n)]
        got, expected = can_complete_circuit(gas, cost), brute_force(gas, cost)
        if expected == -1:
            assert got == -1
        else:
            # with zero-sum legs several starts can work; any valid one is fine
            assert all(level >= 0 for level in lap_fuel(gas, cost, got))


def test_rejects_length_mismatch():
    with pytest.raises(ValueError):
        can_complete_circuit([1, 2], [1])
