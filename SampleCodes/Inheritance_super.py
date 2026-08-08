
class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):
        super().show()   # Calling parent method
        print("This is Child class method")

obj = Child()
obj.show()

