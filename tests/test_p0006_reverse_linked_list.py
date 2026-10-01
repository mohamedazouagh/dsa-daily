import pytest

from problems.p0006_reverse_linked_list import from_list, reverse_list, to_list


@pytest.mark.parametrize(
    "values,expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([7, 7, 3], [3, 7, 7]),
    ],
)
def test_reverse_list(values, expected):
    assert to_list(reverse_list(from_list(values))) == expected


def test_reverses_in_place_without_new_nodes():
    head = from_list([1, 2, 3])
    nodes = [head, head.next, head.next.next]
    new_head = reverse_list(head)
    assert new_head is nodes[2]
    assert nodes[0].next is None


def test_long_list_does_not_recurse():
    values = list(range(100_000))
    assert to_list(reverse_list(from_list(values))) == values[::-1]
