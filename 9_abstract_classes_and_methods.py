# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
from abc import ABC, abstractmethod
# creating abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
       pass
class Rectangle(Shape):
    def __init__(self, width, lenght):
        self.width = width
        self.lenght =lenght

    def area(self):
        print(self.width * self.lenght)

rect = Rectangle(3,5)
rect.area()


