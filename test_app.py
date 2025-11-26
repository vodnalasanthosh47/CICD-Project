import unittest
import app

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(app.add(10, 5), 15)
        self.assertEqual(app.add(-1, 1), 0)
        self.assertEqual(app.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(app.subtract(10, 5), 5)
        self.assertEqual(app.subtract(-1, 1), -2)
        self.assertEqual(app.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(app.multiply(10, 5), 50)
        self.assertEqual(app.multiply(-1, 1), -1)
        self.assertEqual(app.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(app.divide(10, 5), 2)
        self.assertEqual(app.divide(-1, 1), -1)
        self.assertAlmostEqual(app.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            app.divide(10, 0)

if __name__ == '__main__':
    unittest.main()