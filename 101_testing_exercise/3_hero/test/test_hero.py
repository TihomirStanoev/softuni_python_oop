from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    USERNAME = 'Hero'
    LEVEL = 1
    HEALTH = 99.50
    DAMAGE = 60.2
    def setUp(self):
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        self.enemy_hero = Hero('Enemy', 1, 99.9, 12.3)
        self.weakest_hero = Hero('Weakest', 1, 0.1, 0.1)
        self.power_hero = Hero('Power', 20, 500.5, 500.5)


    def test_instance_creation(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)


    def test_attribute_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)
        self.assertIsInstance(self.hero.level, int)


    def test_battle_with_self(self):
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.hero)
        expected_message = "You cannot fight yourself"
        self.assertEqual(expected_message, str(e.exception))


    def test_battle_fails_if_hero_health_is_zero_or_negative(self):
        health_values = [0,-15]
        for health in health_values:
            with self.subTest(health=health):
                self.hero.health = health
                with self.assertRaises(ValueError) as e:
                    self.hero.battle(self.enemy_hero)

                expected_message = "Your health is lower than or equal to 0. You need to rest"
                self.assertEqual(expected_message, str(e.exception))


    def test_battle_fails_if_enemy_health_is_zero_or_negative(self):
        health_values = [0, -15]
        for health in health_values:
            with self.subTest(health=health):
                self.enemy_hero.health = health
                with self.assertRaises(ValueError) as e:
                    self.hero.battle(self.enemy_hero)

                expected_message = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
                self.assertEqual(expected_message, str(e.exception))


    def test_battle_win_incenses(self):
        result = self.hero.battle(self.weakest_hero)
        winning_string = 'You win'
        increased_level = self.LEVEL + 1
        increased_health = self.HEALTH + 5 - (self.weakest_hero.damage * self.weakest_hero.level)
        increased_damage = self.DAMAGE + 5

        self.assertEqual(self.hero.level, increased_level)
        self.assertEqual(self.hero.health, increased_health)
        self.assertEqual(self.hero.damage, increased_damage)
        self.assertEqual(winning_string, result)


    def test_battle_draw(self):
        draw_sting = 'Draw'
        minimum_health = 0.1
        self.enemy_hero.health = minimum_health
        self.hero.health = minimum_health
        self.enemy_hero.damage = self.hero.damage
        self.enemy_hero.level = self.hero.level
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(draw_sting, result)
        self.assertLessEqual(self.hero.health, 0)
        self.assertLessEqual(self.enemy_hero.health, 0)


    def test_battle_lose(self):
        self.hero.damage = 1
        enemy_increased_level = self.power_hero.level + 1
        enemy_increased_damage = self.power_hero.damage + 5
        enemy_increased_health = self.power_hero.health+ 5- (self.hero.damage * self.hero.level)
        result = self.hero.battle(self.power_hero)
        lose_string = 'You lose'

        self.assertEqual(result, lose_string)
        self.assertEqual(enemy_increased_level, self.power_hero.level)
        self.assertEqual(enemy_increased_damage, self.power_hero.damage)
        self.assertEqual(enemy_increased_health, self.power_hero.health)


    def test_string(self):
        result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
        f"Health: {self.hero.health}\n" \
        f"Damage: {self.hero.damage}\n"

        self.assertEqual(result, str(self.hero))



if __name__ == '__main__':
    main()

