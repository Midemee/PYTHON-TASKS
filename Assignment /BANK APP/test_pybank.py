import unittest
import pybank

class TestValidateEmail(unittest.TestCase):

    def test_valid_email_returns_true(self):
        actual = pybank.validate_email("mide@example.com")
        expected = True
        self.assertEqual(actual, expected)
