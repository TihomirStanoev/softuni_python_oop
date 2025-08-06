from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    __INITIAL_STRENGTH = 150
    __NEEDED_STRENGTH = 75
    def __init__(self, name: str):
        super().__init__(name, strength=self.__INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.__NEEDED_STRENGTH

    def climb(self, peak : BasePeak):
        peak_difficulty = peak.calculate_difficulty_level()
        peak_name = peak.name

        if peak_difficulty == 'Advanced':
            self.strength -= 30 * 1.3
        elif peak_difficulty == 'Extreme':
            self.strength -= 30 * 2.5
        self.conquered_peaks.append(peak_name)

