import unittest

from rsa.keys_generation import generate_keypair
from rsa.rsa_operations import rsa_pipeline


class TestRSAOprations(unittest.TestCase):
    def test_rsa_pipeline(self):
        for _ in range(8):
            keys = generate_keypair(1024)
            self.assertEqual(rsa_pipeline("Hello, World!", keys)[0], "Hello, World!")
            m = "The Python interpreter has a number of functions"
            self.assertEqual(rsa_pipeline(m, keys)[0], m)
            m = "Hi John."
            self.assertEqual(rsa_pipeline(m, keys)[0], m)
            m = "Good bye, John."
            self.assertEqual(rsa_pipeline(m, keys)[0], m)
            m = "kljasdiwnlkjxzlxkcj8iuwhlaksdjkqwioi1"
            self.assertEqual(rsa_pipeline(m, keys)[0], m)
            m = "香草丝绒拿铁 无奶油/少少甜"
            self.assertEqual(rsa_pipeline(m, keys)[0], m)
