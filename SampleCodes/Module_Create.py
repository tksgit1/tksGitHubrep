'''
# calc.py

def add(3, 6):
    return (x+y)

def subtract(x, y):
    return (x-y)

'''


# 1. First, import the functions if they are in a separate calc.py file
# from calc import add, subtract

# 2. Or define the functions correctly with variable parameters
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# 3. Call the functions using real numbers down here
result_add = add(3, 6)
result_sub = subtract(10, 4)

# 4. Print the results to see them in your terminal
print("Addition Result:", result_add)
print("Subtraction Result:", result_sub)

