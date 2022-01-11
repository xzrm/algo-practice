import pytest

from balance_brackets import balanced_brackets


@pytest.mark.parametrize(
    "expected_correct",
    [
        "",
        "a",
        "ab",
        "()",
        "[]",
        "([])",
        "[aaabbbccca]",
        "[asvb(asddd)aaaa]",
        "((([[[]]])))",
    ],
)
def test_brackets_are_balanced(expected_correct):
    assert balanced_brackets(expected_correct)


@pytest.mark.parametrize(
    "expected_incorrect",
    [
        "())",
        "[]]",
        "(([]])",
        "[(aaabbbccca]",
        "[as(vb(asddd)aaaa]",
        "((([[[[]]])))",
        "[(1+1)(1+2)]",
    ],
)
def test_brackets_are_not_balanced(expected_incorrect):
    assert not balanced_brackets(expected_incorrect)
