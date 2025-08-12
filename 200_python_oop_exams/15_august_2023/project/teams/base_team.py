from abc import ABC, abstractmethod
from project.equipment.base_equipment import BaseEquipment

class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: list[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str):
        if value.strip() == '':
            raise ValueError('Team name cannot be empty!')
        self.__name = value

    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, value:str):
        if len(value.strip()) < 2:
            raise ValueError('Team country should be at least 2 symbols long!')        
        self.__country = value
    
    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError('Advantage must be greater than zero!')
        self.__advantage = value
    
    @property
    def type_of_team(self):
        return type(self).__name__

    @property
    def total_points(self):
        return sum(e.protection for e in self.equipment) + self.advantage

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_price_of_team_equipment = 0
        total_protection = 0

        for equipment in self.equipment:
            total_price_of_team_equipment += equipment.price
            total_protection += equipment.protection
        

        result = [
            f'Name: {self.name}',
            f'Country: {self.country}',
            f'Advantage: {self.advantage} points',
            f'Budget: {self.budget:.2f}EUR',
            f'Wins: {self.wins}',
            f'Total Equipment Price: {total_price_of_team_equipment:.2f}',
            f'Average Protection: {total_protection // len(self.equipment) if total_protection != 0 else total_protection}'
        ]

        return '\n'.join(result)