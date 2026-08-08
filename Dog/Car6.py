class Car:
    def __init__(this, model, color):
        this.model = model
        this.color = color

    def show(this):
        print("Model:", this.model)
        print("Color:", this.color)

audi = Car("Audi A4", "Blue")
audi.show()
