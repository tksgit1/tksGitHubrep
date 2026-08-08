
class Dog:
    def __init__(self, name, breed="Mixed", age=1):
        self.name = name
        self.breed = breed
        self.age = age

a = Dog("Buddy")
b = Dog("Max", "Golden Retriever", 5)

print(a.name, a.breed, a.age)
print(b.name, b.breed, b.age)

