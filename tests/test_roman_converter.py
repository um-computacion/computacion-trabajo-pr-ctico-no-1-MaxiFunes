import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")
        self.assertEqual(decimal_to_roman(99), "XCIX")
        self.assertEqual(decimal_to_roman(499), "CDXCIX")
        self.assertEqual(decimal_to_roman(999), "CMXCIX")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")
    
    def test_large_numbers(self):
        self.assertEqual(decimal_to_roman(1000), "M")
        self.assertEqual(decimal_to_roman(5000), "V̅")
        self.assertEqual(decimal_to_roman(10000), "X̅")
        self.assertEqual(decimal_to_roman(50000), "L̅")
        self.assertEqual(decimal_to_roman(100000), "C̅")
        self.assertEqual(decimal_to_roman(500000), "D̅")
        self.assertEqual(decimal_to_roman(1000000), "M̅")
        self.assertEqual(decimal_to_roman(2000000), "M̅M̅")
        self.assertEqual(decimal_to_roman(3000000), "M̅M̅M̅")
        self.assertEqual(decimal_to_roman(3999999), "M̅M̅M̅C̅M̅X̅C̅I̅X̅CMXCIX")

    def test_invalid_numbers(self):
        with self.assertRaises(ValueError):
            decimal_to_roman(0)
        with self.assertRaises(ValueError):
            decimal_to_roman(4000000)
        with self.assertRaises(TypeError):
            decimal_to_roman("string")
        with self.assertRaises(TypeError):
            decimal_to_roman(3.14)
        with self.assertRaises(ValueError):
            decimal_to_roman(-1)
if __name__ == '__main__':
    unittest.main()