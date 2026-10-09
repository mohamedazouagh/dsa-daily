import random

import pytest

from problems.p0022_network_delay_time import network_delay_time


def bellman_ford(times, n, k):
    inf = float("inf")
    dist = {i: inf for i in range(1, n + 1)}
    dist[k] = 0
    for _ in range(n - 1):
        for u, v, w in times:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    worst = max(dist.values())
    return -1 if worst == inf else worst


@pytest.mark.parametrize(
    "times,n,k,expected",
    [
        ([(2, 1, 1), (2, 3, 1), (3, 4, 1)], 4, 2, 2),
        ([(1, 2, 1)], 2, 1, 1),
        ([(1, 2, 1)], 2, 2, -1),  # edges are directed
        ([], 1, 1, 0),  # the source alone is reached at time 0
        ([(1, 2, 10), (1, 3, 1), (3, 2, 2)], 3, 1, 3),  # detour beats the direct edge
        ([(1, 2, 0), (2, 3, 0)], 3, 1, 0),  # zero-weight edges
    ],
)
def test_examples(times, n, k, expected):
    assert network_delay_time(times, n, k) == expected


def test_matches_bellman_ford():
    rng = random.Random(22)
    for _ in range(300):
        n = rng.randint(1, 7)
        times = [
            (rng.randint(1, n), rng.randint(1, n), rng.randint(0, 9))
            for _ in range(rng.randint(0, 15))
        ]
        k = rng.randint(1, n)
        assert network_delay_time(times, n, k) == bellman_ford(times, n, k)
