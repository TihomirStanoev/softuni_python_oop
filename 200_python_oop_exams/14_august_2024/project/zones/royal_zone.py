from project.zones.base_zone import BaseZone
from project.battleships.pirate_battleship import PirateBattleship

class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10
    def __init__(self, code:str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        result = []
        total_ships = len(self.ships)
        pirate_ships = sum(1 for s in self.ships if isinstance(s, PirateBattleship))

        result.extend(['@Royal Zone Statistics@',
                       f'Code: {self.code}; Volume: {self.volume}',
                       f'Battleships currently in the Royal Zone: {total_ships}, {pirate_ships} out of them are Pirate Battleships.'])
        if self.ships:
            result.append(self.ship_names)

        return '\n'.join(result).strip()
