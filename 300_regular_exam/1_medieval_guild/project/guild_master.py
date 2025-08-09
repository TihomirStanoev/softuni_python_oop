from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower
from project.guild_members.base_guild_member import BaseGuildMember
from project.guild_members.warrior import Warrior
from project.guild_members.mage import Mage

class GuildMaster:
    __VALID_MEMBERS = {"Warrior": Warrior, "Mage": Mage}
    __VALID_HALLS = {"CombatHall":CombatHall, "MagicTower": MagicTower}
    def __init__(self):
        self.members: list[BaseGuildMember] = []
        self.guild_halls: list[BaseGuildHall] = []

    @staticmethod
    def practice_members(guild_hall: BaseGuildHall, sessions_number: int):
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()
        total_skill_level = sum(m.skill_level for m in guild_hall.members)

        return f'{guild_hall.alias} members have {total_skill_level} total skill level after {sessions_number} practice session/s.'

    @staticmethod
    def _find_member_by_tag(collection, member_tag) -> BaseGuildMember | None:
        return next((m for m in collection if m.tag == member_tag), None)

    def _find_hall_by_alias(self, guild_hall_alias):
        return next((h for h in self.guild_halls if h.alias == guild_hall_alias) ,None)

    def _find_member_in_hall_by_type(self, member_type):
        return next((m for m in self.members if m.type_of_warrior == member_type), None)

    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        if member_type not in self.__VALID_MEMBERS.keys():
            raise ValueError('Invalid member type!')
        member = self._find_member_by_tag(self.members, member_tag)

        if member:
            raise ValueError(f'{member_tag} has already been added!')
        member = self.__VALID_MEMBERS[member_type](member_tag, member_gold)
        self.members.append(member)
        return f'{member_tag} is successfully added as {member_type}.'

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        if guild_hall_type not in self.__VALID_HALLS.keys():
            raise ValueError('Invalid guild hall type!')
        guild_hall = self._find_hall_by_alias(guild_hall_alias)

        if guild_hall:
            raise ValueError(f'{guild_hall_alias} has already been added!')

        guild_hall = self.__VALID_HALLS[guild_hall_type](guild_hall_alias)
        self.guild_halls.append(guild_hall)
        return f'{guild_hall_alias} is successfully added as a {guild_hall_type}.'

    def assign_member(self, guild_hall_alias: str, member_type: str):
        guild_hall = self._find_hall_by_alias(guild_hall_alias)
        if guild_hall is None:
            raise ValueError(f'Guild hall {guild_hall_alias} does not exist!')
        member = self._find_member_in_hall_by_type(member_type)
        if member is None:
            raise ValueError('No available members of the type!')

        if len(guild_hall.members) >= guild_hall.max_member_count:
            return 'Maximum member count reached. Assignment is impossible.'
        self.members.remove(member)
        guild_hall.members.append(member)

        return f'{member.tag} was assigned to {guild_hall.alias}.'

    def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
        member = self._find_member_by_tag(guild_hall.members, member_tag)
        if member is None or member.skill_level == 10:
            return 'The unassignment process was canceled.'

        guild_hall.members.remove(member)
        self.members.append(member)
        return f'Unassigned member {member_tag}.'

    def guild_update(self, min_skill_level_value: int):
        for guild_hall in self.guild_halls:
            guild_hall.increase_gold(min_skill_level_value)
        sorted_guild_hall = sorted(self.guild_halls, key=lambda gh: (-len(gh.members), gh.alias))
        result = ['<<<Guild Updated Status>>>',
                  f'Unassigned members count: {len(self.members)}',
                  f'Guild halls count: {len(self.guild_halls)}']

        for gh in sorted_guild_hall:
            result.append(f'>>>{gh.status()}')

        return '\n'.join(result)

