from project.equipment.base_equipment import BaseEquipment

class ElbowPad(BaseEquipment):
    _PROTECTION = 90
    _PRICE = 25.0
    _INCREASE_PRICE = 1.1
    def __init__(self):
        super().__init__(self._PROTECTION, self._PRICE)
    
    def increase_price(self):
        self.price *= self._INCREASE_PRICE
