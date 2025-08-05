from abc import ABC, abstractmethod


class BaseWaiter(ABC):
    _HOURLY_WAGE = 0
    def __init__(self, name: str, hours_worked: int):
        self.name = name
        self.hours_worked = hours_worked

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str):
        if len(value.strip()) < 3 or len(value.strip()) > 50:
            raise ValueError('Waiter name must be between 3 and 50 characters in length!')
        self.__name = value

    @property
    @abstractmethod
    def _worker_type(self):
        pass

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if value < 0:
            raise ValueError('Cannot have negative hours worked!')
        self.__hours_worked = value


    def calculate_earnings(self):
        return self.hours_worked * self._HOURLY_WAGE

    def report_shift(self):
        return f'{self.name} worked a {self._worker_type} shift of {self.hours_worked} hours.'

    def __str__(self):
        return f'Name: {self.name}, Total earnings: ${self.calculate_earnings():.2f}'
