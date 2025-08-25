from project.band import Band
from project.band_members.musician import Musician
from project.concert import Concert
from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.band_members.singer import Singer


class ConcertTrackerApp:
    VALID_MUSICIAN = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []


    @staticmethod
    def _is_ready(band, concert):
        for member in band.members:
            for skill in concert.GENRE[concert.genre][member.musician_type]:
                if skill not in member.skills:
                    return False
        return True

    @staticmethod
    def _find_musician_by_name(musicians, name) -> Musician | None:
        return next((m for m in musicians if m.name == name), None)

    def _find_band_by_name(self, name) ->Band | None:
        return next((b for b in self.bands if b.name == name), None)

    def _find_concert_by_place(self, place) -> Concert | None:
        return next((c for c in self.concerts if c.place == place), None)

    def _find_band_by_name_raise_exception(self, band_name):
        band = self._find_band_by_name(band_name)
        if band is None:
            raise Exception(f'{band_name} isn\'t a band!')
        return band

    def _compare_band_members(self, band_members):
        current_members_types = set()
        for member in band_members:
            member_type = type(member).__name__
            current_members_types.add(member_type)
            if self.VALID_MUSICIAN == current_members_types:
                return False
        return True

    def _find_musician_by_name_raise_exception(self, musician_name):
        musician = self._find_musician_by_name(self.musicians, musician_name)
        if musician is None:
            raise Exception(f'{musician_name} isn\'t a musician!')
        return musician

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN.keys():
            raise ValueError('Invalid musician type!')

        musician = self._find_musician_by_name(self.musicians, name)
        if musician:
            raise Exception(f'{name} is already a musician!')

        musician = self.VALID_MUSICIAN[musician_type](name, age)
        self.musicians.append(musician)
        return f'{name} is now a {musician_type}.'



    def create_band(self, name: str):
        band = self._find_band_by_name(name)
        if band:
            raise Exception(f'{name} band is already created!')

        band = Band(name)
        self.bands.append(band)
        return f'{name} was created.'


    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._find_concert_by_place(place)
        if concert:
            raise Exception(f'{place} is already registered for {concert.genre} concert!')

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f'{genre} concert in {place} was added.'


    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._find_musician_by_name_raise_exception(musician_name)
        band = self._find_band_by_name_raise_exception(band_name)

        band.members.append(musician)
        return f'{musician_name} was added to {band_name}.'


    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._find_band_by_name_raise_exception(band_name)
        musician = self._find_musician_by_name(band.members, musician_name)
        if musician is None:
            raise Exception(f'{musician_name} isn\'t a member of {band_name}!')
        band.members.remove(musician)

        return f'{musician_name} was removed from {band_name}.'

    def start_concert(self, concert_place: str, band_name: str):
        band = self._find_band_by_name(band_name)
        if not self._compare_band_members(band.members):
            raise Exception(f'{band_name} can\'t start the concert because it doesn\'t have enough members!')

        concert = self._find_concert_by_place(concert_place)
        if not self._is_ready(band, concert):
            raise Exception(f'The {band_name} band is not ready to play at the concert!')

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f'{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}.'

