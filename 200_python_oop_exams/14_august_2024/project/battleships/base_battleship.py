from abc import ABC, abstractmethod


class BaseBattleship(ABC):
    def __init__(self,name: str,health: int, hit_strength: int, ammunition: int):
        self.name = name
        self.health = health
        self.hit_strength = hit_strength
        self.ammunition = ammunition
        self.is_attacking = False
        self.is_available = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str):
        if not value.isalpha():
            raise ValueError('Ship name must contain only letters!')
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value if value > 0 else 0

    @property
    def ammunition(self):
        return self.__ammunition
    
    @ammunition.setter
    def ammunition(self, value):
        self.__ammunition = value if value > 0 else 0

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, enemy_battleship):
        self.health -= enemy_battleship.hit_strength

