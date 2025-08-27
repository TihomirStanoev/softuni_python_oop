from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.5

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.price_for_reservation = self.PRICE_PER_PERSON * number_of_people

    def type_delicacy(self):
        return 'Open Booth'

