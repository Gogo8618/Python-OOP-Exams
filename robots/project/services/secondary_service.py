from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, capacity=15)

    def details(self):
        result = ''
        if len(self.robots) > 0:
            result += f"{self.name} Main Service:\n"
            result += f"Robots: {' '.join([r.name for r in self.robots])}"
        else:
            result += f"Robots: none"

        return result
