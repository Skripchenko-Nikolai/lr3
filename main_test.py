import unittest
from main import calculate
from main import to_fixed


class MainTest(unittest.TestCase):

    def test_calculate_sin(self):
        self.assertEqual(calculate("sin", 0, 0, 'Градусы'), '0')
        self.assertEqual(calculate("sin", 30, 1, 'Градусы'), '0.5')
        self.assertEqual(calculate("sin", 90, 0, 'Градусы'), '1')
        self.assertEqual(calculate("sin", 180, 0, 'Градусы'), '0')
        self.assertEqual(calculate("sin", 270, 0, 'Градусы'), '-1')
        self.assertEqual(calculate("sin", 360, 0, 'Градусы'), '-0')

    def test_calculate_cos(self):
        self.assertEqual(calculate("cos", 0, 0, 'Градусы'), '1')
        self.assertEqual(calculate("cos", 60, 1, 'Градусы'), '0.5')
        self.assertEqual(calculate("cos", 90, 0, 'Градусы'), '0')
        self.assertEqual(calculate("cos", 180, 0, 'Градусы'), '-1')
        self.assertEqual(calculate("cos", 270, 0, 'Градусы'), '-0')
        self.assertEqual(calculate("cos", 360, 0, 'Градусы'), '1')

    def test_calculate_tg(self):
        self.assertEqual(calculate("tg", 0, 0, 'Градусы'), '0')
        self.assertEqual(calculate("tg", 45, 0, 'Градусы'), '1')
        self.assertEqual(calculate("tg", 135, 0, 'Градусы'), '-1')
        self.assertEqual(calculate("tg", 180, 0, 'Градусы'), '-0')
        self.assertEqual(calculate("tg", 360, 0, 'Градусы'), '-0')

    def test_to_fixed(self):
        self.assertEqual(to_fixed(1.2, 0), '1')
        self.assertEqual(to_fixed(1.23, 1), '1.2')
        self.assertEqual(to_fixed(1.234, 2), '1.23')
        self.assertEqual(to_fixed(1.234, 3), '1.234')
