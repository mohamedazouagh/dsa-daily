"""0006 — Reverse Linked List (easy · linked list)

Given the head of a singly linked list, reverse the list in place and return
the new head. An empty list stays empty.

Idea: walk the list once with two pointers, `prev` (the already reversed part)
and `node` (the rest). For each node, remember its successor, point it back at
`prev`, then advance both pointers. When `node` runs off the end, `prev` is
the new head. No recursion, so long lists can't hit the recursion limit.

Time O(n) · Space O(1)
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListNode:
    val: int
    next: ListNode | None = None


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev: ListNode | None = None
    node = head
    while node is not None:
        nxt = node.next
        node.next = prev
        prev, node = node, nxt
    return prev


def from_list(values: list[int]) -> ListNode | None:
    head: ListNode | None = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: ListNode | None) -> list[int]:
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out
