class CSStudent:
    stream = 'cse'          # Class variable

    def __init__(self, name, roll):
        self.name = name    # Instance variable
        self.roll = roll    # Instance variable

# Creating objects
a = CSStudent('Rose', 1)

b = CSStudent('Nat', 2)
b.stream = CSStudent.stream
CSStudent.stream = 'mech'
print(a.stream)
print(b.stream)
