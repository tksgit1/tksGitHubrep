class Car1:
    def __init__(self, brand, model):
        self.brand = brand  # Set instance attribute
        self.model = model  # Set instance attribute

    def display(self):
        return self.brand, self.model

# Create an instance of Car
my_car = Car1("Toyota", "Corolla")

# Call the display method
print(my_car.display())
