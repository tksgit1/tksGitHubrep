# Global variable
x = 10

def my_function():
    # Local variable
    y = 5
    print("Local variable y:", y)  # Accessible within the function
    print("Global variable x:", x)  # Accessible inside function

my_function()

print('Uncommenting below line will raise an error as y is local to my_function', k=y)
print('print("Trying to access y outside function:", y)  # Error: y is not defined')
