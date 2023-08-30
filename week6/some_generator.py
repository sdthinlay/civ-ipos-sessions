import unittest

class Something:
    def do_something(self, value):
        if value != 41:
            raise ValueError
        return 42

class TestSomething(unittest.TestCase):
    def setUp(self) -> None:
        print("Runs before each test case")
        self.something = Something()

    def test_returns_42(self):
        self.assertEquals(self.something.do_something(), 42)


    def test_raises_value_error_when_not_42(self):
        with self.assertRaises(ValueError):
            self.something.do_something(41)
