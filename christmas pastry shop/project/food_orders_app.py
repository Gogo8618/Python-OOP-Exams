from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:

    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number):
        if self._find_client_by_phone_number(client_phone_number):
            raise Exception("The client has already been registered!")
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):

        for meal in meals:
            if type(meal).__name__ in ['Starter', 'MainDish', 'Dessert']:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        details_menu = []
        for meal in self.menu:
            details_menu.append(meal.details())
        return '\n'.join(details_menu)

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        client_obj = self._find_client_by_phone_number(client_phone_number)
        if client_obj is None:
            self.clients_list.append(Client(client_phone_number))
        meals_ordered = []
        current_bill = 0
        for meal_name, meal_quantities in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantities:
                        meals_ordered.append(meal)
                        current_bill += meal.price * meal_quantities
                        break
                    raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            raise Exception(f"{meal_name} is not in the menu!")
        client_obj.shopping_cart.extend(meals_ordered)
        client_obj.bill += current_bill
        for meal_name, meal_quantities in meal_names_and_quantities.items():
            if meal_name not in client_obj.client_ordered_meals:
                client_obj.client_ordered_meals[meal_name] = 0
            client_obj.client_ordered_meals[meal_name] += meal_quantities
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantities
        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(meal.name for meal in client_obj.shopping_cart)} for {client_obj.bill:.2f}lv."

    def cancel_order(self, client_phone_number):

        client = self._find_client_by_phone_number(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        for meal, quantity in client.client_ordered_meals.items():
            for meal_menu in self.menu:
                if meal == meal_menu.name:
                    meal_menu.quantity += quantity
        client.shopping_cart = []
        client.bill = 0
        client.client_ordered_meals = {}
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):

        client = self._find_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise "There are no ordered meals!"

        total_amount = client.bill
        client.shopping_cart = []
        client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount {total_amount:.2f} was successfully paid for " \
               f"{client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on on the menu and {len(self.clients_list)} clients."






    def _find_client_by_phone_number(self, client_phone_number):

        number = [num for num in self.clients_list if num.phone_number == client_phone_number]
        if number:
            return number[0]
        return None
