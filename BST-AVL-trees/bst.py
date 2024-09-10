# Name: Matthew Ilejay
# OSU Email: ilejaym@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4 part 1
# Due Date: 7/29/24
# Description: BST implementation.


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    def print_tree(self):
        """
        Prints the tree using the print_subtree function.

        This method is intended to assist in visualizing the structure of the
        tree. You are encouraged to add this method to the tests in the Basic
        Testing section of the starter code or your own tests as needed.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.get_root():
            self._print_subtree(self.get_root())
        else:
            print('(empty tree)')

    def _print_subtree(self, node, prefix: str = '', branch: str = ''):
        """
        Recursively prints the subtree rooted at this node.

        This is intended as a 'helper' method to assist in visualizing the
        structure of the tree.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        def add_junction(string):
            if len(string) < 2 or branch == '':
                return string
            junction = '|' if string[-2] == '|' else '`'
            return string[:-2] + junction + '-'

        if not node:
            print(add_junction(prefix) + branch + "None")
            return

        if len(prefix) > 2 * 16:
            print(add_junction(prefix) + branch + "(tree continues)")
            return

        if node.left or node.right:
            postfix = ' (root)' if branch == '' else ''
            print(add_junction(prefix) + branch + str(node.value) + postfix)
            self._print_subtree(node.right, prefix + '| ', 'R: ')
            self._print_subtree(node.left, prefix + '  ', 'L: ')
        else:
            print(add_junction(prefix) + branch + str(node.value) + ' (leaf)')

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        '''
        Adds a new value to the tree.
        '''
        new_node = BSTNode(value)
        if self.get_root() is None:
            self._root = new_node
        else:
            p = None
            n = self.get_root()
            while n is not None:
                p = n
                if value < p.value:
                    n = n.left
                else:
                    n = n.right
            if value >= p.value:
                p.right = new_node
            elif value < p.value:
                p.left = new_node

    def remove(self, value: object) -> bool:
        '''
        Removes a value from the tree and returns True if the value is removed. Otherwise, returns False.
        '''
        p = None
        n = self.get_root()

        #traverse to the node to be removed
        while n is not None and n.value != value:
            p = n
            if value < p.value:
                n = n.left
            else:
                n = n.right

        if n is None:
            return False

        #case for removing no subtrees
        if n.left is None and n.right is None:
            self._remove_no_subtrees(p, n)
            return True

        #case for removing one subtree
        elif n.left is None and n.right is not None:
            self._remove_one_subtree(p, n)
            return True

        #case for removing one subtree
        elif n.left is not None and n.right is None:

            self._remove_one_subtree(p, n)
            return True

        elif n.left is not None and n.right is not None:
            self._remove_two_subtrees(p, n)
            return True

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        '''
        Helper method for removing a node with no subtrees.
        '''
        p = remove_parent
        n = remove_node
        #case to handle only root node in tree
        if self._root == n:
            self._root = None

        elif p.left == n:
            p.left = None

        elif p.right == n:
            p.right = None

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        '''
        Helper method for removing a node with one subtree.
        '''
        p = remove_parent
        n = remove_node

        if p is None:
            self._root = n.right
            return

        if n.right is not None:
            if p.left == n:
                p.left = n.right
            elif p.right == n:
                p.right = n.right

        elif n.left is not None:
            if p.left == n:
                p.left = n.left
            elif p.right == n:
                p.right = n.left


    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        '''
        Helper method for removing a node with two subtrees.
        '''
        p = remove_parent
        n = remove_node
        #find inorder successor, s
        s = self._inorder_successor(n)
        #n's left child becomes s's left child
        s.left = n.left
        #n's right child becomes s's right cild
        s.right = n.right
        #n's parent becomes s's parent
        if p.right == n:
            p.right = s
        elif p.left == n:
            p.left = s
        elif n == self.get_root():
            self._root = s

    def _inorder_successor(self, remove_node):
        '''
        Helper method for finding the inorder successor to a node.
        '''
        n = remove_node
        sp = n
        n = n.right
        if n.right is None and n.left is None:
            sp.right = None
            return n
        else:
            while n is not None:
                if n.left is None:
                    sp.left = n.right
                    return n
                elif n.left is not None:
                    sp = n
                    n = n.left

    def contains(self, value: object) -> bool:
        '''
        Methods that returns True if the value is in the tree. Otherwise, it returns False. If the tree is empty, the method returns False.
        '''
        n = self.get_root()

        if n is None:
            return False

        while n is not None and n.value != value:
            if value < n.value:
                n = n.left
            elif value > n.value:
                n = n.right

        if n is None:
            return False

        if n.value == value:
            return True

    def inorder_traversal(self) -> Queue:
        '''
        This method will perform an inorder traversal of the tree and return a Queue object that contains the values of the visited nodes, in the order they were visited. If the tree is empty, the method returns an empty Queue.
        '''
        result_queue = Queue()
        self._inOrder(self.get_root(), result_queue)
        return result_queue

    def _inOrder(self, n: BSTNode, queue: Queue):
        '''
        Helper method for the inorder_traversal method.
        '''
        if n is not None:
            self._inOrder(n.left, queue)
            queue.enqueue(n.value)
            self._inOrder(n.right, queue)

    def find_min(self) -> object:
        '''
        This method returns the lowest value in the tree. If the tree is empty, the method should
        return None.
        '''
        if self.get_root() is None:
            return None
        else:
            n = self.get_root()
            min = n.value
            while n is not None:
                if n.value < min:
                    min = n.value
                n = n.left
            return min

    def find_max(self) -> object:
        '''
        This method returns the highest value in the tree. If the tree is empty, the method should
        return None.
        '''
        if self.get_root() is None:
            return None
        n = self.get_root()
        max = n.value
        while n is not None:
            if n.value > max:
                max = n.value
            n = n.right
        return max

    def is_empty(self) -> bool:
        '''
        his method returns True if the tree is empty. Otherwise, it returns False.
        '''
        if self.get_root():
            return False
        else:
            return True

    def make_empty(self) -> None:
        '''
        This method removes all of the nodes from the tree
        '''
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)
        tree.print_tree()

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.print_tree()
        tree.remove(del_value)
        print('RESULT :', tree)
        tree.print_tree()
        print('')

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
