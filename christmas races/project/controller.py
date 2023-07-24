from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}

    def __init__(self):

        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):

        car = [c for c in self.cars if c.model == model]
        if car:
            raise Exception(f"Car {model} is already created!")
        if car_type in ['MuscleCar', 'SportsCar']:
            self.cars.append(Controller.VALID_CAR_TYPES[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):

        driver = [d for d in self.drivers if d.name == driver_name]

        if driver:
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created!"

    def create_race(self, race_name):

        race = [r for r in self.races if r.name == race_name]

        if race:
            raise Exception(f"Race {race_name} is already already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):

        try:
            driver = next(filter(lambda x: x.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")
        try:
            car = next(filter(lambda x: x.__class__.__name__ == car_type and not x.is_taken, self.cars))[::-1]
        except StopIteration:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car
            driver.car = car.model
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."
        driver.car = car.model
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        try:
            race = next(filter(lambda x: x.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")
        try:
            driver = next(filter(lambda x: x.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        for driver in race.drivers:
            if driver.name == driver_name:
                return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):

        try:
            race = next(filter(lambda x: x.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        fastest_cars = {}
        for i in range(0, 3):
            max1 = 0
            for driver in race.drivers:
                if driver.car.speed_limit > max1:
                    fastest_cars[driver] = driver.car.speed_limit
                    driver.number_of_wins += 1
        sorted_cars = sorted(fastest_cars.items(), key=lambda x: (-x[1], x[0]))
        dict_sorted_cars = dict(sorted_cars)
        for key, value in dict_sorted_cars.items():
            return f"Driver {key} wins the {race_name} race with a speed of {value}."


