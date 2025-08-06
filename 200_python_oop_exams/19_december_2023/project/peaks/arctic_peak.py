from project.peaks.base_peak import BasePeak

class ArcticPeak(BasePeak):
    __RECOMMENDED_GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
    __DIFFICULTY_LEVEL = {
        'Extreme': lambda x: x > 3000,
        'Advanced': lambda x: 2000 <= x <= 3000,
        '' : lambda x: x < 2000
    }
    def get_recommended_gear(self):
        return self.__RECOMMENDED_GEAR

    def calculate_difficulty_level(self):
        return [difficulty for difficulty, meters in self.__DIFFICULTY_LEVEL.items() if meters(self.elevation)][0]
