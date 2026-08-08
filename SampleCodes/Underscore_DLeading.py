class Base:
    def __secret(self):
        print("Base method")

class Child(Base):
    def __secret(self):
        print("Child method")

obj = Child()
obj._Base__secret()

