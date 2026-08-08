
# Python code to demonstrate
# use of bound methods

class Car:
    # Car class created
    gears = 5

    # a class method to change the number of gears
    @classmethod
    def change_gears(cls, gears):
        cls.gears = gears

# instance of class Car created
Car1 = Car()

print(f"Car1 gears before calling change_gears() = {Car1.gears}")
Car1.change_gears(6)
print(f"Gears after calling change_gears() = {Car1.gears}")

# bound method
print(Car1.change_gears)

