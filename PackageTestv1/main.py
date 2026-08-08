'''
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''

# main.py
from shapes import Rectangle, Circle

# Create instances directly
my_rectangle = Rectangle(10, 5)
my_circle = Circle(7)

print(my_rectangle.get_area())  # Outputs: 50
print(my_circle.get_area())     # Outputs: 153.93791
