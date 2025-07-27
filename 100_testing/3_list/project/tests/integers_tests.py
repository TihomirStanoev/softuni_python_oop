from project.integer_list import IntegerList
from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.integer = IntegerList(1,2,3,4,5)

    def test_init(self):
        with self.assertRaises(ValueError) as e:
            x = IntegerList(1,2,'a')
        self.assertEqual(str(e.exception), 'Store only integers!')

    def test_add_integer(self):
        expected_list = [1,2,3,4,5,6]
        len_before_add = len(self.integer.integers)
        len_after_add = len_before_add + 1
        result = self.integer.add(6)
        self.assertEqual(expected_list, result)
        self.assertEqual(len(self.integer.integers), len_after_add)
        self.assertIn(6, self.integer.integers)

    def test_if_not_integer(self):
        with self.assertRaises(ValueError) as e:
            self.integer.add('b')
        self.assertEqual(str(e.exception), 'Element is not a integer!')

    def test_get_return_correct_element(self):
        result = self.integer.get(0)
        zero_element = self.integer.integers[0]
        self.assertEqual(result, zero_element)

    def test_get_if_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as e:
            self.integer.get(len(self.integer.integers)+1)
        self.assertEqual(str(e.exception), 'Index out of range')

    def test_remove_index(self):
        zero_element = self.integer.integers[0]
        result = self.integer.remove_index(0)
        self.assertEqual(zero_element, result)

    def test_remove_index_if_index_do_not_exist(self):
        with self.assertRaises(IndexError) as e:
            self.integer.remove_index(len(self.integer.integers)+1)
        self.assertEqual(str(e.exception), 'Index out of range')


if __name__ == '__main__':
    main()