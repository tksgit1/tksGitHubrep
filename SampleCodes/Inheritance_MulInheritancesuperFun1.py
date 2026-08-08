
class A:
    def __init__(self):
        print("Initializing A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Initializing B")

class C(A):
    def __init__(self):
        super().__init__()
        print("Initializing C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("Initializing D")

d = D()
print("\n")
d1 = A()
print("\n")
d1 = B()
print("\n")
d1 = C()

print("\n")
print(D.__mro__)

print("\n")
print(A.__mro__)

print("\n")
print(B.__mro__)

print("\n")
print(C.__mro__)