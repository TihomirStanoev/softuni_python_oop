from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.route import Route
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}
    def __init__(self):
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []
        self.routes: list[Route] = []

    def _find_user_driving_license_number(self, driving_license_number):
        return next((u for u in self.users if u.driving_license_number == driving_license_number), None)

    def _find_vehicle_by_license_number(self, license_plate_number):
        return next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)

    def _find_route_by_id(self, route_id):
        return next((r for r in self.routes if r.route_id == route_id), None)

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self._find_user_driving_license_number(driving_license_number)

        if user:
            return f'{driving_license_number} has already been registered to our platform.'

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)

        return f'{first_name} {last_name} was successfully registered under DLN-{driving_license_number}'

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE.keys():
            return f'Vehicle type {vehicle_type} is inaccessible.'

        vehicle = self._find_vehicle_by_license_number(license_plate_number)
        if vehicle:
            return f'{license_plate_number} belongs to another vehicle.'

        vehicle = self.VALID_VEHICLE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f'{brand} {model} was successfully uploaded with LPN-{license_plate_number}.'

    def repair_vehicles(self, count: int):
        vehicles_count = 0
        for vehicle in sorted(self.vehicles, key=lambda v: (v.brand, v.model)):
            if vehicles_count == count:
                break
            if vehicle.is_damaged:
                vehicle.change_status()
                vehicle.recharge()
                vehicles_count += 1

        return f'{vehicles_count} vehicles were successfully repaired!'

    def allow_route(self, start_point: str, end_point: str, length: float):
        routes = [r for r in self.routes if r.end_point == end_point and r.start_point == start_point]

        if routes:
            for r in sorted(routes, key=lambda l: -l.length):
                if r.length == length:
                    return f'{start_point}/{end_point} - {length} km had already been added to our platform.'
                if r.length < length:
                    return f'{start_point}/{end_point} shorter route had already been added to our platform.'
                if r.length > length:
                    r.lock_the_route()
                    break

        route_index = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_index)
        self.routes.append(route)

        return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self._find_user_driving_license_number(driving_license_number)
        if user.is_blocked:
            return f'User {driving_license_number} is blocked in the platform! This trip is not allowed.'
        vehicle = self._find_vehicle_by_license_number(license_plate_number)
        if vehicle.is_damaged:
            return f'Vehicle {license_plate_number} is damaged! This trip is not allowed.'
        route = self._find_route_by_id(route_id)
        if route.is_locked:
            return f'Route {route_id} is locked! This trip is not allowed.'

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return (f'{vehicle.brand} {vehicle.model} License plate: {vehicle.license_plate_number}'
                f' Battery: {vehicle.battery_level:.0f}% Status: {"Damaged" if vehicle.is_damaged else "OK"}')

    def users_report(self):
        result = ['*** E-Drive-Rent ***']

        for user in sorted(self.users, key=lambda u: u.rating, reverse=True):
            result.append(str(user))

        return '\n'.join(result)
