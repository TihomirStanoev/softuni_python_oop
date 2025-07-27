def validate_index(method):
    def wrapper(self, i, *args):
        try:
            self.integers[i]
        except IndexError:
            raise IndexError('Index out of range')
        return method(self, i, *args)
    return wrapper

def validate_integer(method):
    def wrapper(self, *args):
        if not all(map(lambda i: isinstance(i, int), args)):
            raise ValueError('Element is not a integer!')
        return method(self, *args)
    return wrapper

class IntegerList:
    def __init__(self, *integers):
        self.integers = integers

    @property
    def integers(self):
        return self.__integers

    @integers.setter
    def integers(self, value):
        if not all(map(lambda i: isinstance(i, int), value)):
            raise ValueError('Store only integers!')
        self.__integers = list(value)

    @validate_integer
    def add(self, element):
        self.__integers.append(element)
        return self.__integers

    @validate_index
    def remove_index(self, index):
        element = self.__integers.pop(index)
        return element

    @validate_index
    def get(self, index):
        element = self.__integers[index]
        return element

    @validate_integer
    @validate_index
    def insert(self, index, element):
        self.__integers.insert(index, element)
        return self.__integers

    @property
    def get_biggest(self):
        return max(self.__integers)

    def get_index(self, element):
        return self.__integers.index(element)

