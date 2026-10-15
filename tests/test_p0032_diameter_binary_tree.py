import pytest

from problems.p0012_max_depth_binary_tree import TreeNode, from_level_order
from problems.p0032_diameter_binary_tree import diameter


@pytest.mark.parametrize(
    "values,expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([1], 0),
        ([], 0),
        ([1, None, 2, None, 3, None, 4], 3),
    ],
)
def test_examples(values, expected):
    assert diameter(from_level_order(values)) == expected


def test_longest_path_can_skip_the_root():
    # Root 1 has a single child 2; the long path bends at 2, not at the root.
    #        1
    #       /
    #      2
    #     / \
    #    3   4
    #   /     \
    #  5       6
    #  /         \
    # 7           8
    root = TreeNode(1, TreeNode(2,
                                TreeNode(3, TreeNode(5, TreeNode(7))),
                                TreeNode(4, None, TreeNode(6, None, TreeNode(8)))))
    assert diameter(root) == 6


def test_deep_chain_does_not_hit_recursion_limit():
    root = node = TreeNode(0)
    for i in range(1, 5000):
        node.left = TreeNode(i)
        node = node.left
    assert diameter(root) == 4999
