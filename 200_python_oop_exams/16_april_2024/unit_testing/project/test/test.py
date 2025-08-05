from project.restaurant import Restaurant
from unittest import TestCase, main


class RestaurantTest(TestCase):
    _VALID_NAME = 'TestsRestaurant'
    _VALID_CAPACITY = 10
    _INVALID_NAME = ''
    _INVALID_CAPACITY = -5

    def setUp(self):
        self.restaurant = Restaurant(name=self._VALID_NAME, capacity=self._VALID_CAPACITY)

    def test_init(self):
        self.assertEqual(self.restaurant.name, self._VALID_NAME)
        self.assertEqual(self.restaurant.capacity, self._VALID_CAPACITY)
        self.assertIsInstance(self.restaurant.waiters, list)
        self.assertEqual(self.restaurant.waiters, [])

    def test_name_can_raised_error_with_invalid_name(self):
        with self.assertRaises(ValueError) as e:
            Restaurant(name=self._INVALID_NAME, capacity=self._VALID_CAPACITY)
        self.assertEqual(str(e.exception), "Invalid name!")

    def test_capacity_with_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as e:
            Restaurant(name=self._VALID_NAME, capacity=self._INVALID_CAPACITY)
        self.assertEqual(str(e.exception), "Invalid capacity!")

    def test_add_waiter_can_add_new_waiter(self):
        waiter_name = 'Test Waiter'
        result = self.restaurant.add_waiter(waiter_name)
        expected_result = f"The waiter {waiter_name} has been added."
        waiters = [waiter['name'] for waiter in self.restaurant.waiters]

        self.assertEqual(result,expected_result)
        self.assertIn(waiter_name, waiters)

    def test_add_waiter_with_full_capacity(self):
        waiter_name = 'Test Waiter'
        self.restaurant.capacity = 0
        result = self.restaurant.add_waiter(waiter_name)
        expected_result = "No more places!"

        self.assertEqual(result, expected_result)

    def test_add_waiter_with_existed_waiter(self):
        waiter_name = 'Test Waiter'
        self.restaurant.add_waiter(waiter_name)
        result = self.restaurant.add_waiter(waiter_name)
        expected_result = f"The waiter {waiter_name} already exists!"

        self.assertEqual(result, expected_result)
        self.assertEqual(len(self.restaurant.waiters), 1)

    def test_remove_waiter_can_remove_existed_waiter(self):
        waiter_name = 'Test Waiter'

        self.restaurant.add_waiter(waiter_name)
        result = self.restaurant.remove_waiter(waiter_name)
        expected_result = f"The waiter {waiter_name} has been removed."
        waiters = [waiter['name'] for waiter in self.restaurant.waiters]

        self.assertEqual(result, expected_result)
        self.assertNotIn(waiter_name, waiters)

    def test_remove_waiter_with_not_found_waiter(self):
        waiter_name = 'Test Waiter'

        result = self.restaurant.remove_waiter(waiter_name)
        expected_result = f"No waiter found with the name {waiter_name}."
        self.assertEqual(result, expected_result)

    def test_get_total_earnings(self):
        earn = 50
        self.restaurant.add_waiter('Test 1')
        self.restaurant.add_waiter('Test 2')
        for waiter in self.restaurant.waiters:
            waiter['total_earnings'] = earn

        total_earnings = len(self.restaurant.waiters) * earn
        result = self.restaurant.get_total_earnings()

        self.assertEqual(total_earnings, result)


    def test_get_waiters_with_nones(self):
        total_waiters = 3
        waiters_earn = [50*i for i in range(1, total_waiters+1)]
        for index in range(total_waiters):
            self.restaurant.add_waiter(f'Waiter {index}')
        for i in range(len(self.restaurant.waiters)):
            self.restaurant.waiters[i]['total_earnings'] = waiters_earn[i]

        result = self.restaurant.get_waiters()
        expected_result = [{'name': 'Waiter 0', 'total_earnings': 50}, {'name': 'Waiter 1', 'total_earnings': 100},
                           {'name': 'Waiter 2', 'total_earnings': 150}]
        self.assertEqual(result, expected_result)

    def test_get_waiters_with_min_earnings(self):
        total_waiters = 3
        waiters_earn = [50*i for i in range(1, total_waiters+1)]
        for index in range(total_waiters):
            self.restaurant.add_waiter(f'Waiter {index}')
        for i in range(len(self.restaurant.waiters)):
            self.restaurant.waiters[i]['total_earnings'] = waiters_earn[i]

        result = self.restaurant.get_waiters(min_earnings=75)
        expected_result = [{'name': 'Waiter 1', 'total_earnings': 100}, {'name': 'Waiter 2', 'total_earnings': 150}]

        self.assertEqual(result, expected_result)

    def test_get_waiters_with_max_earnings(self):
        total_waiters = 3
        waiters_earn = [50*i for i in range(1, total_waiters+1)]
        for index in range(total_waiters):
            self.restaurant.add_waiter(f'Waiter {index}')
        for i in range(len(self.restaurant.waiters)):
            self.restaurant.waiters[i]['total_earnings'] = waiters_earn[i]

        result = self.restaurant.get_waiters(max_earnings=75)
        expected_result = [{'name': 'Waiter 0', 'total_earnings': 50}]

        self.assertEqual(result, expected_result)


    def test_get_waiters_with_min_and_max_earnings(self):
        total_waiters = 3
        waiters_earn = [50*i for i in range(1, total_waiters+1)]
        for index in range(total_waiters):
            self.restaurant.add_waiter(f'Waiter {index}')
        for i in range(len(self.restaurant.waiters)):
            self.restaurant.waiters[i]['total_earnings'] = waiters_earn[i]

        result = self.restaurant.get_waiters(min_earnings=75, max_earnings=125)
        expected_result = [{'name': 'Waiter 1', 'total_earnings': 100}]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    main()