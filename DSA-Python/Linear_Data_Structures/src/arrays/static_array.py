# DSA-Python/Linear-Data-Structures/src/arrays/static_array.py

class StaticArray:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def set(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def __str__(self):
        return str(self.array)
