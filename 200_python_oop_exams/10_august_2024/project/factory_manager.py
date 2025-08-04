from collections import defaultdict

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore

SELL_PRODUCTS = {
    'FurnitureStore': 'Furniture',
    'ToyStore': 'Toys'
}


class FactoryManager:
    _VALID_PRODUCTS = {
        'Chair' : Chair,
        'HobbyHorse': HobbyHorse
    }
    _VALID_STORES = {
        'FurnitureStore': FurnitureStore,
        'ToyStore': ToyStore
    }
    def __init__(self, name):
        self.name = name
        self.income:float = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def _get_store_by_name(self, store_name):
        return next((s for s in self.stores if s.name == store_name), None)


    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self._VALID_PRODUCTS.keys():
            raise Exception('Invalid product type!')
        product = self._VALID_PRODUCTS[product_type](model, price)
        self.products.append(product)
        return f'A product of sub-type {product.sub_type} was produced.'

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self._VALID_STORES.keys():
            raise Exception(f'{store_type} is an invalid type of store!')
        store = self._VALID_STORES[store_type](name, location)
        self.stores.append(store)
        return f'A new {store_type} was successfully registered.'

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f'Store {store.name} has no capacity for this purchase.'

        sell_products = [product for product in products if SELL_PRODUCTS[store.store_type] == product.sub_type and product in self.products]
        total_products = len(sell_products)
        total_price = sum(p.price for p in sell_products)

        if not sell_products:
            return 'Products do not match in type. Nothing sold.'

        for product in sell_products:
                self.products.remove(product)

        self.income += total_price
        store.capacity -= total_products
        store.products.extend(sell_products)

        return f'Store {store.name} successfully purchased {total_products} items.'

    def unregister_store(self, store_name: str):
        store = self._get_store_by_name(store_name)

        if store is None:
            raise Exception('No such store!')

        if store.products:
            return 'The store is still having products in stock! Unregistering is inadvisable.'

        self.stores.remove(store)
        return f'Successfully unregistered store {store.name}, location: {store.location}.'

    def discount_products(self, product_model: str):
        products_count = 0
        for product in self.products:
            if product.model == product_model:
                product.discount()
                products_count += 1

        return f'Discount applied to {products_count} products with model: {product_model}'

    def request_store_stats(self, store_name: str):
        store = self._get_store_by_name(store_name)
        if store is None:
            return 'There is no store registered under this name!'
        return store.store_stats()

    def statistics(self):
        count_by_product = defaultdict(int)
        for product in self.products:
            count_by_product[product.model] += 1


        result = [f'Factory: {self.name}', f'Income: {self.income:.2f}',
                  '***Products Statistics***',
                  f'Unsold Products: {len(self.products)}. '
                  f'Total net price: {sum(p.price for p in self.products):.2f}',
                  '\n'.join(f'{p}: {v}' for p, v in sorted(count_by_product.items(), key=lambda pv: pv[0])),
                  f'***Partner Stores: {len(self.stores)}***',
                  '\n'.join(s.name for s in sorted(self.stores, key=lambda s: s.name))]

        return '\n'.join(result).strip()
