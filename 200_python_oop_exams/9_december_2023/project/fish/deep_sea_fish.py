from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    __TIME_TO_CATCH = 180
    def __init__(self, name, points):
        super().__init__(name, points, time_to_catch=self.__TIME_TO_CATCH)

    def fish_details(self):
        return f'{self.type_of_fish}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]'