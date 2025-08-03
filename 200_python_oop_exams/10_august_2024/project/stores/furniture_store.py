from project.stores.base_store import BaseStore
from collections import defaultdict

class FurnitureStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=50)

    def store_type(self):
        return type(self).__name__

    def store_stats(self):
        result = [f'Store: {self.name}, location: {self.location}, available capacity: {self.capacity}',
                  self.get_estimated_profit(),
                  '**Furniture for sale:']


        available_furniture = defaultdict(lambda: {'count': 0, 'total_price': 0.0})

        for product in self.products:
            available_furniture[product.model]['count'] += 1
            available_furniture[product.model]['total_price'] += product.price

        for model, info in sorted(available_furniture.items()):
            num_of_product_pieces = info['count']
            avg_price_per_model = info['total_price'] / num_of_product_pieces
            result.append(f'{model}: {num_of_product_pieces}pcs, average price: {avg_price_per_model:.2f}')

        return '\n'.join(result).strip()
