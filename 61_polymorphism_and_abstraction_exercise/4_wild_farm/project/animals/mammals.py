from project.animals.animal import Mammal
from project.food import *

class Mouse(Mammal):
    INCREASE_RATE = 0.10
    EATEN_FOODS = [Vegetable, Fruit]

    def make_sound(self):
        return 'Squeak'

class Dog(Mammal):
    INCREASE_RATE = 0.4
    EATEN_FOODS = [Meat]
    def make_sound(self):
        return 'Woof!'

class Cat(Mammal):
    INCREASE_RATE = 0.3
    EATEN_FOODS = [Vegetable, Meat]
    def make_sound(self):
        return 'Meow'

class Tiger(Mammal):
    INCREASE_RATE = 1.00
    EATEN_FOODS = [Meat]
    def make_sound(self):
        return 'ROAR!!!'
