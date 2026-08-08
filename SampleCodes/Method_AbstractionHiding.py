class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        # In a real-world scenario, this method could be more complex
        print("Engine started... Vroom!")

Car.start_engine(Car)