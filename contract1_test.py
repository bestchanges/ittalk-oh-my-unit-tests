# contract1_test.py
import random
import secrets
import string
from unittest.mock import patch


def generate_password():
    """
    Secure password generator.
    Generates password length > 12, including letters and numbers

    :return:
    """
    chars = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(chars) for _ in range(20))
    return password


def test_generate_password_canonical():
    with patch.object(random, 'choice', return_value='a') as choice_mock:

        result = generate_password()

        assert result == 'a' * 20
        assert choice_mock.call_count == 20


def test_generate_password_contract():
    result = generate_password()

    assert len(result) > 12
    assert any(c in result for c in string.ascii_letters)
    assert any(c in result for c in string.digits)
