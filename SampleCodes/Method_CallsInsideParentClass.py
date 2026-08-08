
class Report:
    print("1")
    def generate(self):
        print("2")
        print("Generating report...")
        print("3")
        self.display()

    def display(self):
        print("4")
        print("Displaying basic report")

class SalesReport(Report):
    print("5")
    def display(self):
        print("6")
        print("Displaying sales report")

obj = SalesReport()
print("7")
obj.generate()
print("8")

