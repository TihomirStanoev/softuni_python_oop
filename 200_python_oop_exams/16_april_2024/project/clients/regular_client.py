from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    _SPENT_EVERY = 10
    def __init__(self, name):
        super().__init__(name, membership_type='Regular')

    def earning_points(self, order_amount:float):
        earned_points = order_amount // self._SPENT_EVERY
        self.points += earned_points
        return earned_points
