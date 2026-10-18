"""0039 - Min Stack (easy · stack design with a running minimum)

Design a stack that supports push, pop, top and get_min, each in O(1)
time. get_min returns the smallest value currently on the stack.
Example: push(-2), push(0), push(-3) -> get_min() = -3; pop() -> get_min() = -2.

Idea: store each element together with the minimum of the stack *at the
moment it was pushed*: (value, min(value, previous min)). The minimum of the
whole stack is then always the second field of the top pair, and popping
automatically restores the previous minimum because it is stored in the
pair underneath. No scanning, no extra bookkeeping on pop.

Time O(1) per operation · Space O(n) (one extra number per element)
"""
from __future__ import annotations


class MinStack:
    def __init__(self) -> None:
        self._items: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        current_min = min(val, self._items[-1][1]) if self._items else val
        self._items.append((val, current_min))

    def pop(self) -> int:
        if not self._items:
            raise IndexError("pop from empty MinStack")
        return self._items.pop()[0]

    def top(self) -> int:
        if not self._items:
            raise IndexError("top of empty MinStack")
        return self._items[-1][0]

    def get_min(self) -> int:
        if not self._items:
            raise IndexError("get_min of empty MinStack")
        return self._items[-1][1]

    def __len__(self) -> int:
        return len(self._items)
