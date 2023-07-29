from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    UNITS_OF_OXYGEN = 90

    def __init__(self, name):
        super().__init__(name, oxygen=Meteorologist.UNITS_OF_OXYGEN)

    def breathe(self):
        self.oxygen -= 15



