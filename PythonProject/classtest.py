# Class definition: Blueprint for creating objects
class Animal:
    # Constructor (__init__): Initializes the object with attributes
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method: Function inside a class
    def speak(self):
        print(f"{self.name} makes a sound!")


# Inheritance: Dog class inherits from Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Calls the constructor of Animal class
        self.breed = breed

    # Method Overriding: Overriding speak method of the Animal