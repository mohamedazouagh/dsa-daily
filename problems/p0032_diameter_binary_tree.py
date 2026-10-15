"""0032 - Diameter of Binary Tree (easy · post-order DFS)

Given the root of a binary tree, return the length of its diameter: the
number of edges on the longest path between any two nodes. The path does not
have to pass through the root. An empty tree or a single node has diameter 0.
Example: [1,2,3,4,5] -> 3 (path 4-2-1-3 or 5-2-1-3).

Idea: the longest path "bends" at some node, where it goes down the deepest
branch on the left and the deepest branch on the right. So compute each
node's height (number of nodes on its longest downward path) bottom-up and,
at every node, try left height + right height as a candidate diameter: that
sum is exactly the number of edges of the path bending there.
Post-order is done with an explicit stack so a long, list-like tree cannot
hit Python's recursion limit.

Time O(n) · Space O(h) for the stack plus O(n) for the heights dict
"""
from __future__ import annotations

from problems.p0012_max_depth_binary_tree import TreeNode


def diameter(root: TreeNode | None) -> int:
    if root is None:
        return 0
    height: dict[int, int] = {}  # id(node) -> nodes on the longest downward path
    best = 0
    stack: list[tuple[TreeNode, bool]] = [(root, False)]
    while stack:
        node, children_done = stack.pop()
        if not children_done:
            stack.append((node, True))
            for child in (node.left, node.right):
                if child is not None:
                    stack.append((child, False))
            continue
        left = height.get(id(node.left), 0) if node.left else 0
        right = height.get(id(node.right), 0) if node.right else 0
        best = max(best, left + right)
        height[id(node)] = 1 + max(left, right)
    return best
