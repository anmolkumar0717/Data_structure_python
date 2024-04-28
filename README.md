# Data Structures in Python

This repository contains implementations of three common data structures in Python: linked list, doubly linked list, and dynamic array (list in Python).

## Linked List

A linked list is a linear data structure where elements are stored in nodes. Each node contains a data element and a reference (or pointer) to the next node in the sequence.

### Implementation

The `LinkedList` class is implemented in Python. It consists of a `Node` class for creating individual nodes and a `LinkedList` class for managing the list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
Operations
The following operations are supported by the linked list:

Insertion
Deletion
Traversal
Search
Length calculation
and more...
Doubly Linked List
A doubly linked list is a variation of the linked list where each node contains a reference to both the next node and the previous node in the sequence.

Implementation
Similar to the linked list, the DoublyLinkedList class is implemented with a Node class and a DoublyLinkedList class.

python
Copy code
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
Operations
The doubly linked list supports operations similar to the linked list, with the addition of:

Insertion at the end
Deletion from the end
Reversal
and more...
Dynamic Array (List in Python)
Python's built-in list data structure is a dynamic array that automatically grows and shrinks in size as elements are added or removed.

Implementation
The list in Python is simple to use as it's built into the language. Here's a basic example:

python
Copy code
my_list = [1, 2, 3, 4, 5]
Operations
Python lists support various operations such as:

Insertion (append, insert)
Deletion (remove, pop)
Indexing
Slicing
Concatenation
and more...
Examples
Here's an example of how to use these data structures:

python
Copy code
# Linked List example
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Doubly Linked List example
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)

# List (Dynamic Array) example
my_list = [1, 2, 3]
my_list.append(4)
License
This project is licensed under the lord university.
