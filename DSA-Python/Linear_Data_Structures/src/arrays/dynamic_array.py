import ctypes  # Provides low-level arrays

class DynamicArray:
    def __init__(self):
        self._n = 0               # Count of actual elements
        self._capacity = 1        # Default capacity
        self._array = self._make_array(self._capacity)  # Low-level array

    def __len__(self):
        """Return the number of elements in the array."""
        return self._n

    def __getitem__(self, index):
        """Return element at index."""
        if not 0 <= index < self._n:
            raise IndexError('Index out of bounds')
        return self._array[index]

    def append(self, element):
        """Add element to end of the array."""
        if self._n == self._capacity:  # If the array is full, resize it
            self._resize(2 * self._capacity)  # Double capacity
        self._array[self._n] = element
        self._n += 1

    def _resize(self, new_capacity):
        """Resize internal array to new_capacity."""
        new_array = self._make_array(new_capacity)  # Create a new array
        for i in range(self._n):  # Copy existing elements to the new array
            new_array[i] = self._array[i]
        self._array = new_array  # Use the new array
        self._capacity = new_capacity

    def _make_array(self, capacity):
        """Return a new array with the given capacity."""
        return (capacity * ctypes.py_object)()

    def insert(self, index, element):
        """Insert element at index, shifting subsequent elements."""
        if not 0 <= index <= self._n:
            raise IndexError('Index out of bounds')
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._n, index, -1):  # Shift elements to the right
            self._array[i] = self._array[i - 1]
        self._array[index] = element
        self._n += 1

    def remove(self, element):
        """Remove first occurrence of element. Shift elements to fill the gap."""
        for i in range(self._n):
            if self._array[i] == element:
                for j in range(i, self._n - 1):  # Shift elements to the left
                    self._array[j] = self._array[j + 1]
                self._array[self._n - 1] = None  # Help garbage collection
                self._n -= 1
                return
        raise ValueError('Element not found')


