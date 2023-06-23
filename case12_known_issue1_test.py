# case12_known_issue_test.py
import pytest


def function():
    return


@pytest.mark.xfail(reason="known parser issue")
def test_function_xfail():
    function()


@pytest.mark.skip(reason="known parser issue")
def test_function_mute():
    function()
