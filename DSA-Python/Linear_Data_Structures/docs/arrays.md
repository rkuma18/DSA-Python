
Array is a collection of items of the same variable type that are stored at contiguous memory locations. It is one of the most popular and simple data structures used in programming.

## Terminologies of Array

- **Array Index:** In an array, elements are identified by their indexes. Array index starts from 0.
- **Array element:** Elements are items stored in an array and can be accessed by their index.
- **Array Length:** The length of an array is determined by the number of elements it can contain. 

## Declaration of Array

### All types of lists are created same way

```
arr = []
```

## Initialization of Array

### This list will store integer type elements
```
arr = [1, 2, 3, 4, 5]
```

### This list will store character type elements (strings in Python)
```
arr = ['a', 'b', 'c', 'd', 'e']
```

### This list will store float type elements
```
arr = [1.4, 2.0, 24.0, 5.0, 0.0]
```  

_The idea of an array is to represent many instances in one variable._

## Applications of Array Data Structures

- Array is a fundamental data structure and many other data structure are implemented using this. Implementing data structures such as stacks and queues
- Representing data in tables and matrices
- Creating dynamic data structures such as Hash Tables and Graph.
- When compared to other data structures, arrays have the advantages like random access (we can quickly access i-th item) and cache friendliness (all items are stored at contiguous location)

## Types of Arrays

Arrays can be classified in two ways:
1. On the basis of Size
2. On the basis of Dimensions

## Types of Arrays on the basis of Size:

1. Fixed Sized Arrays:

We cannot alter or update the size of this array. Here only a fixed size of memory will be allocated for storage. In case, we don’t know the size of the array then if we declare a larger size and store a lesser number of elements will result in a wastage of memory or we declare a lesser size than the number of elements then we won’t get enough memory to store all the elements. In such cases, static memory allocation is not preferred.

```
# Create a fixed-size list of length 9, 
# initialized with zeros
arr = [0] * 9

# Output the fixed-size list
print(arr)
```

2. Dynamic Sized Arrays:

The size of the array changes as per user requirements during execution of code so the coders do not have to worry about sizes. They can add and removed the elements as per the need. The memory is mostly dynamically allocated and de-allocated in these arrays.

```
# Dynamic Array
arr = []
```

## Types of Arrays on the basis of Dimensions:

1. One-dimensional Array(1-D Array):

We can imagine a 1d array as a row, where elements are stored one after another.

2. Multi-dimensional Array:

A multi-dimensional array is an array with more than one dimension. We can use multidimensional array to store complex data in the form of tables, etc. We can have 2-D arrays, 3-D arrays, 4-D arrays and so on.

**- Two-Dimensional Array(2-D Array or Matrix):**
2-D Multidimensional arrays can be considered as an array of arrays or as a matrix consisting of rows and columns.

**- Three-Dimensional Array(3-D Array):**
A 3-D Multidimensional array contains three dimensions, so it can be considered an array of two-dimensional arrays.

## Operations on Array

1. Array Traversal:

Array traversal involves visiting all the elements of the array once.

2. Insertion in Array:

We can insert one or multiple elements at any position in the array.

3. Deletion in Array:

We can delete an element at any index in an array.

4. Searching in Array:

We can traverse over an array and search for an element.

## Complexity Analysis of Operations on Array

### Time Complexity:

| Operation | Best Case | Average Case | Worst Case |
| --------- | --------- | ------------ | ---------- |
| Traversal |    Ω(N)   |     θ(N)     |     O(N)   |
| Insertion |    Ω(1)   |     θ(N)     |     O(N)   |
| Deletion  |    Ω(1)   |     θ(N)     |     O(N)   |
| Searching |    Ω(1)   |     θ(N)     |     O(N)   |


### Space Complexity:

| Operation | Best Case | Average Case | Worst Case |
| --------- | --------- | ------------ | ---------- |
| Traversal |    Ω(1)   |     θ(1)     |     O(1)   |
| Insertion |    Ω(1)   |     θ(N)     |     O(N)   |
| Deletion  |    Ω(1)   |     θ(N)     |     O(N)   |
| Searching |    Ω(1)   |     θ(1)     |     O(1)   |


## Advantages of Array

- Arrays allow random access to elements. This makes accessing elements by position faster.
- Arrays have better cache locality which makes a pretty big difference in performance.
- Arrays represent multiple data items of the same type using a single name.
- Arrays are used to implement the other data structures like linked lists, stacks, queues, trees, graphs, etc.

