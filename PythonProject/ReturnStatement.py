# function with no parameters and no return statement
def fun():
    print("fun() called!\n")


# function with parameters but no return statement
def printSum(a, b):
    print("sum = ", a + b, '\n')


# function with no parameters with return statement
def greet():
    print('def greet(): --> return "Hello!" ')
    return "Hello!"
    print('\n')

# function with parameters and return statement
def getSum(a, b):
    print('def getSum(a, b): --> return a + b --> ', a + b)
    return a + b
    print('\n')

fun()
printSum(3, 5)
print('\n')
print(greet())
print('\n')
print(getSum(3, 5))
