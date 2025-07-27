from project.cat import Cat
from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat('Lucky')

    def test_init(self):
        self.assertEqual(self.cat.name, 'Lucky')
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertIs(self.cat.size, 0)

    def test_size_is_increased_after_eating(self):
        new_size = self.cat.size + 1
        self.cat.eat()
        self.assertEqual(new_size, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cannot_eat_if_already_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as e:
            self.cat.eat()
        self.assertEqual('Already fed.', str(e.exception))

    def test_cannot_fall_asleep_if_not_fed(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as e:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(e.exception))

    def test_cat_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    main()
