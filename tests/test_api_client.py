from python_ssr.api_client import APIClient
from unittest.mock import patch
import unittest


class TestAPIClient(unittest.TestCase):

    @patch('python_ssr.api_client.requests.request')  # Correct patch path
    def test_fetch_data_success(self, mock_request):
        # Arrange
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {'key': 'value'}
        api_config = {
            'url': 'https://api.example.com/data',
            'method': 'GET',
            'params': {}
        }

        # Act
        data = APIClient.fetch_data(api_config)

        # Assert
        self.assertEqual(data, {'key': 'value'})

    @patch('python_ssr.api_client.requests.request')  # Correct patch path
    def test_fetch_data_failure(self, mock_request):
        # Arrange
        mock_request.return_value.status_code = 404
        api_config = {
            'url': 'https://api.example.com/data',
            'method': 'GET',
            'params': {}
        }

        # Act
        data = APIClient.fetch_data(api_config)

        # Assert
        self.assertEqual(data, {})


if __name__ == '__main__':
    unittest.main()
