class Car:
    def __init__(self, brand, model):
        # Instance attributes
        self.brand = brand
        self.model = model

    # Custom method
    def start_engine(self):
        return f"The {self.brand} {self.model}'s engine is now running! 🚗💨"

# Creating instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Calling the custom method
print(car1.start_engine())
print(car2.start_engine())