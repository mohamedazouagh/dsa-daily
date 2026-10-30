"""0059 - Invert Binary Tree (easy · tree traversal with an explicit stack)

Given the root of a binary tree, mirror it: every node's left and right
children swap places, all the way down, and return the root. Example: the
tree 4(2(1, 3), 7(6, 9)) becomes 4(7(9, 6), 2(3, 1)). An empty tree stays
empty.

Idea: the mirror of a tree is the root with its two subtrees swapped and each
of them mirrored too. The order in which nodes get their children swapped does
not matter, so any traversal works: pop a node from a stack, swap its two
children, push the non-empty ones. Using a stack instead of recursion keeps a
very deep, list-like tree clear of Python's recursion limit.

`is_mirror(a, b)` checks the result without building anything: two trees are
mirrors when their roots match and a.left mirrors b.right and a.right mirrors
b.left, walked pairwise with the same kind of stack.

Time O(n) · Space O(h) for the stack, h = tree height (O(n) worst case)
"""
from __future__ import annotations

from problems.p0012_max_depth_binary_tree import TreeNode


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    stack = [root] if root else []
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root


def is_mirror(a: TreeNode | None, b: TreeNode | None) -> bool:
    stack = [(a, b)]
    while stack:
        x, y = stack.pop()
        if x is None and y is None:
            continue
        if x is None or y is None or x.val != y.val:
            return False
        stack.append((x.left, y.right))
        stack.append((x.right, y.left))
    return True
