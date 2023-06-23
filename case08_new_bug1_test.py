# case08_new_bug1_test.py
import pytest


def divider(one, two):
    if two == 0:
        return None
    return one / two


@pytest.mark.parametrize(
    'one, two, expected', [
        [1, 1, 1],
        [1, 2, 0.5],
        [12, 3, 4],
        [12, 0, None],
    ])
def test_divider(one, two, expected):
    result = divider(one, two)
    assert result == expected
