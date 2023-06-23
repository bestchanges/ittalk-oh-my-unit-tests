# case1_parametrized_test.py
import pytest


def divider(one, two):
    return one / two


def test_divider_case_1():
    result = divider(10, 2)
    assert result == 5


def test_divider_case_2():
    result = divider(1, 1)
    assert result == 1


def test_divider_case_3():
    result = divider(1, 2)
    assert result == 0.5


def test_divider_case_4():
    result = divider(1e+25, 2)
    assert result == 5e+24


def test_divider_case_5():
    with pytest.raises(TypeError):
        divider(None, 2)


def test_divider_case_6():
    with pytest.raises(TypeError):
        divider("string", 2)


@pytest.mark.parametrize(
    'one, two, expected', [
        [10, 2, 5],
        [1, 1, 1],
        [1, 2, 0.5],
        [1e+25, 2, 5e+24],
])
def test_divider_positive(one, two, expected):
    result = divider(one, two)
    assert result == expected


@pytest.mark.parametrize(
    'one, two, expected', [
        [None, 2, TypeError],
        ["string", 2, TypeError],
])
def test_divider_negative(one, two, expected):
    with pytest.raises(expected):
        divider(one, two)
