from project.guild_members.base_guild_member import BaseGuildMember


class Mage(BaseGuildMember):
    __INITIAL_SKILL_LEVEL = 1

    def __init__(self, tag: str, gold: int):
        super().__init__(tag, gold, role=self.type_of_warrior, skill_level=self.__INITIAL_SKILL_LEVEL)

    def practice(self):
        self.skill_level = min(self.skill_level * 2, 10)


