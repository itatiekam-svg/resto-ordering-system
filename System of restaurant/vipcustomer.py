# Inheritance + Polymorphism example: VIP customer
class VIPCustomer(Customer):
    def get_discount(self):
        return 0.1  # 10% discount on total bill

    def __str__(self):
        return f"VIP Customer: {self.name}"