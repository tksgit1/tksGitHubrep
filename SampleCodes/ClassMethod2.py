
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        n, a = data.split("-")
        return cls(n, int(a))

u = User.from_string("Alex-21")

print(u.name)
print(u.age)

Output

