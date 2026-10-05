"""0014 - Valid Palindrome (easy · two pointers)

Given a string, decide whether it reads the same forwards and backwards once
you ignore case and every character that is not a letter or digit.
"A man, a plan, a canal: Panama" counts as a palindrome.

Idea: put one pointer at each end. Skip non-alphanumeric characters from
either side, then compare the two characters case-insensitively. Any mismatch
means "no"; when the pointers meet, it is a palindrome. This avoids building a
cleaned copy of the string.

Time O(n) · Space O(1)
"""
from __future__ import annotations


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].casefold() != s[right].casefold():
            return False
        else:
            left += 1
            right -= 1
    return True
