# case05_should_fail1_test.py
from unittest.mock import Mock


def generate_password():
    return 'secure_password123'


def test_generate_password():
    result = generate_password()

    assert len(result) >= 12
    assert any(c in result for c in '0123456789')


def test_not_actually_a_test():
    afunction = Mock(return_value=256)

    result = afunction()

    assert result == 256
