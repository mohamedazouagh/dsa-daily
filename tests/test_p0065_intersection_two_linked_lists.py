import random

from problems.p0006_reverse_linked_list import ListNode, from_list, to_list
from problems.p0065_intersection_two_linked_lists import (
    get_intersection_node,
    intersection_by_lengths,
)

SOLVERS = (get_intersection_node, intersection_by_lengths)


def _y(prefix_a: list[int], prefix_b: list[int], shared: list[int]):
    """Build two lists that share the nodes of ``shared`` (same objects)."""
    tail = from_list(shared)

    def attach(prefix):
        if not prefix:
            return tail
        head = from_list(prefix)
        node = head
        while node.next is not None:
            node = node.next
        node.next = tail
        return head

    return attach(prefix_a), attach(prefix_b), tail


def test_example_shared_tail():
    a, b, tail = _y([4, 1], [5, 6, 1], [8, 4, 5])
    for solve in SOLVERS:
        assert solve(a, b) is tail
    assert to_list(a) == [4, 1, 8, 4, 5]  # lists left untouched
    assert to_list(b) == [5, 6, 1, 8, 4, 5]


def test_equal_values_are_not_an_intersection():
    a, b = from_list([1, 2, 3]), from_list([1, 2, 3])
    for solve in SOLVERS:
        assert solve(a, b) is None


def test_edge_cases():
    single = ListNode(7)
    for solve in SOLVERS:
        assert solve(None, None) is None
        assert solve(from_list([1]), None) is None
        assert solve(single, single) is single
        a, b, tail = _y([], [9, 9, 9], [1, 2])  # A starts at the shared node
        assert solve(a, b) is tail


def test_random_y_shapes():
    rng = random.Random(65)
    for _ in range(300):
        pa = [rng.randint(0, 3) for _ in range(rng.randint(0, 6))]
        pb = [rng.randint(0, 3) for _ in range(rng.randint(0, 6))]
        shared = [rng.randint(0, 3) for _ in range(rng.randint(0, 4))]
        a, b, tail = _y(pa, pb, shared)
        if not shared:
            a, b, tail = from_list(pa), from_list(pb), None
        for solve in SOLVERS:
            assert solve(a, b) is tail
