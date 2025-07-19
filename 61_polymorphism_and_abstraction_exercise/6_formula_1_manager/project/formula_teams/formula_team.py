from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    MIN_BUDGET = 1_000_000
    EXPENSES_PER_RACE = None
    def __init__(self, budget:int):
        self.budget = budget
        self.sponsors = {}

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.MIN_BUDGET:
            raise ValueError('F1 is an expensive sport, find more sponsors!')
        self.__budget = value



    def calculate_revenue_after_race(self, race_pos:int):
        revenue = 0
        for _, places in self.sponsors.items():
            for place, money in sorted(places.items()):
                if place >= race_pos:
                    revenue += money
                    break

        revenue -= self.EXPENSES_PER_RACE
        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'