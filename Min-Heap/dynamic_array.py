# Name: Matthew Ilejay
# OSU Email: ilejaym@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2 Part 1
# Due Date: 7/15/24
# Description: Assignment 2 practicing data structures.

from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------
    def pop(self):
        self.set_at_index(self.length() - 1, None)
        self._size -= 1
    def resize(self, new_capacity: int) -> None:
        '''
        This method changes the underlying storage capacity for the elements in the dynamic array.
        It does not change the values or the order of any elements currently stored in the array.
        '''
        if new_capacity < self.length():
            return
        if new_capacity <= 0:
            return
        new_arr = StaticArray(new_capacity)
        for index in range(self.length()):
            #copy elements from old array into new array
            new_arr.set(index, self.get_at_index(index))
        self._data = new_arr
        self._capacity = new_capacity

    def append(self, value: object) -> None:
        '''
        Adds a new value at the end of the dynamic array. If the internal storage
        associated with the dynamic array is already full, doubles its capacity
        before adding a new value.
        '''
        if self.length() == self.get_capacity():
            self.resize(self.get_capacity() * 2)
        #insert value at last index
        self._data.set(self.length(), value)
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        '''
        Adds a new value at the specified index in the dynamic array. Index 0 refers to
        the beginning of the array. If the provided index is invalid, raises a
        “DynamicArrayException”.
        '''
        if index < 0 or index > self.length():
            raise DynamicArrayException

        if self.length() >= self._capacity:
            self.resize(self.get_capacity() * 2)

        if index >= 0:
            for i in range(self.length() - 1, index - 1, -1):
                self._data.set(i + 1, self._data.get(i))
            self._data.set(index, value)
            self._size += 1

    def remove_at_index(self, index: int) -> None:
        '''
        Removes the element at the specified index in the dynamic array. Index 0
        refers to the beginning of the array. If the provided index is invalid, this method must
        raise a custom “DynamicArrayException”.
        '''
        if index < 0 or index >= self._size:
            raise DynamicArrayException

        if self._size < self._capacity * (1/4):
            new_capacity = self._size * 2
            if new_capacity < 10:
                new_capacity = 10
            if self._capacity> 10:
                self.resize(new_capacity)

        #if index is valid, shift all elements to the left
        if index >= 0 and index <= self._size:
            for i in range(index, self._size - 1):
                self._data.set(i, self._data.get(i + 1))
            #decrement size by 1 for each iteration
            self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        '''
        Returns a new DynamicArray object that contains the requested number of
        elements from the original array, starting with the element located at the requested start
        index.
        '''
        if start_index < 0 or start_index >= self._size:
            raise DynamicArrayException

        if size < 0:
            raise DynamicArrayException

        if start_index + size > self._size:
            raise DynamicArrayException

        new_arr = DynamicArray()

        #resize new_arr if size is greater than new_arr._capacity
        while size > new_arr._capacity:
            new_arr.resize(new_arr._capacity * 2)

        new_arr._size = size

        for i in range(size):
            new_arr.set_at_index(i, self.get_at_index(start_index + i))

        return new_arr

    def merge(self, second_da: "DynamicArray") -> None:
        '''
        Takes another DynamicArray object as a parameter, and appends all elements
        from this array onto the current one, in the same order in which they are stored in the input
        array.
        '''
        if self._capacity < second_da.length() + self.length():
            self.resize(self._capacity * 2)

        second_da_index = 0
        for index in range(self._size, self._size + second_da._size):
            self.append(second_da.get_at_index(second_da_index))
            second_da_index += 1
            #self._size += 1
            #self.set_at_index(index, second_da.get_at_index(second_da_index))
            #second_da_index += 1

    def map(self, map_func) -> "DynamicArray":
        '''
        Creates a new dynamic array where the value of each element is derived by
        applying a given map_func to the corresponding value from the original array.
        '''
        new_arr = DynamicArray()

        while new_arr.get_capacity() < self.get_capacity():
            new_arr.resize(new_arr.get_capacity() * 2)

        for index in range(self.length()):
            result = map_func(self.get_at_index(index))
            #increment size before adding result to new dynamic array
            new_arr._size += 1
            new_arr.set_at_index(index, result)
        return new_arr

    def filter(self, filter_func) -> "DynamicArray":
        '''
        Creates a new dynamic array populated only with those elements from the
        original array for which filter_func returns True.
        '''
        new_arr = DynamicArray()

        while new_arr.get_capacity() < self.get_capacity():
            new_arr.resize(new_arr.get_capacity() * 2)

        #initialize variable to keep track of new array index. start at 0
        new_index = 0

        #iterate through initial array
        for index in range(self.length()):
            #if filter function returns true, increment new array size and place at new index. increment new index by +1
            if filter_func(self.get_at_index(index)):
                new_arr._size += 1
                new_arr.set_at_index(new_index, self.get_at_index(index))
                new_index += 1

        #depending on new array size, resize capacity if too large
        while new_arr._size <= new_arr._capacity / 2 and new_arr.get_capacity() > 4:
            new_arr.resize(new_arr._capacity // 2)

        return new_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        '''
        Sequentially applies the reduce_func to all elements of the dynamic array and
        returns the resulting value. It takes an optional initializer parameter. If this parameter is not
        provided, the first value in the array is used as the initializer. If the dynamic array is empty,
        the method returns the value of the initializer (or None, if one was not provided).
        '''
        if self.length() == 0:
            if initializer is None:
                return None
            else:
                return initializer

        if initializer is None:
            accumulator = self.get_at_index(0)
            start_index = 1
        else:
            accumulator = initializer
            start_index = 0

        for index in range(start_index, self.length()):
            accumulator = reduce_func(accumulator, self.get_at_index(index))

        return accumulator


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    '''
    Receives a dynamic array already in sorted order, either non-descending or non-ascending. The function returns a
    tuple containing (in this order) a dynamic array comprising the mode (most-occurring)
    value/s of the array, and an integer that represents the highest frequency
    '''
    if arr.length() == 0:
        return DynamicArray(), 0

    max_frequency = 1
    current_frequency = 1
    modes = DynamicArray()

    #start iterating from second element
    for i in range(1, arr.length()):
        #if previous element is the same, increment current frequency
        if arr.get_at_index(i) == arr.get_at_index(i - 1):
            current_frequency += 1
        else:
            #if new higher frequency is found, reset array and update max frequency
            if current_frequency > max_frequency:
                max_frequency = current_frequency
                modes = DynamicArray()  # Reset modes to an empty array
                modes.append(arr.get_at_index(i - 1))
            elif current_frequency == max_frequency:
                modes.append(arr.get_at_index(i - 1))
            current_frequency = 1

    #check frequency of last element
    if current_frequency > max_frequency:
        max_frequency = current_frequency
        modes = DynamicArray()  # Reset modes to an empty array
        modes.append(arr.get_at_index(arr.length() - 1))
    elif current_frequency == max_frequency:
        modes.append(arr.get_at_index(arr.length() - 1))

    return modes, max_frequency


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
