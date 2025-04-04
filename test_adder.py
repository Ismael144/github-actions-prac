import unittest
from unittest import TestCase
from adder import Adder 

class TestAdder(TestCase):
    def setUp(self): 
        self.adder = Adder()

    def test_add(self): 
        self.assertEqual(self.adder.add(2, 3), 5)


if __name__ == '__main__': 
    unittest.main()
