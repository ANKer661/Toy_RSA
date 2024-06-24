import unittest
from rsa.primes import miller_rabin_test, generate_prime


class TestPrimes(unittest.TestCase):

    def test_miller_rabin_test(self):
        """Test the miller_rabin_test function."""
        # Known primes
        self.assertTrue(miller_rabin_test(2))
        self.assertTrue(miller_rabin_test(3))
        self.assertTrue(miller_rabin_test(65537))
        self.assertTrue(miller_rabin_test(123123123131))
        self.assertTrue(miller_rabin_test(77777777777777797))

        # Known composites
        self.assertFalse(miller_rabin_test(88888))
        self.assertFalse(miller_rabin_test(341))
        self.assertFalse(miller_rabin_test(41041))
        self.assertFalse(miller_rabin_test(75361))
        self.assertFalse(miller_rabin_test(101101))

    def test_generate_prime(self):
        """Test the generate_prime function."""
        prime_16_bits = generate_prime(16)
        self.assertTrue(miller_rabin_test(prime_16_bits))

        prime_32_bits = generate_prime(32)
        self.assertTrue(miller_rabin_test(prime_32_bits))

        prime_64_bits = generate_prime(64)
        self.assertTrue(miller_rabin_test(prime_64_bits))

        # Check if the generated prime is within the specified bit length
        self.assertTrue(prime_16_bits < 2**16)
        self.assertTrue(prime_32_bits < 2**32)
        self.assertTrue(prime_64_bits < 2**64)
