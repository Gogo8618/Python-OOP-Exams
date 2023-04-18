from project.services.base_service import BaseService


class MainService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, capacity=30)

    def details(self):
        result = ''
        if len(self.robots) > 0:
            result += f"{self.name} Main Service:\n"
            result += f"Robots: {' '.join(self.robots)}"
        else:
            result += f"Robots: none"

        return result
