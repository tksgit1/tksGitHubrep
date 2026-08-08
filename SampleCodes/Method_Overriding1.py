#defined in the parent class.

class Animal:
    def display(self):
        print("This is an animal")

class Dog(Animal):
    def display(self):
        print("This is a dog")

obj = Dog()
obj.display()

