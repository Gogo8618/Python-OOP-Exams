class User:
    INCREASE_NUM = 0.5
    DECREASE_NUM = 2.0

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
        if value.strip() == '':
            raise ValueError("First name cannot be be empty!")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value.strip():
            raise ValueError("Last name cannot be be empty!")
        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if not value.strip():
            raise ValueError("Driving license number is required!")
        self.__driving_license_number = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Users rating cannot be negative!")
        self.__rating = value

    def increase(self):
        self.rating += self.INCREASE_NUM
        if self.rating > 10:
            self.rating = 10

    def decrease(self):
        self.rating -= self.DECREASE_NUM
        if self.rating < 0:
            self.rating = 0
            self.is_blocked = True

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} " \
               f"Rating: {self.rating}"
