import unittest
from weather_wizard.utils import get_weather_emoji

# No changes made to the content of the file.
class TestUtils(unittest.TestCase):

    # Test pour les températures inférieures à 0
    def test_get_weather_emoji_below_zero(self):
        self.assertEqual(get_weather_emoji(-5), "❄️")

    # Test pour les températures entre 0 et 14
    def test_get_weather_emoji_below_fifteen(self):
        self.assertEqual(get_weather_emoji(10), "🌥️")

    # Test pour les températures entre 15 et 24
    def test_get_weather_emoji_below_twenty_five(self):
        self.assertEqual(get_weather_emoji(20), "☀️")

    # Test pour les températures de 25 et plus
    def test_get_weather_emoji_above_twenty_five(self):
        self.assertEqual(get_weather_emoji(30), "🔥")

if __name__ == '__main__':
    unittest.main()
