from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    valid_services = {'MainService': MainService, 'SecondaryService': SecondaryService}
    valid_robots = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.valid_services:
            raise Exception("Invalid service type!")
        self.services.append(self.valid_services[service_type](name))

    def add_robot(self, robot_type: str, kind: str, price: float):

        if robot_type not in self.valid_robots:
            raise Exception("Invalid robot type!")
        self.robots.append(self.valid_robots[robot_type](kind, price))

    def add_robot_to_service(self, robot_name: str, service_name: str):
        obj_name = next(filter(lambda x: x.name == robot_name, self.robots))
        obj_services = next(filter(lambda x: x.name == service_name, self.services))

        if obj_name.possible_service != obj_services.__class__.__name__:
            return "Unsuitable service."
        if len(obj_services.robots) >= obj_services.capacity:
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(obj_name)
        obj_services.robots.append(obj_name)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        services = next(filter(lambda s: s.name == service_name, self.services))
        try:
            robot = next(filter(lambda r: r.name == robot_name, services.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")

        services.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}"

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        [r.details() for r in service.robots]
        return f"Robots fed: {len(service.robots)}"

    def service_price(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))
        total_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_price}"

    def __str__(self):
        return "\n".join([s.details() for s in self.services])
