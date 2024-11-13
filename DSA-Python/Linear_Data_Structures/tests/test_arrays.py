# DSA-Python/Linear-Data-Structures/tests/test_static_array.py
import unittest
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Linear-Data-Structures.src.arrays.static_array 
import StaticArray

class TestStaticArray(unittest.TestCase):
    def setUp(self):
        self.array = StaticArray(5)  # Create a static array of size 5

    def test_set_and_get(self):
        self.array.set(0, 10)
        self.assertEqual(self.array.get(0), 10)
        
        self.array.set(4, 20)
        self.assertEqual(self.array.get(4), 20)

    def test_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.array.set(5, 30)  # Out of bounds
            
        with self.assertRaises(IndexError):
            self.array.get(5)  # Out of bounds

if __name__ == "__main__":
    unittest.main()