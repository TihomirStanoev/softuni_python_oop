from project.equipment.base_equipment import BaseEquipment
from project.teams.base_team import BaseTeam
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam

class Tournament:
    VALID_EQUIPMENTS = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam":OutdoorTeam, "IndoorTeam":IndoorTeam}
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list[BaseEquipment] = []
        self.teams: list[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str):
        if not value.strip().isalnum():
            raise ValueError('Tournament name should contain letters and digits only!')
        self.__name = value

    def _find_equipment_by_type(self, equipment_type: str):
        return next((e for e in reversed(self.equipment) if e.type_of_equipment == equipment_type), None)

    def _find_team_by_name(self, team_name):
        return next((t for t in self.teams if t.name == team_name), None)

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENTS.keys():
            raise Exception('Invalid equipment type!')
        equipment = self.VALID_EQUIPMENTS[equipment_type]()
        self.equipment.append(equipment)
        return f'{equipment_type} was successfully added.'
    
    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS.keys():
            raise Exception('Invalid team type!')
        if len(self.teams) >= self.capacity:
            return('Not enough tournament capacity.')
        
        team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f'{team_type} was successfully added.'
    
    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self._find_equipment_by_type(equipment_type)
        team = self._find_team_by_name(team_name)

        if equipment.price > team.budget:
            raise Exception('Budget is not enough!')

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f'Successfully sold {equipment_type} to {team_name}.'
    
    def remove_team(self, team_name: str):
        team = self._find_team_by_name(team_name)
        if team is None:
            raise Exception('No such team!')
        if team.wins != 0:
            raise Exception(f'The team has {team.wins} wins! Removal is impossible!')
        
        self.teams.remove(team)
        return f'Successfully removed {team_name}.'

    def increase_equipment_price(self, equipment_type: str):
        sold_equipment = []
        number_of_changed_equipment = 0

        for team in self.teams:
            for equimpnet in team.equipment:
                sold_equipment.append(equimpnet)

        for equimpnet_increase in self.equipment:
            if equimpnet_increase not in sold_equipment and equimpnet_increase.type_of_equipment == equipment_type:
                equimpnet_increase.increase_price()
                number_of_changed_equipment += 1
        
        return f'Successfully changed {number_of_changed_equipment}pcs of equipment.'

    def play(self, team_name1: str, team_name2: str):
        team_one = self._find_team_by_name(team_name1)
        team_two = self._find_team_by_name(team_name2)

        if team_one.type_of_team != team_two.type_of_team:
            raise Exception('Game cannot start! Team types mismatch!')

        winner = None
        if team_one.total_points == team_two.total_points:
            return 'No winner in this game.'
        elif team_one.total_points > team_two.total_points:
            winner = team_one.name
            team_one.win()
        else:
            winner = team_two.name
            team_two.win()

        return f'The winner is {winner}.'

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        reaulst = [
            f'Tournament: {self.name}',
            f'Number of Teams: {len(self.teams)}',
            'Teams:',
            '\n'.join(t.get_statistics() for t in sorted_teams)
        ]

        return '\n'.join(reaulst)