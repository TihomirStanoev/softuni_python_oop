from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name=name, age=age, gender='Female')

    @staticmethod
    def make_sound():
        return 'Meow'