"""0022 - Network Delay Time (medium · shortest paths, Dijkstra)

A network has n nodes labelled 1..n and directed, weighted edges (u, v, w):
a signal sent from u reaches v after w time units. A signal starts at node k.
Return how long it takes until every node has received it, or -1 if some
node can never be reached.

Idea: the time a node receives the signal is its shortest-path distance from
k, and the answer is the largest of those distances. All weights are
non-negative, so Dijkstra works: pop the closest unsettled node from a
min-heap, settle it, and relax its outgoing edges. Stale heap entries (a node
already settled with a shorter distance) are skipped when popped.

Time O((n + e) log e) · Space O(n + e)
"""
from __future__ import annotations

import heapq


def network_delay_time(times: list[tuple[int, int, int]], n: int, k: int) -> int:
    graph: dict[int, list[tuple[int, int]]] = {}
    for u, v, w in times:
        graph.setdefault(u, []).append((v, w))
    dist: dict[int, int] = {}
    heap = [(0, k)]
    while heap:
        d, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = d
        for nxt, w in graph.get(node, ()):
            if nxt not in dist:
                heapq.heappush(heap, (d + w, nxt))
    return max(dist.values()) if len(dist) == n else -1
