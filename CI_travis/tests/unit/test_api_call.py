from unittest import TestCase
from unittest.mock import patch
import src.api_call


class TestingYourApi(TestCase):
    def test_api_calls(self):
        with patch('src.api_call.requests.get') as mocked_call:
            src.api_call.call_google()
            mocked_call.assert_called_with('https://www.google.com')

    def test_api_return(self):
        with patch('src.api_call.requests.get') as mocked_resp:
            mocked_resp.return_value = 200
            assert src.api_call.call_google() == 200


class TestingInputCall(TestCase):
    def test_input_output(self):
        with patch('builtins.input', return_value='Ashish') as mocked_input:
            src.api_call.get_input()
            mocked_input.assert_called_with('Enter Name: ')
            assert src.api_call.get_input() == 'Ashish'
