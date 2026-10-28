import random

from problems.p0055_move_zeroes import move_value, move_zeroes


def reference(nums, value=0):
    return [x for x in nums if x != value] + [x for x in nums if x == value]


def test_example():
    nums = [0, 1, 0, 3, 12]
    assert move_zeroes(nums) is None  # in place
    assert nums == [1, 3, 12, 0, 0]


def test_edge_cases():
    for nums, expected in [
        ([], []),
        ([0], [0]),
        ([5], [5]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 1], [1, 0, 0]),
        ([-1, 0, -2, 0], [-1, -2, 0, 0]),
    ]:
        move_zeroes(nums)
        assert nums == expected


def test_keeps_same_list_object():
    nums = [0, 2, 0, 1]
    alias = nums
    move_zeroes(nums)
    assert alias is nums and alias == [2, 1, 0, 0]


def test_move_value_other_values_and_count():
    items = ["a", "", "b", "", "c"]
    assert move_value(items, "") == 3
    assert items == ["a", "b", "c", "", ""]
    items = [None, 1, None, 0]
    assert move_value(items, None) == 2
    assert items == [1, 0, None, None]  # 0 is a real value here, not moved


def test_against_reference():
    rng = random.Random(55)
    for _ in range(1000):
        nums = [rng.choice([0, 0, 1, 2, 3, -4]) for _ in range(rng.randint(0, 12))]
        expected = reference(nums)
        move_zeroes(nums)
        assert nums == expected
