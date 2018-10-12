#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_docstring(self):
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_func_doc(self):
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_emptyargs(self):
        self.assertIsNone(max_integer())

    def test_empty(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]), None)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([2, 4, 5, 6, None])

    def test_one(self):
        self.assertEqual(max_integer([24]), 24)

    def test_integers(self):
        self.assertEqual(max_integer([2, 3, 8, 4]), 8)
        self.assertEqual(max_integer([23, 23, 23, 23]), 23)
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)
        self.assertEqual(max_integer([7, 23, 9, 10]), 23)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([8]), 8)

    def test_integer_neg(self):
        self.assertEqual(max_integer([-34, -79, -12, -2]), -2)
        self.assertEqual(max_integer([9, 45, 98, -6]), 98)

    def test_float(self):
        self.assertEqual(max_integer([1.2, 2.4, 3.8, 6.9]), 6.9)
        self.assertEqual(max_integer([-42.3, -69.99, -1.11, -3.14]), -1.11)

    def test_string(self):
        self.assertEqual(max_integer("12345"), "5")
        self.assertEqual(max_integer("6, 7, 8"), "8")

    def test_alpha(self):
        self.assertEqual(max_integer(["abc"]), "abc")
        self.assertEqual(max_integer(["abc", "def"]), "def")
        self.assertEqual(max_integer(["abc", "2", "8", "xyz"]), "xyz")


if __name__ == "__main__":
    unittest.main()
