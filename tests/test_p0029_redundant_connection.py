import random

import pytest

from problems.p0029_redundant_connection import find_redundant_connection


@pytest.mark.parametrize(
    "edges,expected",
    [
        ([[1, 2], [1, 3], [2, 3]], [2, 3]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
        ([[1, 2], [2, 1]], [2, 1]),  # two-node cycle
        ([[3, 4], [1, 2], [2, 4], [3, 1], [2, 5]], [3, 1]),
    ],
)
def test_examples(edges, expected):
    assert find_redundant_connection(edges) == expected


def test_no_cycle_raises():
    with pytest.raises(ValueError):
        find_redundant_connection([[1, 2]])


def _is_tree(n, edges):
    seen, adj = set(), {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    stack = [1]
    while stack:
        x = stack.pop()
        if x not in seen:
            seen.add(x)
            stack.extend(adj[x])
    return len(edges) == n - 1 and len(seen) == n


def test_random_trees_plus_one_edge():
    rng = random.Random(29)
    for _ in range(300):
        n = rng.randint(3, 25)
        tree = [[rng.randint(1, i - 1), i] for i in range(2, n + 1)]
        u, v = rng.sample(range(1, n + 1), 2)
        edges = tree + [[u, v]]
        if [u, v] in tree or [v, u] in tree:
            continue
        rng.shuffle(edges)
        removed = find_redundant_connection(edges)
        rest = list(edges)
        rest.remove(removed)
        assert _is_tree(n, rest)
        # Last-in-input rule: no later edge can be removed instead.
        idx = edges.index(removed)
        for later in edges[idx + 1:]:
            alt = list(edges)
            alt.remove(later)
            assert not _is_tree(n, alt)
