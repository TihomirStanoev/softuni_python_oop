from project.teams.base_team import BaseTeam

class IndoorTeam(BaseTeam):
    _BUDGET = 500.0
    _INCREASES_ADVANTAGE = 145
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self._BUDGET)
    
    def win(self):
        self.advantage += self._INCREASES_ADVANTAGE
        self.wins += 1

    