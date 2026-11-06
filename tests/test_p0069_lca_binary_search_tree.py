import random

import pytest

from problems.p0069_lca_binary_search_tree import bst_insert, lowest_common_ancestor


def _build(values):
    root = None
    for v in values:
        root = bst_insert(root, v)
    return root


def _path(root, val):
    """Root-to-node list of nodes, found with plain BST search."""
    out, node = [], root
    while node:
        out.append(node)
        if val == node.val:
            return out
        node = node.left if val < node.val else node.right
    raise AssertionError(f"{val} not in tree")


def _lca_by_paths(root, p, q):
    last = None
    for a, b in zip(_path(root, p), _path(root, q)):
        if a is not b:
            break
        last = a
    return last


EXAMPLE = [6, 2, 8, 0, 4, 7, 9, 3, 5]


def test_examples():
    root = _build(EXAMPLE)
    assert lowest_common_ancestor(root, 2, 8).val == 6
    assert lowest_common_ancestor(root, 2, 4).val == 2  # a node is its own descendant
    assert lowest_common_ancestor(root, 3, 5).val == 4
    assert lowest_common_ancestor(root, 5, 3).val == 4  # order of p, q doesn't matter


def test_same_value_and_single_node():
    root = _build(EXAMPLE)
    assert lowest_common_ancestor(root, 7, 7).val == 7
    single = _build([1])
    assert lowest_common_ancestor(single, 1, 1) is single


def test_degenerate_deep_tree_no_recursion_limit():
    root = _build(range(5000))  # every node only has a right child
    assert lowest_common_ancestor(root, 4000, 4999).val == 4000


def test_missing_values_raise():
    with pytest.raises(ValueError):
        lowest_common_ancestor(None, 1, 2)
    with pytest.raises(ValueError):
        lowest_common_ancestor(_build([5, 3]), 1, 2)  # walk falls off the tree


def test_random_against_path_comparison():
    rng = random.Random(69)
    for _ in range(300):
        values = rng.sample(range(-50, 50), rng.randint(1, 25))
        root = _build(values)
        p, q = rng.choice(values), rng.choice(values)
        assert lowest_common_ancestor(root, p, q) is _lca_by_paths(root, p, q)
