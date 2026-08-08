
class Student:
    course = "Python"

    @classmethod
    def show_course(cls):
        print(cls.course)

Student.show_course()


