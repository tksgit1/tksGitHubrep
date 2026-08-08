
'''
# Class definition: Blueprint for creating objects
class Animal:
    # Constructor (__init__): Initializes the object with attributes
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method: Function inside a class
    def speak(self):
        print(f"{self.name} makes a sound!")


# Inheritance: Dog class inherits from Animal class
class Dog(Animal):
    species = "Canine"  # Class attribute

    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Calls the constructor of

        # Animal class
        self.breed = breed  # Instance attribute

    # Method Overriding: Overriding speak method of the Animal class
    def speak(self):
        print(f"{self.name}, a {self.breed}, barks!")


class DogBest:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


# Encapsulation: Hiding the internal state (age) of the class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private variable, cannot be accessed directly

    # Getter method to access private attribute __age
    def get_age(self):
        return self.__age

    # Setter method to modify private attribute __age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

class PersonClass:
    def __init__(self, name):
        self.name = name
    # Method
    def greet(self):
        print(f"Hello {self.name}")


# Polymorphism: Using the same method name for different behavior
class Cat(Animal):
    print("4")
    def __init__(self, name):
        print("5")
        super().__init__(name, "Cat")  # Calls the constructor of Animal class with 'Cat' as species

    def speak(self):
        print("6")
        print(f"{self.name} meows!")

c1=Cat("m")
print(c1.speak())
print("7")

# Abstraction: Hiding complex details in a method
class Car:
    print("2")
    def __init__(self, make, model):
        print("3")
        self.make = make
        self.model = model

    def start_engine(self):
        print("1")
        # In a real-world scenario, this method could be more complex
        print("Engine started... Vroom!")
        print(f"C is: {self.make}")

car1=Car("Cmk", "CMl")
print("8")

car1.start_engine()
print("9")

class Circle:
    print("10")

    def __init__(self, r):
        print("11")
        self.r = r

    def area(self):
        print("12")
        a = 3.14 * self.r ** 2
        return a

class Gfg:
    def __init__(self, topic):
        self._topic = topic  # Store parameter value in instance variable

    def topic(self):
        print("Topic:", self._topic)  # Access the renamed variable

class MyClass:
    class_attribute = "I am a class attribute";

class Car1:
    def __init__(self, brand, model):
        # Instance attributes
        self.brand = brand
        self.model = model

class A:
    def __hidden(self):
        print("Inside class A")

class B(A):
    def __hidden(self):
        print("Inside class B")

class Example:
    def __init__(self):
        self._value = "Internal data"

    def get_value(self):
        return self._value

class Employee:
    def __init__(self):
        self.__salary = 0

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary

class Base:
    def __secret(self):
        print("Base method")

class Child(Base):
    def __secret(self):
        print("Child method")

class Car2:
    def __init__(self):

        #Initialize the Car1 with default attributes
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

class Car3:
    def __init__(self, make, model, year):
        # Initialize the Car with specific attributes.
        self.make = make
        self.model = model
        self.year = year

# Python code to demonstrate
# use of bound methods

class A1:
    def func(self, arg):
        self.arg = arg
        print("Value of arg =", arg)

# use of bound methods

class Car4:
    # Car class created
    gears = 5

    # a class method to change the number of gears
    @classmethod
    def change_gears(cls, gears):
        cls.gears = gears

class Student:
    course = "Python"

    @classmethod
    def show_course(cls):
        print(cls.course)

class Car5:
    brand = "Toyota"

    @classmethod
    def show_brand(cls):
        print(cls.brand)

class Student1:
    school = "ABC School"   # Class variable

class Student2:
    def __init__(self, name):
        self.name = name   # Instance variable
'''


# Class definition: Blueprint for creating objects
class Animal:
    # Constructor (__init__): Initializes the object with attributes
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method: Function inside a class
    def speak(self):
        print(f"{self.name} makes a sound!")


# Inheritance: Dog class inherits from Animal class
class Dog(Animal):
    species = "Canine"  # Class attribute

    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Calls the constructor of

        # Animal class
        self.breed = breed  # Instance attribute

    # Method Overriding: Overriding speak method of the Animal class
    def speak(self):
        print(f"{self.name}, a {self.breed}, barks!")


class DogBest:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


# Encapsulation: Hiding the internal state (age) of the class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private variable, cannot be accessed directly

    # Getter method to access private attribute __age
    def get_age(self):
        return self.__age

    # Setter method to modify private attribute __age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

class PersonClass:
    def __init__(self, name):
        self.name = name
    # Method
    def greet(self):
        print(f"Hello {self.name}")

# Polymorphism: Using the same method name for different behavior
class Cat(Animal):
    print("4")
    def __init__(self, name):
        print("5")
        super().__init__(name, "Cat")  # Calls the constructor of Animal class with 'Cat' as species

    def speak(self):
        print("6")
        print(f"{self.name} meows!")

c1=Cat("m")
print(c1.speak())
print("7")
c2=cat(self,”K”,9)
print(c2.speak())




# Abstraction: Hiding complex details in a method
class Car:
    print("2")
    def __init__(self, make, model):
        print("3")
        self.make = make
        self.model = model

    def start_engine(self):
        print("1")
        # In a real-world scenario, this method could be more complex
        print("Engine started... Vroom!")
        print(f"C is: {self.make}")

car1=Car("Cmk", "CMl")
print("8")

car1.start_engine()
print("9")

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        a = 3.14 * self.r ** 2
        return a

