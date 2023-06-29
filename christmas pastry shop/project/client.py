class Client:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.client_ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value[0] != '0' and len(value) < 10 and not value.is_digit():
            raise ValueError("invalid phone number!")
        self.__phone_number = value

