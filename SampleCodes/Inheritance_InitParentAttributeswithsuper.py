
class Emp:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class fun(Emp):
    def __init__(self, id, name, email):
        super().__init__(id, name)   #Calls Emp’s __init__
        self.email = email

obj = fun(101, "Olivia", "olivia@email.com")
print(obj.id, obj.name, obj.email)

