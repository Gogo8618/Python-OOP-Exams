from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    UNITS_OF_OXYGEN = 50

    def __init__(self, name):
        super().__init__(name, oxygen=Geodesist.UNITS_OF_OXYGEN)

    def breathe(self):
        self.oxygen -= 10


