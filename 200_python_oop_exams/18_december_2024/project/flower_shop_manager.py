from project.plants.base_plant import BasePlant
from project.clients.base_client import BaseClient
from project.plants.leaf_plant import LeafPlant
from project.plants.flower import Flower
from project.clients.regular_client import RegularClient
from project.clients.business_client import BusinessClient

class FlowerShopManager:
    _VALID_PLANTS = {"Flower": Flower, "LeafPlant": LeafPlant}
    _VALID_CLIENTS = {"RegularClient": RegularClient, "BusinessClient":BusinessClient}
    def __init__(self):
        self.income:float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def _find_client(self,clients, number) -> None | BaseClient:
        return next((c for c in clients if c.phone_number == number), None)

    def _find_plant(self,plants,  plant_name) -> None | BasePlant:
        return next((p for p in plants if p.name == plant_name), None)

    def add_plant(self,plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self._VALID_PLANTS.keys():
            raise ValueError('Unknown plant type!')
        plant = self._VALID_PLANTS[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)

        return f'{plant_name} is added to the shop as {plant_type}.'

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self._VALID_CLIENTS.keys():
            raise ValueError('Unknown client type!')

        client = self._find_client(self.clients, client_phone_number)
        if client:
            raise ValueError('This phone number has been used!')
        client = self._VALID_CLIENTS[client_type](client_name, client_phone_number)
        self.clients.append(client)

        return f'{client_name} is successfully added as a {client_type}.'


    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = self._find_client(self.clients, client_phone_number)
        if not client:
            raise ValueError('Client not found!')

        plant = self._find_plant(self.plants, plant_name)
        if not plant:
            raise ValueError('Plants not found!')

        plants_stock = sum(1 for p in self.plants if p.name == plant_name)
        if plants_stock < plant_quantity:
            return "Not enough plant quantity."

        plants_for_sell = []
        plants_in_store = []
        counter = 0
        order_amount = 0

        for plant in self.plants:
            if plant.name == plant_name and counter < plant_quantity:
                plants_for_sell.append(plant)
                counter += 1
                order_amount += plant.price
            else:
                plants_in_store.append(plant)
        self.plants = plants_in_store

        order_amount *= (1 - (client.discount / 100))
        self.income += order_amount
        client.update_total_orders()
        client.update_discount()

        return f'{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}'

    def remove_plant(self, plant_name: str):
        plant = self._find_plant(self.plants, plant_name)
        if plant is None:
            return "No such plant name."
        self.plants.remove(plant)
        return f'Removed {plant.plant_details()}'

    def remove_clients(self):
        new_client_list = [client for client in self.clients if client.total_orders > 0]
        count = len(self.clients) - len(new_client_list)
        self.clients = new_client_list

        return f'{count} client/s removed.'


    def shop_report(self):
        result = ['~Flower Shop Report~',f'Income: {self.income:.2f}']
        total_orders = sum(c.total_orders for c in self.clients)
        result.append(f'Count of orders: {total_orders}')

        unsold_plants = {}
        unsold_plants_count = 0
        for plant in self.plants:
            if plant.name not in unsold_plants.keys():
                unsold_plants[plant.name] = 0
            unsold_plants[plant.name] += 1
            unsold_plants_count += 1

        result.append(f'~~Unsold plants: {unsold_plants_count}~~')


        for plant, count in sorted(unsold_plants.items(), key=lambda kv: (-kv[1],kv[0])):
            result.append(f'{plant}: {count}')

        client_count = len(self.clients)
        result.append(f'~~Clients number: {client_count}~~')

        sorted_clents = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        for client in sorted_clents:
            result.append(client.client_details())




        return '\n'.join(result).strip()










