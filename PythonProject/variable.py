# Basic assignment
x = 5
print("x = 5", type(x))
y = 3.14
print("y = 3.14", type(y))
z = "Hi"
print('z = "Hi"', type(z))

# Dynamic typing (same variable holding different types)
x = 10
print('x = 10', type(x))
x = "Now a string"
print('x = "Now a string"', type(x))


# Multiple assignments (same value to multiple variables)
a = b = c = 100
print('a = b = c = 100', a, b, c)  # Output: 100 100 100


# Assigning different values to multiple variables
x, y, z = 1, 2.5, "Python"
print('x, y, z = 1, 2.5, "Python"', x, y, z)  # Output: 1 2.5 Python
print(z)


# Global variable
x = 10

def my_function():
    # Local variable
    y = 5
    print("Local variable y:", y)  # Accessible within the function
    print("Global variable x:", x)  # Accessible inside function

my_function()

# Uncommenting below line will raise an error as y is local to my_function
# print("Trying to access y outside function:", y)  # Error: y is not defined


# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)
print(cnt)
print(s2)


#Taking Input
name = input("Enter your name: ")
print("Hello", name)

#Multiple Inputs
x, y = input("Enter two values: ").split()
print(x, y)  # Output: 5 10

