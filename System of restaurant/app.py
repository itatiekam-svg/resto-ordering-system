from restaurant import Restaurant
from menu_item import MenuItem, SpecialMenuItem
from customer import Customer, VIPCustomer
from order import Order
from persistance import save_data, load_data


class RestaurantApp:
    def __init__(self):
        self.restaurant = Restaurant("Tacos Family")
        self.order = Order()
        self.customer = None

    def setup(self):
        menu_data, customers_data = load_data()

        if menu_data:
            self.restaurant.menu = menu_data
        else:
            self._create_default_menu()

        if customers_data:
            self.restaurant.customers = customers_data

    def _create_default_menu(self):
        self.restaurant.add_menu_item(MenuItem(1, "Burger", 5.99))
        self.restaurant.add_menu_item(SpecialMenuItem(2, "Pizza", 8.99))
        self.restaurant.add_menu_item(MenuItem(3, "Pasta", 7.49))
        self.restaurant.add_menu_item(SpecialMenuItem(4, "Soda", 1.99, discount=0.2))

    def login_customer(self):
        name = input("Enter your name: ")
        vip = input("Are you a VIP customer? (y/n): ").lower()

        if vip == "y":
            self.customer = VIPCustomer(name)
        else:
            self.customer = Customer(name)

        self.restaurant.add_customer(self.customer)

    def show_menu(self):
        self.restaurant.show_menu()

    def add_item_to_order(self):
        self.show_menu()
        try:
            item_id = int(input("Enter item number: "))
            item = self.restaurant.get_item_by_id(item_id)

            if not item:
                print("Invalid item number.")
                return

            qty = int(input("Enter quantity: "))
            self.order.add_item(item, qty)
            print(f"{qty} x {item.get_name()} added.")
        except ValueError:
            print("Invalid input.")

    def checkout(self):
        if self.order.is_empty():
            print("No items ordered.")
            return False

        self.customer.place_order(self.order)
        total = self.order.get_total()
        discount = total * self.customer.get_discount()

        print("\n--- Final Order ---")
        print(self.order)

        if discount > 0:
            print(f"VIP Discount: -${discount:.2f}")

        print(f"Total: ${total - discount:.2f}")
        save_data(self.restaurant)
        return True

    def run(self):
        self.setup()
        self.login_customer()

        while True:
            print("\n--- Main Menu ---")
            print("1. Show Menu")
            print("2. Add Item")
            print("3. View Order")
            print("4. Checkout & Exit")

            choice = input("Choose (1-4): ")

            if choice == "1":
                self.show_menu()
            elif choice == "2":
                self.add_item_to_order()
            elif choice == "3":
                print(self.order)
            elif choice == "4":
                if self.checkout():
                    break
            else:
                print("Invalid choice.")
