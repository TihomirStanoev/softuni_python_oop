from project.zones.base_zone import BaseZone
from project.battleships.royal_battleship import RoyalBattleship

class PirateZone(BaseZone):
    INITIAL_VOLUME = 8
    def __init__(self, code:str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        result = []
        total_ships = len(self.ships)
        royalships_count = sum(1 for s in self.ships if isinstance(s, RoyalBattleship))

        result.extend(['@Pirate Zone Statistics@',
                       f'Code: {self.code}; Volume: {self.volume}',
                       f'Battleships currently in the Pirate Zone: {total_ships}, {royalships_count} out of them are Royal Battleships.'])
        if self.ships:
            result.append(self.ship_names)

        return '\n'.join(result).strip()

