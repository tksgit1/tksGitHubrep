class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

perform_task(Pen())
perform_task(Eraser())

#additional codes

print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings



print(5 + 10)  # Integer addition
print("Hello " + "World!")  # String concatenation
print([1, 2] + [3, 4])  # List concatenation
