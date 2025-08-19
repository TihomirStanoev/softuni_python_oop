from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService




class RobotsManagingApp:
    VALID_SERVICES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    VALID_ROBOTS = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}
    SERVICE_MAPPER = {MaleRobot: MainService, FemaleRobot: SecondaryService}
    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []

    @staticmethod
    def _find_robot_by_name(robot_name, collection) -> BaseRobot | None:
        return next((r for r in collection if r.name == robot_name), None)

    def _find_service_by_name(self, service_name) -> BaseService | None:
        return next((s for s in self.services if s.name == service_name), None)

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES.keys():
            raise Exception('Invalid service type!')

        service = self.VALID_SERVICES[service_type](name)
        self.services.append(service)
        return f'{service_type} is successfully added.'

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS.keys():
            raise Exception('Invalid robot type!')

        robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)
        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._find_robot_by_name(robot_name, self.robots)
        service = self._find_service_by_name(service_name)

        if not self.SERVICE_MAPPER[type(robot)] == type(service):
            return 'Unsuitable service.'
        if service.capacity <= len(service.robots):
            raise Exception('Not enough capacity for this robot!')

        self.robots.remove(robot)
        service.robots.append(robot)

        return f'Successfully added {robot_name} to {service_name}.'

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._find_service_by_name(service_name)
        robot = self._find_robot_by_name(robot_name, service.robots)

        if robot is None:
            raise Exception('No such robot in this service!')

        service.robots.remove(robot)
        self.robots.append(robot)
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name: str):
        service = self._find_service_by_name(service_name)

        for robot in service.robots:
            robot.eating()

        return f'Robots fed: {len(service.robots)}.'

    def service_price(self, service_name: str):
        service = self._find_service_by_name(service_name)
        total_price = sum(r.price for r in service.robots)

        return f'The value of service {service_name} is {total_price:.2f}.'

    def __str__(self):
        return '\n'.join(service.details() for service in self.services).strip()




