from abc import ABC, abstractstaticmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractstaticmethod
    def make_sound():
        pass


    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}'

