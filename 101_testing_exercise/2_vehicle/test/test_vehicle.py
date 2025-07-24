from project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    fuel = 55.5
    horse_power = 150.0
    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_creation(self):
        self.assertEqual(self.vehicle.fuel, self.fuel)
        self.assertEqual(self.vehicle.horse_power, self.horse_power)
        self.assertEqual(self.vehicle.capacity, self.fuel)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_happy(self):
        self.vehicle.drive(11)
        self.assertEqual(self.vehicle.fuel, 41.75)

    def test_drive_sad(self):
        with self.assertRaises(Exception) as e:
            self.vehicle.drive(500)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_refuel_happy(self):
        self.vehicle.fuel = 0
        refueled_fuel = 15.2
        self.vehicle.refuel(refueled_fuel)
        self.assertEqual(self.vehicle.fuel, refueled_fuel)

    def test_refuel_sad(self):
        with self.assertRaises(Exception) as e:
            self.vehicle.refuel(500)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_str_dunder_method(self):
        actual_result = str(self.vehicle)
        expected_result = f"The vehicle has {self.horse_power} " \
               f"horse power with {self.fuel} fuel left and {Vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()