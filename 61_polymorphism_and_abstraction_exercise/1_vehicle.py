from abc import ABC, abstractmethod


class Vehicle(ABC):
    CONSUMPTION_PER_KG = 1
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    def _calculate_consumed_fuel(self, distance):
        return distance * (self.fuel_consumption + self.CONSUMPTION_PER_KG)



class Car(Vehicle):
    CONSUMPTION_PER_KG = 0.9

    def drive(self, distance):
        consumed_fuel = self._calculate_consumed_fuel(distance)
        if consumed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= consumed_fuel


    def refuel(self, fuel):
        if fuel > 0:
            self.fuel_quantity += fuel


class Truck(Vehicle):
    CONSUMPTION_PER_KG = 1.6
    TANK_CONDITION = 0.95

    def drive(self, distance):
        consumed_fuel = self._calculate_consumed_fuel(distance)
        if consumed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= consumed_fuel


    def refuel(self, fuel):
        if fuel > 0:
            self.fuel_quantity += fuel * self.TANK_CONDITION


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
