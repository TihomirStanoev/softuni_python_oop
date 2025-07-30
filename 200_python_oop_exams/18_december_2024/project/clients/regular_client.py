from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def update_discount(self):
        self.discount = 0.0 if self.total_orders == 0 else 5.0
