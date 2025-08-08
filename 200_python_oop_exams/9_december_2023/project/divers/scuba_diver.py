from project.divers.base_diver import BaseDiver

class ScubaDiver(BaseDiver):
    __INITIAL_OXYGEN_LEVEL = 540
    __REDUCE_OXYGEN = 0.3

    def __init__(self,name):
        super().__init__(name, oxygen_level=self.__INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        new_oxygen_level = self.oxygen_level - round(time_to_catch * self.__REDUCE_OXYGEN)
        if new_oxygen_level <= 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = new_oxygen_level

    def renew_oxy(self):
        self.oxygen_level = self.__INITIAL_OXYGEN_LEVEL