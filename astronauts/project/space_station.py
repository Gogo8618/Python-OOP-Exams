from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {'Biologist': Biologist, 'Geodesist': Geodesist,
                             'Meteorologist': Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.failed_mission = 0
        self.mission_completed = 0

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type not in SpaceStation.VALID_ASTRONAUT_TYPES.keys():
            raise Exception('Astronaut type is not valid!')
        astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name]
        if astronaut:
            return f"{name} is already added."
        self.astronaut_repository.astronauts.append(SpaceStation.VALID_ASTRONAUT_TYPES[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {astronaut_type}."

    def add_planet(self, name, items):

        planet = [p for p in self.planet_repository.planets if p.name == name]
        if planet:
            return f"{name} is already added."
        self.planet_repository.planets.append(Planet(name))
        planet = [p for p in self.planet_repository.planets if p.name == name][0]
        planet.items.extend(items.split(', '))
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):

        try:
            astronaut = next(filter(lambda x: x.name == name, self.astronaut_repository.astronauts))
        except StopIteration:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.astronauts.remove(astronaut)
        return f"Astronaut {astronaut.name} was retired!"

    def recharge_oxygen(self):
        [a.increase_oxygen(10) for a in self.astronaut_repository.astronauts]

    def send_on_mission(self, planet_name):

        try:
            planet = next(filter(lambda p: p.name == planet_name, self.planet_repository.planets))
        except StopIteration:
            raise Exception("Invalid planet name!")
        astronaut_5 = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        sorted_astronaut_5 = sorted(astronaut_5, key=lambda a: -a.oxygen)

        if len(astronaut_5) == 0:
            self.failed_mission += 1
            raise Exception("You need at least one astronaut to explore the planet!")
        counter_astro = 1
        for astro in sorted_astronaut_5[:5]:

            while True:
                if astro.oxygen <= 0 or not planet.items:
                    break
                astro.backpack.append(planet.items.pop())
                astro.breathe()
                if astro.oxygen <= 0:
                    counter_astro += 1
                    astro.oxygen = 0
        if planet.items:
            self.failed_mission += 1
            return 'Mission is not completed.'
        self.mission_completed += 1
        return f'Planet: {planet.name} was explored. {counter_astro} astronauts participated in collecting items.'

    def report(self):

        result = f"{self.mission_completed} successful missions!"
        result += f"{self.failed_mission} missions were not completed!"
        result += 'Astronauts inf:\n'

        for astro in self.astronaut_repository.astronauts:
            result += str(astro)

        return result
