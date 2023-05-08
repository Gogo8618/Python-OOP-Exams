from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLES = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):

        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        if driving_license_number in self.users:
            raise ValueError(f"{driving_license_number} has already been registered to our platform.")
        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ['PassengerCar', 'CargoVan']:
            return f"Vehicle type {vehicle_type} is inaccessible."
        if license_plate_number in self.vehicles:
            return f"{license_plate_number} belong to another vehicle."
        self.vehicles.append(self.VALID_VEHICLES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        filtered_route = self._find_route_by_start_point_and_end_point(start_point, end_point)
        if filtered_route is not None:
            if filtered_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if filtered_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if filtered_route.length > length:
                filtered_route.is_locked = True
            new_route = self._create_route(start_point, end_point, length)
            self.routes.append(new_route)
            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int, is_accident_happened: bool):
        current_user = self._find_user_by_driving_license_number(driving_license_number)
        current_vehicle = self._find_vehicle_by_license_plate_number(license_plate_number)

        if current_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed!"
        if current_vehicle.is_damage:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed!"

    def _find_vehicle_by_license_plate_number(self, license_plate_number):
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number]
        if vehicle:
            return vehicle[0]
        return None

    def _find_user_by_driving_license_number(self, driving_license_number):
        user = [user for user in self.users if user.driving_license_number == driving_license_number]
        if user:
            return user[0]
        return None

    def _find_route_by_start_point_and_end_point(self, start_point: str, end_point: str):
        route = [route for route in self.routes if route.start_point == start_point
                 and route.end_point == end_point]
        if route:
            return route[0]
        return None

    def _create_route(self, start_point, end_point, length):
        idx = len(self.routes) + 1
        return Route(start_point, end_point, length, route_id=idx)
