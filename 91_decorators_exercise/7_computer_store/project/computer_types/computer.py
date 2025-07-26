from abc import ABC, abstractmethod, abstractproperty
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    def _is_empty(self, string):
        return True if string.strip() == '' else False


    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if self._is_empty(value):
            raise ValueError('Manufacturer name cannot be empty.')
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if self._is_empty(value):
            raise ValueError('Model name cannot be empty.')
        self.__model = value


    @abstractproperty
    def processors(self):
        pass

    @abstractproperty
    def available_ram(self):
        pass

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price = int(self.processors[processor] + (100 * log2(ram)))

    def __repr__(self):
        return f'{self.__manufacturer} {self.__model} with {self.processor} and {self.ram}GB RAM'
