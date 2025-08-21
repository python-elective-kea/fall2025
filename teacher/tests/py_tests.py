
import unittest

# The code to test
def add(a, b):
    return a + b

# The tests
class TestAddFunction(unittest.TestCase):

    def setUp(self):
        ... # This is run before each test

    def tearDown(self):
        ... # This is run after each test

    def test_add_integers(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        result = add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3)

    def test_add_mixed_types(self):
        with self.assertRaises(TypeError):
            add(1, "2")


if __name__ == "__main__":
    unittest.main()