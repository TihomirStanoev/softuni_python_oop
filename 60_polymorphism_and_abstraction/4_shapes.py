from abc import ABC, abstractmethod
from math import pi

class Shapes(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shapes):
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return pi * self._radius * self._radius

    def calculate_perimeter(self):
        return 2 * pi * self._radius


class Rectangle(Shapes):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        return 2 * (self._width + self._length)





rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())