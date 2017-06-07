from unittest import TestCase

from color_temp import rgb_to_temperature, temperature_to_rgb


class TestColor(TestCase):
    def test_rgb_to_temperature(self):
        self.assertAlmostEqual(3860.44070265, rgb_to_temperature([[233.0, 233.0, 33.0]]))
        self.assertAlmostEqual(-241.06062071, rgb_to_temperature([130.0, 50.0, 220.0]))

    def test_temperature_to_rgb(self):
        rgb = temperature_to_rgb(3500)
        self.assertAlmostEqual(1.21596123, rgb[0])
        self.assertAlmostEqual(0.95122878, rgb[1])
        self.assertAlmostEqual(0.66886992, rgb[2])
