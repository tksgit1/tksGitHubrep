from abc import ABC, abstractmethod

# 1. Define the abstract blueprint
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# 2. Create a concrete subclass that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # You MUST implement the abstract methods here
    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

# 3. Instantiate the concrete subclass instead of the blueprint
a1 = Circle(5)
a1.draw()  # Output: Drawing a circle with radius 5


