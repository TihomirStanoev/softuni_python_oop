from car_manager import Car
from unittest import TestCase, main


class CarTests(TestCase):
    MAKE = 'Test'
    MODEL = 'Car'
    FUEL_CONSUMPTION = 10
    FUEL_CAPACITY = 100
    def setUp(self):
        self.car = Car(self.MAKE,self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)

    def test_valid_init(self):
        self.assertEqual(self.car.make, self.MAKE)
        self.assertEqual(self.car.model, self.MODEL)
        self.assertEqual(self.car.fuel_consumption, self.FUEL_CONSUMPTION)
        self.assertEqual(self.car.fuel_capacity, self.FUEL_CAPACITY)
        self.assertEqual(self.car.fuel_amount, 0)


    def test_make_empty_raises(self):
        for make in ['', None]:
            with self.subTest(make = make):
                with self.assertRaises(Exception) as e:
                    Car(make,self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)
                self.assertEqual(str(e.exception), 'Make cannot be null or empty!')

    def test_model_empty_raises(self):
        for model in ['', None]:
            with self.subTest(model=model):
                with self.assertRaises(Exception) as e:
                    Car(self.MAKE, model, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)
                self.assertEqual(str(e.exception), 'Model cannot be null or empty!')


    def test_fuel_consumption_zero_negative_rises(self):
        for fuel_consumption in [0, -1, -10]:
            with self.subTest(fuel_consumption=fuel_consumption):
                with self.assertRaises(Exception) as e:
                    Car(self.MAKE, self.MODEL, fuel_consumption, self.FUEL_CAPACITY)
                self.assertEqual(str(e.exception), 'Fuel consumption cannot be zero or negative!')

    def test_fuel_capacity_zero_negative_raises(self):
        for fuel_capacity in [0,-1,-10]:
            with self.subTest(fuel_capacity=fuel_capacity):
                with self.assertRaises(Exception) as e:
                    Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, fuel_capacity)
                self.assertEqual(str(e.exception), 'Fuel capacity cannot be zero or negative!')

    def test_fuel_amount_negative_raises(self):
        with self.assertRaises(Exception) as e:
            self.car.fuel_amount = -5
        self.assertEqual(str(e.exception), 'Fuel amount cannot be negative!')

    def test_refuel_with_negative_zero_rises(self):
        for fuel in [-1, 0]:
            with self.subTest(fuel=fuel):
                with self.assertRaises(Exception) as e:
                    self.car.refuel(fuel)
                self.assertEqual(str(e.exception), 'Fuel amount cannot be zero or negative!')

    def test_refuel_should_add_fuel_to_tank_correctly(self):
        refueled_fuel = 50
        self.car.refuel(refueled_fuel)
        self.assertEqual(self.car.fuel_amount, refueled_fuel)

    def test_refuel_should_not_overfill_tank(self):
        self.car.refuel(self.FUEL_CAPACITY+10)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_with_exact_fuel_for_distance_should_empty_tank(self):
        driven_car = Car(self.MAKE, self.MODEL, 10, 100)
        driven_car.fuel_amount = 100
        driven_car.drive(1000)
        self.assertEqual(driven_car.fuel_amount, 0)

    def test_drive_should_reduce_fuel_amount_after_successful_trip(self):
        driven_car = Car(self.MAKE, self.MODEL, 10, 100)
        driven_car.fuel_amount = 100
        driven_car.drive(500)
        self.assertEqual(driven_car.fuel_amount, 50)

    def test_drive_when_not_enough_fuel_should_raise_exception(self):
        distance = (self.FUEL_CONSUMPTION * 100) + 1
        with self.assertRaises(Exception) as e:
            self.car.drive(distance)
        self.assertEqual(str(e.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    main()