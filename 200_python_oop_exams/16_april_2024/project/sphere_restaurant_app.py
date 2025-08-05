from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    _VALID_WAITERS = {
        'FullTimeWaiter': FullTimeWaiter,
        'HalfTimeWaiter': HalfTimeWaiter
    }
    _VALID_CLIENTS = {
        'RegularClient': RegularClient,
        'VIPClient': VIPClient
    }
    def __init__(self):
        self.waiters: list[BaseWaiter] = []
        self.clients: list[BaseClient] = []

    @staticmethod
    def _find_by_name(collection, name):
        return next((n for n in collection if n.name == name), None)

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self._VALID_WAITERS.keys():
            return f'{waiter_type} is not a recognized waiter type.'

        waiter = self._find_by_name(self.waiters, waiter_name)
        if waiter is not None:
            return f'{waiter_name} is already on the staff.'

        waiter = self._VALID_WAITERS[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)

        return f'{waiter_name} is successfully hired as a {waiter_type}.'

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self._VALID_CLIENTS.keys():
            return f'{client_type} is not a recognized client type.'

        client = self._find_by_name(self.clients, client_name)
        if client is not None:
            return f'{client_name} is already a client.'

        client = self._VALID_CLIENTS[client_type](client_name)
        self.clients.append(client)

        return f'{client_name} is successfully admitted as a {client_type}.'

    def process_shifts(self, waiter_name: str):
        waiter = self._find_by_name(self.waiters, waiter_name)
        if waiter is None:
            return f'No waiter found with the name {waiter_name}.'

        report = waiter.report_shift()
        return report

    def process_client_order(self, client_name: str, order_amount: float):
        client = self._find_by_name(self.clients, client_name)
        if client is None:
            return f'{client_name} is not a registered client.'

        points_earned = client.earning_points(order_amount)
        return f'{client_name} earned {int(points_earned)} points from the order.'

    def apply_discount_to_client(self, client_name: str):
        client:BaseClient = self._find_by_name(self.clients, client_name)
        if client is None:
            return f'{client_name} cannot get a discount because this client is not admitted!'

        discount_percentage, remaining_points = client.apply_discount()
        return f'{client_name} received a {discount_percentage}% discount. Remaining points {int(remaining_points)}'

    def generate_report(self):
        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_client_points = sum(c.points for c in self.clients)
        clients_count = len(self.clients)
        waiter_info = []

        for waiter in sorted(self.waiters, key=lambda w: -w.calculate_earnings()):
            waiter_info.append(f'Name: {waiter.name}, Total earnings: ${waiter.calculate_earnings():.2f}')

        result = ['$$ Monthly Report $$',
                  f'Total Earnings: ${total_earnings:.2f}',
                  f'Total Clients Unused Points: {int(total_client_points)}',
                  f'Total Clients Count: {clients_count}',
                  '** Waiter Details **',
                  *waiter_info]

        return '\n'.join(result).strip()

