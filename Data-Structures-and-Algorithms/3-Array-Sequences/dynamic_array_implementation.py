import ctypes


class DynamicArray:
    """
    DYNAMIC ARRAY CLASS
    """

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n

    def __setitem__(self, ind, ele):
        self.A[ind] = ele

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            return IndexError("Index is out of bounds!")

        return self.A[k]

    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self.A[self.n] = ele
        self.n += 1

    def insert(self, ind, ele):
        """
        Inserts an element into the selected index
        """
        if ind >= self.n or ind < 0:
            self.append(ele)
        else:
            if self.n == self.capacity:
                self._resize(2 * self.capacity)

            for i in range(self.n - 1, ind - 1, -1):
                self.A[i + 1] = self.A[i]

            self.A[ind] = ele
            self.n += 1

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """

        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()

    def __str__(self):
        """
        Print the array
        """
        t = "["
        for ind in range(self.n):
            t += str(self.A[ind]) + ", "
        t = t[0:-2] + "]"
        return t


if __name__ == "__main__":

    arr = DynamicArray()

    arr.append(10)
    arr.append(20)
    arr.insert(1, 30)
    arr.insert(200, 40)
    arr.append(50)
    print(arr)

    arr[1] = 20
    arr[2] = 30
    print(arr)
