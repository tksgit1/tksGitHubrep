class Dog:
    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name

d = Dog("Tim")
print(d.get_name())

d2 = Dog("Bill")
print(d2.get_name())
