import unittest
from rsa.utils import quick_power


class TestUtils(unittest.TestCase):

    def test_quick_power(self):
        """Test the quick_power function."""
        self.assertEqual(quick_power(2, 10, 1000), (2 ** 10) % 1000)
        self.assertEqual(quick_power(3, 5, 13), (3 ** 5) % 13)
        self.assertEqual(quick_power(42, 11, 567), (42 ** 11) % 567)
        self.assertEqual(quick_power(3, 19, 98), (3 ** 19) % 98)
