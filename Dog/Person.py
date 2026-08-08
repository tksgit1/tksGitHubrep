class Person:
    @staticmethod
    def is_adult(age):
        return age >= 18

print(Person.is_adult(16))
print(Person.is_adult(21))
