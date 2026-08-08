from collections import UserDict


# Creating a dictionary where deletion is not allowed
class MyDict(UserDict):

    # Prevents using 'del' on dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

        # Prevents using pop() on dictionary

    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

        # Prevents using popitem() on dictionary

    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Create an instance of MyDict


d = MyDict({'a': 1, 'b': 2, 'c': 3})
d.pop(1)
