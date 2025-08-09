from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_members.mage import Mage

class MagicTower(BaseGuildHall):
    __MAX_MEMBERS = 4
    INCREASES_GOLD = {'Mage': lambda g: g*2}

    @property
    def max_member_count(self):
        return self.__MAX_MEMBERS

    def increase_gold(self, min_skill_level_value: int):
        for member in self.members:
            if member.skill_level < min_skill_level_value:
                continue
            if member.type_of_warrior in self.INCREASES_GOLD.keys():
                member.gold = self.INCREASES_GOLD[member.type_of_warrior](member.gold)
