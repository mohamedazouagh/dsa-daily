import random

import pytest

from problems.p0039_min_stack import MinStack


def test_example():
    s = MinStack()
    for v in (-2, 0, -3):
        s.push(v)
    assert s.get_min() == -3
    assert s.pop() == -3
    assert s.top() == 0
    assert s.get_min() == -2


def test_duplicate_minimums_survive_one_pop():
    s = MinStack()
    for v in (2, 1, 1):
        s.push(v)
    s.pop()
    assert s.get_min() == 1
    s.pop()
    assert s.get_min() == 2


@pytest.mark.parametrize("method", ["pop", "top", "get_min"])
def test_empty_stack_raises(method):
    with pytest.raises(IndexError):
        getattr(MinStack(), method)()


def test_matches_list_with_min_on_random_operations():
    rng = random.Random(39)
    for _ in range(200):
        s, ref = MinStack(), []
        for _ in range(rng.randint(1, 40)):
            if ref and rng.random() < 0.4:
                assert s.pop() == ref.pop()
            else:
                v = rng.randint(-20, 20)
                s.push(v)
                ref.append(v)
            assert len(s) == len(ref)
            if ref:
                assert s.top() == ref[-1]
                assert s.get_min() == min(ref)
