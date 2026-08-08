class Student:
    school = "ABC School"   # Class variable

    def __init__(self, name):
        self.name = name   # Instance variable


print(Student.school)

s3 = Student("Jake")
s4 = Student("Emily")

print(s3.name)
print(s4.name)