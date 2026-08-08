
class Payment:
    print("1")
    def process(self):
        print("2")
        print("Processing payment")

class OnlinePayment(Payment):
    print("3")
    def process(self):
        print("4")
        super().process()
        print("5")
        print("Generating receipt")

obj = OnlinePayment()
print("6")
obj.process()
print("7")

