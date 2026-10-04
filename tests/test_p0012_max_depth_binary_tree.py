import pytest

from problems.p0012_max_depth_binary_tree import TreeNode, from_level_order, max_depth


@pytest.mark.parametrize(
    "values,expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([1], 1),
        ([], 0),
        ([1, 2, 3, 4, None, None, 5, 6], 4),  # deepest leaf on the left
    ],
)
def test_max_depth(values, expected):
    assert max_depth(from_level_order(values)) == expected


def test_deep_chain_does_not_hit_recursion_limit():
    root = node = TreeNode(0)
    for i in range(1, 5000):
        node.right = TreeNode(i)
        node = node.right
    assert max_depth(root) == 5000
