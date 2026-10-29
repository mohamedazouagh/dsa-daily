"""0057 - Implement Queue using Stacks (easy · queue design, amortised O(1))

Build a first-in-first-out queue using only stack operations (push to the
top, pop from the top, peek at the top, size). Support push(x), pop(),
peek() and empty(). Example: push 1, push 2, peek -> 1, pop -> 1,
empty -> False.

Idea: keep two stacks. `inbox` takes every push. `outbox` serves pops and
peeks; when it runs empty, pour the whole inbox into it, which reverses the
order so the oldest element ends up on top. Each element is moved from inbox
to outbox at most once, so a sequence of n operations costs O(n) in total
even though a single pop that triggers a pour costs O(size).

Popping or peeking an empty queue raises IndexError, like list.pop() does.

Time push O(1), pop/peek amortised O(1) (worst case O(n)) · Space O(n)
"""
from __future__ import annotations

from typing import Any


class StackQueue:
    def __init__(self) -> None:
        self._inbox: list[Any] = []
        self._outbox: list[Any] = []
        self.moves = 0  # elements poured inbox -> outbox, for checking the amortised bound

    def push(self, x: Any) -> None:
        self._inbox.append(x)

    def _refill(self) -> None:
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())
                self.moves += 1
        if not self._outbox:
            raise IndexError("queue is empty")

    def pop(self) -> Any:
        self._refill()
        return self._outbox.pop()

    def peek(self) -> Any:
        self._refill()
        return self._outbox[-1]

    def empty(self) -> bool:
        return not self._inbox and not self._outbox

    def __len__(self) -> int:
        return len(self._inbox) + len(self._outbox)
