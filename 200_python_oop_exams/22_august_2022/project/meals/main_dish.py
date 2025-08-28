from project.meals.meal import Meal


class MainDish(Meal):
    QUANTITY = 50
    def __init__(self, name: str, price: float, quantity: int = QUANTITY):
        super().__init__(name, price, quantity=quantity)

    @property
    def type_of_meal(self):
        return 'Main Dish'

    def details(self):
        return f'{self.type_of_meal} {self.name}: {self.price:.2f}lv/piece'

