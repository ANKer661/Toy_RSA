import unittest
from rsa.keys_generation import generate_keypair, find_multiplicative_inverse


class TestKeysGeneration(unittest.TestCase):

    def test_find_multiplicative_inverse(self):
        self.assertEqual(find_multiplicative_inverse(5, 14), 3)
        self.assertEqual(find_multiplicative_inverse(79, 3337), 2281)
        self.assertEqual(find_multiplicative_inverse(7, 101), 29)
        self.assertEqual(find_multiplicative_inverse(5, 18), 11)
        self.assertEqual(find_multiplicative_inverse(67, 119), 16)
        self.assertEqual(
            (67*find_multiplicative_inverse(67, 65537) % 65537), 1
        )
        self.assertEqual(
            (65537*find_multiplicative_inverse(65537, 123123123131) % 123123123131), 1
        )
