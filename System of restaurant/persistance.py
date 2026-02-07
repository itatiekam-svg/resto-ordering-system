# persistence.py
import json
from menu_item import MenuItem, SpecialMenuItem
from customer import Customer, VIPCustomer
from order import Order

def save_data(restaurant, filename="restaurant_data.json"):
    data = {
        "menu": [],
        "customers": []
    }

    # Save menu items
    for item in restaurant.menu:
        item_data = {
            "id": item.get_id(),
            "name": item.get_name(),
            "price": item.get_price(),
            "type": "special" if isinstance(item, SpecialMenuItem) else "normal",
            "discount": getattr(item, "discount", 0)
        }
        data["menu"].append(item_data)

    # Save customers and their orders
    for customer in restaurant.customers:
        cust_data = {
            "name": customer.name,
            "vip": isinstance(customer, VIPCustomer),
            "orders": []
        }
        for order in customer.orders:
            order_data = []
            for item, qty in order.items:
                order_data.append({
                    "id": item.get_id(),
                    "name": item.get_name(),
                    "price": item.get_price(),
                    "quantity": qty,
                    "type": "special" if isinstance(item, SpecialMenuItem) else "normal",
                    "discount": getattr(item, "discount", 0)
                })
            cust_data["orders"].append(order_data)
        data["customers"].append(cust_data)

    # Write to JSON file
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved successfully!")


def load_data(filename="restaurant_data.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return None, []

    # Recreate menu items
    menu = []
    for item_data in data.get("menu", []):
        if item_data["type"] == "special":
            menu.append(SpecialMenuItem(
                item_data["id"],
                item_data["name"],
                item_data["price"] / (1 - item_data.get("discount", 0)),  # original price
                discount=item_data.get("discount", 0)
            ))
        else:
            menu.append(MenuItem(item_data["id"], item_data["name"], item_data["price"]))

    # Recreate customers and orders
    customers = []
    for cust_data in data.get("customers", []):
        if cust_data.get("vip", False):
            customer = VIPCustomer(cust_data["name"])
        else:
            customer = Customer(cust_data["name"])

        for order_data in cust_data.get("orders", []):
            order = Order()
            for item_data in order_data:
                if item_data["type"] == "special":
                    item = SpecialMenuItem(
                        item_data["id"],
                        item_data["name"],
                        item_data["price"] / (1 - item_data.get("discount", 0)),
                        discount=item_data.get("discount", 0)
                    )
                else:
                    item = MenuItem(item_data["id"], item_data["name"], item_data["price"])
                order.add_item(item, item_data["quantity"])
            customer.place_order(order)
        customers.append(customer)

    return menu, customers
