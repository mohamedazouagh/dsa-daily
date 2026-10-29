import random
from collections import deque

import pytest

from problems.p0057_queue_using_stacks import StackQueue


def test_example():
    q = StackQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    assert q.pop() == 2
    assert q.empty() is True


def test_interleaved_pushes_keep_fifo_order():
    q = StackQueue()
    q.push("a")
    q.push("b")
    assert q.pop() == "a"  # pours b into the outbox
    q.push("c")  # lands in the inbox behind b
    assert [q.pop(), q.pop()] == ["b", "c"]
    assert len(q) == 0


def test_empty_queue_raises():
    q = StackQueue()
    with pytest.raises(IndexError):
        q.pop()
    with pytest.raises(IndexError):
        q.peek()
    q.push(None)  # None is a real value, not "empty"
    assert q.peek() is None and len(q) == 1


def test_against_deque_and_amortised_moves():
    rng = random.Random(57)
    q, ref, pushes = StackQueue(), deque(), 0
    for _ in range(5000):
        if ref and rng.random() < 0.45:
            assert q.pop() == ref.popleft()
        elif ref and rng.random() < 0.2:
            assert q.peek() == ref[0]
        else:
            x = rng.randint(-100, 100)
            q.push(x)
            ref.append(x)
            pushes += 1
        assert len(q) == len(ref) and q.empty() == (not ref)
    assert q.moves <= pushes  # every element is poured at most once
