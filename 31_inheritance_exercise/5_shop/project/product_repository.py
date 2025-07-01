class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self,product):
        self.products.append(product)

    def find(self,product_name):
        product = self.search_product(product_name)

        if product:
            return product
        return None

    def remove(self, product_name):
        product = self.search_product(product_name)

        if product:
            self.products.remove(product)
        return None

    def search_product(self, product_name):
        return next((product_object for product_object in self.products if product_object.name == product_name),None)

    def __repr__(self):
        return '\n'.join(f'{product.name}: {product.quantity}' for product in self.products)