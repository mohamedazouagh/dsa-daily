import copy
import random

from problems.p0012_max_depth_binary_tree import TreeNode
from problems.p0059_invert_binary_tree import invert_tree, is_mirror


def _inorder(root):
    out, stack, node = [], [], root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out


def _random_tree(rng, n):
    if n == 0:
        return None
    left = rng.randint(0, n - 1)
    return TreeNode(rng.randint(0, 9), _random_tree(rng, left), _random_tree(rng, n - 1 - left))


def test_example():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    out = invert_tree(root)
    assert out is root  # inverted in place
    assert out.left.val == 7 and out.right.val == 2
    assert [out.left.left.val, out.left.right.val, out.right.left.val, out.right.right.val] == [9, 6, 3, 1]


def test_empty_and_single_node():
    assert invert_tree(None) is None
    one = TreeNode(5)
    assert invert_tree(one) is one and one.left is None and one.right is None


def test_deep_chain_does_not_hit_recursion_limit():
    root = node = TreeNode(0)
    for i in range(1, 20000):
        node.left = TreeNode(i)
        node = node.left
    invert_tree(root)
    node, depth = root, 0
    while node:
        assert node.left is None
        node, depth = node.right, depth + 1
    assert depth == 20000


def test_random_trees_mirror_and_reverse_inorder():
    rng = random.Random(59)
    for _ in range(300):
        root = _random_tree(rng, rng.randint(0, 25))
        before = copy.deepcopy(root)
        invert_tree(root)
        assert is_mirror(before, root)
        assert _inorder(root) == _inorder(before)[::-1]
        invert_tree(root)  # inverting twice gives the original back
        assert _inorder(root) == _inorder(before)


def test_is_mirror_rejects_non_mirrors():
    assert is_mirror(None, None)
    assert not is_mirror(TreeNode(1), None)
    assert not is_mirror(TreeNode(1, TreeNode(2)), TreeNode(1, TreeNode(2)))  # same, not mirrored
    assert is_mirror(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)))
