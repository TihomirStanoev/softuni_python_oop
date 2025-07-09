from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10
    def __init__(self, name):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds:list[DVD]  = []


    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY


    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY


    def add_customer(self, customer):
        if customer in self.customers:
            return
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)


    def add_dvd(self, dvd):
        if dvd in self.dvds:
            return
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)


    def _find_by_id(self, collection, item_id):
        return next((item for item in collection if item.id == item_id), None)


    def rent_dvd(self, customer_id, dvd_id):
        customer = self._find_by_id(self.customers, customer_id)
        dvd = self._find_by_id(self.dvds, dvd_id)

        if not customer or not dvd:
            return
        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'
        if dvd.age_restriction > customer.age:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f'{customer.name} has successfully rented {dvd.name}'


    def return_dvd(self, customer_id, dvd_id):
        customer = self._find_by_id(self.customers, customer_id)

        if not customer:
            return

        dvd = self._find_by_id(customer.rented_dvds, dvd_id)
        if dvd:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}'
        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        customer_info = '\n'.join(str(customer) for customer in self.customers)
        dvd_info = '\n'.join(str(dvd) for dvd in self.dvds)
        return f'{customer_info}\n{dvd_info}'