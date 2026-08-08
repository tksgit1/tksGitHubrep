class Employee:
    print("10")
    def __init__(self, name, salary):
        print("11")
        self.name = name
        self.salary = salary
        self.role = "Employee"
        print("1")
    def display(self):
        print(f"Name: {self.name} | Role: {self.role} | Salary: ${self.salary}")
        print("2")
print("12")
class Manager(Employee):
    def __init__(self, name, salary, department):
        print("3")
        # Pass name and salary to the Employee parent constructor
        super().__init__(name, salary)
        print("4")

        # Set attributes unique to the Manager class
        self.role = "Manager"
        print("5")
        self.department = department
        print("6")

    # Method Overriding: Extending the parent display method
    def display(self):
        print("7")
        # Call the parent display() to print Name, Role, and Salary
        super().display()
        print("8")
        # Add the unique Manager information
        print(f"Department: {self.department}")
        print("9")


# Create instances
e1 = Employee("Alice Smith", 60000)
e2 = Manager("Bob Jones", 95000, "Engineering")

print("--- Employee Info ---")
e1.display()

print("\n--- Manager Info ---")
e2.display()

