class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def _get_room(self, number):
        return next((r for r in self.rooms if r.number == number), None)

    def take_room(self, room_number, people):
        room = self._get_room(room_number)
        if room:
            room.take_room(people)

    def free_room(self, room_number):
        room = self._get_room(room_number)

        if room:
            room.free_room()

    def status(self):
        total_guests = 0
        taken_rooms = []
        free_rooms = []

        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(str(room.number))
                total_guests += room.guests
            else:
                free_rooms.append(str(room.number))

        return (f'Hotel {self.name} has {total_guests} total guests\n'
                f'Free rooms: {", ".join(free_rooms)}\n'
                f'Taken rooms: {", ".join(taken_rooms)}')




