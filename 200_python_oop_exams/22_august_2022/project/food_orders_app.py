from collections import defaultdict

from project.meals.meal import Meal
from project.client import Client

class FoodOrdersApp:
    VALID_MEALS = {'Starter', 'MainDish', 'Dessert'}
    MIN_MEALS = 5
    def __init__(self):
        self.menu: list[Meal]= []
        self.clients_list: list[Client] = []
        self._receipt_id = 0

    def _find_client_by_number(self,client_phone_number ):
        return next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

    def _find_meal_by_name(self, meal_name):
        return next((m for m in self.menu if m.name == meal_name), None)


    def register_client(self, client_phone_number: str):
        client = self._find_client_by_number(client_phone_number)
        if client:
            raise Exception('The client has already been registered!')

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, Meal) and type(meal).__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < self.MIN_MEALS:
            raise Exception('The menu is not ready!')
        result = []
        for meal in self.menu:
            result.append(meal.details())

        return '\n'.join(result)


    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < self.MIN_MEALS:
            raise Exception('The menu is not ready!')

        client = self._find_client_by_number(client_phone_number)
        if client is None:
            self.register_client(client_phone_number)
            client = self._find_client_by_number(client_phone_number)

        ordered_meals = dict()
        for ordered_meal, quantity in meal_names_and_quantities.items():
            meal = self._find_meal_by_name(ordered_meal)
            if meal is None:
                raise Exception(f'{ordered_meal} is not on the menu!')
            if meal.quantity < quantity:
                raise Exception(f'Not enough quantity of {type(meal).__name__}: {meal.name}!')
            ordered_meals[ordered_meal] = meal


        for meal_name, quantity in meal_names_and_quantities.items():
            meal = ordered_meals[meal_name]
            meal.quantity -= quantity
            # if meal.quantity == 0:
            #     self.menu.remove(meal)
            ordered_meal = type(meal)(meal_name, meal.price, quantity)
            client.shopping_cart.append(ordered_meal)
            client.bill += ordered_meal.price * quantity

        meal_names = ', '.join(m.name for m in client.shopping_cart)
        return f'Client {client.phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv.'


    def cancel_order(self, client_phone_number: str):
        client = self._find_client_by_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        for client_meal in client.shopping_cart:
            meal = self._find_meal_by_name(client_meal.name)
            # if meal:
            meal.quantity += client_meal.quantity
            # else:
            #     self.menu.append(client_meal)

        client.clear_card()

        return f'Client {client_phone_number} successfully canceled his order.'


    def finish_order(self, client_phone_number: str):
        client = self._find_client_by_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        total_paid_money = client.bill
        client.clear_card()
        self._receipt_id += 1

        return f'Receipt #{self._receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}.'

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'

