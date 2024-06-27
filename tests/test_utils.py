import unittest

from rsa.utils import extend_gcd, quick_power


class TestUtils(unittest.TestCase):
    def test_quick_power(self):
        """Test the quick_power function."""
        self.assertEqual(quick_power(2, 10, 1000), (2**10) % 1000)
        self.assertEqual(quick_power(3, 5, 13), (3**5) % 13)
        self.assertEqual(quick_power(42, 11, 567), (42**11) % 567)
        self.assertEqual(quick_power(3, 19, 98), (3**19) % 98)

    def test_extend_gcd(self):
        """Test the extend_gcd function."""
        gcd, x, y = extend_gcd(35, 12)
        self.assertEqual(gcd, 1)
        self.assertEqual(35 * x + 12 * y, 1)

        gcd, x, y = extend_gcd(48, 18)
        self.assertEqual(gcd, 6)
        self.assertEqual(48 * x + 18 * y, 6)

        gcd, x, y = extend_gcd(17, 0)
        self.assertEqual(gcd, 17)
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)

        gcd, x, y = extend_gcd(13, 13)
        self.assertEqual(gcd, 13)
        self.assertEqual(13 * x + 13 * y, 13)
