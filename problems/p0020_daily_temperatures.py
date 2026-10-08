"""0020 - Daily Temperatures (medium · monotonic stack)

Given a list of daily temperatures, return for each day how many days you
have to wait until a strictly warmer day. If no warmer day follows, use 0.

Idea: walk left to right and keep a stack of indices whose answer is still
unknown. Their temperatures are non-increasing from bottom to top, so when a
new day is warmer than the top, it is the first warmer day for that index:
pop it and record the distance, repeating while the new day keeps winning.
Each index is pushed and popped at most once, which beats the O(n^2)
"scan ahead from every day" approach.

Time O(n) · Space O(n)
"""
from __future__ import annotations


def daily_temperatures(temps: list[float]) -> list[int]:
    answer = [0] * len(temps)
    waiting: list[int] = []  # indices, temperatures non-increasing
    for i, t in enumerate(temps):
        while waiting and temps[waiting[-1]] < t:
            j = waiting.pop()
            answer[j] = i - j
        waiting.append(i)
    return answer
