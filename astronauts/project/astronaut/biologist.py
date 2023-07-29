from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    UNITS_OF_OXYGEN = 70

    def __init__(self, name):
        super().__init__(name, oxygen=Biologist.UNITS_OF_OXYGEN)

    def breathe(self):
        self.oxygen -= 5


