class User:
    INCREASE = 0.5
    DECREASE = 2.0

    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value.strip():
            raise ValueError("First name cannot be empty!")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value.strip():
            raise ValueError("Last name cannot be empty!")
        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if not value.strip():
            raise ValueError("Driving license number is required!")
        self.__driving_license_number = value

    def increase_rating(self):
        if self.rating + self.INCREASE > 10:
            self.rating = 10
        self.rating += self.INCREASE

    def decrease_rating(self):
        if self.rating - self.DECREASE < 0:
            self.rating = 0
        self.rating -= self.DECREASE

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} " \
               f"Rating: {self.rating}"

