class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

    def getSalary(self):
        return self.__salary

emp = Employee("Fedrick", 50000)
print("1")
print(emp.name)
print("2")
print(f"The salary is : {emp.getSalary()}")
print("3")