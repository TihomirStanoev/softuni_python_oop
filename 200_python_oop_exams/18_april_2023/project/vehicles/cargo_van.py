from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00
    ADDITIONAL_BATTERY_REDUCES = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        battery_reduce = (mileage / self.max_mileage) * 100
        battery_reduce += self.ADDITIONAL_BATTERY_REDUCES
        self.battery_level -= round(battery_reduce, 0)

