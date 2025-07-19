from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team:RedBullTeam = None
        self.mercedes_team:MercedesTeam = None


    def register_team_for_season(self, team_name: str, budget: int):
        is_register = False

        if team_name == 'Red Bull' and self.red_bull_team is None:
            self.red_bull_team = RedBullTeam(budget)
            is_register = True
        elif team_name == 'Mercedes' and self.mercedes_team is None:
            self.mercedes_team = MercedesTeam(budget)
            is_register = True

        if is_register:
            return f'{team_name} has joined the new F1 season.'
        raise ValueError('Invalid team name!')

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception('Not all teams have registered for the season.')
        result = []
        better_team = 'Red Bull' if red_bull_pos < mercedes_pos else 'Mercedes'

        result.append(better_team)
        result.append(self.red_bull_team.calculate_revenue_after_race(red_bull_pos))
        result.append(self.mercedes_team.calculate_revenue_after_race(mercedes_pos))

        return f'Red Bull: {result[1]}. Mercedes: {result[2]}. {result[0]} is ahead at the {race_name} race.'