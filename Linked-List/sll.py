# Name: Matthew Ilejay
# OSU Email: ilejaym@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 7/22/24
# Description: Linked lists, stacks, queues, and dequeue practice.


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Insert a new node at the beginning of the linked list.
        """
        new_node = SLNode(value, self._head.next)
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        Insert a new node at the end of the linked list.
        """
        new_node = SLNode(value)
        current = self._head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert a new node at a certain index.
        """
        if index < 0 or index > self.length():
            raise SLLException("Index out of bounds")
        new_node = SLNode(value)
        current = self._head
        for _ in range(index):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove_at_index(self, index: int) -> None:
        '''
        Remove a node at a specified index.
        '''
        if index < 0 or index > self.length() - 1:
            raise SLLException

        if index == 0:
            node = self._head.next
            self._head.next = node.next

        else:
            node = self._head.next
            for x in range(index):
                #create temp to have preceding element point to the next element after removal
                temp = node
                node = node.next
            temp.next = node.next

    def remove(self, value: object) -> bool:
        '''
        Removes the first node that contains the specified value
        '''
        node = self._head.next
        count = 0
        #initialize boolean to False
        remove = False

        while node:
            if node.value == value:
                self.remove_at_index(count)
                #if value is found, make boolean True and return it
                remove = True
                return remove
            else:
                node = node.next
                count += 1
        #else return False
        return remove

    def count(self, value: object) -> int:
        '''
        Counts the number of elements in the list that match the value
        '''
        node = self._head.next
        count = 0
        while node:
            if node.value == value:
                count += 1
                node = node.next
            else:
                node = node.next
        return count

    def find(self, value: object) -> bool:
        '''
        Returns a boolean value based on whether the provided value exists in the list
        '''
        node = self._head.next
        #initialize found boolean to False.
        found = False
        while node:
            if node.value == value:
                #if found, make found boolean True and return it
                found = True
                return found
            else:
                node = node.next
        #else, return False
        return found

    def slice(self, start_index: int, size: int) -> "LinkedList":
        '''
        Returns a new LinkedList that contains the requested number of nodes from the original list, starting with the start index node
        '''
        if start_index < 0 or start_index >=self.length():
            raise SLLException

        if size > self.length() - start_index or size < 0:
            raise SLLException

        #initialization
        new_ll = LinkedList()
        node = self._head.next
        index = 0

        #iterate to the start point of slicing
        for x in range(start_index):
            node = node.next

        #add node at index and iterate through "size" amount times. index is incremented each time
        for value in range(size):
            new_node = SLNode(node.value)
            new_ll.insert_at_index(index, new_node.value)
            index += 1
            node = node.next

        return new_ll

if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
