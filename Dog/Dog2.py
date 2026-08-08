class Dog2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    name = "Sausage"
    age = 1
    my_dog = Dog2(name, age)
    print(f'my dog is called {my_dog.name} and is {my_dog.age} years old')

if __name__ == '__main__':
    main()
