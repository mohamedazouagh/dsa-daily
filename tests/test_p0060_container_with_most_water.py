import random

from problems.p0060_container_with_most_water import best_pair, max_area


def _brute(heights):
    n = len(heights)
    return max((min(heights[i], heights[j]) * (j - i) for i in range(n) for j in range(i + 1, n)), default=0)


def test_example():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert best_pair([1, 8, 6, 2, 5, 4, 8, 3, 7]) == (49, 1, 8)


def test_small_and_empty():
    assert max_area([]) == 0
    assert max_area([5]) == 0
    assert best_pair([5]) == (0, -1, -1)
    assert max_area([1, 1]) == 1
    assert max_area([0, 0, 0]) == 0
    assert best_pair([0, 0]) == (0, 0, 1)


def test_best_is_not_the_tallest_walls():
    # the two 10s are adjacent (area 10); the outer 4s span 5 positions (area 20)
    assert max_area([4, 1, 10, 10, 1, 4]) == 20


def test_equal_heights_and_monotone():
    assert max_area([3] * 6) == 15
    assert max_area(list(range(1, 11))) == 25  # 5 * 5 (indices 4..9)
    assert max_area(list(range(10, 0, -1))) == 25


def test_pair_matches_area_and_brute_force():
    rng = random.Random(60)
    for _ in range(400):
        h = [rng.randint(0, 12) for _ in range(rng.randint(0, 25))]
        area, i, j = best_pair(h)
        assert area == _brute(h)
        if len(h) >= 2:
            assert 0 <= i < j < len(h)
            assert min(h[i], h[j]) * (j - i) == area
