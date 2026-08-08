

class Teacher:
    print("1")
    def introduce(self):
        print("2")
        print("I am a Teacher")

class Writer:
    print("3")
    def write(self):
        print("4")
        print("Writing an article")

class Author(Teacher, Writer):
    print("5")
    def introduce(self):
        print("6")
        print("I am an Author")

obj = Author()
print("7")
obj.introduce()
print("8")
obj.write()
print("9")


