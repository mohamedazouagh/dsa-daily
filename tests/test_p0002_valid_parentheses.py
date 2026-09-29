import pytest

from problems.p0002_valid_parentheses import is_valid


@pytest.mark.parametrize(
    "s,expected",
    [
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("{[()()]}", True),
        ("(]", False),
        ("([)]", False),
        ("(((", False),
        ("())", False),
        ("]", False),
    ],
)
def test_is_valid(s, expected):
    assert is_valid(s) is expected


def test_rejects_other_characters():
    with pytest.raises(ValueError):
        is_valid("(a)")
