"""0069 - Lowest Common Ancestor of a BST (easy · binary search tree walk)

Given the root of a binary search tree with distinct values and two values p
and q that are both in the tree, return the lowest node that has both of them
in its subtree. A node counts as its own descendant, so if p sits below q the
answer is q itself. Example: in 6(2(0, 4(3, 5)), 8(7, 9)), the LCA of 2 and 8
is 6, of 2 and 4 is 2, and of 3 and 5 is 4.

Idea: the BST order tells us where both values live without searching. If p
and q are both smaller than the current node, both are in the left subtree,
so the answer is there too; both larger means go right. The first node where
they split (one on each side, or one of them equal to the node) is the lowest
node that still holds both. No visited set or parent pointers needed, and
walking with a loop keeps a degenerate, list-shaped tree clear of the
recursion limit.

`bst_insert` builds trees for the tests; the tests check the walk against a
general-tree answer built from root-to-node paths.

Time O(h) · Space O(1), h = tree height (O(log n) balanced, O(n) worst case)
"""
from __future__ import annotations

from problems.p0012_max_depth_binary_tree import TreeNode


def lowest_common_ancestor(root: TreeNode | None, p: int, q: int) -> TreeNode:
    lo, hi = min(p, q), max(p, q)
    node = root
    while node:
        if hi < node.val:
            node = node.left
        elif lo > node.val:
            node = node.right
        else:
            return node
    raise ValueError("p and q must both be in the tree")


def bst_insert(root: TreeNode | None, val: int) -> TreeNode:
    """Insert ``val`` (iteratively) and return the root; duplicates are ignored."""
    new = TreeNode(val)
    if root is None:
        return new
    node = root
    while True:
        if val < node.val:
            if node.left is None:
                node.left = new
                return root
            node = node.left
        elif val > node.val:
            if node.right is None:
                node.right = new
                return root
            node = node.right
        else:
            return root
