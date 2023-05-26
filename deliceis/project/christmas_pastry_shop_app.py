from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_TYPE_DELICACY = {'Gingerbread': Gingerbread, 'Stolen': Stolen}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        delicacy_obj = self._find_delicacy_by_name(name, self.delicacies)
        if delicacy_obj:
            raise Exception(f"{name} already exist!")
        if type_delicacy not in self.VALID_TYPE_DELICACY:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        self.delicacies.append(self.VALID_TYPE_DELICACY[type_delicacy](name, price))
        return f"Added {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth_obj = self._find_booth_by_number(booth_number, self.booths)
        if booth_obj:
            raise Exception(f"Booth number {booth_number} already exist!")
        if type_booth == 'Open Booth':
            booth = OpenBooth(booth_number, capacity)
        elif type_booth == 'Private Booth':
            booth = PrivateBooth(booth_number, capacity)
        else:
            raise Exception(f"{type_booth} is not a valid booth!")
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth_obj in self.booths:
            if booth_obj.capacity >= number_of_people and not booth_obj.is_reserved:
                booth_obj.reserve(number_of_people)
                return f'Booth {booth_obj.booth_number} has been reserved for {number_of_people} people!'
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self,booth_number: int, delicacy_name: str):
        booth_obj = self._find_booth_by_number(booth_number, self.booths)
        delicacy_obj = self._find_delicacy_by_name(delicacy_name, self.delicacies)
        if booth_obj is None:
            raise Exception(f"Could not find booth {booth_number}!")
        if delicacy_obj is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth_obj.delicacy_orders.append(delicacy_obj)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth_obj = self._find_booth_by_number(booth_number, self.booths)
        bill = booth_obj.get_bill()
        self.income += bill
        booth_obj.delicacy_orders = []
        booth_obj.is_reserved = False
        booth_obj.price_for_reservation = 0
        return f"Booth: {booth_number}\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."








    def _find_booth_by_number(self, number, collection):
        booth = [b for b in collection if b.number == number]
        if not booth:
            return None
        return booth[0]


    def _find_delicacy_by_name(self, name, collection):

        delicacy = [d for d in collection if d.name == name]

        if not delicacy:
            return None
        return delicacy[0]
