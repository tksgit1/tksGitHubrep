class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model:", self.model)
        print("Color:", self.color)

audi = Car("Audi A4", "Blue")
ferrari = Car("Ferrari 488", "Green")

audi.show()
ferrari.show()