"""0001 · Two Sum (easy · hash map)

Given a list of integers and a target, return the indices of the two numbers
that add up to the target. Exactly one solution exists; don't reuse an element.

Idea: walk the list once. For each number, check whether its complement
(target - n) was already seen. A dict gives O(1) lookups.

Time O(n) · Space O(n)
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    for i, n in enumerate(nums):
        j = seen.get(target - n)
        if j is not None:
            return (j, i)
        seen[n] = i
    raise ValueError("no pair adds up to target")
