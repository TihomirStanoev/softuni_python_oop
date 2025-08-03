from abc import ABC, abstractmethod
from project.battleships.base_battleship import BaseBattleship

class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: list[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value:str):
        if not value.isdigit():
            raise ValueError('Zone code must contain digits only!')
        self.__code = value

    @abstractmethod
    def zone_info(self):
        pass

    def get_ships(self):
        return sorted(self.ships, key=lambda s: (-s.hit_strength, s.name))

    @property
    def ship_names(self):
        return f'#{", ".join(s.name for s in self.get_ships())}#'