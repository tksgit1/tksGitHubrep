
class Vehicle:
    print("1")
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    print("2")
    def start(self):
        print("3")
        print("Car started")

class SportsCar(Car):
    print("4")
    def start(self):
        print("5")
        print("Sports Car started")

obj = SportsCar()
print("6")
obj.start()
print("7")
car1=Car()
print("8")
car1.start()
v1=Vehicle()
print("8")
v1.start()