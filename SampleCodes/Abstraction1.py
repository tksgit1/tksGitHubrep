from abc import ABC, abstractmethod
print("1")

class Shape(ABC):
    print("2")
    @abstractmethod
    def draw(self):
        print("3")
        pass

    