
class A:
    def fun(self):
        print("In class A")

class B(A):
    def fun(self):
        print("In class B")

a = B()
a.fun()

