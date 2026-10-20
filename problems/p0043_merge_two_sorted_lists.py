"""0043 - Merge Two Sorted Lists (easy · linked list splicing with a dummy head)

Given the heads of two singly linked lists that are each sorted in
non-decreasing order, splice their nodes together into one sorted list and
return its head. No new nodes are created; the existing ones are relinked.
Example: 1->2->4 and 1->3->4 -> 1->1->2->3->4->4; empty and 0 -> 0.

Idea: keep a dummy node in front of the result and a `tail` pointer to its
last node. While both lists have nodes, attach the smaller head to `tail`
and advance that list. Taking from the first list on ties keeps the merge
stable (equal values keep their original order, first list first). When one
list runs out, the rest of the other is already sorted, so it is attached in
one step. The dummy removes the special case for "the result is still empty".

Time O(n + m) · Space O(1) extra (iterative, so long lists are fine)
"""
from __future__ import annotations

from problems.p0006_reverse_linked_list import ListNode


def merge_two_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next
