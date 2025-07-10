from project.animals.animal import Bird
from project.food import *

class Owl(Bird):
    INCREASE_RATE = 0.25
    EATEN_FOODS = [Meat]

    def make_sound(self):
        return 'Hoot Hoot'



class Hen(Bird):
    INCREASE_RATE = 0.35
    EATEN_FOODS = [Meat, Seed, Vegetable, Fruit]

    def make_sound(self):
        return 'Cluck'

