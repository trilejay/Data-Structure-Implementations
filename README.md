# Data Structures Implementations

This repository contains Python implementations of several fundamental data structures. Each data structure is implemented with basic operations and methods. 

## Table of Contents

- [Dynamic Array](#dynamic-array)
- [Binary Search Tree (BST)](#binary-search-tree-bst)
- [AVL Tree](#avl-tree)
- [Linked List](#linked-list)
- [Hash Map](#hash-map)
- [Min Heap](#min-heap)

## Dynamic Array

The `DynamicArray` class provides a dynamic array implementation with methods to resize, append, insert, remove, slice, merge, map, filter, reduce, and find mode. 

### Example Usage

```python
da = DynamicArray()
da.append(10)
print(da)
```

## Binary Search Tree (BST)

The `BST` class provides an implementation of a binary search tree with methods to add, remove, check if tree contains, find min, find max, and return empty.

### Example Usage

```python
bst = BST()
bst.insert(10)
bst.insert(5)
print(bst.in_order_traversal())
```
## AVL Tree

The AVLTree class implements an AVL tree with methods to add, remove, and balance (rotate) to maintain efficient time complexity for insertions and deletions.

### Example Usage

```python
avl_tree = AVLTree()
avl_tree.insert(10)
avl_tree.insert(5)
print(avl_tree.in_order_traversal())
```

## Linked List

The LinkedList class provides an implementation of a singly linked list, queue, and stack with methods for insertion, deletion, and traversal

### Example Usage

```python
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
print(linked_list)
```
## Hash Map

The HashMap class implements a hash map with methods for adding, removing, and retrieving key-value pairs.

### Example Usage

```python
hash_map = HashMap()
hash_map.put("key1", "value1")
print(hash_map.get("key1"))
```

## Min Heap

The MinHeap class provides an implementation of a min heap with operations for insertion, extraction of the minimum element, and heapification.

### Example Usage

```python
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
print(min_heap.extract_min())
```