## Disadvantages of Array

- As arrays have a fixed size, once the memory is allocated to them, it cannot be increased or decreased, making it impossible to store extra data if required. An array of fixed size is referred to as a static array. 
- Allocating less memory than required to an array leads to loss of data.
- An array is homogeneous in nature so, a single array cannot store values of different data types. 
- Arrays store data in contiguous memory locations, which makes deletion and insertion very difficult to implement. This problem is overcome by implementing linked lists, which allow elements to be accessed sequentially.

## Applications of Array

- They are used in the implementation of other data structures such as array lists, heaps, hash tables, vectors, and matrices.
- Database records are usually implemented as arrays.
- It is used in lookup tables by computer.

## Real-World Applications of Array:

- Signal Processing
- Multimedia Applications
- Data Mining
- Robotics
- Real-time Monitoring and Control Systems
- Financial Analysis
- Scientific Computing

## Python List

List is a built-in data structure that is used to store an ordered collection of items. Lists are mutable, meaning that their contents can be changed after the list has been created. They can hold a various of data types, including integers, floats, strings, and even other lists.

```
a = [1, 'apple', 3.14, [5, 6]]

print(a)
```

**Output**
```
[1, 'apple', 3.14, [5, 6]]
```

## Creating a List
We can create a list in Python using square brackets [] or by using the list() constructor. Here are some common methods to create a list:

### Using Square Brackets
We can directly create a list by enclosing elements in square brackets.

```
# List of integers
a = [1, 2, 3, 4, 5]

# List of strings
b = ['apple', 'banana', 'cherry']

# Mixed data types
c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)
```

**Output**

```
[1, 2, 3, 4, 5]
['apple', 'banana', 'cherry']
[1, 'hello', 3.14, True]
```

### Using the list() Constructor
We can also create a list by passing an iterable (like a string, tuple, or another list) to the list() function.

```
# From a tuple
a = list((1, 2, 3, 'apple', 4.5))  

print(a)
```

**Output**

```
[1, 2, 3, 'apple', 4.5]
```

### Creating a List with Repeated Elements
We can create a list with repeated elements using the multiplication operator.

```
# Create a list [2, 2, 2, 2, 2]
a = [2] * 5

# Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 7

print(a)
print(b)
```

**Output**
```
[2, 2, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0]
```

### Accessing List Elements

Elements in a list can be accessed using indexing. Python indexes start at 0, so a[0] will access the first element, while negative indexing allows us to access elements from the end of the list. Like index -1 represents the last elements of list.

```
a = [10, 20, 30, 40, 50]

# Access first element
print(a[0])    

# Access last element
print(a[-1])
```

**Output**
```
10
50
```

### Adding Elements into List

- **append()**: Adds an element at the end of the list.
- **extend()**: Adds multiple elements to the end of the list.
- **insert()**: Adds an element at a specific position.

```
# Initialize an empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 
```

**Output**
```
After append(10): [10]
After insert(0, 5): [5, 10]
After extend([15, 20, 25]): [5, 10, 15, 20, 25]
```
### Updating Elements into List

```
a = [10, 20, 30, 40, 50]

# Change the second element
a[1] = 25 

print(a)
```
**Output**
```
[10, 25, 30, 40, 50]
```

### Removing Elements from List

- **remove()**: Removes the first occurrence of an element.
- **pop()**: Removes the element at a specific index or the last element if no index is specified.
- **del statement**: Deletes an element at a specified index.

```
a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)  
```

**Output**
```
After remove(30): [10, 20, 40, 50]
Popped element: 20
After pop(1): [10, 40, 50]
After del a[0]: [40, 50]
```

### Iterating Over Lists

We can iterate the Lists easily by using a for loop or other iteration methods. Iterating over lists is useful when we want to do some operation on each item or access specific items based on certain conditions. Let’s take an example to iterate over the list using for loop.

```
a = ['apple', 'banana', 'cherry']

# Iterating over the list
for item in a:
    print(item)

```

**Output**
```
apple
banana
cherry
```

### Nested Lists and Multidimensional Lists

A nested list is a list within another list, which is useful for representing matrices or tables. We can access nested elements by chaining indexes.

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 2, column 3
print(matrix[1][2]) 
```

**Output**
```
6
```