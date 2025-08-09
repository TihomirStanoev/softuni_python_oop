from abc import ABC, abstractmethod


class BaseGuildMember(ABC):
    def __init__(self, tag: str, gold: int, role: str, skill_level: int):
        self.tag = tag
        self.gold = gold
        self.role = role
        self.skill_level = skill_level

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value:str):
        if not value.isalnum():
            raise ValueError('Tag must contain only letters and digits!')
        self.__tag = value

    @property
    def gold(self):
        return self.__gold

    @gold.setter
    def gold(self, value):
        if value < 0:
            raise ValueError('Gold must be a non-negative integer!')
        self.__gold = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value:str):
        if value.strip() == '':
            raise ValueError('Role cannot be empty!')
        self.__role = value

    @property
    def skill_level(self):
        return self.__skill_level

    @skill_level.setter
    def skill_level(self, value):
        if value < 1 or value > 10:
            raise ValueError('Skill level is out of range!')
        self.__skill_level = value

    @abstractmethod
    def practice(self):
        pass

    @property
    def type_of_warrior(self):
        return type(self).__name__

