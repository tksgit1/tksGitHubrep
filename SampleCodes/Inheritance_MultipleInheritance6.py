
class A:
    def __init__(self, a):
        self.a = a

class B:
    def __init__(self, b):
        self.b = b

class C(A, B):
    def __init__(self, a, b, c):
        super().__init__(a)
        B.__init__(self, b)
        self.c = c

# Creating an instance of the C class
my_instance = C("A_attr", "B_attr", "C_attr")
print(f"A: {my_instance.a}, B: {my_instance.b}, C: {my_instance.c}")

