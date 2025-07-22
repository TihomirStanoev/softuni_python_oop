from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def area(self):
        return 0.5 * self.width * self.height


class AreaCalculator:

    def __init__(self, shapes):

#        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise ValueError('`shapes` should be of type `list`.')
        self.__shapes = value


    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)