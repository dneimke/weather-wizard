# This file will contain the tests for the Weather Wizard application

import unittest
from weather_wizard.main import get_weather

class TestWeatherWizard(unittest.TestCase):
    def test_get_weather(self):
        # Test with a known city
        city_name = 'London'
        temperature = get_weather(city_name)
        self.assertIsNotNone(temperature)

        # Test with an unknown city
        city_name = 'UnknownCity'
        temperature = get_weather(city_name)
        self.assertIsNone(temperature)

if __name__ == '__main__':
    unittest.main()
