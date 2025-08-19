from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INCREASES_WEIGHT = 3
    INITIAL_WEIGHT = 9

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.INITIAL_WEIGHT)

    def eating(self):
        self.weight += self.INCREASES_WEIGHT