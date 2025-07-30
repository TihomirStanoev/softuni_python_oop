from project.clients.base_client import BaseClient


class BusinessClient(BaseClient):
    def update_discount(self):
        self.discount = 10.0 if self.total_orders >= 2 else 0.0