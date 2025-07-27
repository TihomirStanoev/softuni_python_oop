from project.extended_list import IntegerList

from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1,2,3)

    def test_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_init_with_integers(self):
        self.assertIn(1, self.integer_list.get_data())
        self.assertIn(2, self.integer_list.get_data())
        self.assertIn(3, self.integer_list.get_data())

    def test_init_with_non_integer(self):
        integer_list = IntegerList(1, 'a')
        self.assertNotIn('a', integer_list.get_data())

    def test_add_with_integer_element(self):
        result = self.integer_list.add(5)
        self.assertIn(5, result)

    def test_add_if_element_raise_error(self):
        with self.assertRaises(ValueError) as e:
            self.integer_list.add('a')
        self.assertEqual(str(e.exception), "Element is not Integer")

    def test_remove_index(self):
        zero_element = self.integer_list.get_data()[0]
        result = self.integer_list.remove_index(0)
        self.assertNotEqual(zero_element, self.integer_list.get_data()[0])
        self.assertEqual(zero_element, result)
        self.assertNotIn(zero_element, self.integer_list.get_data())

    def test_remove_index_if_out_of_range(self):
        outer_index = len(self.integer_list.get_data())
        with self.assertRaises(IndexError) as e:
            self.integer_list.remove_index(outer_index)
        self.assertEqual(str(e.exception), "Index is out of range")

    def test_get_method_with_index_out_of_range(self):
        outer_index = len(self.integer_list.get_data())
        with self.assertRaises(IndexError) as e:
            self.integer_list.get(outer_index)
        self.assertEqual(str(e.exception), "Index is out of range")

    def test_get_method_with_correct_index(self):
        expected_result = self.integer_list.get_data()[0]
        result = self.integer_list.get(0)
        self.assertEqual(expected_result, result)

    def test_insert_with_currect_index_and_element(self):
        self.integer_list.insert(0,99)
        self.assertEqual(self.integer_list.get_data()[0], 99)

    def test_insert_when_raise_index_error(self):
        outer_index = len(self.integer_list.get_data())
        integer = 5
        with self.assertRaises(IndexError) as e:
            self.integer_list.insert(outer_index, integer)
        self.assertEqual(str(e.exception), 'Index is out of range')

    def test_insert_when_rise_value_error(self):
        valid_index = 0
        non_integer = 'a'
        with self.assertRaises(ValueError) as e:
            self.integer_list.insert(valid_index, non_integer)
        self.assertEqual(str(e.exception), 'Element is not Integer')

    def test_get_biggest(self):
        biggest_number = max(self.integer_list.get_data())
        self.assertEqual(biggest_number, self.integer_list.get_biggest())

    def test_get_index(self):
        expected_index = self.integer_list.get_data().index(1)
        result = self.integer_list.get_index(1)
        self.assertEqual(expected_index, result)




if __name__ == '__main__':
    main()