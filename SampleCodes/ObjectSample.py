import ClassSample
from ClassSample import DogBest
from ClassSample import Dog
from ClassSample import Cat
from ClassSample import Person
from ClassSample import Car
from ClassSample import Circle
from ClassSample import PersonClass
from ClassSample import Gfg
from ClassSample import MyClass
from ClassSample import Car1
from ClassSample import A
from ClassSample import B
from ClassSample import Example
from ClassSample import Employee
from ClassSample import Base
from ClassSample import Child
from ClassSample import Car2
from ClassSample import Car3
from ClassSample import A1
from ClassSample import Car4
from ClassSample import Student
from ClassSample import Car5
from ClassSample import Student1
from ClassSample import Student2



# Creating an object of the DogBest class
dog1 = DogBest("Buddy", 3)
print(dog1.name)
print(dog1.species)

# Creating objects
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")  # This will now work without error
person = Person("Alice", 30)
car = Car("Tesla", "Model S")

# Using objects and demonstrating OOPs concepts
print(f"{dog.name} is a {dog.species}")
dog.speak()  # Method Overriding (Polymorphism)

cat.speak()  # Polymorphism: Different behavior, same method name

print(f"{person.name} is {person.get_age()} years old.")
person.set_age(35)
print(f"New age of {person.name}: {person.get_age()}")

car.start_engine()  # Abstraction: Details hidden in the method

#Attributes_Acces
# Creating an instance of Circle
ins = Circle(5)

# Calling the area method
print("Area of the circle:", ins.area())

# Creating object
p = PersonClass("shakshi")
# Method calling
p.greet()


# Creating an instance of Gfg
ins = Gfg("Python")

# Calling the topic method
ins.topic()

print(ins)

# Accessing class attribute
print(MyClass.class_attribute)

# Modifying class attribute
MyClass.class_attribute = "New value for class attribut";
print(MyClass.class_attribute)

# Creating instances of the Car class
car1 = Car1("Toyota", "Camry")
car2 = Car1("Honda", "Civic")

# Accessing instance attributes
print(f"{car1.brand} {car1.model}")
print(f"{car2.brand} {car2.model}")

obj = B()
obj._A__hidden()
print(obj._A__hidden())
print(obj._B__hidden())

obj = Example()
print(obj.get_value())


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

obj = Child()
obj._Base__secret()

# Creating an instance using the default constructor
car = Car2()
print(car.make)
print(car.model)
print(car.year)

# Creating an instance using the parameterized constructor
car = Car3("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)

# Creating an instance
obj = A1()

# Calling the bound method
obj.func(10)  # Pass any argument you wish to see printed

A1.func(obj, 50)


# instance of class Car created
Car1 = Car4()

print(f"Car1 gears before calling change_gears() = {Car1.gears}")
Car1.change_gears(6)
print(f"Gears after calling change_gears() = {Car1.gears}")

# bound method
print(Car1.change_gears)

Student.show_course()

Car5.show_brand()

s1 = Student1()
s2 = Student1()

print(s1.school)
print(s2.school)

#instance variable
s1 = Student2("Jake")
s2 = Student2("Emily")

print(s1.name)
print(s2.name)
