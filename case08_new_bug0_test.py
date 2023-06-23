# case08_new_bug0_test.py
import pytest


def divider(one, two):
    return one / two


@pytest.mark.parametrize(
    'one, two, expected', [
        [1, 1, 1],
        [1, 2, 0.5],
        [12, 3, 4],
    ])
def test_divider(one, two, expected):
    result = divider(one, two)
    assert result == expected
