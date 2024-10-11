import requests


class APIClient:
    """
    A class for fetching data from APIs.

    Methods:
        fetch_data(api_config): Fetch data from an API using the provided configuration.
    """

    @staticmethod
    def fetch_data(api_config):
        """
        Fetch data from an API using the provided configuration.

        Args:
            api_config (dict): A dictionary containing API configuration.
                Expected keys:
                    - url (str): The API endpoint URL.
                    - method (str): The HTTP method to use (e.g., GET, POST).
                    - params (dict): A dictionary of query parameters for the request.

        Returns:
            dict: The JSON response from the API, or an empty dictionary if the request fails.
        """
        api_url = api_config.get('url', '')
        api_method = api_config.get('method', 'GET')
        api_params = api_config.get('params', {})

        # Make the HTTP request to the API
        response = requests.request(api_method, api_url, params=api_params)

        # Check for successful response
        if response.status_code == 200:
            return response.json()
        else:
            return {}
