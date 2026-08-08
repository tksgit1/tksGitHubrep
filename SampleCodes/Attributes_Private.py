class Student:
    name = "Lokesh Singh"
    __id = 1234

    # Method for Printing Private Attribute
    def Print_Id(self):
        print(f"The Id of student is : {self.__id}")


lokesh = Student()
print(f"The name of student is : {lokesh.name}")  # Public Attribute can be accessed directly from outside class

lokesh.Print_Id()

