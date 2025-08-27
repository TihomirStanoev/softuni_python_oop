from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}
    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0.0

    def _find_delicacy_by_name(self, name) -> Delicacy | None:
        return next((d for d in self.delicacies if d.name == name), None)

    def _find_booth_by_number(self, booth_number: int) -> Booth | None:
        return next((b for b in self.booths if b.booth_number == booth_number), None)

    def _find_booth_for_reserve(self, number_of_people: int) -> Booth | None:
        return next((b for b in self.booths if not b.is_reserved and b.capacity > number_of_people), None)

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = self._find_delicacy_by_name(name)
        if delicacy:
            raise Exception(f'{name} already exists!')
        if type_delicacy not in self.VALID_DELICACY.keys():
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        delicacy = self.VALID_DELICACY[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f'Added delicacy {delicacy.name} - {delicacy.type_delicacy} to the pastry shop.'


    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = self._find_booth_by_number(booth_number)
        if booth:
            raise Exception(f'Booth number {booth_number} already exists!')
        if type_booth not in self.VALID_BOOTH.keys():
            raise Exception(f'{type_booth} is not a valid booth!')

        booth = self.VALID_BOOTH[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f'Added booth number {booth.booth_number} in the pastry shop.'


    def reserve_booth(self, number_of_people: int):
        booth = self._find_booth_for_reserve(number_of_people)
        if booth is None:
            raise Exception(f'No available booth for {number_of_people} people!')

        booth.reserve(number_of_people)

        return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'


    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._find_booth_by_number(booth_number)
        if booth is None:
            raise Exception(f'Could not find booth {booth_number}!')

        delicacy = self._find_delicacy_by_name(delicacy_name)
        if delicacy is None:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        booth.order(delicacy)

        return f'Booth {booth.booth_number} ordered {delicacy.name}.'


    def leave_booth(self, booth_number: int):
        booth = self._find_booth_by_number(booth_number)

        orders_amount = sum(d.price for d in booth.delicacy_orders) + booth.price_for_reservation
        self.income += orders_amount

        booth.leave()

        return f'Booth {booth.booth_number}:\nBill: {orders_amount:.2f}lv.'


    def get_income(self):
        return f'Income: {self.income:.2f}lv.'

