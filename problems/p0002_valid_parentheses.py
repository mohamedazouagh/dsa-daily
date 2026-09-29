"""0002 — Valid Parentheses (easy · stack)

Given a string made of the brackets ()[]{}, decide whether every opening
bracket is closed by the same type of bracket, in the right order.

Idea: push opening brackets on a stack. On a closing bracket the top of the
stack must be its matching opener, otherwise the string is invalid. At the
end the stack must be empty (nothing left unclosed).

Time O(n) · Space O(n)
"""

PAIRS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    stack: list[str] = []
    for ch in s:
        if ch in PAIRS:
            if not stack or stack.pop() != PAIRS[ch]:
                return False
        elif ch in "([{":
            stack.append(ch)
        else:
            raise ValueError(f"unexpected character {ch!r}")
    return not stack
