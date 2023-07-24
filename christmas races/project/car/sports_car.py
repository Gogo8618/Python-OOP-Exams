from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED_LIMIT = 400
    MAX_SPEED_LIMIT = 600

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not SportsCar.MIN_SPEED_LIMIT < value < SportsCar.MAX_SPEED_LIMIT:
            raise ValueError(
                f"Invalid speed limit! Must be between {SportsCar.MIN_SPEED_LIMIT} and {SportsCar.MAX_SPEED_LIMIT}!")
        self.__speed_limit = value
