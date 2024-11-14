# DSA-Python/Linear-Data-Structures/tests/test_static_array.py
import unittest
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Linear_Data_Structures.src.arrays.dynamic_array import DynamicArray
from Linear_Data_Structures.src.arrays.static_array import StaticArray


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


class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.array = DynamicArray()  # Create an empty dynamic array

    def test_append(self):
        self.array.append(10)
        self.array.append(20)
        self.array.append(30)
        self.assertEqual([self.array[i] for i in range(len(self.array))], [10, 20, 30])

    def test_insert(self):
        self.array.append(10)
        self.array.append(20)
        self.array.append(30)
        self.array.insert(1, 15)  # Insert 15 at index 1
        self.assertEqual([self.array[i] for i in range(len(self.array))], [10, 15, 20, 30])

    def test_remove(self):
        self.array.append(10)
        self.array.append(20)
        self.array.append(30)
        self.array.remove(20)  # Remove the first occurrence of 20
        self.assertEqual([self.array[i] for i in range(len(self.array))], [10, 30])

    def test_out_of_bounds_access(self):
        self.array.append(10)
        with self.assertRaises(IndexError):
            _ = self.array[10]  # This should raise an IndexError

    def test_remove_non_existent_element(self):
        self.array.append(10)
        with self.assertRaises(ValueError):
            self.array.remove(100)  # This should raise a ValueError

    def test_automatic_resizing(self):
        for i in range(100):  # Add 100 elements to test resizing
            self.array.append(i)
        self.assertEqual(len(self.array), 100)


if __name__ == "__main__":
    unittest.main()
