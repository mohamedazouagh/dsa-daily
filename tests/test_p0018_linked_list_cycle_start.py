import pytest

from problems.p0018_linked_list_cycle_start import build_with_cycle, detect_cycle


@pytest.mark.parametrize(
    "values,pos",
    [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),  # whole list is the cycle
        ([1], 0),  # single node pointing at itself
        ([1, 2, 3, 4, 5, 6], 5),  # tail points at itself
        ([7, 7, 7, 7], 2),  # duplicate values: identity matters, not value
    ],
)
def test_returns_cycle_entry_node(values, pos):
    head, nodes = build_with_cycle(values, pos)
    assert detect_cycle(head) is nodes[pos]


@pytest.mark.parametrize("values", [[], [1], [1, 2], [1, 2, 3, 4, 5]])
def test_no_cycle_returns_none(values):
    head, _ = build_with_cycle(values, -1)
    assert detect_cycle(head) is None


def test_all_entry_points_for_many_lengths():
    for n in range(1, 30):
        for pos in range(n):
            head, nodes = build_with_cycle(list(range(n)), pos)
            assert detect_cycle(head) is nodes[pos]


def test_list_is_not_modified():
    head, nodes = build_with_cycle([1, 2, 3, 4], 1)
    links = [n.next for n in nodes]
    detect_cycle(head)
    assert all(n.next is link for n, link in zip(nodes, links))
