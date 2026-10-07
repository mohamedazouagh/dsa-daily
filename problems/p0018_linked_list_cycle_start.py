"""0018 - Linked List Cycle II (medium · fast/slow pointers)

Given the head of a singly linked list, return the node where a cycle begins,
or None if the list ends normally. The list must not be modified and no extra
memory proportional to its length may be used.

Idea: Floyd's tortoise and hare. A slow pointer moves 1 step, a fast pointer 2.
With no cycle the fast one falls off the end. With a cycle they must meet
inside it. Say the cycle starts after `a` nodes and they meet `b` steps into
the cycle (cycle length L): slow walked a + b, fast walked 2(a + b), and the
difference a + b is a multiple of L. So walking `a` more steps from the
meeting point lands exactly on the cycle start. Reset one pointer to the head,
move both 1 step at a time, and they meet at the entry.

Nodes are compared with `is`, never `==`: the dataclass `==` would compare
whole chains and recurse forever on a cyclic list.

Time O(n) · Space O(1)
"""
from __future__ import annotations

from problems.p0006_reverse_linked_list import ListNode


def detect_cycle(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None


def build_with_cycle(values: list[int], pos: int) -> tuple[ListNode | None, list[ListNode]]:
    """Build a list; the tail links back to node ``pos`` (-1 means no cycle).

    Returns the head and the nodes in order, so tests can check identity.
    """
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    return (nodes[0] if nodes else None), nodes
