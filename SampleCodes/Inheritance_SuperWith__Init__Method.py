
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

# Creating an instance of the Dog class
my_dog = Dog("Buddy","Labrador.")
print(f"My dog's name is {my_dog.name} and it's a {my_dog.breed}")

