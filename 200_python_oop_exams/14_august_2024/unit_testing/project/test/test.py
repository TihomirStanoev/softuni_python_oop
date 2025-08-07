from project.furniture import Furniture
from unittest import TestCase, main


class TestsFurniture(TestCase):
    VALID_MODEL = 'Test Model'
    VALID_PRICE = 100.00
    VALID_DIMENSIONS = (10, 20, 30)


    def setUp(self):
        self.furniture = Furniture(
            model=self.VALID_MODEL,
            price= self.VALID_PRICE,
            dimensions= self.VALID_DIMENSIONS)

    def test_init(self):
        self.assertEqual(self.furniture.model, self.VALID_MODEL)
        self.assertEqual(self.furniture.price, self.VALID_PRICE)
        self.assertEqual(self.furniture.dimensions, self.VALID_DIMENSIONS)
        self.assertTrue(self.furniture.in_stock)
        self.assertIsNone(self.furniture.weight)

    def test_model_raises_if_len_over_fifty(self):
        fifty_chars = 'c' * 51
        with self.assertRaises(ValueError) as e:
            self.furniture.model = fifty_chars
        self.assertEqual(str(e.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_model_raises_if_empty_string(self):
        non_valid_strings = ['', ' ']
        for model in non_valid_strings:
            with self.subTest(model=model):
                with self.assertRaises(ValueError) as e:
                    self.furniture.model = model
                self.assertEqual(str(e.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_price_raises_negative(self):
        with self.assertRaises(ValueError) as e:
            self.furniture.price = -1
        self.assertEqual(str(e.exception), "Price must be a non-negative number.")

    def test_dimensions_raises_error_with_invalid_tuple(self):
        invalid_tuples = [(1,2), (1,), (1,2,3,4)]
        for dimensions in invalid_tuples:
            with self.subTest(dimensions=dimensions):
                with self.assertRaises(ValueError) as e:
                    self.furniture.dimensions = dimensions
                self.assertEqual(str(e.exception), "Dimensions tuple must contain 3 integers.")

    def test_dimensions_raises_error_with_negative_numbers(self):
        negative_tuples = [(-2, -2, -2),(-2,2,2),(-2,-2,2)]
        for dimensions in negative_tuples:
            with self.subTest(dimensions=dimensions):
                with self.assertRaises(ValueError) as e:
                    self.furniture.dimensions = dimensions
                self.assertEqual(str(e.exception),"Dimensions tuple must contain integers greater than zero.")

    def test_weight_raises_error_negative_number_and_zero(self):
        negative_and_zero = [-1, 0]
        for weight in negative_and_zero:
            with self.subTest(weight = weight):
                with self.assertRaises(ValueError) as e:
                    self.furniture.weight = weight
                self.assertEqual(str(e.exception), "Weight must be greater than zero.")

    def test_get_available_status_with_existed_stock(self):
        self.furniture.in_stock = True
        result = self.furniture.get_available_status()
        expected_result = 'Model: Test Model is currently in stock.'
        self.assertEqual(result, expected_result)

    def test_get_available_status_without_stock(self):
        self.furniture.in_stock = False
        result = self.furniture.get_available_status()
        expected_result = 'Model: Test Model is currently unavailable.'
        self.assertEqual(result, expected_result)

    def test_get_specifications_with_none_weighs(self):
        result = self.furniture.get_specifications()
        expected_result = 'Model: Test Model has the following dimensions: 10mm x 20mm x 30mm and weighs: N/A'
        self.assertEqual(result, expected_result)

    def test_get_specifications_with_weighs(self):
        weight = 20
        self.furniture.weight = weight
        result = self.furniture.get_specifications()
        expected_result = f'Model: Test Model has the following dimensions: 10mm x 20mm x 30mm and weighs: {weight}'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    main()
