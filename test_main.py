from unittest import TestCase
from main import(
    add,
    subtract,
    divide,
    multiply,
)


class Test(TestCase):

    def test_add_base(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_str(self):
        with self.assertRaises(TypeError):
            add('a', 5)

    def test_subtract_base(self):
        self.assertEqual(subtract(0, 5), -5)

    def test_subtract_str(self):
        with self.assertRaises(TypeError):
            subtract('a', 3)

    def test_multiply_base(self):
        self.assertEqual(multiply(0, 5), 0)

    def test_multiply_str(self):
        self.assertEqual(multiply('a', 3), 'aaa')

    def test_divide_base(self):
        self.assertEqual(divide(3, 2), 1.5)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_divide_str(self):
        with self.assertRaises(TypeError):
            divide('a', 3)
