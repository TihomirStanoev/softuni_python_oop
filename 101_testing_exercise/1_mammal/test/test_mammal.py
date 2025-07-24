from project.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('Pesho', 'Mammal', 'Yo!')

    def test_creation(self):
        self.assertEqual(self.mammal.name, 'Pesho')
        self.assertEqual(self.mammal.type, 'Mammal')
        self.assertEqual(self.mammal.sound, 'Yo!')

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_make_sound(self):
        expected_result = "Pesho makes Yo!"
        actual_result = self.mammal.make_sound()
        self.assertEqual(actual_result, expected_result)

    def test_info(self):
        expected_result = "Pesho is of type Mammal"
        actual_result = self.mammal.info()
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
