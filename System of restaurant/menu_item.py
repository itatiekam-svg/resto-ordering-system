# menu_item.py

class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def get_id(self):
        return self.item_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.item_id}. {self.name} - ${self.price:.2f}"


# Inheritance example: a special menu item with discount
class SpecialMenuItem(MenuItem):
    def __init__(self, item_id, name, price, discount=0.1):
        super().__init__(item_id, name, price)
        self.discount = discount  # 10% discount by default

    def get_price(self):
        # Override polymorphically to apply discount
        return round(self.price * (1 - self.discount), 2)

    def __str__(self):
        return f"{self.item_id}. {self.name} - ${self.get_price():.2f} (Special!)"



