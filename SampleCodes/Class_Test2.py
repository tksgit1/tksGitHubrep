# Class definition: Blueprint for creating objects
class Animal:
    # Constructor (__init__): Initializes the object with attributes
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method: Function inside a class
    def speak(self):
        print(f"{self.name} makes a sound!")


class Cat(Animal):
    # 1. Add the new attribute (color) to the parameters
    def __init__(self, name, color):
        # 2. super() forwards the shared data to the parent class
        super().__init__(name, "Cat")

        # 3. Initialize the unique attribute locally
        self.color = color

    # Example instantiation:


c1 = Cat("Whiskers", "Orange")
print(c1.name)  # Inherited: Whiskers
print(c1.color)  # Unique to Cat: Orange


class Cat(Animal):
    # Constructor remains the same
    def __init__(self, name):
        super().__init__(name, "Cat")

    def speak(self):
        # 1. Call the parent class speak method first
        super().speak()

        # 2. Run the child class specific logic
        print(f"{self.name} meows!")
        return "test"

c1=Cat("m")
print(c1.speak())
print("7")


class Dog(Animal):
    def __init__(self, name, breed):
        # Pass name and hardcoded species to parent
        super().__init__(name, "Dog")
        # Save unique attribute
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks!")


d1=Dog("Tom", "A")
print(d1.speak())
print(super.speak())