
# customer.py

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

    def get_total(self):
        total = sum(order.get_total() for order in self.orders)
        return total

    def get_discount(self):
        return 0  # Regular customers have no discount

    def __str__(self):
        return f"Customer: {self.name}"


# Inheritance + Polymorphism example: VIP customer
class VIPCustomer(Customer):
    def get_discount(self):
        return 0.1  # 10% discount on total bill

    def __str__(self):
        return f"VIP Customer: {self.name}"

