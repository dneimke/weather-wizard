# This file will contain the tests for the Weather Wizard application

import unittest
from unittest.mock import patch, Mock
from weather_wizard.main import get_weather
import requests

class TestWeatherWizard(unittest.TestCase):
    @patch('weather_wizard.main.requests.get')
    def test_get_weather(self, mock_get):
        # Mock the API response for a known city
        mock_response = Mock()
        mock_response.json.return_value = {
            'main': {'temp': 15.0, 'feels_like': 12.0},
            'weather': [{'description': 'clear sky'}]
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        city_name = 'London'
        weather_info = get_weather(city_name)
        self.assertEqual(weather_info['temp'], 15.0)

        # Mock the API response for an unknown city
        mock_get.side_effect = requests.RequestException
        city_name = 'UnknownCity'
        weather_info = get_weather(city_name)
        self.assertIsNone(weather_info)

if __name__ == '__main__':
    unittest.main()
