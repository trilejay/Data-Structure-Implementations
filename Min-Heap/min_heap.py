# Name: Matthew Ilejay
# OSU Email: ilejaym@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 5
# Due Date: 8/05/24
# Description: Implementation of heap data structure.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        '''
        Adds a new object to the min heap while maintaining min heap properties.
        '''
        #append new node to end of array
        self._heap.append(node)
        #get index of newly added node
        index = self._heap.length() - 1
        value = self._heap.get_at_index(index)

        #percolate up
        while index > 0:
            #initialize parent index
            parent_index = (index - 1) // 2
            parent_value = self._heap.get_at_index(parent_index)
            if parent_value > value:
                #set parent value to index position, move index up to parent index
                self._heap.set_at_index(index, parent_value)
                index = parent_index
            else:
                break

        #set index value to parent
        self._heap.set_at_index(index, value)

    def is_empty(self) -> bool:
        '''
        Returns True if the heap is empty. Returns false otherwise.
        '''
        return self._heap.is_empty()

    def get_min(self) -> object:
        '''
        Returns an object with the minimum key, without removing it from the heap. Raises a MinHeapException if the heap is empty.
        '''
        if self.is_empty():
            raise MinHeapException
        else:
            return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        '''
        Returns an object with the minimum key and removes it from the heap. If the heap is empty, raises a MinHeapException.
        '''
        if self.is_empty():
            raise MinHeapException
        else:
            #save value of first element in array, to be returned later
            value = self._heap.get_at_index(0)

            #replace value of first element in array with last element, and remove last element
            self._heap.set_at_index(0, self._heap.get_at_index(self._heap.length() - 1))
            self._heap.pop()
            if self._heap.length() > 0:
                _percolate_down(self._heap, 0)
        return value

    def build_heap(self, da: DynamicArray) -> None:
        '''
        Receives a DynamicArray with objects in any order, and builds a proper MinHeap from them. The current content of the MinHeap is overwritten.
        '''
        #clear the heap
        self._heap = DynamicArray()

        #copy elements from da to heap
        for i in range(da.length()):
            self._heap.append(da.get_at_index(i))

        #convert to heap using percolate down method
        last_parent = (self._heap.length() - 2) // 2
        while last_parent >= 0:
            _percolate_down(self._heap, last_parent)
            last_parent -= 1

    def size(self) -> int:
        '''
        Returns the size of the heap.
        '''
        return self._heap.length()

    def clear(self) -> None:
        '''
        Clears the contents of the heap.
        '''
        self._heap = DynamicArray()

def _percolate_down_max (da: DynamicArray, parent: int, length: int) -> None:
    '''
    Helper method for the heapsort method.
    '''
    while True:
        left_child_index = parent * 2 + 1
        right_child_index = parent * 2 + 2

        # if left child index out of bounds, break loop
        if left_child_index >= length:
            break

        # determine smallest child
        if right_child_index < length and da.get_at_index(right_child_index) < da.get_at_index(left_child_index):
            smallest_child_index = right_child_index
        else:
            smallest_child_index = left_child_index

        # if parent is smaller than smallest child, break loop
        if da.get_at_index(parent) <= da.get_at_index(smallest_child_index):
            break

        # swap parent and smallest child
        temp = da.get_at_index(parent)
        da.set_at_index(parent, da.get_at_index(smallest_child_index))
        da.set_at_index(smallest_child_index, temp)

        # move down to child index
        parent = smallest_child_index

def heapsort(da: DynamicArray) -> None:
    '''
    Receives a DynamicArray and sorts its content in non-ascending order, using the Heapsort algorithm.
    '''
    length = da.length()

    #build a min heap
    last_parent = (length - 2) // 2
    while last_parent >= 0:
        _percolate_down(da, last_parent)
        last_parent -= 1

    #sort array
    k = length - 1
    while k > 0:
        #swap root with last element
        temp = da.get_at_index(0)
        da.set_at_index(0, da.get_at_index(k))
        da.set_at_index(k, temp)

        #reduces size of heap
        length -= 1  # Update length to reflect the new heap size

        _percolate_down_max(da, 0, length)

        k -= 1


# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #


def _percolate_down(da: DynamicArray, parent: int) -> None:
    '''
    Helper function that percolates a node down the heap, maintaining heap properties.
    '''
    length = da.length()
    while True:
        left_child_index = parent * 2 + 1
        right_child_index = parent * 2 + 2

        #if left child index out of bounds, break loop
        if left_child_index >= length:
            break

        #determine smallest child
        if right_child_index < length and da.get_at_index(right_child_index) < da.get_at_index(left_child_index):
            smallest_child_index = right_child_index
        else:
            smallest_child_index = left_child_index

        #if parent is smaller than smallest child, break loop
        if da.get_at_index(parent) <= da.get_at_index(smallest_child_index):
            break

        #swap parent and smallest child
        temp = da.get_at_index(parent)
        da.set_at_index(parent, da.get_at_index(smallest_child_index))
        da.set_at_index(smallest_child_index, temp)

        #move down to child index
        parent = smallest_child_index

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())
    #
    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
