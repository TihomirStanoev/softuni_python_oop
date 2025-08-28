from project.meals.meal import Meal
from project.client import Client

class FoodOrdersApp:
    VALID_MEALS = {'Starter', 'MainDish', 'Dessert'}
    def __init__(self):
        self.menu: list[Meal]= []
        self.clients_list: list[Client] = []

    def _find_client_by_number(self,client_phone_number ):
        return next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

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



