
class A:
    def __init__(self):
        print("A init called")

class B(A):
    def __init__(self):
        super().__init__()   # Call parent __init__
        print("B init called")

obj = B()

