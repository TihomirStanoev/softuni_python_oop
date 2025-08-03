from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.battleships.base_battleship import BaseBattleship
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone

FRIENDLY_ZONES_MAPPER = {
    RoyalBattleship: RoyalZone,
    PirateBattleship: PirateZone
}


class BattleManager:
    VALID_ZONES = {
        "RoyalZone": RoyalZone ,
        "PirateZone": PirateZone
    }
    VALID_SHIPS = {
        'RoyalBattleship': RoyalBattleship,
        'PirateBattleship': PirateBattleship
    }
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []


    def _find_zone_by_code(self, code):
        return next((z for z in self.zones if z.code == code), None)

    def _find_ship_by_name (self, name):
        return next((s for s in self.ships if s.name == name), None)


    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.VALID_ZONES.keys():
            raise Exception('Invalid zone type!')
        zone = self._find_zone_by_code(zone_code)

        if zone:
            raise Exception('Zone already exists!')

        zone = self.VALID_ZONES[zone_type](zone_code)
        self.zones.append(zone)
        return f'A zone of type {zone_type} was successfully added.'

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.VALID_SHIPS.keys():
            raise Exception(f'{ship_type} is an invalid type of ship!')

        ship = self.VALID_SHIPS[ship_type](name, health, hit_strength)
        self.ships.append(ship)

        return f'A new {ship_type} was successfully added.'

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f'Zone {zone.code} does not allow more participants!'
        if ship.health <= 0:
            return f'Ship {ship.name} is considered sunk! Participation not allowed!'

        if not ship.is_available:
            return f'Ship {ship.name} is not available and could not participate!'

        ship_class = type(ship)
        if isinstance(zone, FRIENDLY_ZONES_MAPPER.get(ship_class)):
            ship.is_attacking = True

        ship.is_available = False
        zone.ships.append(ship)
        zone.volume -= 1

        return f'Ship {ship.name} successfully participated in zone {zone.code}.'

    def remove_battleship(self, ship_name: str):
        ship = self._find_ship_by_name(ship_name)

        if ship is None:
            return 'No ship with this name!'
        if not ship.is_available:
            return 'The ship participates in zone battles! Removal is impossible!'

        self.ships.remove(ship)
        return f'Successfully removed ship {ship.name}.'

    def start_battle(self, zone: BaseZone):
        attackers: list[BaseBattleship] = []
        targets: list[BaseBattleship] = []
        for ship in zone.ships:
            is_friendly = isinstance(zone, FRIENDLY_ZONES_MAPPER.get(type(ship)))
            if is_friendly and ship.is_attacking:
                attackers.append(ship)
            elif not is_friendly and not ship.is_attacking:
                targets.append(ship)


        if not attackers or not targets:
            return 'Not enough participants. The battle is canceled.'

        attacker = sorted(attackers, key= lambda s: -s.hit_strength)[0]
        target = sorted(targets, key=lambda s: -s.health)[0]

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f'{target.name} lost the battle and was sunk.'

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f'{attacker.name} ran out of ammunition and leaves.'
        return 'Both ships survived the battle.'

    def get_statistics(self):
        available_ships = [ship for ship in self.ships if ship.is_available]
        total_zones = len(self.zones)
        sorted_zones = sorted(self.zones, key=lambda z: z.code)

        result = [f'Available Battleships: {len(available_ships)}']

        if available_ships:
            result.append(f'#{", ".join(s.name for s in available_ships)}#')

        result.extend(['***Zones Statistics:***',
                  f'Total Zones: {total_zones}'])

        for zone in sorted_zones:
            result.append(zone.zone_info())


        return '\n'.join(result).strip()


