from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    possible_service = 'MainService'

    def __init__(self, name: str, kind: str, price: float, weight: int):
        super().__init__(name, kind, price, weight=9)

    def eating(self):
        self.weight += 3