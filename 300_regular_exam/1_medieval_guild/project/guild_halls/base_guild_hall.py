from abc import ABC, abstractmethod

from project.guild_members.base_guild_member import BaseGuildMember


class BaseGuildHall(ABC):
    def __init__(self, alias: str):
        self.alias = alias
        self.members: list[BaseGuildMember] = []

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, value:str):
        if len(value.strip()) < 2 or not all([True if char == ' ' or char.isalpha() else False for char in value ]):
            raise ValueError('Guild hall alias is invalid!')
        self.__alias = value

    @abstractmethod
    def increase_gold(self, min_skill_level_value: int):
        pass

    @property
    @abstractmethod
    def max_member_count(self):
        pass

    def calculate_total_gold(self):
        return sum(member.gold for member in self.members)

    def status(self):
        sorted_members = sorted(self.members, key=lambda m: m.tag)
        total_gold = self.calculate_total_gold()
        members = ' *'.join(m.tag for m in sorted_members) if sorted_members else 'N/A'

        return f'Guild hall: {self.alias}; Members: {members}; Total gold: {total_gold}'
