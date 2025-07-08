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

    @staticmethod
    def _find_rented_dvd(dvd_list, dvd_id):
        for dvd in dvd_list:
            if dvd.is_rented and dvd.id == dvd_id:
                return dvd
        else:
            return None


    def rent_dvd(self, customer_id, dvd_id):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        if not customer:
            return


        dvd = MovieWorld._find_rented_dvd(customer.rented_dvds, dvd_id)
        if dvd:
            return f'{customer.name} has already rented {dvd.name}'

        dvd_from_rent = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)

        if not dvd_from_rent:
            return

        if MovieWorld._find_rented_dvd(self.dvds, dvd_id):
            return 'DVD is already rented'


        if dvd_from_rent.age_restriction > customer.age:
            return f'{customer.name} should be at least {dvd_from_rent.age_restriction} to rent this movie'

        dvd_from_rent.is_rented = True
        customer.rented_dvds.append(dvd_from_rent)

        return f'{customer.name} has successfully rented {dvd_from_rent.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        if not customer:
            return

        dvd = next((d for d in customer.rented_dvds if d.id == dvd_id), None)

        if dvd:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}'

        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        customer_info = '\n'.join(str(customer) for customer in self.customers)
        dvd_info = '\n'.join(str(dvd) for dvd in self.dvds)
        return f'{customer_info}\n{dvd_info}'