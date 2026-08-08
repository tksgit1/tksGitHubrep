class Employee:
    def __init__(self):
        self.__salary = 0

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary


# Method for Printing Private Attribute
def Print__salary ():
    print("1")
    print(f"The salary is : {emp1.getSalary()}")
    print("2")

emp1=Employee()
print("3")

emp1.setSalary(2000)
print("6")

#print(emp1.salary)
print("4")
print(f"Salary = : {Print__salary ()}")
print("5")

print(emp1.getSalary())

