from abc import ABC, abstractmethod
from project.products.base_product import BaseProduct

class BaseStore(ABC):
    additional_percentage = 0.1

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list[BaseProduct] = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value:str ):
        if value.strip() == '':
            raise ValueError('Store name cannot be empty!')
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value:str):
        if len(value.strip()) != 3:
            raise ValueError('Store location must be 3 chars long!')
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError('Store capacity must be a positive number or 0!')
        self.__capacity = value

    @abstractmethod
    def store_stats(self):
        pass

    @property
    @abstractmethod
    def store_type(self):
        pass


    def get_estimated_profit(self):
        future_profit = sum(p.price for p in self.products) * self.additional_percentage
        return f'Estimated future profit for {len(self.products)} products is {future_profit:.2f}'


