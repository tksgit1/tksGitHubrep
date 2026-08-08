# Class definition: Blueprint for creating objects
class Animal:
    # Constructor (__init__): Initializes the object with attributes
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method: Function inside a class
    def speak(self):
        print(f"{self.name} makes a sound!")


# Polymorphism: Using the same method name for different behavior
class Cat(Animal):
    print("4")

    def __init__(self, name):
        print("5")
        super().__init__(name, "Cat")  # Calls the constructor of Animal class with 'Cat' as species

    def speak(self):
        print("6")
        print(f"{self.name} meows!")
        return "test"


c1 = Cat("m")
print(c1.speak())
print("7")


