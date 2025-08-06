from project.peaks.base_peak import BasePeak

class SummitPeak(BasePeak):
    __RECOMMENDED_GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
    __DIFFICULTY_LEVEL = {
        'Extreme': lambda x: x > 2500,
        'Advanced': lambda x: 1500 <= x <= 2500
    }
    def get_recommended_gear(self):
        return self.__RECOMMENDED_GEAR

    def calculate_difficulty_level(self):
        return [difficulty for difficulty, meters in self.__DIFFICULTY_LEVEL.items() if meters(self.elevation)][0]
