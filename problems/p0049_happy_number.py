"""0049 - Happy Number (easy · cycle detection on an implicit sequence)

Start from a positive integer and repeatedly replace it with the sum of the
squares of its digits. The number is "happy" if this process reaches 1;
otherwise it loops forever without reaching 1.
Example: 19 -> 82 -> 68 -> 100 -> 1, so 19 is happy. 2 -> 4 -> 16 -> 37 ->
58 -> 89 -> 145 -> 42 -> 20 -> 4 -> ... loops, so 2 is not.

Idea: each number has exactly one successor, so the sequence is a path that
either ends in the fixed point 1 or runs into a cycle. That is the same
shape as a linked list with a loop, so Floyd's tortoise and hare works
without remembering visited numbers: move `slow` one step and `fast` two
steps until they meet; the number is happy exactly when they meet at 1.

The sequence never grows without bound: a d-digit number maps to at most
81 * d, which is smaller than the number itself once d >= 4, so it soon
drops below 1000 and stays there.

Also included: the explicit trail up to 1 or up to the first repeated
number, handy for showing why a number is (not) happy.

Time O(log n) per step, a bounded number of steps · Space O(1) for Floyd
"""
from __future__ import annotations


def digit_square_sum(n: int) -> int:
    total = 0
    while n:
        n, d = divmod(n, 10)
        total += d * d
    return total


def is_happy(n: int) -> bool:
    if n < 1:
        raise ValueError(f"expected a positive integer, got {n}")
    slow = fast = n
    while True:
        slow = digit_square_sum(slow)
        fast = digit_square_sum(digit_square_sum(fast))
        if slow == fast:
            return slow == 1


def happy_trail(n: int) -> list[int]:
    """Numbers visited from n until reaching 1 or repeating a number (repeat included)."""
    if n < 1:
        raise ValueError(f"expected a positive integer, got {n}")
    trail, seen = [n], {n}
    while n != 1:
        n = digit_square_sum(n)
        trail.append(n)
        if n in seen:
            break
        seen.add(n)
    return trail
