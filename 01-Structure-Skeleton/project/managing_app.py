from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    valid_types_vehicles = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):

        self.users = []
        self.vehicles = []
        self.routes = []

    def _find_route_by_route_id(self, route_id):
        for route in self.routes:
            if route.route_id == route_id:
                return route[0]
            return None

    def _find_user_by_driver_license_number(self, number):
        for user in self.users:
            if user.driving_license_number == number:
                return user[0]
            return None

    def _find_vehicle_by_license_plate_number(self, number):

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == number:
                return vehicle[0]
            return None

    def _find_route_with_start_point_and_end_point(self, s_point, e_point):

        route_obj = [route for route in self.routes if route.start_point == s_point and route.end_point == e_point]

        if route_obj:
            return route_obj[0]
        return None

    def register_user(self, first_name, last_name, driving_license_number):

        user_obj = self._find_user_by_driver_license_number(driving_license_number)
        if user_obj is not None:
            return f"{driving_license_number} has already been registered to pur platform."
        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type, brand, model, license_plate_number):

        if vehicle_type not in ['PassengerCar', 'CargoVan']:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle_obj = self._find_vehicle_by_license_plate_number(license_plate_number)
        if vehicle_obj is not None:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.valid_types_vehicles[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point, end_point, length):

        route = self._find_route_with_start_point_and_end_point(start_point, end_point)

        if route is not None:

            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.length > length:
                route.is_locked = True
        idx = len(self.routes) + 1
        self.routes.append(Route(start_point, end_point, length, route_id=idx))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number, license_plate_number, route_id, is_accident_happened):

        user = self._find_user_by_driver_license_number(driving_license_number)
        vehicle = self._find_vehicle_by_license_plate_number(license_plate_number)
        route = self._find_route_by_route_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.lenght)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        selected_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))[:count]

        for vehicle in selected_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()
        return f"{len(selected_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["***E-Drive-Rent***"]
        sorted_users = sorted(self.users, key=lambda user: -user.rating)
        result.append('\n'.join(str(user) for user in sorted_users))
        return '\n'.join(result)




