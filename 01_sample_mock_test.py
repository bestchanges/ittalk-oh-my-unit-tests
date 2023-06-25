# case00_sample_request_mock_test.py
from unittest.mock import patch, call

import requests


def get_ip():
    return requests.get('https://ifconfig.io/ip').text


@patch.object(requests, 'get')
def test_get_ip(get_mock):
    get_mock.return_value.text = '1.1.1.1'

    result = get_ip()

    assert result == '1.1.1.1'
    assert get_mock.called
    assert get_mock.call_args == call('https://ifconfig.io/ip')
