# order.py

class Order:
    def __init__(self):
        self.items = []  # Each item is a tuple (MenuItem, quantity)

    def add_item(self, menu_item, quantity=1):
        self.items.append((menu_item, quantity))

    def is_empty(self):
        return len(self.items) == 0

    def get_total(self):
        total = sum(item.get_price() * qty for item, qty in self.items)
        return total

    def __str__(self):
        if self.is_empty():
            return "No items in order."
        result = ""
        for item, qty in self.items:
            result += f"{item.get_name()} x {qty} = ${item.get_price() * qty:.2f}\n"
        result += f"Order Total: ${self.get_total():.2f}"
        return result


