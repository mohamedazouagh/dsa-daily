"""0029 - Redundant Connection (medium · union-find / disjoint set)

A tree on nodes 1..n got one extra edge, so the graph now has exactly one
cycle. Given the n edges in input order, return the edge that can be removed
to get a tree back; if several qualify, return the one that appears last.
Example: [[1, 2], [1, 3], [2, 3]] -> [2, 3].

Idea: add edges one by one to a union-find structure. Before joining u and v,
check whether they already share a root: if so, they are already connected
and this edge closes the cycle. Because edges are processed in order, the
first such edge is the last edge of the cycle in the input, which is the
one the problem asks for. Path compression (halving) plus union by size
keeps the trees almost flat.

Time O(n · α(n)) ≈ O(n) · Space O(n)
"""
from __future__ import annotations


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    # Size by the largest label so malformed input (no cycle) fails cleanly.
    n = max((max(e) for e in edges), default=0)
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path halving
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return [u, v]
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]
    raise ValueError("edges contain no cycle")
