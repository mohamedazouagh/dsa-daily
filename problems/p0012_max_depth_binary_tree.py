"""0012 - Maximum Depth of Binary Tree (easy · binary tree)

Given the root of a binary tree, return its depth: the number of nodes on the
longest path from the root down to a leaf. An empty tree has depth 0.

Idea: walk the tree level by level with an explicit queue (BFS) and count the
levels. Doing it iteratively instead of with the classic recursive
`1 + max(depth(left), depth(right))` means a very deep, list-like tree cannot
hit Python's recursion limit.

Time O(n) · Space O(w), where w is the widest level (at most n)
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    depth = 0
    level = deque([root])
    while level:
        depth += 1
        for _ in range(len(level)):
            node = level.popleft()
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
    return depth


def from_level_order(values: list[int | None]) -> TreeNode | None:
    """Build a tree from LeetCode-style level order, where None marks a missing child."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = TreeNode(values[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root
