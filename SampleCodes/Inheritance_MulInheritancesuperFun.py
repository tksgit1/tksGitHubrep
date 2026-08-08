
class Parent1:
    def __init__(self):
        print("Parent1 initialized")

class Parent2:
    def __init__(self):
        print("Parent2 initialized")

class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        print("Child initialized")

child = Child()

