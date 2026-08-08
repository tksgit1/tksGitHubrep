#def greet(name: str = "Guest") -> None
print('#def greet(name: str = "Guest") -> None\n')
print('def greet(name="Guest"):')
def greet(name="Guest"):
    print("Hello", name,'\n')
print('')
print('greet() -->', end=" ")
greet()
print('greet("Alice") -->', end=" ")
greet("Alice")
