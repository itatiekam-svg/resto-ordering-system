# restaurant.py

class Restaurant:
    def __init__(self, name="My Restaurant"):
        self.name = name
        self.menu = []
        self.customers = []

    def add_menu_item(self, menu_item):
        self.menu.append(menu_item)

    def show_menu(self):
        print(f"\n--- {self.name} Menu ---")
        for item in self.menu:
            print(item)

    def get_item_by_id(self, item_id):
        for item in self.menu:
            if item.get_id() == item_id:
                return item
        return None

    def add_customer(self, customer):
        self.customers.append(customer)

    def show_customers(self):
        print(f"\n--- Customers at {self.name} ---")
        for customer in self.customers:
            print(customer)


