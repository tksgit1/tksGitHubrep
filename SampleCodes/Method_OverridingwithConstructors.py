
class Employee:
    def __init__(self):
        self.role = "Employee"

    def display(self):
        print("Role:", self.role)

class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.role = "Manager"

    def display(self):
        print("Role:", self.role)

e1 = Employee()
e2 = Manager()
e1.display()
e2.display()

