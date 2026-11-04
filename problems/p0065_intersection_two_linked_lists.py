"""0065 - Intersection of Two Linked Lists (easy · two pointers that switch heads)

Two singly linked lists may merge at some node and share every node after it
(a Y shape). Return that first shared node, or None if they never meet. The
lists must not be modified, and "shared" means the same node object, not just
an equal value.

Idea: walk pointer a along list A and pointer b along list B. When a pointer
falls off the end it jumps to the head of the *other* list. Both pointers then
travel exactly len(A) + len(B) steps before running out, so if a shared tail
exists they line up at its first node; if not, they both reach None at the
same moment and the loop ends.

`intersection_by_lengths` is the classic alternative: measure both lists,
skip the difference on the longer one, then step together.

Time O(m + n) · Space O(1)
"""
from __future__ import annotations

from problems.p0006_reverse_linked_list import ListNode


def get_intersection_node(head_a: ListNode | None, head_b: ListNode | None) -> ListNode | None:
    a, b = head_a, head_b
    while a is not b:
        a = a.next if a is not None else head_b
        b = b.next if b is not None else head_a
    return a


def _length(node: ListNode | None) -> int:
    n = 0
    while node is not None:
        n, node = n + 1, node.next
    return n


def intersection_by_lengths(head_a: ListNode | None, head_b: ListNode | None) -> ListNode | None:
    la, lb = _length(head_a), _length(head_b)
    a, b = head_a, head_b
    for _ in range(la - lb):
        a = a.next
    for _ in range(lb - la):
        b = b.next
    while a is not b:
        a, b = a.next, b.next
    return a
