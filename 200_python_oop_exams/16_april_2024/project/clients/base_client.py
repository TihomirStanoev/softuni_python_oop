from abc import ABC, abstractmethod


class BaseClient(ABC):
    _VALID_MEMBERSHIPS = ["Regular", "VIP"]
    _POINTS_DISCOUNT = {
        100: {'needed_points': 100, 'discount': 10},
        50: {'needed_points': 50, 'discount': 5},
        0: {'needed_points': 0, 'discount': 0}
    }
    def __init__(self,name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str ):
        if value.strip() == '':
            raise ValueError('Client name should be determined!')
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in self._VALID_MEMBERSHIPS:
            raise ValueError('Invalid membership type. Allowed types: Regular, VIP.')

        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        for points in sorted(self._POINTS_DISCOUNT.keys(), reverse=True):
            if self.points >= points:
                self.points -= self._POINTS_DISCOUNT[points]['needed_points']
                return self._POINTS_DISCOUNT[points]['discount'], self.points
