from project.teams.base_team import BaseTeam

class OutdoorTeam(BaseTeam):
    _BUDGET = 1000.0
    _INCREASES_ADVANTAGE = 115
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self._BUDGET)
    
    def win(self):
        self.advantage += self._INCREASES_ADVANTAGE
        self.wins += 1
