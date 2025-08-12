from project.equipment.base_equipment import BaseEquipment

class KneePad(BaseEquipment):
    _PROTECTION = 120
    _PRICE = 15.0
    _INCREASE_PRICE = 1.2
    def __init__(self):
        super().__init__(self._PROTECTION, self._PRICE)
    
    def increase_price(self):
        self.price *= self._INCREASE_PRICE

        