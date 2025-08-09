from project.legendary_item import LegendaryItem
from unittest import TestCase, main


class TestsLegendaryItem(TestCase):
    VALID_ID = 'TEST123'
    VALID_POWER = 15
    VALID_DURABILITY = 50
    VALID_PRICE = 100
    def setUp(self):
        self.item = LegendaryItem(self.VALID_ID, self.VALID_POWER, self.VALID_DURABILITY, self.VALID_PRICE)

    def test_init(self):
        self.assertEqual(self.item.identifier, self.VALID_ID)
        self.assertEqual(self.item.power, self.VALID_POWER)
        self.assertEqual(self.item.durability, self.VALID_DURABILITY)
        self.assertEqual(self.item.price, self.VALID_PRICE)

    def test_is_precious_can_return_true(self):
        self.item.power = 100
        self.assertTrue(self.item.is_precious)

    def test_is_precious_can_return_false(self):
        self.item.power = 15
        self.assertFalse(self.item.is_precious)

    def test_identifier_raise_more_four_chars(self):
        with self.assertRaises(ValueError) as e:
            self.item.identifier = 'a12'
        self.assertEqual(str(e.exception), "Identifier must be at least 4 characters long!")

    def test_identifier_raise_not_letters_digits_hyphens(self):
        with self.assertRaises(ValueError) as e:
            self.item.identifier = 'KL&!!45'
        self.assertEqual(str(e.exception), "Identifier can only contain letters, digits, or hyphens!")

    def test_identifier_with_valid_values(self):
        valid_id = [self.VALID_ID, 'TESTID', 'TEST-ID', '1234-44', '12345']
        for identifier in valid_id:
            with self.subTest(identifier=identifier):
                self.item.identifier = identifier
                self.assertEqual(self.item.identifier, identifier)

    def test_power_raise_negative_error(self):
        with self.assertRaises(ValueError) as e:
            self.item.power = -1
        self.assertEqual(str(e.exception), "Power must be a non-negative integer!")

    def test_durability_raise_error_with_values_out_of_range(self):
        out_of_range = [-1,0,101]
        for durability in out_of_range:
            with self.subTest(durability=durability):
                with self.assertRaises(ValueError) as e:
                    self.item.durability = durability
                self.assertEqual(str(e.exception), "Durability must be between 1 and 100 inclusive!")

    def test_price_raise_not_multiple_of_ten_and_zero(self):
        non_ten_multiple_and_zero = [0,7, 121]
        for price in non_ten_multiple_and_zero:
            with self.subTest(price=price):
                with self.assertRaises(ValueError) as e:
                    self.item.price = price
                self.assertEqual(str(e.exception), "Price must be a multiple of 10 and not 0!")

    def test_enhance(self):
        power = self.item.power * 2
        price = self.item.price + 10
        durability = self.VALID_DURABILITY + 10

        self.item.enhance()
        self.assertEqual(self.item.power, power)
        self.assertEqual(self.item.price, price)
        self.assertEqual(self.item.durability, durability)

    def test_enhance_can_overload_durability(self):
        power = self.item.power * 2
        price = self.item.price + 10
        self.item.durability = 99

        self.item.enhance()
        self.assertEqual(self.item.power, power)
        self.assertEqual(self.item.price, price)
        self.assertEqual(self.item.durability, 100)

    def test_evaluate_with_valid_durability_and_is_precious_true(self):
        self.item.power = 100
        min_durability_eq_gr = [self.VALID_DURABILITY, self.VALID_DURABILITY - 5]

        self.assertTrue(self.item.is_precious)

        for min_durability in min_durability_eq_gr:
            with self.subTest(min_durability=min_durability):
                print(min_durability)
                expected_result = f"{self.item.identifier} is eligible."
                result = self.item.evaluate(min_durability)
                self.assertEqual(expected_result, result)

    def test_evaluate_with_valid_durability_and_is_precious_false(self):
        self.item.power = 10
        min_durability_eq_gr = [self.VALID_DURABILITY, self.VALID_DURABILITY - 5]

        self.assertFalse(self.item.is_precious)

        for min_durability in min_durability_eq_gr:
            with self.subTest(min_durability=min_durability):
                print(min_durability)
                expected_result = "Item not eligible."
                result = self.item.evaluate(min_durability)
                self.assertEqual(expected_result, result)




if __name__ == '__main__':
    main()

