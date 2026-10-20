import random

import pytest

from problems.p0006_reverse_linked_list import ListNode, from_list, to_list
from problems.p0043_merge_two_sorted_lists import merge_two_lists


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([5], [], [5]),
        ([1, 2, 3], [4, 5], [1, 2, 3, 4, 5]),
        ([-3, 0, 0], [-5, 0, 9], [-5, -3, 0, 0, 0, 9]),
    ],
)
def test_examples(a, b, expected):
    assert to_list(merge_two_lists(from_list(a), from_list(b))) == expected


def test_reuses_nodes_and_is_stable_on_ties():
    a1, a2 = ListNode(1), ListNode(2)
    a1.next = a2
    b1 = ListNode(1)
    head = merge_two_lists(a1, b1)
    nodes = []
    while head is not None:
        nodes.append(head)
        head = head.next
    assert [id(n) for n in nodes] == [id(a1), id(b1), id(a2)]


def test_long_lists_do_not_hit_recursion_limit():
    n = 50_000
    merged = merge_two_lists(from_list(list(range(0, 2 * n, 2))), from_list(list(range(1, 2 * n, 2))))
    assert to_list(merged) == list(range(2 * n))


def test_matches_sorted_on_random_inputs():
    rng = random.Random(43)
    for _ in range(500):
        a = sorted(rng.randint(-10, 10) for _ in range(rng.randint(0, 8)))
        b = sorted(rng.randint(-10, 10) for _ in range(rng.randint(0, 8)))
        assert to_list(merge_two_lists(from_list(a), from_list(b))) == sorted(a + b)
