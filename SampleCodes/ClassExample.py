class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

d1=Dog("Tod", 2)
print(d1.species)
print(d1.name)
print(d1.age)
print(d1.name, d1.age)

