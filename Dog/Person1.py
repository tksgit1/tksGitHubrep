# Creating class
class Person:
    def __init__(self, name):
        self.name = name
    # Method
    def greet(self):
        print(f"Hello {self.name}")

# Creating object
p = Person("shakshi")
# Method calling
p.greet()