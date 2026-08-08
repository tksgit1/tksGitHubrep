# Python code to demonstrate
# use of bound methods

class A:
    def func(self, arg):
        self.arg = arg
        print("Value of arg =", arg)

# Creating an instance
obj = A()

# Calling the bound method
obj.func(10)  # Pass any argument you wish to see printed

A.func(obj, 50)

