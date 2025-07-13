from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.subscriptions: list[Subscription] = []
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []

    def _add_item(self, items, item):
        if item not in items:
            items.append(item)

    def add_customer(self, customer: Customer):
        self._add_item(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        self._add_item(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        self._add_item(self.equipment, equipment)

    def add_subscription(self, subscription: Subscription):
        self._add_item(self.subscriptions, subscription)

    def add_plan(self, plan: ExercisePlan):
        self._add_item(self.plans, plan)


    def subscription_info(self, subscription_id: int):
        result = [f'{gym_item[subscription_id-1]}' for gym_item in self.__dict__.values()]
        return '\n'.join(result)


