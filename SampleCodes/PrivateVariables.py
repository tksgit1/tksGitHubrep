class A:
    def __hidden(self):
        print("Inside class A")

class B(A):
    def __hidden(self):
        print("Inside class B")

obj = B()
obj._A__hidden()
print(obj._A__hidden())
print(obj._B__hidden())